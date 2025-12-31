from fastapi import FastAPI, APIRouter, HTTPException, Depends, Request, Response
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
import uuid
from datetime import datetime, timezone, timedelta
import bcrypt
import jwt
import httpx

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

JWT_SECRET = os.environ.get('JWT_SECRET', 'codechain_secret_key_2024')
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_HOURS = 168  # 7 days

app = FastAPI(title="CodeChain API")
api_router = APIRouter(prefix="/api")

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# ============== MODELS ==============

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    user_id: str
    email: str
    name: str
    picture: Optional[str] = None
    elo_rating: int = 1200
    problems_solved: int = 0
    subscription: str = "basic"
    created_at: datetime

class ProblemCreate(BaseModel):
    title: str
    description: str
    difficulty: str  # junior, middle, senior, expert
    category: str  # solidity, rust, move, tvm
    initial_code: str
    test_cases: List[dict]
    hints: Optional[List[str]] = []
    tags: Optional[List[str]] = []

class ProblemResponse(BaseModel):
    problem_id: str
    title: str
    description: str
    difficulty: str
    category: str
    initial_code: str
    test_cases: List[dict]
    hints: List[str]
    tags: List[str]
    solved_count: int
    created_at: datetime

class SubmissionCreate(BaseModel):
    problem_id: str
    code: str
    language: str = "solidity"

class SubmissionResponse(BaseModel):
    submission_id: str
    problem_id: str
    user_id: str
    code: str
    status: str  # pending, passed, failed
    test_results: List[dict]
    gas_used: Optional[int] = None
    execution_time_ms: Optional[int] = None
    elo_change: Optional[int] = None
    created_at: datetime

class HackathonCreate(BaseModel):
    title: str
    description: str
    prize_pool: int
    start_date: datetime
    end_date: datetime
    problems: List[str] = []
    max_participants: int = 1000

class HackathonResponse(BaseModel):
    hackathon_id: str
    title: str
    description: str
    prize_pool: int
    start_date: datetime
    end_date: datetime
    problems: List[str]
    participants: List[str]
    status: str
    created_at: datetime

class LeaderboardEntry(BaseModel):
    rank: int
    user_id: str
    name: str
    elo_rating: int
    problems_solved: int
    picture: Optional[str] = None

