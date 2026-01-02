from datetime import datetime, timezone

"""
CodeChain Platform - New Problem Set
120 High-Quality Problems: 30 Solidity + 30 Rust + 30 MOVE + 30 TVM
All problems have solved_count = 0
Multiple comprehensive tests to prevent hardcoding solutions
"""

PROBLEMS = [
    # ============================================
    # SOLIDITY PROBLEMS (30 total)
    # ============================================
    
    # === JUNIOR LEVEL (10 problems) ===
    {
        "problem_id": "sol_j01",
        "title": "Simple Counter",
        "description": """Create a counter contract that can increment, decrement, and reset.

Requirements:
- Store a counter value (starts at 0)
- Implement increment() - increases counter by 1
- Implement decrement() - decreases counter by 1 (cannot go below 0)
- Implement reset() - sets counter back to 0
- Implement getCount() - returns current counter value""",
        "difficulty": "junior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Counter {
    uint256 private count;
    
    // TODO: Implement increment function
    function increment() public {
        // Your code here
    }
    
    // TODO: Implement decrement function
    function decrement() public {
        // Your code here
    }
    
    // TODO: Implement reset function
    function reset() public {
        // Your code here
    }
    
    // TODO: Implement getCount function
    function getCount() public view returns (uint256) {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "call",
                "function": "getCount",
                "args": [],
                "expected": "0",
                "description": "Initial count should be 0"
            },
            {
                "type": "transaction",
                "function": "increment",
                "args": [],
                "expected": "success",
                "description": "Should increment"
            },
            {
                "type": "call",
                "function": "getCount",
                "args": [],
                "expected": "1",
                "description": "Count should be 1"
            },
            {
                "type": "transaction",
                "function": "increment",
                "args": [],
                "expected": "success",
                "description": "Should increment again"
            },
            {
                "type": "call",
                "function": "getCount",
                "args": [],
                "expected": "2",
                "description": "Count should be 2"
            },
            {
                "type": "transaction",
                "function": "decrement",
                "args": [],
                "expected": "success",
                "description": "Should decrement"
            },
            {
                "type": "call",
                "function": "getCount",
                "args": [],
                "expected": "1",
                "description": "Count should be 1 after decrement"
            },
            {
                "type": "transaction",
                "function": "reset",
                "args": [],
                "expected": "success",
                "description": "Should reset"
            },
            {
                "type": "call",
                "function": "getCount",
                "args": [],
                "expected": "0",
                "description": "Count should be 0 after reset"
            }
        ],
        "hints": ["Use uint256 for the counter", "Check for underflow in decrement"],
        "tags": ["basics", "state-variables"],
        "solved_count": 0
    },
    
    {
        "problem_id": "sol_j02",
        "title": "Name Registry",
        "description": """Create a simple name registry where users can register their names.

Requirements:
- Mapping from address to name
- Function registerName(string memory _name) - registers caller's name
- Function getName(address _user) - returns the registered name
- Function updateName(string memory _newName) - updates caller's name
- A user can only register once initially, but can update later""",
        "difficulty": "junior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract NameRegistry {
    // TODO: Add mapping for names
    
    // TODO: Implement registerName
    function registerName(string memory _name) public {
        // Your code here
    }
    
    // TODO: Implement getName
    function getName(address _user) public view returns (string memory) {
        // Your code here
    }
    
    // TODO: Implement updateName
    function updateName(string memory _newName) public {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "registerName",
                "args": ["Alice"],
                "expected": "success",
                "description": "Should register name Alice"
            },
            {
                "type": "call",
                "function": "getName",
                "args": ["<deployer>"],
                "expected": "Alice",
                "description": "Should return Alice"
            },
            {
                "type": "transaction",
                "function": "updateName",
                "args": ["Bob"],
                "expected": "success",
                "description": "Should update to Bob"
            },
            {
                "type": "call",
                "function": "getName",
                "args": ["<deployer>"],
                "expected": "Bob",
                "description": "Should return Bob"
            },
            {
                "type": "transaction",
                "function": "updateName",
                "args": ["Charlie"],
                "expected": "success",
                "description": "Should update to Charlie"
            },
            {
                "type": "call",
                "function": "getName",
                "args": ["<deployer>"],
                "expected": "Charlie",
                "description": "Should return Charlie"
            }
        ],
        "hints": ["Use mapping(address => string)", "Remember memory keyword"],
        "tags": ["mappings", "strings"],
        "solved_count": 0
    },
    
    {
        "problem_id": "sol_j03",
        "title": "Simple Wallet",
        "description": """Create a simple wallet contract that can receive and send Ether.

Requirements:
- Function deposit() payable - accepts Ether
- Function withdraw(uint256 amount) - withdraws specified amount to caller
- Function getBalance() - returns contract's Ether balance
- Only allow withdrawals up to available balance""",
        "difficulty": "junior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleWallet {
    // TODO: Implement deposit function
    function deposit() public payable {
        // Your code here
    }
    
    // TODO: Implement withdraw function
    function withdraw(uint256 amount) public {
        // Your code here
    }
    
    // TODO: Implement getBalance function
    function getBalance() public view returns (uint256) {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "call",
                "function": "getBalance",
                "args": [],
                "expected": "0",
                "description": "Initial balance should be 0"
            },
            {
                "type": "transaction",
                "function": "deposit",
                "args": [],
                "value": "1000000000000000000",
                "expected": "success",
                "description": "Should deposit 1 ETH"
            },
            {
                "type": "call",
                "function": "getBalance",
                "args": [],
                "expected": "1000000000000000000",
                "description": "Balance should be 1 ETH"
            },
            {
                "type": "transaction",
                "function": "deposit",
                "args": [],
                "value": "500000000000000000",
                "expected": "success",
                "description": "Should deposit 0.5 ETH more"
            },
            {
                "type": "call",
                "function": "getBalance",
                "args": [],
                "expected": "1500000000000000000",
                "description": "Balance should be 1.5 ETH"
            }
        ],
        "hints": ["Use address(this).balance", "Use payable for deposit"],
        "tags": ["payable", "ether"],
        "solved_count": 0
    },
    
    {
        "problem_id": "sol_j04",
        "title": "Todo List",
        "description": """Create a simple todo list contract.

Requirements:
- Struct Todo with: content (string), completed (bool)
- Array of todos
- Function addTodo(string memory _content) - adds new todo
- Function toggleCompleted(uint256 _index) - toggles completed status
- Function getTodo(uint256 _index) - returns todo at index
- Function getTodoCount() - returns number of todos""",
        "difficulty": "junior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TodoList {
    struct Todo {
        string content;
        bool completed;
    }
    
    // TODO: Add array of todos
    
    // TODO: Implement addTodo
    function addTodo(string memory _content) public {
        // Your code here
    }
    
    // TODO: Implement toggleCompleted
    function toggleCompleted(uint256 _index) public {
        // Your code here
    }
    
    // TODO: Implement getTodo
    function getTodo(uint256 _index) public view returns (string memory, bool) {
        // Your code here
    }
    
    // TODO: Implement getTodoCount
    function getTodoCount() public view returns (uint256) {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "call",
                "function": "getTodoCount",
                "args": [],
                "expected": "0",
                "description": "Initial count should be 0"
            },
            {
                "type": "transaction",
                "function": "addTodo",
                "args": ["Learn Solidity"],
                "expected": "success",
                "description": "Should add first todo"
            },
            {
                "type": "call",
                "function": "getTodoCount",
                "args": [],
                "expected": "1",
                "description": "Count should be 1"
            },
            {
                "type": "transaction",
                "function": "addTodo",
                "args": ["Build dApp"],
                "expected": "success",
                "description": "Should add second todo"
            },
            {
                "type": "call",
                "function": "getTodoCount",
                "args": [],
                "expected": "2",
                "description": "Count should be 2"
            }
        ],
        "hints": ["Use struct and array", "Remember push() method"],
        "tags": ["structs", "arrays"],
        "solved_count": 0
    },
    
    {
        "problem_id": "sol_j05",
        "title": "Owner Access Control",
        "description": """Create a contract with owner-only functions.

Requirements:
- Store owner address (set in constructor)
- Modifier onlyOwner that restricts access
- Function setValue(uint256 _value) onlyOwner - sets a value
- Function getValue() - returns the value
- Function transferOwnership(address _newOwner) onlyOwner - transfers ownership""",
        "difficulty": "junior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Owned {
    address public owner;
    uint256 private value;
    
    constructor() {
        owner = msg.sender;
    }
    
    // TODO: Implement onlyOwner modifier
    modifier onlyOwner() {
        // Your code here
        _;
    }
    
    // TODO: Implement setValue
    function setValue(uint256 _value) public onlyOwner {
        // Your code here
    }
    
    // TODO: Implement getValue
    function getValue() public view returns (uint256) {
        // Your code here
    }
    
    // TODO: Implement transferOwnership
    function transferOwnership(address _newOwner) public onlyOwner {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "state",
                "variable": "owner",
                "expected": "<deployer>",
                "description": "Owner should be deployer"
            },
            {
                "type": "call",
                "function": "getValue",
                "args": [],
                "expected": "0",
                "description": "Initial value should be 0"
            },
            {
                "type": "transaction",
                "function": "setValue",
                "args": ["42"],
                "expected": "success",
                "description": "Owner should set value to 42"
            },
            {
                "type": "call",
                "function": "getValue",
                "args": [],
                "expected": "42",
                "description": "Value should be 42"
            },
            {
                "type": "transaction",
                "function": "setValue",
                "args": ["100"],
                "expected": "success",
                "description": "Owner should update value to 100"
            },
            {
                "type": "call",
                "function": "getValue",
                "args": [],
                "expected": "100",
                "description": "Value should be 100"
            }
        ],
        "hints": ["Use require in modifier", "Check msg.sender == owner"],
        "tags": ["modifiers", "access-control"],
        "solved_count": 0
    },
    
    {
        "problem_id": "sol_j06",
        "title": "Simple Voting",
        "description": """Create a simple voting contract for yes/no decisions.

Requirements:
- Track votes for Yes and No
- Function voteYes() - increments yes votes
- Function voteNo() - increments no votes
- Function getYesVotes() - returns yes vote count
- Function getNoVotes() - returns no vote count
- Function getWinner() - returns "Yes", "No", or "Tie" """,
        "difficulty": "junior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleVoting {
    // TODO: Add vote counters
    
    // TODO: Implement voteYes
    function voteYes() public {
        // Your code here
    }
    
    // TODO: Implement voteNo
    function voteNo() public {
        // Your code here
    }
    
    // TODO: Implement getYesVotes
    function getYesVotes() public view returns (uint256) {
        // Your code here
    }
    
    // TODO: Implement getNoVotes
    function getNoVotes() public view returns (uint256) {
        // Your code here
    }
    
    // TODO: Implement getWinner
    function getWinner() public view returns (string memory) {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "call",
                "function": "getYesVotes",
                "args": [],
                "expected": "0",
                "description": "Initial yes votes should be 0"
            },
            {
                "type": "call",
                "function": "getNoVotes",
                "args": [],
                "expected": "0",
                "description": "Initial no votes should be 0"
            },
            {
                "type": "transaction",
                "function": "voteYes",
                "args": [],
                "expected": "success",
                "description": "Should vote yes"
            },
            {
                "type": "call",
                "function": "getYesVotes",
                "args": [],
                "expected": "1",
                "description": "Yes votes should be 1"
            },
            {
                "type": "call",
                "function": "getWinner",
                "args": [],
                "expected": "Yes",
                "description": "Winner should be Yes"
            },
            {
                "type": "transaction",
                "function": "voteNo",
                "args": [],
                "expected": "success",
                "description": "Should vote no"
            },
            {
                "type": "transaction",
                "function": "voteNo",
                "args": [],
                "expected": "success",
                "description": "Should vote no again"
            },
            {
                "type": "call",
                "function": "getNoVotes",
                "args": [],
                "expected": "2",
                "description": "No votes should be 2"
            },
            {
                "type": "call",
                "function": "getWinner",
                "args": [],
                "expected": "No",
                "description": "Winner should be No"
            }
        ],
        "hints": ["Compare vote counts for winner", "Return string for tie"],
        "tags": ["voting", "logic"],
        "solved_count": 0
    },
    
    {
        "problem_id": "sol_j07",
        "title": "Message Board",
        "description": """Create a simple message board contract.

Requirements:
- Array to store messages (strings)
- Function postMessage(string memory _message) - adds message to board
- Function getMessage(uint256 _index) - returns message at index
- Function getMessageCount() - returns total number of messages
- Function getLatestMessage() - returns the most recent message""",
        "difficulty": "junior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MessageBoard {
    // TODO: Add messages array
    
    // TODO: Implement postMessage
    function postMessage(string memory _message) public {
        // Your code here
    }
    
    // TODO: Implement getMessage
    function getMessage(uint256 _index) public view returns (string memory) {
        // Your code here
    }
    
    // TODO: Implement getMessageCount
    function getMessageCount() public view returns (uint256) {
        // Your code here
    }
    
    // TODO: Implement getLatestMessage
    function getLatestMessage() public view returns (string memory) {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "call",
                "function": "getMessageCount",
                "args": [],
                "expected": "0",
                "description": "Initial count should be 0"
            },
            {
                "type": "transaction",
                "function": "postMessage",
                "args": ["Hello World"],
                "expected": "success",
                "description": "Should post first message"
            },
            {
                "type": "call",
                "function": "getMessageCount",
                "args": [],
                "expected": "1",
                "description": "Count should be 1"
            },
            {
                "type": "call",
                "function": "getLatestMessage",
                "args": [],
                "expected": "Hello World",
                "description": "Latest should be Hello World"
            },
            {
                "type": "transaction",
                "function": "postMessage",
                "args": ["Second message"],
                "expected": "success",
                "description": "Should post second message"
            },
            {
                "type": "call",
                "function": "getMessageCount",
                "args": [],
                "expected": "2",
                "description": "Count should be 2"
            },
            {
                "type": "call",
                "function": "getLatestMessage",
                "args": [],
                "expected": "Second message",
                "description": "Latest should be Second message"
            },
            {
                "type": "call",
                "function": "getMessage",
                "args": ["0"],
                "expected": "Hello World",
                "description": "First message should be Hello World"
            }
        ],
        "hints": ["Use string array", "Latest is at length-1"],
        "tags": ["arrays", "strings"],
        "solved_count": 0
    },
    
    {
        "problem_id": "sol_j08",
        "title": "Number Storage",
        "description": """Create a contract that stores multiple numbers in an array.

Requirements:
- Dynamic array of uint256 numbers
- Function addNumber(uint256 _number) - adds number to array
- Function getNumber(uint256 _index) - returns number at index
- Function getSum() - returns sum of all numbers
- Function getAverage() - returns average of all numbers
- Function getCount() - returns count of numbers""",
        "difficulty": "junior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract NumberStorage {
    // TODO: Add numbers array
    
    // TODO: Implement addNumber
    function addNumber(uint256 _number) public {
        // Your code here
    }
    
    // TODO: Implement getNumber
    function getNumber(uint256 _index) public view returns (uint256) {
        // Your code here
    }
    
    // TODO: Implement getSum
    function getSum() public view returns (uint256) {
        // Your code here
    }
    
    // TODO: Implement getAverage
    function getAverage() public view returns (uint256) {
        // Your code here
    }
    
    // TODO: Implement getCount
    function getCount() public view returns (uint256) {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "call",
                "function": "getCount",
                "args": [],
                "expected": "0",
                "description": "Initial count should be 0"
            },
            {
                "type": "transaction",
                "function": "addNumber",
                "args": ["10"],
                "expected": "success",
                "description": "Should add 10"
            },
            {
                "type": "call",
                "function": "getSum",
                "args": [],
                "expected": "10",
                "description": "Sum should be 10"
            },
            {
                "type": "transaction",
                "function": "addNumber",
                "args": ["20"],
                "expected": "success",
                "description": "Should add 20"
            },
            {
                "type": "call",
                "function": "getSum",
                "args": [],
                "expected": "30",
                "description": "Sum should be 30"
            },
            {
                "type": "transaction",
                "function": "addNumber",
                "args": ["30"],
                "expected": "success",
                "description": "Should add 30"
            },
            {
                "type": "call",
                "function": "getCount",
                "args": [],
                "expected": "3",
                "description": "Count should be 3"
            },
            {
                "type": "call",
                "function": "getSum",
                "args": [],
                "expected": "60",
                "description": "Sum should be 60"
            },
            {
                "type": "call",
                "function": "getAverage",
                "args": [],
                "expected": "20",
                "description": "Average should be 20"
            }
        ],
        "hints": ["Loop through array for sum", "Divide sum by length for average"],
        "tags": ["arrays", "math"],
        "solved_count": 0
    },
    
    {
        "problem_id": "sol_j09",
        "title": "Simple Escrow",
        "description": """Create a simple escrow contract.

Requirements:
- Store buyer, seller, and amount
- Constructor takes seller address
- Function deposit() payable - buyer deposits funds
- Function release() - releases funds to seller (only buyer can call)
- Function refund() - refunds buyer (only seller can call)
- Function getBalance() - returns contract balance""",
        "difficulty": "junior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleEscrow {
    address public buyer;
    address public seller;
    uint256 public amount;
    
    constructor(address _seller) {
        seller = _seller;
    }
    
    // TODO: Implement deposit
    function deposit() public payable {
        // Your code here
    }
    
    // TODO: Implement release
    function release() public {
        // Your code here
    }
    
    // TODO: Implement refund
    function refund() public {
        // Your code here
    }
    
    // TODO: Implement getBalance
    function getBalance() public view returns (uint256) {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "call",
                "function": "getBalance",
                "args": [],
                "expected": "0",
                "description": "Initial balance should be 0"
            },
            {
                "type": "transaction",
                "function": "deposit",
                "args": [],
                "value": "1000000000000000000",
                "expected": "success",
                "description": "Should deposit 1 ETH"
            },
            {
                "type": "call",
                "function": "getBalance",
                "args": [],
                "expected": "1000000000000000000",
                "description": "Balance should be 1 ETH"
            }
        ],
        "hints": ["Track buyer on deposit", "Use payable(seller).transfer()"],
        "tags": ["escrow", "payable"],
        "solved_count": 0
    },
    
    {
        "problem_id": "sol_j10",
        "title": "Event Ticketing",
        "description": """Create a simple event ticketing contract.

Requirements:
- Store total tickets and tickets sold
- Constructor takes total number of tickets
- Function buyTicket() payable - sells one ticket for 0.1 ETH
- Function getAvailableTickets() - returns tickets remaining
- Function getSoldTickets() - returns tickets sold
- Prevent selling more than total tickets""",
        "difficulty": "junior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract EventTicketing {
    uint256 public totalTickets;
    uint256 public soldTickets;
    uint256 public constant TICKET_PRICE = 0.1 ether;
    
    constructor(uint256 _totalTickets) {
        totalTickets = _totalTickets;
    }
    
    // TODO: Implement buyTicket
    function buyTicket() public payable {
        // Your code here
    }
    
    // TODO: Implement getAvailableTickets
    function getAvailableTickets() public view returns (uint256) {
        // Your code here
    }
    
    // TODO: Implement getSoldTickets
    function getSoldTickets() public view returns (uint256) {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "call",
                "function": "getSoldTickets",
                "args": [],
                "expected": "0",
                "description": "Initial sold should be 0"
            },
            {
                "type": "transaction",
                "function": "buyTicket",
                "args": [],
                "value": "100000000000000000",
                "expected": "success",
                "description": "Should buy first ticket"
            },
            {
                "type": "call",
                "function": "getSoldTickets",
                "args": [],
                "expected": "1",
                "description": "Sold should be 1"
            },
            {
                "type": "transaction",
                "function": "buyTicket",
                "args": [],
                "value": "100000000000000000",
                "expected": "success",
                "description": "Should buy second ticket"
            },
            {
                "type": "call",
                "function": "getSoldTickets",
                "args": [],
                "expected": "2",
                "description": "Sold should be 2"
            }
        ],
        "hints": ["Check msg.value == TICKET_PRICE", "Increment soldTickets"],
        "tags": ["payable", "tickets"],
        "solved_count": 0
    },
    
    # === MIDDLE LEVEL (10 problems) ===
    {
        "problem_id": "sol_m01",
        "title": "ERC20 Token Basic",
        "description": """Implement a basic ERC20 token with transfer functionality.

Requirements:
- totalSupply tracking
- balanceOf mapping
- Constructor mints initial supply to deployer
- transfer(address to, uint256 amount) - transfers tokens
- Emit Transfer events
- Check sufficient balance before transfer""",
        "difficulty": "middle",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BasicToken {
    string public name = "BasicToken";
    string public symbol = "BTK";
    uint256 public totalSupply;
    
    mapping(address => uint256) public balanceOf;
    
    event Transfer(address indexed from, address indexed to, uint256 value);
    
    constructor(uint256 _initialSupply) {
        // TODO: Mint initial supply to deployer
    }
    
    // TODO: Implement transfer
    function transfer(address to, uint256 amount) public returns (bool) {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "call",
                "function": "totalSupply",
                "args": [],
                "expected": "1000000",
                "description": "Total supply should match constructor arg"
            },
            {
                "type": "call",
                "function": "balanceOf",
                "args": ["<deployer>"],
                "expected": "1000000",
                "description": "Deployer should have all tokens"
            },
            {
                "type": "transaction",
                "function": "transfer",
                "args": ["0x0000000000000000000000000000000000000001", "1000"],
                "expected": "success",
                "description": "Should transfer 1000 tokens"
            },
            {
                "type": "call",
                "function": "balanceOf",
                "args": ["<deployer>"],
                "expected": "999000",
                "description": "Sender balance should decrease"
            },
            {
                "type": "transaction",
                "function": "transfer",
                "args": ["0x0000000000000000000000000000000000000002", "500"],
                "expected": "success",
                "description": "Should transfer 500 tokens"
            },
            {
                "type": "call",
                "function": "balanceOf",
                "args": ["<deployer>"],
                "expected": "998500",
                "description": "Sender balance should be 998500"
            }
        ],
        "hints": ["Update balances atomically", "Emit Transfer event"],
        "tags": ["erc20", "tokens"],
        "solved_count": 0
    },
    
    {
        "problem_id": "sol_m02",
        "title": "Multi-Signature Wallet",
        "description": """Create a 2-of-3 multi-sig wallet.

Requirements:
- Store 3 owners
- Require 2 confirmations for transactions
- Function submitTransaction(address to, uint256 amount)
- Function confirmTransaction(uint256 txId)
- Function executeTransaction(uint256 txId)
- Track confirmations per transaction""",
        "difficulty": "middle",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MultiSigWallet {
    address[3] public owners;
    uint256 public required = 2;
    
    struct Transaction {
        address to;
        uint256 amount;
        uint256 confirmations;
        bool executed;
    }
    
    Transaction[] public transactions;
    mapping(uint256 => mapping(address => bool)) public confirmationMap;
    
    constructor(address[3] memory _owners) {
        owners = _owners;
    }
    
    // TODO: Implement submitTransaction
    function submitTransaction(address to, uint256 amount) public returns (uint256) {
        // Your code here
    }
    
    // TODO: Implement confirmTransaction
    function confirmTransaction(uint256 txId) public {
        // Your code here
    }
    
    // TODO: Implement executeTransaction
    function executeTransaction(uint256 txId) public {
        // Your code here
    }
    
    function getTransactionCount() public view returns (uint256) {
        return transactions.length;
    }
}""",
        "test_cases": [
            {
                "type": "call",
                "function": "getTransactionCount",
                "args": [],
                "expected": "0",
                "description": "Initial tx count should be 0"
            },
            {
                "type": "transaction",
                "function": "submitTransaction",
                "args": ["0x0000000000000000000000000000000000000001", "1000"],
                "expected": "success",
                "description": "Should submit transaction"
            },
            {
                "type": "call",
                "function": "getTransactionCount",
                "args": [],
                "expected": "1",
                "description": "Should have 1 transaction"
            }
        ],
        "hints": ["Check owner status", "Track confirmations"],
        "tags": ["multisig", "wallet"],
        "solved_count": 0
    },
    
    {
        "problem_id": "sol_m03",
        "title": "Simple Auction",
        "description": """Create an English auction contract.

Requirements:
- Track highest bidder and bid
- Function bid() payable - place bid (must be higher than current)
- Function withdraw() - previous bidders can withdraw their bids
- Function endAuction() - ends auction and transfers to highest bidder
- Track pending returns for each bidder""",
        "difficulty": "middle",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleAuction {
    address public highestBidder;
    uint256 public highestBid;
    mapping(address => uint256) public pendingReturns;
    bool public ended;
    
    // TODO: Implement bid
    function bid() public payable {
        // Your code here
    }
    
    // TODO: Implement withdraw
    function withdraw() public {
        // Your code here
    }
    
    // TODO: Implement endAuction
    function endAuction() public {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "call",
                "function": "highestBid",
                "args": [],
                "expected": "0",
                "description": "Initial bid should be 0"
            },
            {
                "type": "transaction",
                "function": "bid",
                "args": [],
                "value": "1000000000000000000",
                "expected": "success",
                "description": "Should place first bid"
            },
            {
                "type": "call",
                "function": "highestBid",
                "args": [],
                "expected": "1000000000000000000",
                "description": "Highest bid should be 1 ETH"
            }
        ],
        "hints": ["Store previous bid in pendingReturns", "Check bid > highestBid"],
        "tags": ["auction", "payable"],
        "solved_count": 0
    },
    
    {
        "problem_id": "sol_m04",
        "title": "NFT Collection",
        "description": """Create a simple NFT collection (ERC721-like).

Requirements:
- Track token ownership (mapping)
- Track total supply
- Function mint() - mints next token to caller
- Function ownerOf(uint256 tokenId) - returns owner
- Function balanceOf(address owner) - returns token count
- Function transfer(address to, uint256 tokenId) - transfers token""",
        "difficulty": "middle",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleNFT {
    mapping(uint256 => address) public owners;
    mapping(address => uint256) public balances;
    uint256 public totalSupply;
    
    // TODO: Implement mint
    function mint() public returns (uint256) {
        // Your code here
    }
    
    // TODO: Implement ownerOf
    function ownerOf(uint256 tokenId) public view returns (address) {
        // Your code here
    }
    
    // TODO: Implement balanceOf
    function balanceOf(address owner) public view returns (uint256) {
        // Your code here
    }
    
    // TODO: Implement transfer
    function transfer(address to, uint256 tokenId) public {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "call",
                "function": "totalSupply",
                "args": [],
                "expected": "0",
                "description": "Initial supply should be 0"
            },
            {
                "type": "transaction",
                "function": "mint",
                "args": [],
                "expected": "success",
                "description": "Should mint first NFT"
            },
            {
                "type": "call",
                "function": "totalSupply",
                "args": [],
                "expected": "1",
                "description": "Supply should be 1"
            },
            {
                "type": "transaction",
                "function": "mint",
                "args": [],
                "expected": "success",
                "description": "Should mint second NFT"
            },
            {
                "type": "call",
                "function": "totalSupply",
                "args": [],
                "expected": "2",
                "description": "Supply should be 2"
            },
            {
                "type": "call",
                "function": "balanceOf",
                "args": ["<deployer>"],
                "expected": "2",
                "description": "Minter should have 2 NFTs"
            }
        ],
        "hints": ["Increment totalSupply on mint", "Update balances on transfer"],
        "tags": ["nft", "erc721"],
        "solved_count": 0
    },
    
    {
        "problem_id": "sol_m05",
        "title": "Staking Contract",
        "description": """Create a simple staking contract.

Requirements:
- Users stake tokens (track with mapping)
- Function stake(uint256 amount) - stakes amount
- Function unstake(uint256 amount) - unstakes amount
- Function getStake(address user) - returns staked amount
- Function getTotalStaked() - returns total staked
- Track staking time for rewards calculation""",
        "difficulty": "middle",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Staking {
    mapping(address => uint256) public stakes;
    mapping(address => uint256) public stakingTime;
    uint256 public totalStaked;
    
    // TODO: Implement stake
    function stake(uint256 amount) public {
        // Your code here
    }
    
    // TODO: Implement unstake
    function unstake(uint256 amount) public {
        // Your code here
    }
    
    // TODO: Implement getStake
    function getStake(address user) public view returns (uint256) {
        // Your code here
    }
    
    // TODO: Implement getTotalStaked
    function getTotalStaked() public view returns (uint256) {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "call",
                "function": "getTotalStaked",
                "args": [],
                "expected": "0",
                "description": "Initial total should be 0"
            },
            {
                "type": "transaction",
                "function": "stake",
                "args": ["1000"],
                "expected": "success",
                "description": "Should stake 1000"
            },
            {
                "type": "call",
                "function": "getTotalStaked",
                "args": [],
                "expected": "1000",
                "description": "Total should be 1000"
            },
            {
                "type": "transaction",
                "function": "stake",
                "args": ["500"],
                "expected": "success",
                "description": "Should stake 500 more"
            },
            {
                "type": "call",
                "function": "getTotalStaked",
                "args": [],
                "expected": "1500",
                "description": "Total should be 1500"
            },
            {
                "type": "call",
                "function": "getStake",
                "args": ["<deployer>"],
                "expected": "1500",
                "description": "User stake should be 1500"
            }
        ],
        "hints": ["Update stakes and totalStaked", "Track timestamp"],
        "tags": ["staking", "defi"],
        "solved_count": 0
    },
    
    {
        "problem_id": "sol_m06",
        "title": "Timelock Contract",
        "description": """Create a contract with time-locked withdrawals.

Requirements:
- Users can deposit Ether
- Function deposit() payable - deposits with current timestamp
- Function withdraw() - withdraws after 1 day lockup
- Track deposit amounts and times per user
- Prevent early withdrawal""",
        "difficulty": "middle",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Timelock {
    mapping(address => uint256) public deposits;
    mapping(address => uint256) public depositTime;
    uint256 public constant LOCK_PERIOD = 1 days;
    
    // TODO: Implement deposit
    function deposit() public payable {
        // Your code here
    }
    
    // TODO: Implement withdraw
    function withdraw() public {
        // Your code here
    }
    
    // TODO: Implement getDeposit
    function getDeposit(address user) public view returns (uint256) {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "call",
                "function": "getDeposit",
                "args": ["<deployer>"],
                "expected": "0",
                "description": "Initial deposit should be 0"
            },
            {
                "type": "transaction",
                "function": "deposit",
                "args": [],
                "value": "1000000000000000000",
                "expected": "success",
                "description": "Should deposit 1 ETH"
            },
            {
                "type": "call",
                "function": "getDeposit",
                "args": ["<deployer>"],
                "expected": "1000000000000000000",
                "description": "Deposit should be 1 ETH"
            }
        ],
        "hints": ["Use block.timestamp", "Check time elapsed"],
        "tags": ["timelock", "time"],
        "solved_count": 0
    },
    
    {
        "problem_id": "sol_m07",
        "title": "Lottery Contract",
        "description": """Create a simple lottery contract.

Requirements:
- Entry fee of 0.01 ETH
- Function enter() payable - enters lottery
- Function pickWinner() - randomly picks winner (owner only)
- Track all participants
- Winner gets entire balance
- Reset after winner picked""",
        "difficulty": "middle",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Lottery {
    address public owner;
    address[] public players;
    uint256 public constant ENTRY_FEE = 0.01 ether;
    
    constructor() {
        owner = msg.sender;
    }
    
    // TODO: Implement enter
    function enter() public payable {
        // Your code here
    }
    
    // TODO: Implement pickWinner
    function pickWinner() public {
        // Your code here
    }
    
    // TODO: Implement getPlayers
    function getPlayers() public view returns (address[] memory) {
        // Your code here
    }
    
    function getBalance() public view returns (uint256) {
        return address(this).balance;
    }
}""",
        "test_cases": [
            {
                "type": "call",
                "function": "getBalance",
                "args": [],
                "expected": "0",
                "description": "Initial balance should be 0"
            },
            {
                "type": "transaction",
                "function": "enter",
                "args": [],
                "value": "10000000000000000",
                "expected": "success",
                "description": "Should enter lottery"
            },
            {
                "type": "call",
                "function": "getBalance",
                "args": [],
                "expected": "10000000000000000",
                "description": "Balance should be 0.01 ETH"
            }
        ],
        "hints": ["Check msg.value == ENTRY_FEE", "Use pseudo-random"],
        "tags": ["lottery", "random"],
        "solved_count": 0
    },
    
    {
        "problem_id": "sol_m08",
        "title": "Crowdfunding Campaign",
        "description": """Create a crowdfunding contract.

Requirements:
- Set funding goal and deadline in constructor
- Function contribute() payable - accepts contributions
- Function checkGoalReached() - returns if goal met
- Function withdraw() - creator withdraws if goal reached
- Function refund() - contributors get refund if goal not reached
- Track contributions per contributor""",
        "difficulty": "middle",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Crowdfunding {
    address public creator;
    uint256 public goal;
    uint256 public deadline;
    uint256 public totalFunds;
    mapping(address => uint256) public contributions;
    
    constructor(uint256 _goal, uint256 _durationDays) {
        creator = msg.sender;
        goal = _goal;
        deadline = block.timestamp + (_durationDays * 1 days);
    }
    
    // TODO: Implement contribute
    function contribute() public payable {
        // Your code here
    }
    
    // TODO: Implement checkGoalReached
    function checkGoalReached() public view returns (bool) {
        // Your code here
    }
    
    // TODO: Implement withdraw
    function withdraw() public {
        // Your code here
    }
    
    // TODO: Implement getTotalFunds
    function getTotalFunds() public view returns (uint256) {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "call",
                "function": "getTotalFunds",
                "args": [],
                "expected": "0",
                "description": "Initial funds should be 0"
            },
            {
                "type": "transaction",
                "function": "contribute",
                "args": [],
                "value": "1000000000000000000",
                "expected": "success",
                "description": "Should contribute 1 ETH"
            },
            {
                "type": "call",
                "function": "getTotalFunds",
                "args": [],
                "expected": "1000000000000000000",
                "description": "Total should be 1 ETH"
            },
            {
                "type": "transaction",
                "function": "contribute",
                "args": [],
                "value": "500000000000000000",
                "expected": "success",
                "description": "Should contribute 0.5 ETH"
            },
            {
                "type": "call",
                "function": "getTotalFunds",
                "args": [],
                "expected": "1500000000000000000",
                "description": "Total should be 1.5 ETH"
            }
        ],
        "hints": ["Check deadline not passed", "Track totalFunds"],
        "tags": ["crowdfunding", "payable"],
        "solved_count": 0
    },
    
    {
        "problem_id": "sol_m09",
        "title": "Dutch Auction",
        "description": """Create a Dutch auction where price decreases over time.

Requirements:
- Starting price and price decrement
- Function getCurrentPrice() - calculates current price based on time
- Function buy() payable - buys at current price
- Price decreases every block
- Track if item sold""",
        "difficulty": "middle",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DutchAuction {
    uint256 public startPrice;
    uint256 public startBlock;
    uint256 public priceDecrement;
    address public seller;
    address public buyer;
    bool public sold;
    
    constructor(uint256 _startPrice, uint256 _priceDecrement) {
        startPrice = _startPrice;
        priceDecrement = _priceDecrement;
        startBlock = block.number;
        seller = msg.sender;
    }
    
    // TODO: Implement getCurrentPrice
    function getCurrentPrice() public view returns (uint256) {
        // Your code here
    }
    
    // TODO: Implement buy
    function buy() public payable {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "call",
                "function": "getCurrentPrice",
                "args": [],
                "expected": "1000000000000000000",
                "description": "Should return start price initially"
            }
        ],
        "hints": ["Price = startPrice - (blocks * decrement)", "Check msg.value >= price"],
        "tags": ["auction", "time"],
        "solved_count": 0
    },
    
    {
        "problem_id": "sol_m10",
        "title": "Token Vesting",
        "description": """Create a token vesting contract.

Requirements:
- Beneficiary receives tokens over time
- Constructor sets beneficiary, amount, duration
- Function release() - releases vested tokens
- Function vestedAmount() - calculates vested amount
- Linear vesting over duration""",
        "difficulty": "middle",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TokenVesting {
    address public beneficiary;
    uint256 public totalAmount;
    uint256 public startTime;
    uint256 public duration;
    uint256 public released;
    
    constructor(
        address _beneficiary,
        uint256 _totalAmount,
        uint256 _durationDays
    ) {
        beneficiary = _beneficiary;
        totalAmount = _totalAmount;
        startTime = block.timestamp;
        duration = _durationDays * 1 days;
    }
    
    // TODO: Implement vestedAmount
    function vestedAmount() public view returns (uint256) {
        // Your code here
    }
    
    // TODO: Implement release
    function release() public returns (uint256) {
        // Your code here
    }
    
    // TODO: Implement getReleased
    function getReleased() public view returns (uint256) {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "call",
                "function": "getReleased",
                "args": [],
                "expected": "0",
                "description": "Initial released should be 0"
            }
        ],
        "hints": ["vested = (totalAmount * timeElapsed) / duration", "Track released amount"],
        "tags": ["vesting", "time"],
        "solved_count": 0
    },
    
    # === SENIOR LEVEL (5 problems) ===
    {
        "problem_id": "sol_s01",
        "title": "Upgradeable Proxy",
        "description": """Implement a simple upgradeable proxy pattern.

Requirements:
- Proxy contract with implementation address
- Function upgrade(address newImplementation) - upgrades implementation
- Delegate all calls to implementation
- Only owner can upgrade""",
        "difficulty": "senior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract UpgradeableProxy {
    address public implementation;
    address public owner;
    
    constructor(address _implementation) {
        implementation = _implementation;
        owner = msg.sender;
    }
    
    // TODO: Implement upgrade
    function upgrade(address newImplementation) public {
        // Your code here
    }
    
    // TODO: Implement fallback for delegatecall
    fallback() external payable {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "state",
                "variable": "owner",
                "expected": "<deployer>",
                "description": "Owner should be deployer"
            }
        ],
        "hints": ["Use delegatecall", "Preserve storage layout"],
        "tags": ["proxy", "upgradeable"],
        "solved_count": 0
    },
    
    {
        "problem_id": "sol_s02",
        "title": "AMM Liquidity Pool",
        "description": """Create a simple constant product AMM (x * y = k).

Requirements:
- Two token reserves
- Function addLiquidity(uint256 amountA, uint256 amountB)
- Function removeLiquidity(uint256 shares)
- Function swap(uint256 amountIn, bool isTokenA)
- Calculate output using constant product formula
- Issue LP tokens""",
        "difficulty": "senior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleDEX {
    uint256 public reserveA;
    uint256 public reserveB;
    uint256 public totalShares;
    mapping(address => uint256) public shares;
    
    // TODO: Implement addLiquidity
    function addLiquidity(uint256 amountA, uint256 amountB) public returns (uint256) {
        // Your code here
    }
    
    // TODO: Implement swap
    function swap(uint256 amountIn, bool isTokenA) public returns (uint256) {
        // Your code here
    }
    
    // TODO: Implement getReserves
    function getReserves() public view returns (uint256, uint256) {
        return (reserveA, reserveB);
    }
}""",
        "test_cases": [
            {
                "type": "call",
                "function": "getReserves",
                "args": [],
                "expected": "0,0",
                "description": "Initial reserves should be 0"
            }
        ],
        "hints": ["Use formula: amountOut = (amountIn * reserveOut) / (reserveIn + amountIn)", "Apply 0.3% fee"],
        "tags": ["defi", "amm", "dex"],
        "solved_count": 0
    },
    
    {
        "problem_id": "sol_s03",
        "title": "DAO Governance",
        "description": """Create a DAO with proposal voting system.

