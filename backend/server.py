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
from code_validator import code_validator

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


class SkillNode(BaseModel):
    skill_id: str
    name: str
    description: str
    category: str  # solidity, rust, move, tvm, general
    dependencies: List[str] = []  # skill_ids that must be completed first
    required_problems: List[str] = []  # problem_ids that unlock this skill
    level: int = 1  # 1-5 proficiency level

class UserSkillProgress(BaseModel):
    user_id: str
    skill_id: str
    progress: int  # 0-100
    level: int  # 1-5
    unlocked: bool
    unlocked_at: Optional[datetime] = None

class Achievement(BaseModel):
    achievement_id: str
    name: str
    description: str
    category: str  # progress, technical, efficiency, streak
    icon: str  # emoji or icon name
    criteria: dict  # conditions to unlock
    points: int  # bonus points
    rarity: str  # common, rare, epic, legendary

class UserAchievement(BaseModel):
    user_id: str
    achievement_id: str
    unlocked_at: datetime
    progress: Optional[int] = None  # for progressive achievements

class Rank(BaseModel):
    rank_id: str
    name: str
    min_elo: int
    min_problems: int
    required_skills: List[str] = []
    icon: str
    color: str

class ActivityDay(BaseModel):
    user_id: str
    date: str  # YYYY-MM-DD
    problems_solved: int
    submissions_count: int
    elo_gained: int

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


# ============== SKILLS & ACHIEVEMENTS HELPERS ==============

# Predefined skill tree
SKILL_TREE = [
    {
        "skill_id": "sol_basics",
        "name": "Solidity Basics",
        "description": "Understanding of Solidity syntax, variables, and functions",
        "category": "solidity",
        "dependencies": [],
        "level": 1
    },
    {
        "skill_id": "sol_storage",
        "name": "Storage & State",
        "description": "Working with storage, state variables, and mappings",
        "category": "solidity",
        "dependencies": ["sol_basics"],
        "level": 2
    },
    {
        "skill_id": "sol_security",
        "name": "Smart Contract Security",
        "description": "Security patterns, reentrancy, access control",
        "category": "solidity",
        "dependencies": ["sol_basics", "sol_storage"],
        "level": 3
    },
    {
        "skill_id": "sol_gas",
        "name": "Gas Optimization",
        "description": "Optimizing contracts for lower gas costs",
        "category": "solidity",
        "dependencies": ["sol_storage"],
        "level": 3
    },
    {
        "skill_id": "sol_advanced",
        "name": "Advanced Patterns",
        "description": "Proxies, upgradeable contracts, advanced patterns",
        "category": "solidity",
        "dependencies": ["sol_security", "sol_gas"],
        "level": 4
    },
    {
        "skill_id": "erc20",
        "name": "ERC-20 Tokens",
        "description": "Creating and managing ERC-20 tokens",
        "category": "solidity",
        "dependencies": ["sol_basics"],
        "level": 2
    },
    {
        "skill_id": "erc721",
        "name": "NFTs (ERC-721)",
        "description": "NFT standards and implementation",
        "category": "solidity",
        "dependencies": ["erc20"],
        "level": 3
    },
    {
        "skill_id": "defi",
        "name": "DeFi Protocols",
        "description": "AMM, lending, staking protocols",
        "category": "solidity",
        "dependencies": ["erc20", "sol_security"],
        "level": 4
    },
    {
        "skill_id": "rust_basics",
        "name": "Rust Basics",
        "description": "Rust syntax, ownership, borrowing",
        "category": "rust",
        "dependencies": [],
        "level": 1
    },
    {
        "skill_id": "solana_prog",
        "name": "Solana Programs",
        "description": "Building programs on Solana",
        "category": "rust",
        "dependencies": ["rust_basics"],
        "level": 3
    },
    {
        "skill_id": "func_basics",
        "name": "FunC Basics",
        "description": "TON smart contracts with FunC",
        "category": "tvm",
        "dependencies": [],
        "level": 2
    },
    {
        "skill_id": "crypto_basics",
        "name": "Cryptography Fundamentals",
        "description": "Hashing, signatures, encryption",
        "category": "general",
        "dependencies": [],
        "level": 2
    }
]

# Predefined achievements
ACHIEVEMENTS_LIST = [
    {
        "achievement_id": "first_solve",
        "name": "First Steps",
        "description": "Solve your first problem",
        "category": "progress",
        "icon": "🎯",
        "criteria": {"problems_solved": 1},
        "points": 10,
        "rarity": "common"
    },
    {
        "achievement_id": "solve_10",
        "name": "Problem Solver",
        "description": "Solve 10 problems",
        "category": "progress",
        "icon": "⚡",
        "criteria": {"problems_solved": 10},
        "points": 50,
        "rarity": "common"
    },
    {
        "achievement_id": "solve_50",
        "name": "Coding Warrior",
        "description": "Solve 50 problems",
        "category": "progress",
        "icon": "🔥",
        "criteria": {"problems_solved": 50},
        "points": 200,
        "rarity": "rare"
    },
    {
        "achievement_id": "solve_100",
        "name": "Century Club",
        "description": "Solve 100 problems",
        "category": "progress",
        "icon": "💯",
        "criteria": {"problems_solved": 100},
        "points": 500,
        "rarity": "epic"
    },
    {
        "achievement_id": "expert_solver",
        "name": "Expert Problem Solver",
        "description": "Solve an expert-level problem",
        "category": "technical",
        "icon": "🏆",
        "criteria": {"expert_problems": 1},
        "points": 100,
        "rarity": "rare"
    },
    {
        "achievement_id": "sol_master",
        "name": "Solidity Master",
        "description": "Solve 20 Solidity problems",
        "category": "technical",
        "icon": "💎",
        "criteria": {"solidity_problems": 20},
        "points": 150,
        "rarity": "rare"
    },
    {
        "achievement_id": "rust_expert",
        "name": "Rust Expert",
        "description": "Solve 10 Rust/Solana problems",
        "category": "technical",
        "icon": "🦀",
        "criteria": {"rust_problems": 10},
        "points": 150,
        "rarity": "rare"
    },
    {
        "achievement_id": "gas_optimizer",
        "name": "Gas Optimizer",
        "description": "Submit 5 solutions with excellent gas efficiency",
        "category": "efficiency",
        "icon": "⚙️",
        "criteria": {"efficient_solutions": 5},
        "points": 100,
        "rarity": "rare"
    },
    {
        "achievement_id": "first_try",
        "name": "First Try Success",
        "description": "Solve a problem on the first attempt",
        "category": "efficiency",
        "icon": "🎪",
        "criteria": {"first_try_solve": 1},
        "points": 50,
        "rarity": "common"
    },
    {
        "achievement_id": "week_streak",
        "name": "Week Warrior",
        "description": "Solve at least 1 problem for 7 consecutive days",
        "category": "streak",
        "icon": "📅",
        "criteria": {"daily_streak": 7},
        "points": 150,
        "rarity": "rare"
    },
    {
        "achievement_id": "month_streak",
        "name": "Consistency King",
        "description": "Solve at least 1 problem for 30 consecutive days",
        "category": "streak",
        "icon": "👑",
        "criteria": {"daily_streak": 30},
        "points": 500,
        "rarity": "legendary"
    },
    {
        "achievement_id": "speed_demon",
        "name": "Speed Demon",
        "description": "Solve 10 problems in a single day",
        "category": "efficiency",
        "icon": "⚡",
        "criteria": {"problems_in_day": 10},
        "points": 200,
        "rarity": "epic"
    },
    {
        "achievement_id": "top_10",
        "name": "Top 10 Elite",
        "description": "Reach top 10 in global leaderboard",
        "category": "progress",
        "icon": "🌟",
        "criteria": {"leaderboard_rank": 10},
        "points": 500,
        "rarity": "legendary"
    }
]

