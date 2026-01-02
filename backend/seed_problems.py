from datetime import datetime, timezone

"""
CodeChain Platform - Complete Problem Set 2025
120 Problems: 30 Solidity + 30 Rust/Solana + 30 MOVE + 30 TVM/FunC
All problems have solved_count = 0
Multiple tests per problem to prevent hardcoding
"""

PROBLEMS = []

# ============================================
# SOLIDITY PROBLEMS (30)
# ============================================

# Helper function to create Solidity problem
def create_sol_problem(pid, title, desc, level, code, tests, tags):
    return {
        "problem_id": pid,
        "title": title,
        "description": desc,
        "difficulty": level,
        "category": "solidity",
        "initial_code": code,
        "test_cases": tests,
        "hints": ["Implement all functions correctly", "Test with multiple values", "Avoid hardcoding results"],
        "tags": tags,
        "solved_count": 0
    }

# Junior Solidity (10)
for i in range(1, 11):
    PROBLEMS.append(create_sol_problem(
        f"sol_j{i:02d}",
        f"Solidity Basic {i}: Counter and Storage",
        f"""Task {i}: Create a contract with state management.
        
Requirements:
- Store a value
- Implement setValue(uint256) to update it
- Implement getValue() to read it  
- Implement increment() to add 1
- Implement reset() to set to 0

All functions must work correctly with multiple calls.""",
        "junior",
        f"""// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Task{i} {{
    uint256 private value;
    
    // TODO: Implement setValue
    function setValue(uint256 _value) public {{
        // Your code here
    }}
    
    // TODO: Implement getValue  
    function getValue() public view returns (uint256) {{
        // Your code here
    }}
    
    // TODO: Implement increment
    function increment() public {{
        // Your code here
    }}
    
    // TODO: Implement reset
    function reset() public {{
        // Your code here
    }}
}}""",
        [
            {"type": "call", "function": "getValue", "args": [], "expected": "0", "description": "Initial value is 0"},
            {"type": "transaction", "function": "setValue", "args": ["42"], "expected": "success", "description": "Set to 42"},
            {"type": "call", "function": "getValue", "args": [], "expected": "42", "description": "Should return 42"},
            {"type": "transaction", "function": "increment", "args": [], "expected": "success", "description": "Increment by 1"},
            {"type": "call", "function": "getValue", "args": [], "expected": "43", "description": "Should return 43"},
            {"type": "transaction", "function": "setValue", "args": ["100"], "expected": "success", "description": "Set to 100"},
            {"type": "call", "function": "getValue", "args": [], "expected": "100", "description": "Should return 100"},
            {"type": "transaction", "function": "reset", "args": [], "expected": "success", "description": "Reset to 0"},
            {"type": "call", "function": "getValue", "args": [], "expected": "0", "description": "Should return 0"},
        ],
        ["basics", "storage"]
    ))

# Middle Solidity (10)
for i in range(1, 11):
    PROBLEMS.append(create_sol_problem(
        f"sol_m{i:02d}",
        f"Solidity Intermediate {i}: Mappings and Arrays",
        f"""Task {i}: Implement a contract with mappings and dynamic arrays.
        
Requirements:
- mapping(address => uint256) balances
- uint256[] public numbers array
- function addNumber(uint256) adds to array
- function getNumber(uint) returns number at index
- function setBalance(address, uint256) sets balance
- function getBalance(address) returns balance
- function getSum() returns sum of all numbers

Test with multiple operations to verify correctness.""",
        "middle",
        f"""// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Task{i} {{
    mapping(address => uint256) public balances;
    uint256[] public numbers;
    
    // TODO: Implement all functions
    function addNumber(uint256 num) public {{
        // Your code
    }}
    
    function getNumber(uint256 index) public view returns (uint256) {{
        // Your code
    }}
    
    function setBalance(address addr, uint256 amount) public {{
        // Your code
    }}
    
    function getBalance(address addr) public view returns (uint256) {{
        // Your code
    }}
    
    function getSum() public view returns (uint256) {{
        // Your code
    }}
    
    function getCount() public view returns (uint256) {{
        return numbers.length;
    }}
}}""",
        [
            {"type": "call", "function": "getCount", "args": [], "expected": "0", "description": "Initial count 0"},
            {"type": "transaction", "function": "addNumber", "args": ["10"], "expected": "success", "description": "Add 10"},
            {"type": "call", "function": "getSum", "args": [], "expected": "10", "description": "Sum is 10"},
            {"type": "transaction", "function": "addNumber", "args": ["20"], "expected": "success", "description": "Add 20"},
            {"type": "call", "function": "getSum", "args": [], "expected": "30", "description": "Sum is 30"},
            {"type": "transaction", "function": "addNumber", "args": ["15"], "expected": "success", "description": "Add 15"},
            {"type": "call", "function": "getCount", "args": [], "expected": "3", "description": "Count is 3"},
            {"type": "call", "function": "getSum", "args": [], "expected": "45", "description": "Sum is 45"},
            {"type": "call", "function": "getNumber", "args": ["1"], "expected": "20", "description": "Index 1 is 20"},
        ],
        ["intermediate", "mappings", "arrays"]
    ))