# ============== AUTH HELPERS ==============

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def create_jwt_token(user_id: str) -> str:
    payload = {
        "user_id": user_id,
        "exp": datetime.now(timezone.utc) + timedelta(hours=JWT_EXPIRATION_HOURS),
        "iat": datetime.now(timezone.utc)
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

def decode_jwt_token(token: str) -> Optional[dict]:
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

async def get_current_user(request: Request) -> dict:
    # Check cookie first
    session_token = request.cookies.get("session_token")
    if session_token:
        session = await db.user_sessions.find_one({"session_token": session_token}, {"_id": 0})
        if session:
            expires_at = session["expires_at"]
            if isinstance(expires_at, str):
                expires_at = datetime.fromisoformat(expires_at)
            if expires_at.tzinfo is None:
                expires_at = expires_at.replace(tzinfo=timezone.utc)
            if expires_at > datetime.now(timezone.utc):
                user = await db.users.find_one({"user_id": session["user_id"]}, {"_id": 0})
                if user:
                    return user
    
    # Check Authorization header
    auth_header = request.headers.get("Authorization")
    if auth_header and auth_header.startswith("Bearer "):
        token = auth_header.split(" ")[1]
        payload = decode_jwt_token(token)
        if payload:
            user = await db.users.find_one({"user_id": payload["user_id"]}, {"_id": 0})
            if user:
                return user
    
    raise HTTPException(status_code=401, detail="Not authenticated")

async def get_optional_user(request: Request) -> Optional[dict]:
    try:
        return await get_current_user(request)
    except HTTPException:
        return None

# ============== AUTH ENDPOINTS ==============

@api_router.post("/auth/register")
async def register(user_data: UserCreate):
    existing = await db.users.find_one({"email": user_data.email}, {"_id": 0})
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    user_id = f"user_{uuid.uuid4().hex[:12]}"
    user_doc = {
        "user_id": user_id,
        "email": user_data.email,
        "name": user_data.name,
        "password_hash": hash_password(user_data.password),
        "picture": None,
        "elo_rating": 1200,
        "problems_solved": 0,
        "subscription": "basic",
        "achievements": [],
        "created_at": datetime.now(timezone.utc).isoformat()
    }
    await db.users.insert_one(user_doc)
    
    token = create_jwt_token(user_id)
    user_doc.pop("password_hash", None)
    user_doc.pop("_id", None)
    
    return {"token": token, "user": user_doc}

@api_router.post("/auth/login")
async def login(credentials: UserLogin):
    user = await db.users.find_one({"email": credentials.email}, {"_id": 0})
    if not user or not verify_password(credentials.password, user.get("password_hash", "")):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_jwt_token(user["user_id"])
    user.pop("password_hash", None)
    
    return {"token": token, "user": user}

# REMINDER: DO NOT HARDCODE THE URL, OR ADD ANY FALLBACKS OR REDIRECT URLS, THIS BREAKS THE AUTH
@api_router.get("/auth/session")
async def get_session(request: Request, response: Response):
    session_id = request.headers.get("X-Session-ID")
    if not session_id:
        raise HTTPException(status_code=400, detail="Session ID required")
    
    async with httpx.AsyncClient() as client:
        resp = await client.get(
            "https://demobackend.emergentagent.com/auth/v1/env/oauth/session-data",
            headers={"X-Session-ID": session_id}
        )
        if resp.status_code != 200:
            raise HTTPException(status_code=401, detail="Invalid session")
        
        data = resp.json()
    
    # Check if user exists
    existing = await db.users.find_one({"email": data["email"]}, {"_id": 0})
    if existing:
        user_id = existing["user_id"]
        # Update user info if needed
        await db.users.update_one(
            {"user_id": user_id},
            {"$set": {"name": data["name"], "picture": data.get("picture")}}
        )
    else:
        user_id = f"user_{uuid.uuid4().hex[:12]}"
        user_doc = {
            "user_id": user_id,
            "email": data["email"],
            "name": data["name"],
            "picture": data.get("picture"),
            "elo_rating": 1200,
            "problems_solved": 0,
            "subscription": "basic",
            "achievements": [],
            "created_at": datetime.now(timezone.utc).isoformat()
        }
        await db.users.insert_one(user_doc)
    
    # Create session
    session_token = data.get("session_token", str(uuid.uuid4()))
    expires_at = datetime.now(timezone.utc) + timedelta(days=7)
    
    await db.user_sessions.delete_many({"user_id": user_id})
    await db.user_sessions.insert_one({
        "user_id": user_id,
        "session_token": session_token,
        "expires_at": expires_at.isoformat(),
        "created_at": datetime.now(timezone.utc).isoformat()
    })
    
    response.set_cookie(
        key="session_token",
        value=session_token,
        httponly=True,
        secure=True,
        samesite="none",
        path="/",
        max_age=7*24*60*60
    )
    
    user = await db.users.find_one({"user_id": user_id}, {"_id": 0, "password_hash": 0})
    return user

@api_router.get("/auth/me")
async def get_me(user: dict = Depends(get_current_user)):
    user.pop("password_hash", None)
    return user

@api_router.post("/auth/logout")
async def logout(request: Request, response: Response):
    session_token = request.cookies.get("session_token")
    if session_token:
        await db.user_sessions.delete_many({"session_token": session_token})
    response.delete_cookie("session_token", path="/")
    return {"message": "Logged out"}

# ============== PROBLEMS ENDPOINTS ==============

@api_router.get("/problems")
async def get_problems(
    difficulty: Optional[str] = None,
    category: Optional[str] = None,
    search: Optional[str] = None,
    limit: int = 50,
    offset: int = 0
):
    query = {}
    if difficulty:
        query["difficulty"] = difficulty
    if category:
        query["category"] = category
    if search:
        query["$or"] = [
            {"title": {"$regex": search, "$options": "i"}},
            {"tags": {"$in": [search.lower()]}}
        ]
    
    problems = await db.problems.find(query, {"_id": 0}).skip(offset).limit(limit).to_list(limit)
    total = await db.problems.count_documents(query)
    
    return {"problems": problems, "total": total}

@api_router.get("/problems/{problem_id}")
async def get_problem(problem_id: str):
    problem = await db.problems.find_one({"problem_id": problem_id}, {"_id": 0})
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")
    return problem

@api_router.post("/problems")
async def create_problem(problem: ProblemCreate, user: dict = Depends(get_current_user)):
    problem_id = f"prob_{uuid.uuid4().hex[:8]}"
    problem_doc = {
        "problem_id": problem_id,
        **problem.model_dump(),
        "solved_count": 0,
        "author_id": user["user_id"],
        "created_at": datetime.now(timezone.utc).isoformat()
    }
    await db.problems.insert_one(problem_doc)
    problem_doc.pop("_id", None)
    return problem_doc

# ============== SUBMISSIONS ENDPOINTS ==============

@api_router.post("/submissions")
async def create_submission(submission: SubmissionCreate, user: dict = Depends(get_current_user)):
    problem = await db.problems.find_one({"problem_id": submission.problem_id}, {"_id": 0})
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")
    
    submission_id = f"sub_{uuid.uuid4().hex[:8]}"
    
    # Simulate Solidity compilation and test execution
    test_results = []
    all_passed = True
    total_gas = 0
    
    for i, test_case in enumerate(problem.get("test_cases", [])):
        # Simplified simulation - in production, use actual Solidity compiler
        passed = "revert" not in submission.code.lower() and "error" not in submission.code.lower()
        gas = 21000 + len(submission.code) * 10  # Simplified gas calculation
        
        test_results.append({
            "test_id": i + 1,
            "input": test_case.get("input", ""),
            "expected": test_case.get("expected", ""),
            "passed": passed,
            "gas_used": gas,
            "error": None if passed else "Execution failed"
        })
        
        if not passed:
            all_passed = False
        total_gas += gas
    
    status = "passed" if all_passed else "failed"
    elo_change = 0
    
    if all_passed:
        # Calculate ELO change based on difficulty
        difficulty_elo = {"junior": 10, "middle": 20, "senior": 35, "expert": 50}
        elo_change = difficulty_elo.get(problem.get("difficulty", "junior"), 10)
        
        # Update user stats
        await db.users.update_one(
            {"user_id": user["user_id"]},
            {
                "$inc": {"elo_rating": elo_change, "problems_solved": 1}
            }
        )
        
        # Update problem solved count
        await db.problems.update_one(
            {"problem_id": submission.problem_id},
            {"$inc": {"solved_count": 1}}
        )
    
    submission_doc = {
        "submission_id": submission_id,
        "problem_id": submission.problem_id,
        "user_id": user["user_id"],
        "code": submission.code,
        "language": submission.language,
        "status": status,
        "test_results": test_results,
        "gas_used": total_gas,
        "execution_time_ms": len(submission.code) // 10,
        "elo_change": elo_change if all_passed else 0,
        "created_at": datetime.now(timezone.utc).isoformat()
    }
    
    await db.submissions.insert_one(submission_doc)
    submission_doc.pop("_id", None)
    
    return submission_doc

@api_router.get("/submissions")
async def get_user_submissions(user: dict = Depends(get_current_user), limit: int = 20):
    submissions = await db.submissions.find(
        {"user_id": user["user_id"]},
        {"_id": 0}
    ).sort("created_at", -1).limit(limit).to_list(limit)
    return submissions

@api_router.get("/submissions/{problem_id}")
async def get_problem_submissions(problem_id: str, user: dict = Depends(get_current_user)):
    submissions = await db.submissions.find(
        {"problem_id": problem_id, "user_id": user["user_id"]},
        {"_id": 0}
    ).sort("created_at", -1).to_list(50)
    return submissions

# ============== LEADERBOARD ENDPOINTS ==============

@api_router.get("/leaderboard")
async def get_leaderboard(
    category: Optional[str] = None,
    limit: int = 100
):
    users = await db.users.find(
        {},
        {"_id": 0, "user_id": 1, "name": 1, "elo_rating": 1, "problems_solved": 1, "picture": 1}
    ).sort("elo_rating", -1).limit(limit).to_list(limit)
    
    leaderboard = []
    for i, user in enumerate(users):
        leaderboard.append({
            "rank": i + 1,
            **user
        })
    
    return leaderboard

@api_router.get("/leaderboard/user/{user_id}")
async def get_user_rank(user_id: str):
    user = await db.users.find_one({"user_id": user_id}, {"_id": 0})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    rank = await db.users.count_documents({"elo_rating": {"$gt": user.get("elo_rating", 0)}}) + 1
    return {"rank": rank, **user}

# ============== HACKATHONS ENDPOINTS ==============

@api_router.get("/hackathons")
async def get_hackathons(status: Optional[str] = None):
    query = {}
    now = datetime.now(timezone.utc)
    
    if status == "active":
        query["start_date"] = {"$lte": now.isoformat()}
        query["end_date"] = {"$gte": now.isoformat()}
    elif status == "upcoming":
        query["start_date"] = {"$gt": now.isoformat()}
    elif status == "completed":
        query["end_date"] = {"$lt": now.isoformat()}
    
    hackathons = await db.hackathons.find(query, {"_id": 0}).to_list(100)
    return hackathons

@api_router.get("/hackathons/{hackathon_id}")
async def get_hackathon(hackathon_id: str):
    hackathon = await db.hackathons.find_one({"hackathon_id": hackathon_id}, {"_id": 0})
    if not hackathon:
        raise HTTPException(status_code=404, detail="Hackathon not found")
    return hackathon

@api_router.post("/hackathons")
async def create_hackathon(hackathon: HackathonCreate, user: dict = Depends(get_current_user)):
    hackathon_id = f"hack_{uuid.uuid4().hex[:8]}"
    hackathon_doc = {
        "hackathon_id": hackathon_id,
        **hackathon.model_dump(),
        "start_date": hackathon.start_date.isoformat(),
        "end_date": hackathon.end_date.isoformat(),
        "participants": [],
        "status": "upcoming",
        "organizer_id": user["user_id"],
        "created_at": datetime.now(timezone.utc).isoformat()
    }
    await db.hackathons.insert_one(hackathon_doc)
    hackathon_doc.pop("_id", None)
    return hackathon_doc

@api_router.post("/hackathons/{hackathon_id}/join")
async def join_hackathon(hackathon_id: str, user: dict = Depends(get_current_user)):
    hackathon = await db.hackathons.find_one({"hackathon_id": hackathon_id}, {"_id": 0})
    if not hackathon:
        raise HTTPException(status_code=404, detail="Hackathon not found")
    
    if user["user_id"] in hackathon.get("participants", []):
        raise HTTPException(status_code=400, detail="Already joined")
    
    await db.hackathons.update_one(
        {"hackathon_id": hackathon_id},
        {"$push": {"participants": user["user_id"]}}
    )
    
    return {"message": "Joined successfully"}

# ============== USER PROFILE ENDPOINTS ==============

@api_router.get("/users/{user_id}")
async def get_user_profile(user_id: str):
    user = await db.users.find_one({"user_id": user_id}, {"_id": 0, "password_hash": 0})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Get recent submissions
    submissions = await db.submissions.find(
        {"user_id": user_id},
        {"_id": 0}
    ).sort("created_at", -1).limit(10).to_list(10)
    
    # Get user rank
    rank = await db.users.count_documents({"elo_rating": {"$gt": user.get("elo_rating", 0)}}) + 1
    
    return {**user, "rank": rank, "recent_submissions": submissions}

@api_router.put("/users/profile")
async def update_profile(
    name: Optional[str] = None,
    picture: Optional[str] = None,
    user: dict = Depends(get_current_user)
):
    update_data = {}
    if name:
        update_data["name"] = name
    if picture:
        update_data["picture"] = picture
    
    if update_data:
        await db.users.update_one(
            {"user_id": user["user_id"]},
            {"$set": update_data}
        )
    
    updated_user = await db.users.find_one({"user_id": user["user_id"]}, {"_id": 0, "password_hash": 0})
    return updated_user

# ============== STATS ENDPOINTS ==============

@api_router.get("/stats/dashboard")
async def get_dashboard_stats(user: dict = Depends(get_current_user)):
    # User stats
    total_submissions = await db.submissions.count_documents({"user_id": user["user_id"]})
    passed_submissions = await db.submissions.count_documents({"user_id": user["user_id"], "status": "passed"})
    
    # Recent activity
    recent_submissions = await db.submissions.find(
        {"user_id": user["user_id"]},
        {"_id": 0}
    ).sort("created_at", -1).limit(5).to_list(5)
    
    # Problems by difficulty
    problems_by_difficulty = {}
    for diff in ["junior", "middle", "senior", "expert"]:
        count = await db.submissions.count_documents({
            "user_id": user["user_id"],
            "status": "passed"
        })
        problems_by_difficulty[diff] = count
    
    # User rank
    rank = await db.users.count_documents({"elo_rating": {"$gt": user.get("elo_rating", 0)}}) + 1
    total_users = await db.users.count_documents({})
    
    return {
        "total_submissions": total_submissions,
        "passed_submissions": passed_submissions,
        "success_rate": round(passed_submissions / max(total_submissions, 1) * 100, 1),
        "elo_rating": user.get("elo_rating", 1200),
        "problems_solved": user.get("problems_solved", 0),
        "rank": rank,
        "total_users": total_users,
        "recent_submissions": recent_submissions,
        "problems_by_difficulty": problems_by_difficulty
    }

@api_router.get("/stats/global")
async def get_global_stats():
    total_users = await db.users.count_documents({})
    total_problems = await db.problems.count_documents({})
    total_submissions = await db.submissions.count_documents({})
    total_hackathons = await db.hackathons.count_documents({})
    
    return {
        "total_users": total_users,
        "total_problems": total_problems,
        "total_submissions": total_submissions,
        "total_hackathons": total_hackathons
    }

# ============== SEED DATA ==============

@api_router.post("/seed")
async def seed_data():
    """Seed initial problems for demo"""
    problems = [
        {
            "problem_id": "prob_001",
            "title": "Hello Blockchain",
            "description": "Write a simple smart contract that stores and retrieves a greeting message. The contract should have a `setGreeting` function and a `getGreeting` function.",
            "difficulty": "junior",
            "category": "solidity",
            "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Greeting {
    // Your code here
    
    function setGreeting(string memory _greeting) public {
        // Implement this
    }
    
    function getGreeting() public view returns (string memory) {
        // Implement this
    }
}""",
            "test_cases": [
                {"input": "setGreeting('Hello, World!')", "expected": "true"},
                {"input": "getGreeting()", "expected": "Hello, World!"}
            ],
            "hints": ["Use a string state variable", "Don't forget the memory keyword"],
            "tags": ["basics", "storage", "functions"],
            "solved_count": 1250,
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "problem_id": "prob_002",
            "title": "Simple Token",
            "description": "Create a basic ERC20-like token with mint, transfer, and balanceOf functions. The contract should track balances using a mapping.",
            "difficulty": "junior",
            "category": "solidity",
            "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleToken {
    mapping(address => uint256) private balances;
    
    function mint(uint256 amount) public {
        // Implement this
    }
    
    function transfer(address to, uint256 amount) public {
        // Implement this
    }
    
    function balanceOf(address account) public view returns (uint256) {
        // Implement this
    }
}""",
            "test_cases": [
                {"input": "mint(1000)", "expected": "true"},
                {"input": "balanceOf(msg.sender)", "expected": "1000"}
            ],
            "hints": ["Use the mapping to track balances", "Check for sufficient balance before transfer"],
            "tags": ["token", "mapping", "erc20"],
            "solved_count": 890,
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "problem_id": "prob_003",
            "title": "Reentrancy Guard",
            "description": "Implement a withdrawal function that is protected against reentrancy attacks. Use the checks-effects-interactions pattern.",
            "difficulty": "middle",
            "category": "solidity",
            "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SecureVault {
    mapping(address => uint256) public balances;
    
    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }
    
    function withdraw() public {
        // Implement secure withdrawal
        // Hint: Update state BEFORE external call
    }
}""",
            "test_cases": [
                {"input": "deposit{value: 1 ether}()", "expected": "true"},
                {"input": "withdraw()", "expected": "Balance: 0"}
            ],
            "hints": ["Update balance before making external call", "Consider using a reentrancy guard modifier"],
            "tags": ["security", "reentrancy", "patterns"],
            "solved_count": 456,
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "problem_id": "prob_004",
            "title": "Gas Optimizer",
            "description": "Optimize the given contract to reduce gas consumption by at least 30%. Use storage packing, memory vs calldata, and other optimization techniques.",
            "difficulty": "senior",
            "category": "solidity",
            "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Original: ~85,000 gas
// Target: <60,000 gas

contract Unoptimized {
    struct User {
        uint256 id;
        uint256 balance;
        uint256 lastUpdate;
        bool isActive;
        address wallet;
    }
    
    User[] public users;
    
    function addUser(uint256 id, uint256 balance, address wallet) public {
        User memory user = User({
            id: id,
            balance: balance,
            lastUpdate: block.timestamp,
            isActive: true,
            wallet: wallet
        });
        users.push(user);
    }
}""",
            "test_cases": [
                {"input": "addUser(1, 1000, address)", "expected": "gas < 60000"}
            ],
            "hints": ["Pack smaller types together in structs", "Use uint128 or smaller where possible"],
            "tags": ["optimization", "gas", "advanced"],
            "solved_count": 234,
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "problem_id": "prob_005",
            "title": "Flash Loan Arbitrage",
            "description": "Implement a flash loan callback that performs arbitrage between two DEXes. Calculate profit and ensure the loan is repaid.",
            "difficulty": "expert",
            "category": "solidity",
            "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IFlashLoanProvider {
    function flashLoan(uint256 amount, bytes calldata data) external;
}