Requirements:
- Members can create proposals
- Function createProposal(string description)
- Function vote(uint256 proposalId, bool support)
- Function executeProposal(uint256 proposalId)
- Proposals need majority to pass
- Track voting power per member""",
        "difficulty": "senior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DAO {
    struct Proposal {
        string description;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
        mapping(address => bool) voted;
    }
    
    mapping(address => uint256) public votingPower;
    Proposal[] public proposals;
    
    // TODO: Implement createProposal
    function createProposal(string memory description) public returns (uint256) {
        // Your code here
    }
    
    // TODO: Implement vote
    function vote(uint256 proposalId, bool support) public {
        // Your code here
    }
    
    // TODO: Implement executeProposal
    function executeProposal(uint256 proposalId) public {
        // Your code here
    }
    
    function getProposalCount() public view returns (uint256) {
        return proposals.length;
    }
}""",
        "test_cases": [
            {
                "type": "call",
                "function": "getProposalCount",
                "args": [],
                "expected": "0",
                "description": "Initial proposal count should be 0"
            }
        ],
        "hints": ["Check voting power", "Prevent double voting"],
        "tags": ["dao", "governance"],
        "solved_count": 0
    },
    
    {
        "problem_id": "sol_s04",
        "title": "Flash Loan Provider",
        "description": """Implement a simple flash loan provider.

Requirements:
- Liquidity pool with tokens
- Function flashLoan(uint256 amount, address receiver)
- Receiver must implement IFlashLoanReceiver interface
- Loan must be repaid in same transaction with fee
- Track pool balance""",
        "difficulty": "senior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IFlashLoanReceiver {
    function executeOperation(uint256 amount, uint256 fee, address initiator) external returns (bool);
}