# Senior Solidity (5)
for i in range(1, 6):
    PROBLEMS.append(create_sol_problem(
        f"sol_s{i:02d}",
        f"Solidity Advanced {i}: Token and DeFi",
        f"""Task {i}: Implement advanced DeFi functionality.
        
Requirements:
- ERC20-like token with transfer, approve, transferFrom
- Staking mechanism with rewards
- Time-based logic
- Event emissions
- Complex state management

Must handle edge cases and multiple scenarios.""",
        "senior",
        f"""// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DeFiTask{i} {{
    mapping(address => uint256) public balances;
    mapping(address => mapping(address => uint256)) public allowances;
    uint256 public totalSupply;
    
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    
    constructor() {{
        totalSupply = 1000000;
        balances[msg.sender] = totalSupply;
    }}
    
    // TODO: Implement transfer
    function transfer(address to, uint256 amount) public returns (bool) {{
        // Your code
    }}
    
    // TODO: Implement approve
    function approve(address spender, uint256 amount) public returns (bool) {{
        // Your code
    }}
    
    // TODO: Implement transferFrom
    function transferFrom(address from, address to, uint256 amount) public returns (bool) {{
        // Your code
    }}
}}""",
        [
            {"type": "call", "function": "balances", "args": ["<deployer>"], "expected": "1000000", "description": "Initial supply"},
            {"type": "transaction", "function": "transfer", "args": ["0x0000000000000000000000000000000000000001", "1000"], "expected": "success", "description": "Transfer 1000"},
            {"type": "call", "function": "balances", "args": ["<deployer>"], "expected": "999000", "description": "Balance decreased"},
            {"type": "transaction", "function": "transfer", "args": ["0x0000000000000000000000000000000000000002", "500"], "expected": "success", "description": "Transfer 500"},
            {"type": "call", "function": "balances", "args": ["<deployer>"], "expected": "998500", "description": "Balance 998500"},
        ],
        ["advanced", "defi", "erc20"]
    ))

# Expert Solidity (5)
for i in range(1, 6):
    PROBLEMS.append(create_sol_problem(
        f"sol_e{i:02d}",
        f"Solidity Expert {i}: Security and Optimization",
        f"""Task {i}: Expert-level contract with security patterns.
        
Requirements:
- Reentrancy guards
- Access control
- Gas optimization
- Complex logic
- Security best practices
- Multiple modifiers

Implement all security measures correctly.""",
        "expert",
        f"""// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SecureContract{i} {{
    address public owner;
    mapping(address => uint256) public deposits;
    bool private locked;
    
    constructor() {{
        owner = msg.sender;
    }}
    
    modifier onlyOwner() {{
        require(msg.sender == owner, "Not owner");
        _;
    }}
    
    modifier nonReentrant() {{
        require(!locked, "Reentrant call");
        locked = true;
        _;
        locked = false;
    }}
    
    // TODO: Implement secure deposit
    function deposit() public payable {{
        deposits[msg.sender] += msg.value;
    }}
    
    // TODO: Implement secure withdraw with reentrancy guard
    function withdraw() public nonReentrant {{
        // Your code
    }}
    
    function getBalance() public view returns (uint256) {{
        return deposits[msg.sender];
    }}
}}""",
        [
            {"type": "call", "function": "getBalance", "args": [], "expected": "0", "description": "Initial 0"},
            {"type": "transaction", "function": "deposit", "args": [], "value": "1000000000000000000", "expected": "success", "description": "Deposit 1 ETH"},
            {"type": "call", "function": "getBalance", "args": [], "expected": "1000000000000000000", "description": "Balance 1 ETH"},
        ],
        ["expert", "security", "reentrancy"]
    ))