# Enhanced Rank System with detailed progression
RANKS = [
    {
        "rank_id": "newbie",
        "name": "Newbie",
        "min_elo": 0,
        "max_elo": 1199,
        "min_problems": 0,
        "max_problems": 4,
        "icon": "🌱",
        "color": "#94a3b8",
        "description": "Just starting your blockchain journey",
        "benefits": ["Access to Junior problems", "Basic learning resources"],
        "next_rank_hint": "Solve 5 problems and reach 1200 ELO to become Junior Developer"
    },
    {
        "rank_id": "junior",
        "name": "Junior Developer",
        "min_elo": 1200,
        "max_elo": 1399,
        "min_problems": 5,
        "max_problems": 19,
        "icon": "👨‍💻",
        "color": "#22c55e",
        "description": "Learning fundamentals of blockchain development",
        "benefits": ["Access to Junior & Middle problems", "Code review tools", "Community forums"],
        "next_rank_hint": "Solve 20 problems and reach 1400 ELO to advance to Middle Developer"
    },
    {
        "rank_id": "middle",
        "name": "Middle Developer",
        "min_elo": 1400,
        "max_elo": 1599,
        "min_problems": 20,
        "max_problems": 49,
        "icon": "⚡",
        "color": "#eab308",
        "description": "Mastering smart contract patterns and security",
        "benefits": ["Access to Senior problems", "Advanced debugging tools", "Priority support"],
        "next_rank_hint": "Solve 50 problems and reach 1600 ELO to become Senior Developer"
    },
    {
        "rank_id": "senior",
        "name": "Senior Developer",
        "min_elo": 1600,
        "max_elo": 1799,
        "min_problems": 50,
        "max_problems": 99,
        "icon": "🔥",
        "color": "#f97316",
        "description": "Expert in DeFi protocols and complex systems",
        "benefits": ["Access to Expert problems", "Gas optimization insights", "Exclusive hackathons"],
        "next_rank_hint": "Solve 100 problems and reach 1800 ELO to become an Expert"
    },
    {
        "rank_id": "expert",
        "name": "Expert",
        "min_elo": 1800,
        "max_elo": 1999,
        "min_problems": 100,
        "max_problems": 199,
        "icon": "💎",
        "color": "#a855f7",
        "description": "Top-tier developer with deep expertise",
        "benefits": ["All problem access", "NFT certificates", "Mentorship opportunities", "Job board access"],
        "next_rank_hint": "Solve 200 problems and reach 2000 ELO to become Blockchain Architect"
    },
    {
        "rank_id": "architect",
        "name": "Blockchain Architect",
        "min_elo": 2000,
        "max_elo": 9999,
        "min_problems": 200,
        "max_problems": 999999,
        "icon": "👑",
        "color": "#fbbf24",
        "description": "Elite blockchain architect - you've mastered the craft",
        "benefits": ["Legendary status", "Create custom problems", "Exclusive events", "Platform recognition"],
        "next_rank_hint": "You've reached the pinnacle! Keep solving to maintain your status."
    }
]

async def check_and_unlock_achievements(user_id: str):
    """Check if user has unlocked any new achievements"""
    user = await db.users.find_one({"user_id": user_id})
    if not user:
        return []
    
    # Get user stats
    total_solved = user.get("problems_solved", 0)
    user_achievements = user.get("achievements", [])
    
    # Get detailed stats
    submissions = await db.submissions.find({"user_id": user_id, "status": "passed"}).to_list(None)
    
    # Count by category
    solidity_count = len([s for s in submissions if await get_problem_category(s["problem_id"]) == "solidity"])
    rust_count = len([s for s in submissions if await get_problem_category(s["problem_id"]) == "rust"])
    
    # Count by difficulty
    expert_count = len([s for s in submissions if await get_problem_difficulty(s["problem_id"]) == "expert"])
    
    # Calculate streak
    daily_streak = await calculate_daily_streak(user_id)
    
    # Check problems solved today
    today = datetime.now(timezone.utc).date().isoformat()
    problems_today = await db.submissions.count_documents({
        "user_id": user_id,
        "status": "passed",
        "created_at": {"$regex": f"^{today}"}
    })
    
    # Get leaderboard rank
    rank = await db.users.count_documents({"elo_rating": {"$gt": user.get("elo_rating", 0)}}) + 1
    
    # Build user stats for criteria checking
    user_stats = {
        "problems_solved": total_solved,
        "solidity_problems": solidity_count,
        "rust_problems": rust_count,
        "expert_problems": expert_count,
        "daily_streak": daily_streak,
        "problems_in_day": problems_today,
        "leaderboard_rank": rank
    }
    
    newly_unlocked = []
    
    for achievement in ACHIEVEMENTS_LIST:
        achievement_id = achievement["achievement_id"]
        
        # Skip if already unlocked
        if achievement_id in user_achievements:
            continue
        
        # Check criteria
        criteria_met = True
        for key, required_value in achievement["criteria"].items():
            if key == "leaderboard_rank":
                if user_stats.get(key, 999999) > required_value:
                    criteria_met = False
                    break
            else:
                if user_stats.get(key, 0) < required_value:
                    criteria_met = False
                    break
        
        if criteria_met:
            # Unlock achievement
            await db.users.update_one(
                {"user_id": user_id},
                {"$push": {"achievements": achievement_id}}
            )
            
            # Record unlock
            await db.user_achievements.insert_one({
                "user_id": user_id,
                "achievement_id": achievement_id,
                "unlocked_at": datetime.now(timezone.utc).isoformat()
            })
            
            newly_unlocked.append(achievement)
    
    return newly_unlocked

async def get_problem_category(problem_id: str) -> str:
    """Get category of a problem"""
    problem = await db.problems.find_one({"problem_id": problem_id})
    return problem.get("category", "") if problem else ""

async def get_problem_difficulty(problem_id: str) -> str:
    """Get difficulty of a problem"""
    problem = await db.problems.find_one({"problem_id": problem_id})
    return problem.get("difficulty", "") if problem else ""

async def calculate_daily_streak(user_id: str) -> int:
    """Calculate current daily streak"""
    # Get all submission dates
    submissions = await db.submissions.find(
        {"user_id": user_id, "status": "passed"},
        {"created_at": 1}
    ).sort("created_at", -1).to_list(None)
    
    if not submissions:
        return 0
    
    # Extract unique dates
    dates = []
    for sub in submissions:
        created_at = sub["created_at"]
        if isinstance(created_at, str):
            date_str = created_at.split("T")[0]
        else:
            date_str = created_at.date().isoformat()
        if date_str not in dates:
            dates.append(date_str)
    
    if not dates:
        return 0
    
    # Check streak from today backwards
    today = datetime.now(timezone.utc).date()
    streak = 0
    
    for i in range(len(dates)):
        expected_date = (today - timedelta(days=i)).isoformat()
        if expected_date in dates:
            streak += 1
        else:
            break
    
    return streak

async def update_skill_progress(user_id: str, problem_id: str):
    """Update user's skill progress based on solved problem"""
    problem = await db.problems.find_one({"problem_id": problem_id})
    if not problem:
        return
    
    # Map problem tags to skills
    problem_tags = problem.get("tags", [])
    category = problem.get("category", "")
    
    # Determine which skills this problem contributes to
    skill_mapping = {
        "basics": "sol_basics",
        "storage": "sol_storage",
        "security": "sol_security",
        "gas": "sol_gas",
        "erc20": "erc20",
        "nft": "erc721",
        "defi": "defi",
        "rust": "rust_basics",
        "solana": "solana_prog",
        "func": "func_basics",
        "crypto": "crypto_basics"
    }
    
    skills_to_update = []
    for tag in problem_tags:
        if tag in skill_mapping:
            skills_to_update.append(skill_mapping[tag])
    
    # Category-based skills
    if category == "solidity":
        skills_to_update.append("sol_basics")
    elif category == "rust":
        skills_to_update.append("rust_basics")
    elif category == "tvm":
        skills_to_update.append("func_basics")
    
    # Update progress
    for skill_id in skills_to_update:
        existing = await db.user_skills.find_one({"user_id": user_id, "skill_id": skill_id})
        if existing:
            new_progress = min(100, existing.get("progress", 0) + 10)
            await db.user_skills.update_one(
                {"user_id": user_id, "skill_id": skill_id},
                {"$set": {"progress": new_progress}}
            )
        else:
            await db.user_skills.insert_one({
                "user_id": user_id,
                "skill_id": skill_id,
                "progress": 10,
                "level": 1,
                "unlocked": True,
                "unlocked_at": datetime.now(timezone.utc).isoformat()
            })