interface IDEX {
    function swap(address tokenIn, address tokenOut, uint256 amountIn) external returns (uint256);
    function getPrice(address token) external view returns (uint256);
}

contract FlashArbitrage {
    IFlashLoanProvider public loanProvider;
    IDEX public dex1;
    IDEX public dex2;
    
    constructor(address _provider, address _dex1, address _dex2) {
        loanProvider = IFlashLoanProvider(_provider);
        dex1 = IDEX(_dex1);
        dex2 = IDEX(_dex2);
    }
    
    function executeArbitrage(address tokenA, address tokenB, uint256 amount) external {
        // Implement flash loan arbitrage
    }
    
    function onFlashLoan(uint256 amount, uint256 fee, bytes calldata data) external {
        // Implement callback
    }
}""",
            "test_cases": [
                {"input": "executeArbitrage(tokenA, tokenB, 1000e18)", "expected": "profit > 0"}
            ],
            "hints": ["Check price difference between DEXes first", "Account for fees in profit calculation"],
            "tags": ["defi", "flash-loans", "arbitrage", "advanced"],
            "solved_count": 89,
            "created_at": datetime.now(timezone.utc).isoformat()
        }
    ]
    
    # Clear and insert
    await db.problems.delete_many({})
    await db.problems.insert_many(problems)
    
    # Seed hackathons
    hackathons = [
        {
            "hackathon_id": "hack_001",
            "title": "DeFi Security Challenge",
            "description": "Find and fix vulnerabilities in DeFi protocols. Top security researchers compete for prizes.",
            "prize_pool": 25000,
            "start_date": (datetime.now(timezone.utc) + timedelta(days=7)).isoformat(),
            "end_date": (datetime.now(timezone.utc) + timedelta(days=14)).isoformat(),
            "problems": ["prob_003", "prob_004"],
            "participants": [],
            "max_participants": 500,
            "status": "upcoming",
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "hackathon_id": "hack_002",
            "title": "Gas Wars 2024",
            "description": "Optimize smart contracts for minimal gas usage. Every wei counts!",
            "prize_pool": 15000,
            "start_date": (datetime.now(timezone.utc) - timedelta(days=2)).isoformat(),
            "end_date": (datetime.now(timezone.utc) + timedelta(days=5)).isoformat(),
            "problems": ["prob_004"],
            "participants": [],
            "max_participants": 300,
            "status": "active",
            "created_at": datetime.now(timezone.utc).isoformat()
        }
    ]
    
    await db.hackathons.delete_many({})
    await db.hackathons.insert_many(hackathons)
    
    return {"message": "Seeded successfully", "problems": len(problems), "hackathons": len(hackathons)}

# ============== MAIN ==============

app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