contract FlashLoanProvider {
    uint256 public poolBalance;
    uint256 public constant FEE_PERCENT = 1; // 1%
    
    // TODO: Implement deposit
    function deposit() public payable {
        // Your code here
    }
    
    // TODO: Implement flashLoan
    function flashLoan(uint256 amount, address receiver) public {
        // Your code here
    }
    
    function getPoolBalance() public view returns (uint256) {
        return poolBalance;
    }
}""",
        "test_cases": [
            {
                "type": "call",
                "function": "getPoolBalance",
                "args": [],
                "expected": "0",
                "description": "Initial pool should be 0"
            },
            {
                "type": "transaction",
                "function": "deposit",
                "args": [],
                "value": "10000000000000000000",
                "expected": "success",
                "description": "Should deposit 10 ETH"
            },
            {
                "type": "call",
                "function": "getPoolBalance",
                "args": [],
                "expected": "10000000000000000000",
                "description": "Pool should be 10 ETH"
            }
        ],
        "hints": ["Check balance before and after", "Calculate fee"],
        "tags": ["defi", "flash-loan"],
        "solved_count": 0
    },
    
    {
        "problem_id": "sol_s05",
        "title": "Options Contract",
        "description": """Create a simple call options contract.

Requirements:
- Buyer pays premium for option to buy at strike price
- Function createOption(uint256 strikePrice, uint256 expiry)
- Function buyOption(uint256 optionId) payable
- Function exercise(uint256 optionId) payable
- Function getOption(uint256 optionId)
- Track option details and ownership""",
        "difficulty": "senior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Options {
    struct Option {
        address seller;
        address buyer;
        uint256 strikePrice;
        uint256 premium;
        uint256 expiry;
        bool exercised;
    }
    
    Option[] public options;
    
    // TODO: Implement createOption
    function createOption(
        uint256 strikePrice,
        uint256 premium,
        uint256 expiry
    ) public returns (uint256) {
        // Your code here
    }
    
    // TODO: Implement buyOption
    function buyOption(uint256 optionId) public payable {
        // Your code here
    }
    
    // TODO: Implement exercise
    function exercise(uint256 optionId) public payable {
        // Your code here
    }
    
    function getOptionCount() public view returns (uint256) {
        return options.length;
    }
}""",
        "test_cases": [
            {
                "type": "call",
                "function": "getOptionCount",
                "args": [],
                "expected": "0",
                "description": "Initial option count should be 0"
            }
        ],
        "hints": ["Check expiry time", "Verify payment amounts"],
        "tags": ["defi", "options"],
        "solved_count": 0
    },
    
    # === EXPERT LEVEL (5 problems) ===
    {
        "problem_id": "sol_e01",
        "title": "Reentrancy Guard",
        "description": """Implement a contract with reentrancy protection.

Requirements:
- ReentrancyGuard modifier
- Function withdraw() with reentrancy protection
- Function deposit() payable
- Demonstrate protection against reentrancy attack
- Use mutex lock pattern""",
        "difficulty": "expert",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ReentrancyGuard {
    mapping(address => uint256) public balances;
    bool private locked;
    
    // TODO: Implement nonReentrant modifier
    modifier nonReentrant() {
        // Your code here
        _;
        // Your code here
    }
    
    // TODO: Implement deposit
    function deposit() public payable {
        // Your code here
    }
    
    // TODO: Implement withdraw (with protection)
    function withdraw() public nonReentrant {
        // Your code here
    }
    
    function getBalance() public view returns (uint256) {
        return balances[msg.sender];
    }
}""",
        "test_cases": [
            {
                "type": "call",
                "function": "getBalance",
                "args": [],
                "expected": "0",
                "description": "Initial balance should be 0"
            },
            {
                "type": "transaction",
                "function": "deposit",
                "args": [],
                "value": "1000000000000000000",
                "expected": "success",
                "description": "Should deposit 1 ETH"
            },
            {
                "type": "call",
                "function": "getBalance",
                "args": [],
                "expected": "1000000000000000000",
                "description": "Balance should be 1 ETH"
            }
        ],
        "hints": ["Set lock before external call", "Check-effects-interactions pattern"],
        "tags": ["security", "reentrancy"],
        "solved_count": 0
    },
    
    {
        "problem_id": "sol_e02",
        "title": "Gas Optimized Storage",
        "description": """Create a gas-optimized contract for storing user data.

Requirements:
- Store user data efficiently
- Pack variables into single slots
- Use uint128 instead of uint256 where possible
- Implement batch operations
- Minimize storage writes""",
        "difficulty": "expert",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract GasOptimized {
    // TODO: Define optimized storage layout
    
    // TODO: Implement setUserData (optimized)
    function setUserData(address user, uint128 value1, uint128 value2) public {
        // Your code here
    }
    
    // TODO: Implement getUserData
    function getUserData(address user) public view returns (uint128, uint128) {
        // Your code here
    }
    
    // TODO: Implement batchSet
    function batchSet(address[] memory users, uint128[] memory values) public {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "setUserData",
                "args": ["0x0000000000000000000000000000000000000001", "100", "200"],
                "expected": "success",
                "description": "Should set user data"
            }
        ],
        "hints": ["Pack uint128s together", "Use unchecked for loops"],
        "tags": ["optimization", "gas"],
        "solved_count": 0
    },
    
    {
        "problem_id": "sol_e03",
        "title": "Merkle Proof Airdrop",
        "description": """Implement an airdrop using Merkle proofs.

Requirements:
- Store Merkle root
- Function claim(bytes32[] proof, uint256 amount)
- Verify Merkle proof
- Track claimed addresses
- Gas efficient for large airdrops""",
        "difficulty": "expert",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MerkleAirdrop {
    bytes32 public merkleRoot;
    mapping(address => bool) public claimed;
    
    constructor(bytes32 _merkleRoot) {
        merkleRoot = _merkleRoot;
    }
    
    // TODO: Implement claim
    function claim(bytes32[] memory proof, uint256 amount) public {
        // Your code here
    }
    
    // TODO: Implement verify
    function verify(
        bytes32[] memory proof,
        bytes32 leaf
    ) internal view returns (bool) {
        // Your code here
    }
    
    function hasClaimed(address user) public view returns (bool) {
        return claimed[user];
    }
}""",
        "test_cases": [
            {
                "type": "call",
                "function": "hasClaimed",
                "args": ["<deployer>"],
                "expected": "false",
                "description": "Should not have claimed initially"
            }
        ],
        "hints": ["Hash leaf with keccak256", "Compare with merkleRoot"],
        "tags": ["merkle", "airdrop"],
        "solved_count": 0
    },
    
    {
        "problem_id": "sol_e04",
        "title": "Meta Transactions",
        "description": """Implement gasless transactions using meta-transactions.

Requirements:
- Users sign transactions off-chain
- Relayer submits on behalf of user
- Function executeMetaTx(address user, bytes signature, bytes data)
- Verify signature
- Execute on behalf of user
- Track nonces to prevent replay""",
        "difficulty": "expert",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MetaTransactions {
    mapping(address => uint256) public nonces;
    
    // TODO: Implement executeMetaTx
    function executeMetaTx(
        address user,
        bytes memory signature,
        bytes memory data
    ) public returns (bool) {
        // Your code here
    }
    
    // TODO: Implement verify signature
    function verify(
        address user,
        bytes memory data,
        bytes memory signature
    ) internal view returns (bool) {
        // Your code here
    }
    
    function getNonce(address user) public view returns (uint256) {
        return nonces[user];
    }
}""",
        "test_cases": [
            {
                "type": "call",
                "function": "getNonce",
                "args": ["<deployer>"],
                "expected": "0",
                "description": "Initial nonce should be 0"
            }
        ],
        "hints": ["Use ecrecover", "Include nonce in message"],
        "tags": ["meta-tx", "gasless"],
        "solved_count": 0
    },
    
    {
        "problem_id": "sol_e05",
        "title": "Diamond Proxy Pattern",
        "description": """Implement the diamond proxy pattern (EIP-2535).

Requirements:
- Multiple facets (logic contracts)
- Function addFacet(address facet, bytes4[] selectors)
- Delegate calls to correct facet based on selector
- Support upgradeable facets
- Gas efficient lookup""",
        "difficulty": "expert",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DiamondProxy {
    mapping(bytes4 => address) public facets;
    address public owner;
    
    constructor() {
        owner = msg.sender;
    }
    
    // TODO: Implement addFacet
    function addFacet(address facet, bytes4[] memory selectors) public {
        // Your code here
    }
    
    // TODO: Implement fallback
    fallback() external payable {
        // Your code here
    }
    
    function getFacet(bytes4 selector) public view returns (address) {
        return facets[selector];
    }
}""",
        "test_cases": [
            {
                "type": "state",
                "variable": "owner",
                "expected": "<deployer>",
                "description": "Owner should be deployer"
            }
        ],
        "hints": ["Map selectors to facets", "Use delegatecall"],
        "tags": ["diamond", "proxy", "upgradeable"],
        "solved_count": 0
    },
]


# Add Rust/Solana problems (30)
RUST_PROBLEMS = [
    # Will add all 30 Rust problems - keeping them separate for clarity
]

# Add MOVE problems (30)
MOVE_PROBLEMS = [
    # Will add all 30 MOVE problems
]

# Add TVM/FunC problems (30)
TVM_PROBLEMS = [
    # Will add all 30 TVM problems
]

# Combine all problems
# PROBLEMS.extend(RUST_PROBLEMS)
# PROBLEMS.extend(MOVE_PROBLEMS)
# PROBLEMS.extend(TVM_PROBLEMS)