async def get_user_rank(user_id: str) -> dict:
    """Get user's current rank"""
    user = await db.users.find_one({"user_id": user_id})
    if not user:
        return RANKS[0]
    
    elo = user.get("elo_rating", 0)
    problems = user.get("problems_solved", 0)
    
    # Find highest rank user qualifies for
    current_rank = RANKS[0]
    for rank in RANKS:
        if elo >= rank["min_elo"] and problems >= rank["min_problems"]:
            current_rank = rank
        else:
            break
    
    return current_rank

async def record_daily_activity(user_id: str, problems_solved: int = 0, elo_gained: int = 0):
    """Record user's daily activity"""
    today = datetime.now(timezone.utc).date().isoformat()
    
    existing = await db.daily_activity.find_one({"user_id": user_id, "date": today})
    if existing:
        await db.daily_activity.update_one(
            {"user_id": user_id, "date": today},
            {
                "$inc": {
                    "problems_solved": problems_solved,
                    "submissions_count": 1,
                    "elo_gained": elo_gained
                }
            }
        )
    else:
        await db.daily_activity.insert_one({
            "user_id": user_id,
            "date": today,
            "problems_solved": problems_solved,
            "submissions_count": 1,
            "elo_gained": elo_gained
        })

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
    
    # Validate code is not empty and has minimum content
    code_stripped = submission.code.strip()
    if not code_stripped or len(code_stripped) < 10:
        raise HTTPException(
            status_code=400, 
            detail="Code is too short. Please write a meaningful solution (minimum 10 characters)."
        )
    
    # Check if user has already solved this problem successfully
    existing_solved = await db.submissions.find_one({
        "user_id": user["user_id"],
        "problem_id": submission.problem_id,
        "status": "passed"
    })
    
    if existing_solved:
        raise HTTPException(
            status_code=400, 
            detail="You have already solved this problem. Each problem can only be solved once."
        )
    
    submission_id = f"sub_{uuid.uuid4().hex[:8]}"
    
    # Real code validation and testing
    try:
        all_passed, test_results, total_gas, error_message = await code_validator.validate_submission(
            code=submission.code,
            problem=problem,
            language=submission.language
        )
    except Exception as e:
        # If validator fails, return error
        all_passed = False
        test_results = [{
            "test_id": 0,
            "input": "Validation",
            "expected": "Success",
            "passed": False,
            "gas_used": 0,
            "error": f"Validation system error: {str(e)}"
        }]
        total_gas = 0
        error_message = str(e)
    
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
        
        # Update skills progress
        await update_skill_progress(user["user_id"], submission.problem_id)
        
        # Check and unlock achievements
        await check_and_unlock_achievements(user["user_id"])
        
        # Record daily activity
        await record_daily_activity(user["user_id"], problems_solved=1, elo_gained=elo_change)
    
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
        "error_message": error_message if not all_passed else None,
        "created_at": datetime.now(timezone.utc).isoformat()
    }
    
    await db.submissions.insert_one(submission_doc)
    submission_doc.pop("_id", None)
    
    return submission_doc

@api_router.get("/problems/{problem_id}/status")
async def get_problem_status(problem_id: str, user: dict = Depends(get_current_user)):
    """Check if user has solved this problem"""
    solved_submission = await db.submissions.find_one({
        "user_id": user["user_id"],
        "problem_id": problem_id,
        "status": "passed"
    }, {"_id": 0})
    
    return {
        "problem_id": problem_id,
        "is_solved": solved_submission is not None,
        "submission": solved_submission
    }


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
    
    # Get current rank info
    current_rank = await get_user_rank(user["user_id"])
    
    # Daily streak
    daily_streak = await calculate_daily_streak(user["user_id"])
    
    # Recent achievements (last 3)
    recent_achievements = await db.user_achievements.find(
        {"user_id": user["user_id"]},
        {"_id": 0}
    ).sort("unlocked_at", -1).limit(3).to_list(3)
    
    # Get achievement details
    recent_achievements_full = []
    for ach in recent_achievements:
        ach_details = next((a for a in ACHIEVEMENTS_LIST if a["achievement_id"] == ach["achievement_id"]), None)
        if ach_details:
            recent_achievements_full.append({
                **ach_details,
                "unlocked_at": ach["unlocked_at"]
            })
    
    return {
        "total_submissions": total_submissions,
        "passed_submissions": passed_submissions,
        "success_rate": round(passed_submissions / max(total_submissions, 1) * 100, 1),
        "elo_rating": user.get("elo_rating", 1200),
        "problems_solved": user.get("problems_solved", 0),
        "rank": rank,
        "total_users": total_users,
        "recent_submissions": recent_submissions,
        "problems_by_difficulty": problems_by_difficulty,
        "current_rank": current_rank,
        "daily_streak": daily_streak,
        "recent_achievements": recent_achievements_full
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
    from seed_problems import get_problems
    
    # Get comprehensive problem set
    problems = get_problems()
    
    # Also add some basic demo problems
    demo_problems = [
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
    
    # Combine demo and comprehensive problems
    all_problems = problems  # Use comprehensive set from seed_problems.py
    
    # Clear and insert
    await db.problems.delete_many({})
    await db.problems.insert_many(all_problems)
    
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
    
    return {"message": "Seeded successfully", "problems": len(all_problems), "hackathons": len(hackathons)}

# ============== SUBSCRIPTIONS ENDPOINTS ==============

@api_router.get("/subscriptions/plans")
async def get_subscription_plans():
    """Get available subscription plans"""
    plans = [
        {
            "id": "basic",
            "name": "Basic",
            "price": 0,
            "features": [
                "10 задач в месяц",
                "Базовый рейтинг",
                "Доступ к сообществу",
                "Просмотр лидерборда"
            ],
            "limits": {
                "problems_per_month": 10,
                "hackathons": False,
                "certificates": False
            }
        },
        {
            "id": "pro",
            "name": "Pro",
            "price": 29,
            "features": [
                "Неограниченные задачи",
                "Продвинутая аналитика",
                "Участие в хакатонах",
                "Приоритетная поддержка",
                "Детальная статистика по газу",
                "Сравнение с топ-разработчиками"
            ],
            "limits": {
                "problems_per_month": -1,  # unlimited
                "hackathons": True,
                "certificates": False
            }
        },
        {
            "id": "expert",
            "name": "Expert",
            "price": 99,
            "features": [
                "Всё из Pro +",
                "NFT сертификация",
                "Менторинг от экспертов",
                "Приватные соревнования",
                "Доступ к эксклюзивным задачам",
                "Прямой доступ к компаниям-партнёрам",
                "Персональные рекомендации"
            ],
            "limits": {
                "problems_per_month": -1,
                "hackathons": True,
                "certificates": True,
                "mentoring": True,
                "private_competitions": True
            }
        }
    ]
    return plans

@api_router.post("/subscriptions/upgrade")
async def upgrade_subscription(plan_id: str, user: dict = Depends(get_current_user)):
    """Upgrade user subscription"""
    valid_plans = ["basic", "pro", "expert"]
    if plan_id not in valid_plans:
        raise HTTPException(status_code=400, detail="Invalid plan")
    
    # In production, integrate with payment gateway (Stripe, etc.)
    await db.users.update_one(
        {"user_id": user["user_id"]},
        {"$set": {"subscription": plan_id, "subscription_updated_at": datetime.now(timezone.utc).isoformat()}}
    )
    
    updated_user = await db.users.find_one({"user_id": user["user_id"]}, {"_id": 0, "password_hash": 0})
    return updated_user

@api_router.get("/subscriptions/current")
async def get_current_subscription(user: dict = Depends(get_current_user)):
    """Get current subscription info"""
    subscription = user.get("subscription", "basic")
    
    # Calculate usage this month
    start_of_month = datetime.now(timezone.utc).replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    submissions_this_month = await db.submissions.count_documents({
        "user_id": user["user_id"],
        "created_at": {"$gte": start_of_month.isoformat()}
    })
    
    return {
        "plan": subscription,
        "problems_solved_this_month": submissions_this_month
    }

# ============== CERTIFICATES (NFT) ENDPOINTS ==============

class CertificateRequest(BaseModel):
    certificate_type: str  # "problem_master", "hackathon_winner", "expert_rating"
    metadata: dict = {}

@api_router.post("/certificates/mint")
async def mint_certificate(cert_request: CertificateRequest, user: dict = Depends(get_current_user)):
    """Mint NFT certificate on Polygon blockchain"""
    
    # Check if user has Expert subscription
    if user.get("subscription") != "expert":
        raise HTTPException(status_code=403, detail="Expert subscription required for NFT certificates")
    
    # Validate certificate type and criteria
    certificate_types = {
        "problem_master": {"min_problems": 50, "min_rating": 1500},
        "hackathon_winner": {"requires": "hackathon_win"},
        "expert_rating": {"min_rating": 2000},
        "security_expert": {"category": "security", "min_problems": 20},
        "gas_optimizer": {"category": "optimization", "min_problems": 15}
    }
    
    cert_type = cert_request.certificate_type
    if cert_type not in certificate_types:
        raise HTTPException(status_code=400, detail="Invalid certificate type")
    
    criteria = certificate_types[cert_type]
    
    # Verify user meets criteria
    if "min_problems" in criteria:
        if user.get("problems_solved", 0) < criteria["min_problems"]:
            raise HTTPException(status_code=400, detail=f"Need at least {criteria['min_problems']} solved problems")
    
    if "min_rating" in criteria:
        if user.get("elo_rating", 1200) < criteria["min_rating"]:
            raise HTTPException(status_code=400, detail=f"Need at least {criteria['min_rating']} ELO rating")
    
    # Generate certificate metadata
    certificate_id = f"cert_{uuid.uuid4().hex[:12]}"
    certificate_doc = {
        "certificate_id": certificate_id,
        "user_id": user["user_id"],
        "type": cert_type,
        "name": user.get("name"),
        "metadata": {
            "problems_solved": user.get("problems_solved", 0),
            "elo_rating": user.get("elo_rating", 1200),
            "issue_date": datetime.now(timezone.utc).isoformat(),
            **cert_request.metadata
        },
        # In production, this would be actual blockchain transaction
        "blockchain": "polygon",
        "contract_address": "0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb",  # Example
        "token_id": int(uuid.uuid4().hex[:8], 16),  # Simulated token ID
        "transaction_hash": f"0x{uuid.uuid4().hex}",  # Simulated tx hash
        "status": "minted",
        "created_at": datetime.now(timezone.utc).isoformat()
    }
    
    await db.certificates.insert_one(certificate_doc)
    certificate_doc.pop("_id", None)
    
    # Update user achievements
    await db.users.update_one(
        {"user_id": user["user_id"]},
        {"$push": {"achievements": cert_type}}
    )
    
    return certificate_doc

@api_router.get("/certificates")
async def get_user_certificates(user: dict = Depends(get_current_user)):
    """Get all certificates for current user"""
    certificates = await db.certificates.find(
        {"user_id": user["user_id"]},
        {"_id": 0}
    ).to_list(100)
    return certificates

@api_router.get("/certificates/{certificate_id}")
async def get_certificate(certificate_id: str):
    """Get specific certificate (public)"""
    certificate = await db.certificates.find_one({"certificate_id": certificate_id}, {"_id": 0})
    if not certificate:
        raise HTTPException(status_code=404, detail="Certificate not found")
    return certificate

@api_router.get("/certificates/verify/{token_id}")
async def verify_certificate(token_id: int):
    """Verify certificate authenticity by token ID"""
    certificate = await db.certificates.find_one({"token_id": token_id}, {"_id": 0})
    if not certificate:
        return {"valid": False, "message": "Certificate not found"}
    
    return {
        "valid": True,
        "certificate": certificate,
        "message": "Certificate is authentic"
    }


# ============== SKILLS ENDPOINTS ==============

@api_router.get("/skills/tree")
async def get_skill_tree():
    """Get complete skill tree structure"""
    return {"skills": SKILL_TREE}

@api_router.get("/skills/user-progress")
async def get_user_skill_progress(user: dict = Depends(get_current_user)):
    """Get user's progress across all skills"""
    user_skills = await db.user_skills.find({"user_id": user["user_id"]}, {"_id": 0}).to_list(100)
    
    # Build complete skill progress including locked skills
    skill_progress = []
    for skill in SKILL_TREE:
        user_skill = next((s for s in user_skills if s["skill_id"] == skill["skill_id"]), None)
        
        if user_skill:
            skill_progress.append({
                **skill,
                "progress": user_skill.get("progress", 0),
                "unlocked": user_skill.get("unlocked", False),
                "unlocked_at": user_skill.get("unlocked_at")
            })
        else:
            skill_progress.append({
                **skill,
                "progress": 0,
                "unlocked": False,
                "unlocked_at": None
            })
    
    return {"skills": skill_progress}

# ============== ACHIEVEMENTS ENDPOINTS ==============

@api_router.get("/achievements")
async def get_all_achievements():
    """Get list of all available achievements"""
    return {"achievements": ACHIEVEMENTS_LIST}

@api_router.get("/achievements/user")
async def get_user_achievements(user: dict = Depends(get_current_user)):
    """Get user's unlocked achievements"""
    user_achievements = user.get("achievements", [])
    
    # Get full achievement details
    unlocked = []
    locked = []
    
    for achievement in ACHIEVEMENTS_LIST:
        achievement_id = achievement["achievement_id"]
        if achievement_id in user_achievements:
            # Get unlock timestamp
            unlock_record = await db.user_achievements.find_one({
                "user_id": user["user_id"],
                "achievement_id": achievement_id
            })
            unlocked.append({
                **achievement,
                "unlocked": True,
                "unlocked_at": unlock_record.get("unlocked_at") if unlock_record else None
            })
        else:
            # Calculate progress for this achievement
            progress = await calculate_achievement_progress(user["user_id"], achievement)
            locked.append({
                **achievement,
                "unlocked": False,
                "progress": progress
            })
    
    return {
        "unlocked": unlocked,
        "locked": locked,
        "total": len(ACHIEVEMENTS_LIST),
        "unlocked_count": len(unlocked)
    }

async def calculate_achievement_progress(user_id: str, achievement: dict) -> dict:
    """Calculate progress towards an achievement"""
    user = await db.users.find_one({"user_id": user_id})
    if not user:
        return {"current": 0, "required": 0, "percentage": 0}
    
    criteria = achievement["criteria"]
    
    # Get user stats
    total_solved = user.get("problems_solved", 0)
    submissions = await db.submissions.find({"user_id": user_id, "status": "passed"}).to_list(None)
    
    solidity_count = len([s for s in submissions if await get_problem_category(s["problem_id"]) == "solidity"])
    rust_count = len([s for s in submissions if await get_problem_category(s["problem_id"]) == "rust"])
    expert_count = len([s for s in submissions if await get_problem_difficulty(s["problem_id"]) == "expert"])
    daily_streak = await calculate_daily_streak(user_id)
    
    # Count problems solved today
    today = datetime.now(timezone.utc).date().isoformat()
    problems_today = await db.submissions.count_documents({
        "user_id": user_id,
        "status": "passed",
        "created_at": {"$regex": f"^{today}"}
    })
    
    rank = await db.users.count_documents({"elo_rating": {"$gt": user.get("elo_rating", 0)}}) + 1
    
    user_stats = {
        "problems_solved": total_solved,
        "solidity_problems": solidity_count,
        "rust_problems": rust_count,
        "expert_problems": expert_count,
        "daily_streak": daily_streak,
        "problems_in_day": problems_today,
        "leaderboard_rank": rank
    }
    
    # Find the relevant stat and calculate progress
    for key, required in criteria.items():
        current = user_stats.get(key, 0)
        if key == "leaderboard_rank":
            # For rank, lower is better
            if current <= required:
                percentage = 100
            else:
                percentage = min(100, int((required / max(current, 1)) * 100))
        else:
            percentage = min(100, int((current / required) * 100))
        
        return {
            "current": current,
            "required": required,
            "percentage": percentage,
            "stat_name": key
        }
    
    return {"current": 0, "required": 0, "percentage": 0}

# ============== RANK ENDPOINTS ==============

@api_router.get("/user/rank")
async def get_current_user_rank(user: dict = Depends(get_current_user)):
    """Get user's current rank and progress to next rank"""
    current_rank = await get_user_rank(user["user_id"])
    
    # Find next rank
    next_rank = None
    for i, rank in enumerate(RANKS):
        if rank["rank_id"] == current_rank["rank_id"] and i < len(RANKS) - 1:
            next_rank = RANKS[i + 1]
            break
    
    # Calculate progress to next rank
    progress = None
    if next_rank:
        elo = user.get("elo_rating", 0)
        problems = user.get("problems_solved", 0)
        
        elo_progress = min(100, int((elo / next_rank["min_elo"]) * 100))
        problems_progress = min(100, int((problems / next_rank["min_problems"]) * 100))
        
        progress = {
            "elo": {"current": elo, "required": next_rank["min_elo"], "percentage": elo_progress},
            "problems": {"current": problems, "required": next_rank["min_problems"], "percentage": problems_progress},
            "overall": min(elo_progress, problems_progress)
        }
    
    return {
        "current_rank": current_rank,
        "next_rank": next_rank,
        "progress": progress
    }

@api_router.get("/ranks")
async def get_all_ranks():
    """Get all available ranks"""
    return {"ranks": RANKS}

# ============== ANALYTICS ENDPOINTS ==============

@api_router.get("/stats/activity-calendar")
async def get_activity_calendar(user: dict = Depends(get_current_user)):
    """Get daily activity for calendar heatmap (last 365 days)"""
    # Get activity for last year
    one_year_ago = (datetime.now(timezone.utc) - timedelta(days=365)).date().isoformat()
    
    activities = await db.daily_activity.find(
        {"user_id": user["user_id"], "date": {"$gte": one_year_ago}},
        {"_id": 0}
    ).to_list(365)
    
    # Create map of date -> activity
    activity_map = {act["date"]: act for act in activities}
    
    # Fill in all dates (including zeros)
    calendar_data = []
    for i in range(365):
        date = (datetime.now(timezone.utc).date() - timedelta(days=i)).isoformat()
        if date in activity_map:
            calendar_data.append(activity_map[date])
        else:
            calendar_data.append({
                "date": date,
                "problems_solved": 0,
                "submissions_count": 0,
                "elo_gained": 0
            })
    
    calendar_data.reverse()  # Oldest first
    
    return {"calendar": calendar_data}

@api_router.get("/stats/detailed")
async def get_detailed_stats(user: dict = Depends(get_current_user)):
    """Get comprehensive statistics"""
    submissions = await db.submissions.find({"user_id": user["user_id"]}, {"_id": 0}).to_list(None)
    passed_submissions = [s for s in submissions if s["status"] == "passed"]
    
    # By difficulty
    by_difficulty = {}
    for diff in ["junior", "middle", "senior", "expert"]:
        count = 0
        for sub in passed_submissions:
            problem = await db.problems.find_one({"problem_id": sub["problem_id"]})
            if problem and problem.get("difficulty") == diff:
                count += 1
        by_difficulty[diff] = count
    
    # By category
    by_category = {}
    for cat in ["solidity", "rust", "tvm", "crypto"]:
        count = 0
        for sub in passed_submissions:
            problem = await db.problems.find_one({"problem_id": sub["problem_id"]})
            if problem and problem.get("category") == cat:
                count += 1
        by_category[cat] = count
    
    # Success rate
    total = len(submissions)
    passed = len(passed_submissions)
    success_rate = round((passed / total * 100) if total > 0 else 0, 1)
    
    # Average gas usage
    avg_gas = 0
    if passed_submissions:
        total_gas = sum(s.get("gas_used", 0) for s in passed_submissions)
        avg_gas = round(total_gas / len(passed_submissions))
    
    # Streak info
    current_streak = await calculate_daily_streak(user["user_id"])
    
    # Time-based stats (last 7 days, 30 days)
    today = datetime.now(timezone.utc).date()
    week_ago = (today - timedelta(days=7)).isoformat()
    month_ago = (today - timedelta(days=30)).isoformat()
    
    week_solved = len([s for s in passed_submissions if s.get("created_at", "").split("T")[0] >= week_ago])
    month_solved = len([s for s in passed_submissions if s.get("created_at", "").split("T")[0] >= month_ago])
    
    # ELO progression (last 30 days)
    elo_history = []
    for i in range(30, -1, -1):
        date = (today - timedelta(days=i)).isoformat()
        # Get ELO at end of that day
        day_subs = [s for s in passed_submissions if s.get("created_at", "").split("T")[0] <= date]
        day_elo = 1200 + sum(s.get("elo_change", 0) for s in day_subs)
        elo_history.append({"date": date, "elo": day_elo})
    
    return {
        "total_submissions": total,
        "passed_submissions": passed,
        "success_rate": success_rate,
        "by_difficulty": by_difficulty,
        "by_category": by_category,
        "average_gas": avg_gas,
        "current_streak": current_streak,
        "week_solved": week_solved,
        "month_solved": month_solved,
        "elo_history": elo_history
    }

@api_router.get("/stats/compare")
async def get_comparative_stats(user: dict = Depends(get_current_user)):
    """Compare user stats with platform averages"""
    # User stats
    user_elo = user.get("elo_rating", 1200)
    user_solved = user.get("problems_solved", 0)
    
    # Platform averages
    all_users = await db.users.find({}, {"elo_rating": 1, "problems_solved": 1}).to_list(None)
    
    if all_users:
        avg_elo = sum(u.get("elo_rating", 1200) for u in all_users) / len(all_users)
        avg_solved = sum(u.get("problems_solved", 0) for u in all_users) / len(all_users)
    else:
        avg_elo = 1200
        avg_solved = 0
    
    # User rank
    rank = await db.users.count_documents({"elo_rating": {"$gt": user_elo}}) + 1
    total_users = len(all_users)
    percentile = 100 - (rank / max(total_users, 1) * 100)
    
    return {
        "user": {
            "elo": user_elo,
            "problems_solved": user_solved,
            "rank": rank,
            "percentile": round(percentile, 1)
        },
        "platform_average": {
            "elo": round(avg_elo),
            "problems_solved": round(avg_solved, 1)
        },
        "comparison": {
            "elo_diff": user_elo - avg_elo,
            "problems_diff": user_solved - avg_solved
        }
    }

# ============== RECOMMENDATIONS ENDPOINTS ==============

@api_router.get("/recommendations/next-problem")
async def get_next_problem_recommendation(user: dict = Depends(get_current_user)):
    """Get personalized problem recommendation"""
    elo = user.get("elo_rating", 1200)
    problems_solved = user.get("problems_solved", 0)
    
    # Get user's solved problems
    solved_submissions = await db.submissions.find({
        "user_id": user["user_id"],
        "status": "passed"
    }, {"problem_id": 1}).to_list(None)
    solved_ids = [s["problem_id"] for s in solved_submissions]
    
    # Get user's skill progress
    user_skills = await db.user_skills.find({"user_id": user["user_id"]}, {"_id": 0}).to_list(100)
    
    # Find weakest skills (areas for improvement)
    skill_scores = {}
    for skill in user_skills:
        skill_scores[skill["skill_id"]] = skill.get("progress", 0)
    
    # Determine appropriate difficulty
    if elo < 1300:
        target_difficulty = "junior"
    elif elo < 1500:
        target_difficulty = "middle"
    elif elo < 1700:
        target_difficulty = "senior"
    else:
        target_difficulty = "expert"
    
    # Find unsolved problems at appropriate difficulty
    query = {
        "difficulty": target_difficulty,
        "problem_id": {"$nin": solved_ids}
    }
    
    # Prioritize problems that help with weak skills
    weakest_skill = min(skill_scores.items(), key=lambda x: x[1])[0] if skill_scores else None
    if weakest_skill:
        # Map skill to category
        skill_category_map = {
            "sol_basics": "solidity", "sol_storage": "solidity", "sol_security": "solidity",
            "sol_gas": "solidity", "erc20": "solidity", "erc721": "solidity", "defi": "solidity",
            "rust_basics": "rust", "solana_prog": "rust",
            "func_basics": "tvm", "crypto_basics": "crypto"
        }
        category = skill_category_map.get(weakest_skill)
        if category:
            query["category"] = category
    
    recommended_problems = await db.problems.find(query, {"_id": 0}).limit(5).to_list(5)
    
    # If no problems found at strict criteria, relax it
    if not recommended_problems:
        query.pop("category", None)
        recommended_problems = await db.problems.find(query, {"_id": 0}).limit(5).to_list(5)
    
    reason = f"Based on your ELO ({elo}), these {target_difficulty}-level problems are perfect for you."
    if weakest_skill:
        reason += f" Focusing on improving your {weakest_skill} skill."
    
    return {
        "recommendations": recommended_problems,
        "reason": reason,
        "target_difficulty": target_difficulty
    }

@api_router.get("/insights/personal")
async def get_personal_insights(user: dict = Depends(get_current_user)):
    """Get personalized insights and suggestions"""
    user_id = user["user_id"]
    elo = user.get("elo_rating", 1200)
    problems_solved = user.get("problems_solved", 0)
    
    # Get streak info
    current_streak = await calculate_daily_streak(user_id)
    
    # Get recent activity (last 7 days)
    week_ago = (datetime.now(timezone.utc) - timedelta(days=7)).date().isoformat()
    recent_submissions = await db.submissions.find({
        "user_id": user_id,
        "status": "passed",
        "created_at": {"$gte": week_ago}
    }).to_list(None)
    
    # Get user's weakest areas
    user_skills = await db.user_skills.find({"user_id": user_id}).to_list(None)
    skill_progress = {skill["skill_id"]: skill.get("progress", 0) for skill in user_skills}
    
    weakest_skills = sorted(skill_progress.items(), key=lambda x: x[1])[:3] if skill_progress else []
    strongest_skills = sorted(skill_progress.items(), key=lambda x: x[1], reverse=True)[:3] if skill_progress else []
    
    # Calculate velocity (problems per week)
    velocity = len(recent_submissions)
    
    # Get rank and percentile
    rank = await db.users.count_documents({"elo_rating": {"$gt": elo}}) + 1
    total_users = await db.users.count_documents({})
    percentile = 100 - (rank / max(total_users, 1) * 100)
    
    # Generate insights
    insights = []
    
    # Streak insight
    if current_streak >= 7:
        insights.append({
            "type": "positive",
            "icon": "🔥",
            "title": "Amazing Consistency!",
            "message": f"You're on a {current_streak}-day streak. Keep the momentum going!"
        })
    elif current_streak == 0:
        insights.append({
            "type": "reminder",
            "icon": "⏰",
            "title": "Time to Practice",
            "message": "Solve a problem today to start your streak!"
        })
    
    # Velocity insight
    if velocity >= 10:
        insights.append({
            "type": "positive",
            "icon": "⚡",
            "title": "High Velocity!",
            "message": f"You've solved {velocity} problems this week. Outstanding work!"
        })
    elif velocity == 0:
        insights.append({
            "type": "reminder",
            "icon": "📚",
            "title": "Let's Get Started",
            "message": "You haven't solved any problems this week. Start now to build momentum!"
        })
    
    # ELO progression insight
    if elo >= 1500:
        insights.append({
            "type": "positive",
            "icon": "🏆",
            "title": "Expert Level",
            "message": f"You're in the top {100 - percentile:.1f}% of all users!"
        })
    
    # Skill development insight
    if weakest_skills:
        skill_name = weakest_skills[0][0].replace("_", " ").title()
        insights.append({
            "type": "suggestion",
            "icon": "🎯",
            "title": "Growth Opportunity",
            "message": f"Focus on {skill_name} to become more well-rounded."
        })
    
    # Next milestone
    next_elo_milestone = ((elo // 100) + 1) * 100
    elo_to_milestone = next_elo_milestone - elo
    if elo_to_milestone <= 50:
        insights.append({
            "type": "motivation",
            "icon": "🎖️",
            "title": "Milestone Ahead",
            "message": f"Just {elo_to_milestone} ELO away from reaching {next_elo_milestone}!"
        })
    
    return {
        "insights": insights,
        "stats": {
            "current_streak": current_streak,
            "weekly_velocity": velocity,
            "percentile": round(percentile, 1),
            "weakest_skills": [{"skill_id": s[0], "progress": s[1]} for s in weakest_skills],
            "strongest_skills": [{"skill_id": s[0], "progress": s[1]} for s in strongest_skills]
        }
    }

# ============== DAILY CHALLENGES ENDPOINTS ==============

@api_router.get("/challenges/daily")
async def get_daily_challenges(user: dict = Depends(get_current_user)):
    """Get today's daily challenges"""
    user_id = user["user_id"]
    today = datetime.now(timezone.utc).date().isoformat()
    
    # Check if daily challenges already exist for today
    existing_challenges = await db.daily_challenges.find_one({
        "user_id": user_id,
        "date": today
    })
    
    if existing_challenges:
        return {
            "date": today,
            "challenges": existing_challenges.get("challenges", []),
            "completed": existing_challenges.get("completed", 0),
            "total": 3,
            "bonus_earned": existing_challenges.get("bonus_earned", False)
        }
    
    # Generate new daily challenges
    user_elo = user.get("elo_rating", 1200)
    
    # Determine appropriate difficulties
    if user_elo < 1300:
        difficulties = ["junior", "junior", "middle"]
    elif user_elo < 1600:
        difficulties = ["junior", "middle", "senior"]
    else:
        difficulties = ["middle", "senior", "expert"]
    
    # Get solved problem IDs
    solved_ids = []
    solved_subs = await db.submissions.find(
        {"user_id": user_id, "status": "passed"},
        {"problem_id": 1}
    ).to_list(None)
    solved_ids = [s["problem_id"] for s in solved_subs]
    
    challenges = []
    for i, diff in enumerate(difficulties):
        # Find unsolved problem
        problem = await db.problems.find_one({
            "difficulty": diff,
            "problem_id": {"$nin": solved_ids + [c.get("problem_id") for c in challenges]}
        }, {"_id": 0})
        
        if problem:
            bonus_elo = {"junior": 5, "middle": 10, "senior": 15, "expert": 25}
            challenges.append({
                "challenge_id": f"daily_{today}_{i+1}",
                "problem_id": problem["problem_id"],
                "title": problem["title"],
                "difficulty": problem["difficulty"],
                "category": problem["category"],
                "bonus_elo": bonus_elo.get(diff, 5),
                "completed": False
            })
    
    # Store challenges
    await db.daily_challenges.insert_one({
        "user_id": user_id,
        "date": today,
        "challenges": challenges,
        "completed": 0,
        "bonus_earned": False,
        "created_at": datetime.now(timezone.utc).isoformat()
    })
    
    return {
        "date": today,
        "challenges": challenges,
        "completed": 0,
        "total": len(challenges),
        "bonus_earned": False
    }

@api_router.post("/challenges/daily/complete/{problem_id}")
async def complete_daily_challenge(problem_id: str, user: dict = Depends(get_current_user)):
    """Mark a daily challenge as complete"""
    user_id = user["user_id"]
    today = datetime.now(timezone.utc).date().isoformat()
    
    # Get today's challenges
    daily_record = await db.daily_challenges.find_one({
        "user_id": user_id,
        "date": today
    })
    
    if not daily_record:
        raise HTTPException(status_code=404, detail="No daily challenges found for today")
    
    challenges = daily_record.get("challenges", [])
    challenge_index = next((i for i, c in enumerate(challenges) if c["problem_id"] == problem_id), None)
    
    if challenge_index is None:
        raise HTTPException(status_code=404, detail="Problem is not in today's challenges")
    
    # Mark challenge as completed
    challenges[challenge_index]["completed"] = True
    completed_count = sum(1 for c in challenges if c["completed"])
    
    # Award bonus if all challenges completed
    bonus_earned = False
    if completed_count == len(challenges) and not daily_record.get("bonus_earned"):
        # Award completion bonus
        total_bonus = sum(c["bonus_elo"] for c in challenges)
        await db.users.update_one(
            {"user_id": user_id},
            {"$inc": {"elo_rating": total_bonus}}
        )
        bonus_earned = True
    
    # Update record
    await db.daily_challenges.update_one(
        {"user_id": user_id, "date": today},
        {
            "$set": {
                "challenges": challenges,
                "completed": completed_count,
                "bonus_earned": bonus_earned
            }
        }
    )
    
    return {
        "completed": completed_count,
        "total": len(challenges),
        "bonus_earned": bonus_earned,
        "bonus_elo": sum(c["bonus_elo"] for c in challenges) if bonus_earned else 0
    }

# ============== PROBLEM ANALYTICS ENDPOINTS ==============

@api_router.get("/problems/{problem_id}/analytics")
async def get_problem_analytics(problem_id: str, user: dict = Depends(get_current_user)):
    """Get detailed analytics for a specific problem"""
    user_id = user["user_id"]
    
    # Get problem details
    problem = await db.problems.find_one({"problem_id": problem_id}, {"_id": 0})
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")
    
    # Get all user's submissions for this problem
    user_submissions = await db.submissions.find({
        "user_id": user_id,
        "problem_id": problem_id
    }, {"_id": 0}).sort("created_at", 1).to_list(None)
    
    attempts_count = len(user_submissions)
    passed_submission = next((s for s in user_submissions if s["status"] == "passed"), None)
    
    # Calculate time spent (if solved)
    time_spent_minutes = None
    if passed_submission and attempts_count > 0:
        first_attempt = user_submissions[0]
        last_attempt = passed_submission
        first_time = datetime.fromisoformat(first_attempt["created_at"])
        last_time = datetime.fromisoformat(last_attempt["created_at"])
        time_spent_minutes = int((last_time - first_time).total_seconds() / 60)
    
    # Get global statistics
    all_submissions = await db.submissions.find({"problem_id": problem_id}).to_list(None)
    total_attempts = len(all_submissions)
    successful_submissions = [s for s in all_submissions if s["status"] == "passed"]
    success_count = len(successful_submissions)
    success_rate = (success_count / max(total_attempts, 1)) * 100
    
    # Calculate average gas and time
    avg_gas = sum(s.get("gas_used", 0) for s in successful_submissions) / max(success_count, 1)
    avg_time_ms = sum(s.get("execution_time_ms", 0) for s in successful_submissions) / max(success_count, 1)
    
    # User's best performance
    user_performance = None
    if passed_submission:
        user_gas = passed_submission.get("gas_used", 0)
        user_time_ms = passed_submission.get("execution_time_ms", 0)
        
        # Calculate efficiency score (lower is better)
        gas_efficiency = (user_gas / max(avg_gas, 1)) * 100
        time_efficiency = (user_time_ms / max(avg_time_ms, 1)) * 100
        overall_efficiency = (gas_efficiency + time_efficiency) / 2
        
        # Rank among all solvers
        better_solutions = 0
        for sub in successful_submissions:
            sub_gas = sub.get("gas_used", 0)
            sub_time = sub.get("execution_time_ms", 0)
            sub_score = (sub_gas / max(avg_gas, 1) + sub_time / max(avg_time_ms, 1)) / 2
            if sub_score < (gas_efficiency + time_efficiency) / 200:
                better_solutions += 1
        
        user_rank = better_solutions + 1
        
        user_performance = {
            "gas_used": user_gas,
            "execution_time_ms": user_time_ms,
            "gas_efficiency_percentile": 100 - gas_efficiency if gas_efficiency <= 100 else 0,
            "time_efficiency_percentile": 100 - time_efficiency if time_efficiency <= 100 else 0,
            "overall_efficiency_score": round(overall_efficiency, 1),
            "rank_among_solvers": user_rank,
            "total_solvers": success_count
        }
    
    return {
        "problem": problem,
        "user_stats": {
            "attempts": attempts_count,
            "solved": passed_submission is not None,
            "time_spent_minutes": time_spent_minutes,
            "performance": user_performance
        },
        "global_stats": {
            "total_attempts": total_attempts,
            "success_count": success_count,
            "success_rate": round(success_rate, 1),
            "avg_gas_used": round(avg_gas, 0),
            "avg_execution_time_ms": round(avg_time_ms, 0)
        }
    }

# ============== FRIENDS & SOCIAL ENDPOINTS ==============

@api_router.post("/friends/add/{friend_id}")
async def add_friend(friend_id: str, user: dict = Depends(get_current_user)):
    """Send friend request"""
    user_id = user["user_id"]
    
    if user_id == friend_id:
        raise HTTPException(status_code=400, detail="Cannot add yourself as friend")
    
    # Check if friend exists
    friend = await db.users.find_one({"user_id": friend_id})
    if not friend:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Check if already friends or request pending
    existing = await db.friendships.find_one({
        "$or": [
            {"user_id": user_id, "friend_id": friend_id},
            {"user_id": friend_id, "friend_id": user_id}
        ]
    })
    
    if existing:
        if existing.get("status") == "accepted":
            raise HTTPException(status_code=400, detail="Already friends")
        else:
            raise HTTPException(status_code=400, detail="Friend request already sent")
    
    # Create friendship request
    await db.friendships.insert_one({
        "user_id": user_id,
        "friend_id": friend_id,
        "status": "pending",
        "created_at": datetime.now(timezone.utc).isoformat()
    })
    
    return {"message": "Friend request sent"}

@api_router.post("/friends/accept/{user_id}")
async def accept_friend_request(user_id: str, user: dict = Depends(get_current_user)):
    """Accept friend request"""
    friend_id = user["user_id"]
    
    # Find pending request
    request_doc = await db.friendships.find_one({
        "user_id": user_id,
        "friend_id": friend_id,
        "status": "pending"
    })
    
    if not request_doc:
        raise HTTPException(status_code=404, detail="Friend request not found")
    
    # Update status
    await db.friendships.update_one(
        {"user_id": user_id, "friend_id": friend_id},
        {"$set": {"status": "accepted", "accepted_at": datetime.now(timezone.utc).isoformat()}}
    )
    
    return {"message": "Friend request accepted"}

@api_router.get("/friends/list")
async def get_friends_list(user: dict = Depends(get_current_user)):
    """Get list of friends"""
    user_id = user["user_id"]
    
    # Find all accepted friendships
    friendships = await db.friendships.find({
        "$or": [
            {"user_id": user_id, "status": "accepted"},
            {"friend_id": user_id, "status": "accepted"}
        ]
    }).to_list(None)
    
    friend_ids = []
    for fs in friendships:
        friend_id = fs["friend_id"] if fs["user_id"] == user_id else fs["user_id"]
        friend_ids.append(friend_id)
    
    # Get friend details
    friends = await db.users.find(
        {"user_id": {"$in": friend_ids}},
        {"_id": 0, "user_id": 1, "name": 1, "picture": 1, "elo_rating": 1, "problems_solved": 1}
    ).to_list(None)
    
    return {"friends": friends, "count": len(friends)}

@api_router.get("/friends/requests")
async def get_friend_requests(user: dict = Depends(get_current_user)):
    """Get pending friend requests"""
    user_id = user["user_id"]
    
    # Find pending requests where user is the recipient
    requests = await db.friendships.find({
        "friend_id": user_id,
        "status": "pending"
    }).to_list(None)
    
    # Get requester details
    requester_ids = [r["user_id"] for r in requests]
    requesters = await db.users.find(
        {"user_id": {"$in": requester_ids}},
        {"_id": 0, "user_id": 1, "name": 1, "picture": 1, "elo_rating": 1}
    ).to_list(None)
    
    return {"requests": requesters, "count": len(requesters)}

@api_router.get("/friends/compare/{friend_id}")
async def compare_with_friend(friend_id: str, user: dict = Depends(get_current_user)):
    """Compare stats with a friend"""
    user_id = user["user_id"]
    
    # Verify friendship
    friendship = await db.friendships.find_one({
        "$or": [
            {"user_id": user_id, "friend_id": friend_id, "status": "accepted"},
            {"user_id": friend_id, "friend_id": user_id, "status": "accepted"}
        ]
    })
    
    if not friendship:
        raise HTTPException(status_code=403, detail="Not friends with this user")
    
    # Get both users' stats
    friend = await db.users.find_one({"user_id": friend_id}, {"_id": 0})
    if not friend:
        raise HTTPException(status_code=404, detail="Friend not found")
    
    # Get detailed stats for both
    user_submissions = await db.submissions.find({"user_id": user_id, "status": "passed"}).to_list(None)
    friend_submissions = await db.submissions.find({"user_id": friend_id, "status": "passed"}).to_list(None)
    
    user_streak = await calculate_daily_streak(user_id)
    friend_streak = await calculate_daily_streak(friend_id)
    
    comparison = {
        "user": {
            "user_id": user_id,
            "name": user["name"],
            "picture": user.get("picture"),
            "elo": user.get("elo_rating", 1200),
            "problems_solved": user.get("problems_solved", 0),
            "daily_streak": user_streak,
            "submissions_count": len(user_submissions)
        },
        "friend": {
            "user_id": friend_id,
            "name": friend["name"],
            "picture": friend.get("picture"),
            "elo": friend.get("elo_rating", 1200),
            "problems_solved": friend.get("problems_solved", 0),
            "daily_streak": friend_streak,
            "submissions_count": len(friend_submissions)
        },
        "differences": {
            "elo": user.get("elo_rating", 1200) - friend.get("elo_rating", 1200),
            "problems_solved": user.get("problems_solved", 0) - friend.get("problems_solved", 0),
            "streak": user_streak - friend_streak
        }
    }
    
    return comparison

# ============== ADVANCED LEADERBOARD ENDPOINTS ==============

@api_router.get("/leaderboard/by-category/{category}")
async def get_category_leaderboard(category: str, limit: int = 100):
    """Get leaderboard filtered by technology category"""
    # Get all users with their submissions
    pipeline = [
        {
            "$lookup": {
                "from": "submissions",
                "let": {"user_id": "$user_id"},
                "pipeline": [
                    {
                        "$match": {
                            "$expr": {"$eq": ["$user_id", "$$user_id"]},
                            "status": "passed"
                        }
                    },
                    {
                        "$lookup": {
                            "from": "problems",
                            "localField": "problem_id",
                            "foreignField": "problem_id",
                            "as": "problem"
                        }
                    },
                    {"$unwind": "$problem"},
                    {"$match": {"problem.category": category}}
                ],
                "as": "category_submissions"
            }
        },
        {
            "$addFields": {
                "category_problems_solved": {"$size": "$category_submissions"}
            }
        },
        {"$match": {"category_problems_solved": {"$gt": 0}}},
        {"$sort": {"category_problems_solved": -1, "elo_rating": -1}},
        {"$limit": limit},
        {
            "$project": {
                "_id": 0,
                "user_id": 1,
                "name": 1,
                "picture": 1,
                "elo_rating": 1,
                "category_problems_solved": 1
            }
        }
    ]
    
    users = await db.users.aggregate(pipeline).to_list(limit)
    
    leaderboard = []
    for i, user_data in enumerate(users):
        leaderboard.append({
            "rank": i + 1,
            **user_data
        })
    
    return {"category": category, "leaderboard": leaderboard}

@api_router.get("/leaderboard/by-period/{period}")
async def get_period_leaderboard(period: str, limit: int = 100):
    """Get leaderboard for a specific time period (week, month, year)"""
    now = datetime.now(timezone.utc)
    
    if period == "week":
        start_date = (now - timedelta(days=7)).isoformat()
    elif period == "month":
        start_date = (now - timedelta(days=30)).isoformat()
    elif period == "year":
        start_date = (now - timedelta(days=365)).isoformat()
    else:
        raise HTTPException(status_code=400, detail="Invalid period. Use: week, month, or year")
    
    # Get users with submissions in period
    pipeline = [
        {
            "$lookup": {
                "from": "submissions",
                "let": {"user_id": "$user_id"},
                "pipeline": [
                    {
                        "$match": {
                            "$expr": {"$eq": ["$user_id", "$$user_id"]},
                            "status": "passed",
                            "created_at": {"$gte": start_date}
                        }
                    }
                ],
                "as": "period_submissions"
            }
        },
        {
            "$addFields": {
                "period_problems_solved": {"$size": "$period_submissions"},
                "period_elo_gained": {"$sum": "$period_submissions.elo_change"}
            }
        },
        {"$match": {"period_problems_solved": {"$gt": 0}}},
        {"$sort": {"period_problems_solved": -1, "period_elo_gained": -1}},
        {"$limit": limit},
        {
            "$project": {
                "_id": 0,
                "user_id": 1,
                "name": 1,
                "picture": 1,
                "elo_rating": 1,
                "period_problems_solved": 1,
                "period_elo_gained": 1
            }
        }
    ]
    
    users = await db.users.aggregate(pipeline).to_list(limit)
    
    leaderboard = []
    for i, user_data in enumerate(users):
        leaderboard.append({
            "rank": i + 1,
            **user_data
        })
    
    return {"period": period, "start_date": start_date, "leaderboard": leaderboard}

# ============== NOTIFICATIONS ENDPOINTS ==============

@api_router.get("/notifications")
async def get_notifications(user: dict = Depends(get_current_user), limit: int = 20):
    """Get user notifications"""
    user_id = user["user_id"]
    
    notifications = await db.notifications.find(
        {"user_id": user_id},
        {"_id": 0}
    ).sort("created_at", -1).limit(limit).to_list(limit)
    
    unread_count = await db.notifications.count_documents({
        "user_id": user_id,
        "read": False
    })
    
    return {
        "notifications": notifications,
        "unread_count": unread_count
    }

@api_router.post("/notifications/{notification_id}/read")
async def mark_notification_read(notification_id: str, user: dict = Depends(get_current_user)):
    """Mark notification as read"""
    result = await db.notifications.update_one(
        {"notification_id": notification_id, "user_id": user["user_id"]},
        {"$set": {"read": True}}
    )
    
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Notification not found")
    
    return {"message": "Notification marked as read"}

async def create_notification(user_id: str, type: str, title: str, message: str, data: dict = None):
    """Helper function to create notifications"""
    notification = {
        "notification_id": f"notif_{uuid.uuid4().hex[:12]}",
        "user_id": user_id,
        "type": type,
        "title": title,
        "message": message,
        "data": data or {},
        "read": False,
        "created_at": datetime.now(timezone.utc).isoformat()
    }
    await db.notifications.insert_one(notification)
    return notification

# ============== RANKS ENDPOINTS ==============

@api_router.get("/ranks/all")
async def get_all_ranks():
    """Get all available ranks"""
    return {"ranks": RANKS}

@api_router.get("/ranks/next")
async def get_next_rank(user: dict = Depends(get_current_user)):
    """Get information about next rank"""
    current_rank = await get_user_rank(user["user_id"])
    
    # Find next rank
    current_index = next((i for i, r in enumerate(RANKS) if r["rank_id"] == current_rank["rank_id"]), 0)
    
    if current_index < len(RANKS) - 1:
        next_rank = RANKS[current_index + 1]
        elo_needed = next_rank["min_elo"] - user.get("elo_rating", 1200)
        problems_needed = next_rank["min_problems"] - user.get("problems_solved", 0)
        
        return {
            "current_rank": current_rank,
            "next_rank": next_rank,
            "requirements": {
                "elo_needed": max(0, elo_needed),
                "problems_needed": max(0, problems_needed)
            },
            "progress": {
                "elo_progress": min(100, (user.get("elo_rating", 1200) / next_rank["min_elo"]) * 100),
                "problems_progress": min(100, (user.get("problems_solved", 0) / next_rank["min_problems"]) * 100)
            }
        }
    else:
        return {
            "current_rank": current_rank,
            "next_rank": None,
            "message": "You've reached the highest rank!"
        }

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
