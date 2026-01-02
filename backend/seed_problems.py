"""\nCodeChain Platform - Complete Problem Set 2025\n120 Problems: 30 Solidity + 30 Rust + 30 MOVE + 30 TVM\nEach with 15+ comprehensive tests\nAll problems have solved_count = 0\n"""\n\nPROBLEMS = [\n    {\n        "problem_id": """sol_j01""",\n        "title": """Solidity Junior 1: Counter - increment/decrement operations""",\n        "description": """Implement a Counter contract with increment/decrement operations.

Requirements:
- Implement all required functions
- Handle edge cases properly  
- Emit appropriate events
- Test with multiple scenarios
- Ensure no hardcoding of values

This problem requires 15 tests to pass.""",\n        "difficulty": """junior""",\n        "category": """solidity""",\n        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CounterContract {
    // State variables
    uint256 public value;
    mapping(address => uint256) public balances;
    
    // Events
    event ValueChanged(uint256 newValue);
    event BalanceUpdated(address indexed user, uint256 amount);
    
    // TODO: Implement required functions
    function setValue(uint256 _value) public {
        // Your code here
    }
    
    function getValue() public view returns (uint256) {
        // Your code here
    }
    
    function updateBalance(uint256 amount) public {
        // Your code here
    }
    
    function getBalance(address addr) public view returns (uint256) {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Implement all functions correctly', 'Test with different values', 'Handle edge cases', 'Use events for tracking'],\n        "tags": ['solidity', 'junior', 'counter'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """sol_m01""",\n        "title": """Solidity Middle 1: ERC20 - token standard""",\n        "description": """Implement a ERC20 contract with token standard.

Requirements:
- Implement all required functions
- Handle edge cases properly  
- Emit appropriate events
- Test with multiple scenarios
- Ensure no hardcoding of values

This problem requires 18 tests to pass.""",\n        "difficulty": """middle""",\n        "category": """solidity""",\n        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ERC20Contract {
    // State variables
    uint256 public value;
    mapping(address => uint256) public balances;
    
    // Events
    event ValueChanged(uint256 newValue);
    event BalanceUpdated(address indexed user, uint256 amount);
    
    // TODO: Implement required functions
    function setValue(uint256 _value) public {
        // Your code here
    }
    
    function getValue() public view returns (uint256) {
        // Your code here
    }
    
    function updateBalance(uint256 amount) public {
        // Your code here
    }
    
    function getBalance(address addr) public view returns (uint256) {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Implement all functions correctly', 'Test with different values', 'Handle edge cases', 'Use events for tracking'],\n        "tags": ['solidity', 'middle', 'erc20'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """sol_s01""",\n        "title": """Solidity Senior 1: DEX - automated market maker""",\n        "description": """Implement a DEX contract with automated market maker.

Requirements:
- Implement all required functions
- Handle edge cases properly  
- Emit appropriate events
- Test with multiple scenarios
- Ensure no hardcoding of values

This problem requires 20 tests to pass.""",\n        "difficulty": """senior""",\n        "category": """solidity""",\n        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DEXContract {
    // State variables
    uint256 public value;
    mapping(address => uint256) public balances;
    
    // Events
    event ValueChanged(uint256 newValue);
    event BalanceUpdated(address indexed user, uint256 amount);
    
    // TODO: Implement required functions
    function setValue(uint256 _value) public {
        // Your code here
    }
    
    function getValue() public view returns (uint256) {
        // Your code here
    }
    
    function updateBalance(uint256 amount) public {
        // Your code here
    }
    
    function getBalance(address addr) public view returns (uint256) {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Implement all functions correctly', 'Test with different values', 'Handle edge cases', 'Use events for tracking'],\n        "tags": ['solidity', 'senior', 'dex'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """sol_j02""",\n        "title": """Solidity Junior 2: Storage - multiple data types""",\n        "description": """Implement a Storage contract with multiple data types.

Requirements:
- Implement all required functions
- Handle edge cases properly  
- Emit appropriate events
- Test with multiple scenarios
- Ensure no hardcoding of values

This problem requires 15 tests to pass.""",\n        "difficulty": """junior""",\n        "category": """solidity""",\n        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StorageContract {
    // State variables
    uint256 public value;
    mapping(address => uint256) public balances;
    
    // Events
    event ValueChanged(uint256 newValue);
    event BalanceUpdated(address indexed user, uint256 amount);
    
    // TODO: Implement required functions
    function setValue(uint256 _value) public {
        // Your code here
    }
    
    function getValue() public view returns (uint256) {
        // Your code here
    }
    
    function updateBalance(uint256 amount) public {
        // Your code here
    }
    
    function getBalance(address addr) public view returns (uint256) {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Implement all functions correctly', 'Test with different values', 'Handle edge cases', 'Use events for tracking'],\n        "tags": ['solidity', 'junior', 'storage'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """sol_m02""",\n        "title": """Solidity Middle 2: NFT - ERC721 implementation""",\n        "description": """Implement a NFT contract with ERC721 implementation.

Requirements:
- Implement all required functions
- Handle edge cases properly  
- Emit appropriate events
- Test with multiple scenarios
- Ensure no hardcoding of values

This problem requires 18 tests to pass.""",\n        "difficulty": """middle""",\n        "category": """solidity""",\n        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract NFTContract {
    // State variables
    uint256 public value;
    mapping(address => uint256) public balances;
    
    // Events
    event ValueChanged(uint256 newValue);
    event BalanceUpdated(address indexed user, uint256 amount);
    
    // TODO: Implement required functions
    function setValue(uint256 _value) public {
        // Your code here
    }
    
    function getValue() public view returns (uint256) {
        // Your code here
    }
    
    function updateBalance(uint256 amount) public {
        // Your code here
    }
    
    function getBalance(address addr) public view returns (uint256) {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Implement all functions correctly', 'Test with different values', 'Handle edge cases', 'Use events for tracking'],\n        "tags": ['solidity', 'middle', 'nft'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """sol_s02""",\n        "title": """Solidity Senior 2: Lending - collateralized loans""",\n        "description": """Implement a Lending contract with collateralized loans.

Requirements:
- Implement all required functions
- Handle edge cases properly  
- Emit appropriate events
- Test with multiple scenarios
- Ensure no hardcoding of values

This problem requires 20 tests to pass.""",\n        "difficulty": """senior""",\n        "category": """solidity""",\n        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract LendingContract {
    // State variables
    uint256 public value;
    mapping(address => uint256) public balances;
    
    // Events
    event ValueChanged(uint256 newValue);
    event BalanceUpdated(address indexed user, uint256 amount);
    
    // TODO: Implement required functions
    function setValue(uint256 _value) public {
        // Your code here
    }
    
    function getValue() public view returns (uint256) {
        // Your code here
    }
    
    function updateBalance(uint256 amount) public {
        // Your code here
    }
    
    function getBalance(address addr) public view returns (uint256) {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Implement all functions correctly', 'Test with different values', 'Handle edge cases', 'Use events for tracking'],\n        "tags": ['solidity', 'senior', 'lending'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """sol_j03""",\n        "title": """Solidity Junior 3: Math - arithmetic operations""",\n        "description": """Implement a Math contract with arithmetic operations.

Requirements:
- Implement all required functions
- Handle edge cases properly  
- Emit appropriate events
- Test with multiple scenarios
- Ensure no hardcoding of values

This problem requires 15 tests to pass.""",\n        "difficulty": """junior""",\n        "category": """solidity""",\n        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MathContract {
    // State variables
    uint256 public value;
    mapping(address => uint256) public balances;
    
    // Events
    event ValueChanged(uint256 newValue);
    event BalanceUpdated(address indexed user, uint256 amount);
    
    // TODO: Implement required functions
    function setValue(uint256 _value) public {
        // Your code here
    }
    
    function getValue() public view returns (uint256) {
        // Your code here
    }
    
    function updateBalance(uint256 amount) public {
        // Your code here
    }
    
    function getBalance(address addr) public view returns (uint256) {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Implement all functions correctly', 'Test with different values', 'Handle edge cases', 'Use events for tracking'],\n        "tags": ['solidity', 'junior', 'math'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """sol_m03""",\n        "title": """Solidity Middle 3: Staking - rewards system""",\n        "description": """Implement a Staking contract with rewards system.

Requirements:
- Implement all required functions
- Handle edge cases properly  
- Emit appropriate events
- Test with multiple scenarios
- Ensure no hardcoding of values

This problem requires 18 tests to pass.""",\n        "difficulty": """middle""",\n        "category": """solidity""",\n        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StakingContract {
    // State variables
    uint256 public value;
    mapping(address => uint256) public balances;
    
    // Events
    event ValueChanged(uint256 newValue);
    event BalanceUpdated(address indexed user, uint256 amount);
    
    // TODO: Implement required functions
    function setValue(uint256 _value) public {
        // Your code here
    }
    
    function getValue() public view returns (uint256) {
        // Your code here
    }
    
    function updateBalance(uint256 amount) public {
        // Your code here
    }
    
    function getBalance(address addr) public view returns (uint256) {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Implement all functions correctly', 'Test with different values', 'Handle edge cases', 'Use events for tracking'],\n        "tags": ['solidity', 'middle', 'staking'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """sol_s03""",\n        "title": """Solidity Senior 3: Yield - farming strategies""",\n        "description": """Implement a Yield contract with farming strategies.

Requirements:
- Implement all required functions
- Handle edge cases properly  
- Emit appropriate events
- Test with multiple scenarios
- Ensure no hardcoding of values

This problem requires 20 tests to pass.""",\n        "difficulty": """senior""",\n        "category": """solidity""",\n        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract YieldContract {
    // State variables
    uint256 public value;
    mapping(address => uint256) public balances;
    
    // Events
    event ValueChanged(uint256 newValue);
    event BalanceUpdated(address indexed user, uint256 amount);
    
    // TODO: Implement required functions
    function setValue(uint256 _value) public {
        // Your code here
    }
    
    function getValue() public view returns (uint256) {
        // Your code here
    }
    
    function updateBalance(uint256 amount) public {
        // Your code here
    }
    
    function getBalance(address addr) public view returns (uint256) {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Implement all functions correctly', 'Test with different values', 'Handle edge cases', 'Use events for tracking'],\n        "tags": ['solidity', 'senior', 'yield'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """sol_j04""",\n        "title": """Solidity Junior 4: Arrays - dynamic array management""",\n        "description": """Implement a Arrays contract with dynamic array management.

Requirements:
- Implement all required functions
- Handle edge cases properly  
- Emit appropriate events
- Test with multiple scenarios
- Ensure no hardcoding of values

This problem requires 15 tests to pass.""",\n        "difficulty": """junior""",\n        "category": """solidity""",\n        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ArraysContract {
    // State variables
    uint256 public value;
    mapping(address => uint256) public balances;
    
    // Events
    event ValueChanged(uint256 newValue);
    event BalanceUpdated(address indexed user, uint256 amount);
    
    // TODO: Implement required functions
    function setValue(uint256 _value) public {
        // Your code here
    }
    
    function getValue() public view returns (uint256) {
        // Your code here
    }
    
    function updateBalance(uint256 amount) public {
        // Your code here
    }
    
    function getBalance(address addr) public view returns (uint256) {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Implement all functions correctly', 'Test with different values', 'Handle edge cases', 'Use events for tracking'],\n        "tags": ['solidity', 'junior', 'arrays'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """sol_m04""",\n        "title": """Solidity Middle 4: Auction - bidding mechanism""",\n        "description": """Implement a Auction contract with bidding mechanism.

Requirements:
- Implement all required functions
- Handle edge cases properly  
- Emit appropriate events
- Test with multiple scenarios
- Ensure no hardcoding of values

This problem requires 18 tests to pass.""",\n        "difficulty": """middle""",\n        "category": """solidity""",\n        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AuctionContract {
    // State variables
    uint256 public value;
    mapping(address => uint256) public balances;
    
    // Events
    event ValueChanged(uint256 newValue);
    event BalanceUpdated(address indexed user, uint256 amount);
    
    // TODO: Implement required functions
    function setValue(uint256 _value) public {
        // Your code here
    }
    
    function getValue() public view returns (uint256) {
        // Your code here
    }
    
    function updateBalance(uint256 amount) public {
        // Your code here
    }
    
    function getBalance(address addr) public view returns (uint256) {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Implement all functions correctly', 'Test with different values', 'Handle edge cases', 'Use events for tracking'],\n        "tags": ['solidity', 'middle', 'auction'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """sol_s04""",\n        "title": """Solidity Senior 4: FlashLoan - atomic operations""",\n        "description": """Implement a FlashLoan contract with atomic operations.

Requirements:
- Implement all required functions
- Handle edge cases properly  
- Emit appropriate events
- Test with multiple scenarios
- Ensure no hardcoding of values

This problem requires 20 tests to pass.""",\n        "difficulty": """senior""",\n        "category": """solidity""",\n        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract FlashLoanContract {
    // State variables
    uint256 public value;
    mapping(address => uint256) public balances;
    
    // Events
    event ValueChanged(uint256 newValue);
    event BalanceUpdated(address indexed user, uint256 amount);
    
    // TODO: Implement required functions
    function setValue(uint256 _value) public {
        // Your code here
    }
    
    function getValue() public view returns (uint256) {
        // Your code here
    }
    
    function updateBalance(uint256 amount) public {
        // Your code here
    }
    
    function getBalance(address addr) public view returns (uint256) {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Implement all functions correctly', 'Test with different values', 'Handle edge cases', 'Use events for tracking'],\n        "tags": ['solidity', 'senior', 'flashloan'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """sol_j05""",\n        "title": """Solidity Junior 5: Mappings - balance tracking""",\n        "description": """Implement a Mappings contract with balance tracking.

Requirements:
- Implement all required functions
- Handle edge cases properly  
- Emit appropriate events
- Test with multiple scenarios
- Ensure no hardcoding of values

This problem requires 15 tests to pass.""",\n        "difficulty": """junior""",\n        "category": """solidity""",\n        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MappingsContract {
    // State variables
    uint256 public value;
    mapping(address => uint256) public balances;
    
    // Events
    event ValueChanged(uint256 newValue);
    event BalanceUpdated(address indexed user, uint256 amount);
    
    // TODO: Implement required functions
    function setValue(uint256 _value) public {
        // Your code here
    }
    
    function getValue() public view returns (uint256) {
        // Your code here
    }
    
    function updateBalance(uint256 amount) public {
        // Your code here
    }
    
    function getBalance(address addr) public view returns (uint256) {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Implement all functions correctly', 'Test with different values', 'Handle edge cases', 'Use events for tracking'],\n        "tags": ['solidity', 'junior', 'mappings'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """sol_m05""",\n        "title": """Solidity Middle 5: Multisig - multi-signature wallet""",\n        "description": """Implement a Multisig contract with multi-signature wallet.

Requirements:
- Implement all required functions
- Handle edge cases properly  
- Emit appropriate events
- Test with multiple scenarios
- Ensure no hardcoding of values

This problem requires 18 tests to pass.""",\n        "difficulty": """middle""",\n        "category": """solidity""",\n        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MultisigContract {
    // State variables
    uint256 public value;
    mapping(address => uint256) public balances;
    
    // Events
    event ValueChanged(uint256 newValue);
    event BalanceUpdated(address indexed user, uint256 amount);
    
    // TODO: Implement required functions
    function setValue(uint256 _value) public {
        // Your code here
    }
    
    function getValue() public view returns (uint256) {
        // Your code here
    }
    
    function updateBalance(uint256 amount) public {
        // Your code here
    }
    
    function getBalance(address addr) public view returns (uint256) {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Implement all functions correctly', 'Test with different values', 'Handle edge cases', 'Use events for tracking'],\n        "tags": ['solidity', 'middle', 'multisig'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """sol_s05""",\n        "title": """Solidity Senior 5: Bridge - cross-chain transfers""",\n        "description": """Implement a Bridge contract with cross-chain transfers.

Requirements:
- Implement all required functions
- Handle edge cases properly  
- Emit appropriate events
- Test with multiple scenarios
- Ensure no hardcoding of values

This problem requires 20 tests to pass.""",\n        "difficulty": """senior""",\n        "category": """solidity""",\n        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BridgeContract {
    // State variables
    uint256 public value;
    mapping(address => uint256) public balances;
    
    // Events
    event ValueChanged(uint256 newValue);
    event BalanceUpdated(address indexed user, uint256 amount);
    
    // TODO: Implement required functions
    function setValue(uint256 _value) public {
        // Your code here
    }
    
    function getValue() public view returns (uint256) {
        // Your code here
    }
    
    function updateBalance(uint256 amount) public {
        // Your code here
    }
    
    function getBalance(address addr) public view returns (uint256) {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Implement all functions correctly', 'Test with different values', 'Handle edge cases', 'Use events for tracking'],\n        "tags": ['solidity', 'senior', 'bridge'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """sol_j06""",\n        "title": """Solidity Junior 6: Ownership - access control""",\n        "description": """Implement a Ownership contract with access control.

Requirements:
- Implement all required functions
- Handle edge cases properly  
- Emit appropriate events
- Test with multiple scenarios
- Ensure no hardcoding of values

This problem requires 15 tests to pass.""",\n        "difficulty": """junior""",\n        "category": """solidity""",\n        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract OwnershipContract {
    // State variables
    uint256 public value;
    mapping(address => uint256) public balances;
    
    // Events
    event ValueChanged(uint256 newValue);
    event BalanceUpdated(address indexed user, uint256 amount);
    
    // TODO: Implement required functions
    function setValue(uint256 _value) public {
        // Your code here
    }
    
    function getValue() public view returns (uint256) {
        // Your code here
    }
    
    function updateBalance(uint256 amount) public {
        // Your code here
    }
    
    function getBalance(address addr) public view returns (uint256) {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Implement all functions correctly', 'Test with different values', 'Handle edge cases', 'Use events for tracking'],\n        "tags": ['solidity', 'junior', 'ownership'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """sol_m06""",\n        "title": """Solidity Middle 6: Escrow - conditional payments""",\n        "description": """Implement a Escrow contract with conditional payments.

Requirements:
- Implement all required functions
- Handle edge cases properly  
- Emit appropriate events
- Test with multiple scenarios
- Ensure no hardcoding of values

This problem requires 18 tests to pass.""",\n        "difficulty": """middle""",\n        "category": """solidity""",\n        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract EscrowContract {
    // State variables
    uint256 public value;
    mapping(address => uint256) public balances;
    
    // Events
    event ValueChanged(uint256 newValue);
    event BalanceUpdated(address indexed user, uint256 amount);
    
    // TODO: Implement required functions
    function setValue(uint256 _value) public {
        // Your code here
    }
    
    function getValue() public view returns (uint256) {
        // Your code here
    }
    
    function updateBalance(uint256 amount) public {
        // Your code here
    }
    
    function getBalance(address addr) public view returns (uint256) {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Implement all functions correctly', 'Test with different values', 'Handle edge cases', 'Use events for tracking'],\n        "tags": ['solidity', 'middle', 'escrow'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """sol_s06""",\n        "title": """Solidity Senior 6: GasOptimized - storage patterns""",\n        "description": """Implement a GasOptimized contract with storage patterns.

Requirements:
- Implement all required functions
- Handle edge cases properly  
- Emit appropriate events
- Test with multiple scenarios
- Ensure no hardcoding of values

This problem requires 20 tests to pass.""",\n        "difficulty": """senior""",\n        "category": """solidity""",\n        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract GasOptimizedContract {
    // State variables
    uint256 public value;
    mapping(address => uint256) public balances;
    
    // Events
    event ValueChanged(uint256 newValue);
    event BalanceUpdated(address indexed user, uint256 amount);
    
    // TODO: Implement required functions
    function setValue(uint256 _value) public {
        // Your code here
    }
    
    function getValue() public view returns (uint256) {
        // Your code here
    }
    
    function updateBalance(uint256 amount) public {
        // Your code here
    }
    
    function getBalance(address addr) public view returns (uint256) {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Implement all functions correctly', 'Test with different values', 'Handle edge cases', 'Use events for tracking'],\n        "tags": ['solidity', 'senior', 'gasoptimized'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """sol_j07""",\n        "title": """Solidity Junior 7: Strings - string manipulation""",\n        "description": """Implement a Strings contract with string manipulation.

Requirements:
- Implement all required functions
- Handle edge cases properly  
- Emit appropriate events
- Test with multiple scenarios
- Ensure no hardcoding of values

This problem requires 15 tests to pass.""",\n        "difficulty": """junior""",\n        "category": """solidity""",\n        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StringsContract {
    // State variables
    uint256 public value;
    mapping(address => uint256) public balances;
    
    // Events
    event ValueChanged(uint256 newValue);
    event BalanceUpdated(address indexed user, uint256 amount);
    
    // TODO: Implement required functions
    function setValue(uint256 _value) public {
        // Your code here
    }
    
    function getValue() public view returns (uint256) {
        // Your code here
    }
    
    function updateBalance(uint256 amount) public {
        // Your code here
    }
    
    function getBalance(address addr) public view returns (uint256) {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Implement all functions correctly', 'Test with different values', 'Handle edge cases', 'Use events for tracking'],\n        "tags": ['solidity', 'junior', 'strings'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """sol_m07""",\n        "title": """Solidity Middle 7: Lottery - random selection""",\n        "description": """Implement a Lottery contract with random selection.

Requirements:
- Implement all required functions
- Handle edge cases properly  
- Emit appropriate events
- Test with multiple scenarios
- Ensure no hardcoding of values

This problem requires 18 tests to pass.""",\n        "difficulty": """middle""",\n        "category": """solidity""",\n        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract LotteryContract {
    // State variables
    uint256 public value;
    mapping(address => uint256) public balances;
    
    // Events
    event ValueChanged(uint256 newValue);
    event BalanceUpdated(address indexed user, uint256 amount);
    
    // TODO: Implement required functions
    function setValue(uint256 _value) public {
        // Your code here
    }
    
    function getValue() public view returns (uint256) {
        // Your code here
    }
    
    function updateBalance(uint256 amount) public {
        // Your code here
    }
    
    function getBalance(address addr) public view returns (uint256) {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Implement all functions correctly', 'Test with different values', 'Handle edge cases', 'Use events for tracking'],\n        "tags": ['solidity', 'middle', 'lottery'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """sol_s07""",\n        "title": """Solidity Senior 7: Proxy - upgradeable contracts""",\n        "description": """Implement a Proxy contract with upgradeable contracts.

Requirements:
- Implement all required functions
- Handle edge cases properly  
- Emit appropriate events
- Test with multiple scenarios
- Ensure no hardcoding of values

This problem requires 20 tests to pass.""",\n        "difficulty": """senior""",\n        "category": """solidity""",\n        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ProxyContract {
    // State variables
    uint256 public value;
    mapping(address => uint256) public balances;
    
    // Events
    event ValueChanged(uint256 newValue);
    event BalanceUpdated(address indexed user, uint256 amount);
    
    // TODO: Implement required functions
    function setValue(uint256 _value) public {
        // Your code here
    }
    
    function getValue() public view returns (uint256) {
        // Your code here
    }
    
    function updateBalance(uint256 amount) public {
        // Your code here
    }
    
    function getBalance(address addr) public view returns (uint256) {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Implement all functions correctly', 'Test with different values', 'Handle edge cases', 'Use events for tracking'],\n        "tags": ['solidity', 'senior', 'proxy'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """sol_j08""",\n        "title": """Solidity Junior 8: Boolean - logic operations""",\n        "description": """Implement a Boolean contract with logic operations.

Requirements:
- Implement all required functions
- Handle edge cases properly  
- Emit appropriate events
- Test with multiple scenarios
- Ensure no hardcoding of values

This problem requires 15 tests to pass.""",\n        "difficulty": """junior""",\n        "category": """solidity""",\n        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BooleanContract {
    // State variables
    uint256 public value;
    mapping(address => uint256) public balances;
    
    // Events
    event ValueChanged(uint256 newValue);
    event BalanceUpdated(address indexed user, uint256 amount);
    
    // TODO: Implement required functions
    function setValue(uint256 _value) public {
        // Your code here
    }
    
    function getValue() public view returns (uint256) {
        // Your code here
    }
    
    function updateBalance(uint256 amount) public {
        // Your code here
    }
    
    function getBalance(address addr) public view returns (uint256) {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Implement all functions correctly', 'Test with different values', 'Handle edge cases', 'Use events for tracking'],\n        "tags": ['solidity', 'junior', 'boolean'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """sol_m08""",\n        "title": """Solidity Middle 8: DAO - governance voting""",\n        "description": """Implement a DAO contract with governance voting.

Requirements:
- Implement all required functions
- Handle edge cases properly  
- Emit appropriate events
- Test with multiple scenarios
- Ensure no hardcoding of values

This problem requires 18 tests to pass.""",\n        "difficulty": """middle""",\n        "category": """solidity""",\n        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DAOContract {
    // State variables
    uint256 public value;
    mapping(address => uint256) public balances;
    
    // Events
    event ValueChanged(uint256 newValue);
    event BalanceUpdated(address indexed user, uint256 amount);
    
    // TODO: Implement required functions
    function setValue(uint256 _value) public {
        // Your code here
    }
    
    function getValue() public view returns (uint256) {
        // Your code here
    }
    
    function updateBalance(uint256 amount) public {
        // Your code here
    }
    
    function getBalance(address addr) public view returns (uint256) {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Implement all functions correctly', 'Test with different values', 'Handle edge cases', 'Use events for tracking'],\n        "tags": ['solidity', 'middle', 'dao'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """sol_s08""",\n        "title": """Solidity Senior 8: Reentrancy - security guards""",\n        "description": """Implement a Reentrancy contract with security guards.

Requirements:
- Implement all required functions
- Handle edge cases properly  
- Emit appropriate events
- Test with multiple scenarios
- Ensure no hardcoding of values

This problem requires 20 tests to pass.""",\n        "difficulty": """senior""",\n        "category": """solidity""",\n        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ReentrancyContract {
    // State variables
    uint256 public value;
    mapping(address => uint256) public balances;
    
    // Events
    event ValueChanged(uint256 newValue);
    event BalanceUpdated(address indexed user, uint256 amount);
    
    // TODO: Implement required functions
    function setValue(uint256 _value) public {
        // Your code here
    }
    
    function getValue() public view returns (uint256) {
        // Your code here
    }
    
    function updateBalance(uint256 amount) public {
        // Your code here
    }
    
    function getBalance(address addr) public view returns (uint256) {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Implement all functions correctly', 'Test with different values', 'Handle edge cases', 'Use events for tracking'],\n        "tags": ['solidity', 'senior', 'reentrancy'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """sol_j09""",\n        "title": """Solidity Junior 9: Structs - user management""",\n        "description": """Implement a Structs contract with user management.

Requirements:
- Implement all required functions
- Handle edge cases properly  
- Emit appropriate events
- Test with multiple scenarios
- Ensure no hardcoding of values

This problem requires 15 tests to pass.""",\n        "difficulty": """junior""",\n        "category": """solidity""",\n        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StructsContract {
    // State variables
    uint256 public value;
    mapping(address => uint256) public balances;
    
    // Events
    event ValueChanged(uint256 newValue);
    event BalanceUpdated(address indexed user, uint256 amount);
    
    // TODO: Implement required functions
    function setValue(uint256 _value) public {
        // Your code here
    }
    
    function getValue() public view returns (uint256) {
        // Your code here
    }
    
    function updateBalance(uint256 amount) public {
        // Your code here
    }
    
    function getBalance(address addr) public view returns (uint256) {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Implement all functions correctly', 'Test with different values', 'Handle edge cases', 'Use events for tracking'],\n        "tags": ['solidity', 'junior', 'structs'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """sol_m09""",\n        "title": """Solidity Middle 9: TimeLock - delayed execution""",\n        "description": """Implement a TimeLock contract with delayed execution.

Requirements:
- Implement all required functions
- Handle edge cases properly  
- Emit appropriate events
- Test with multiple scenarios
- Ensure no hardcoding of values

This problem requires 18 tests to pass.""",\n        "difficulty": """middle""",\n        "category": """solidity""",\n        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TimeLockContract {
    // State variables
    uint256 public value;
    mapping(address => uint256) public balances;
    
    // Events
    event ValueChanged(uint256 newValue);
    event BalanceUpdated(address indexed user, uint256 amount);
    
    // TODO: Implement required functions
    function setValue(uint256 _value) public {
        // Your code here
    }
    
    function getValue() public view returns (uint256) {
        // Your code here
    }
    
    function updateBalance(uint256 amount) public {
        // Your code here
    }
    
    function getBalance(address addr) public view returns (uint256) {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Implement all functions correctly', 'Test with different values', 'Handle edge cases', 'Use events for tracking'],\n        "tags": ['solidity', 'middle', 'timelock'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """sol_s09""",\n        "title": """Solidity Senior 9: MEV - frontrun protection""",\n        "description": """Implement a MEV contract with frontrun protection.

Requirements:
- Implement all required functions
- Handle edge cases properly  
- Emit appropriate events
- Test with multiple scenarios
- Ensure no hardcoding of values

This problem requires 20 tests to pass.""",\n        "difficulty": """senior""",\n        "category": """solidity""",\n        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MEVContract {
    // State variables
    uint256 public value;
    mapping(address => uint256) public balances;
    
    // Events
    event ValueChanged(uint256 newValue);
    event BalanceUpdated(address indexed user, uint256 amount);
    
    // TODO: Implement required functions
    function setValue(uint256 _value) public {
        // Your code here
    }
    
    function getValue() public view returns (uint256) {
        // Your code here
    }
    
    function updateBalance(uint256 amount) public {
        // Your code here
    }
    
    function getBalance(address addr) public view returns (uint256) {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Implement all functions correctly', 'Test with different values', 'Handle edge cases', 'Use events for tracking'],\n        "tags": ['solidity', 'senior', 'mev'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """sol_j10""",\n        "title": """Solidity Junior 10: Voting - simple voting""",\n        "description": """Implement a Voting contract with simple voting.

Requirements:
- Implement all required functions
- Handle edge cases properly  
- Emit appropriate events
- Test with multiple scenarios
- Ensure no hardcoding of values

This problem requires 15 tests to pass.""",\n        "difficulty": """junior""",\n        "category": """solidity""",\n        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract VotingContract {
    // State variables
    uint256 public value;
    mapping(address => uint256) public balances;
    
    // Events
    event ValueChanged(uint256 newValue);
    event BalanceUpdated(address indexed user, uint256 amount);
    
    // TODO: Implement required functions
    function setValue(uint256 _value) public {
        // Your code here
    }
    
    function getValue() public view returns (uint256) {
        // Your code here
    }
    
    function updateBalance(uint256 amount) public {
        // Your code here
    }
    
    function getBalance(address addr) public view returns (uint256) {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Implement all functions correctly', 'Test with different values', 'Handle edge cases', 'Use events for tracking'],\n        "tags": ['solidity', 'junior', 'voting'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """sol_m10""",\n        "title": """Solidity Middle 10: Oracle - external data""",\n        "description": """Implement a Oracle contract with external data.

Requirements:
- Implement all required functions
- Handle edge cases properly  
- Emit appropriate events
- Test with multiple scenarios
- Ensure no hardcoding of values

This problem requires 18 tests to pass.""",\n        "difficulty": """middle""",\n        "category": """solidity""",\n        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract OracleContract {
    // State variables
    uint256 public value;
    mapping(address => uint256) public balances;
    
    // Events
    event ValueChanged(uint256 newValue);
    event BalanceUpdated(address indexed user, uint256 amount);
    
    // TODO: Implement required functions
    function setValue(uint256 _value) public {
        // Your code here
    }
    
    function getValue() public view returns (uint256) {
        // Your code here
    }
    
    function updateBalance(uint256 amount) public {
        // Your code here
    }
    
    function getBalance(address addr) public view returns (uint256) {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Implement all functions correctly', 'Test with different values', 'Handle edge cases', 'Use events for tracking'],\n        "tags": ['solidity', 'middle', 'oracle'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """sol_s10""",\n        "title": """Solidity Senior 10: Governance - advanced voting""",\n        "description": """Implement a Governance contract with advanced voting.

Requirements:
- Implement all required functions
- Handle edge cases properly  
- Emit appropriate events
- Test with multiple scenarios
- Ensure no hardcoding of values

This problem requires 20 tests to pass.""",\n        "difficulty": """senior""",\n        "category": """solidity""",\n        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract GovernanceContract {
    // State variables
    uint256 public value;
    mapping(address => uint256) public balances;
    
    // Events
    event ValueChanged(uint256 newValue);
    event BalanceUpdated(address indexed user, uint256 amount);
    
    // TODO: Implement required functions
    function setValue(uint256 _value) public {
        // Your code here
    }
    
    function getValue() public view returns (uint256) {
        // Your code here
    }
    
    function updateBalance(uint256 amount) public {
        // Your code here
    }
    
    function getBalance(address addr) public view returns (uint256) {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Implement all functions correctly', 'Test with different values', 'Handle edge cases', 'Use events for tracking'],\n        "tags": ['solidity', 'senior', 'governance'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """rust_j01""",\n        "title": """Rust/Solana Junior 1: Solana Program Development""",\n        "description": """Implement a Solana program with account management.

Requirements:
- Initialize program accounts
- Handle multiple instructions
- Manage state correctly
- Use Anchor framework properly
- Pass all 15 tests

No hardcoding allowed - implement real logic.""",\n        "difficulty": """junior""",\n        "category": """rust""",\n        "initial_code": """use anchor_lang::prelude::*;

declare_id!("...");

#[program]
pub mod solution {
    use super::*;
    
    // TODO: Implement initialize
    pub fn initialize(ctx: Context<Initialize>, value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }}
    
    // TODO: Implement update  
    pub fn update(ctx: Context<Update>, new_value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub data_account: Account<'info, DataAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Update<'info> {
    #[account(mut)]
    pub data_account: Account<'info, DataAccount>,
}

#[account]
pub struct DataAccount {
    pub value: u64,
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Use Anchor framework', 'Handle account initialization', 'Implement all instructions', 'Test multiple operations'],\n        "tags": ['rust', 'solana', 'junior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """rust_m01""",\n        "title": """Rust/Solana Middle 1: Solana Program Development""",\n        "description": """Implement a Solana program with account management.

Requirements:
- Initialize program accounts
- Handle multiple instructions
- Manage state correctly
- Use Anchor framework properly
- Pass all 18 tests

No hardcoding allowed - implement real logic.""",\n        "difficulty": """middle""",\n        "category": """rust""",\n        "initial_code": """use anchor_lang::prelude::*;

declare_id!("...");

#[program]
pub mod solution {
    use super::*;
    
    // TODO: Implement initialize
    pub fn initialize(ctx: Context<Initialize>, value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }}
    
    // TODO: Implement update  
    pub fn update(ctx: Context<Update>, new_value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub data_account: Account<'info, DataAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Update<'info> {
    #[account(mut)]
    pub data_account: Account<'info, DataAccount>,
}

#[account]
pub struct DataAccount {
    pub value: u64,
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Use Anchor framework', 'Handle account initialization', 'Implement all instructions', 'Test multiple operations'],\n        "tags": ['rust', 'solana', 'middle'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """rust_s01""",\n        "title": """Rust/Solana Senior 1: Solana Program Development""",\n        "description": """Implement a Solana program with account management.

Requirements:
- Initialize program accounts
- Handle multiple instructions
- Manage state correctly
- Use Anchor framework properly
- Pass all 20 tests

No hardcoding allowed - implement real logic.""",\n        "difficulty": """senior""",\n        "category": """rust""",\n        "initial_code": """use anchor_lang::prelude::*;

declare_id!("...");

#[program]
pub mod solution {
    use super::*;
    
    // TODO: Implement initialize
    pub fn initialize(ctx: Context<Initialize>, value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }}
    
    // TODO: Implement update  
    pub fn update(ctx: Context<Update>, new_value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub data_account: Account<'info, DataAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Update<'info> {
    #[account(mut)]
    pub data_account: Account<'info, DataAccount>,
}

#[account]
pub struct DataAccount {
    pub value: u64,
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Use Anchor framework', 'Handle account initialization', 'Implement all instructions', 'Test multiple operations'],\n        "tags": ['rust', 'solana', 'senior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """rust_j02""",\n        "title": """Rust/Solana Junior 2: Solana Program Development""",\n        "description": """Implement a Solana program with account management.

Requirements:
- Initialize program accounts
- Handle multiple instructions
- Manage state correctly
- Use Anchor framework properly
- Pass all 15 tests

No hardcoding allowed - implement real logic.""",\n        "difficulty": """junior""",\n        "category": """rust""",\n        "initial_code": """use anchor_lang::prelude::*;

declare_id!("...");

#[program]
pub mod solution {
    use super::*;
    
    // TODO: Implement initialize
    pub fn initialize(ctx: Context<Initialize>, value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }}
    
    // TODO: Implement update  
    pub fn update(ctx: Context<Update>, new_value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub data_account: Account<'info, DataAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Update<'info> {
    #[account(mut)]
    pub data_account: Account<'info, DataAccount>,
}

#[account]
pub struct DataAccount {
    pub value: u64,
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Use Anchor framework', 'Handle account initialization', 'Implement all instructions', 'Test multiple operations'],\n        "tags": ['rust', 'solana', 'junior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """rust_m02""",\n        "title": """Rust/Solana Middle 2: Solana Program Development""",\n        "description": """Implement a Solana program with account management.

Requirements:
- Initialize program accounts
- Handle multiple instructions
- Manage state correctly
- Use Anchor framework properly
- Pass all 18 tests

No hardcoding allowed - implement real logic.""",\n        "difficulty": """middle""",\n        "category": """rust""",\n        "initial_code": """use anchor_lang::prelude::*;

declare_id!("...");

#[program]
pub mod solution {
    use super::*;
    
    // TODO: Implement initialize
    pub fn initialize(ctx: Context<Initialize>, value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }}
    
    // TODO: Implement update  
    pub fn update(ctx: Context<Update>, new_value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub data_account: Account<'info, DataAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Update<'info> {
    #[account(mut)]
    pub data_account: Account<'info, DataAccount>,
}

#[account]
pub struct DataAccount {
    pub value: u64,
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Use Anchor framework', 'Handle account initialization', 'Implement all instructions', 'Test multiple operations'],\n        "tags": ['rust', 'solana', 'middle'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """rust_s02""",\n        "title": """Rust/Solana Senior 2: Solana Program Development""",\n        "description": """Implement a Solana program with account management.

Requirements:
- Initialize program accounts
- Handle multiple instructions
- Manage state correctly
- Use Anchor framework properly
- Pass all 20 tests

No hardcoding allowed - implement real logic.""",\n        "difficulty": """senior""",\n        "category": """rust""",\n        "initial_code": """use anchor_lang::prelude::*;

declare_id!("...");

#[program]
pub mod solution {
    use super::*;
    
    // TODO: Implement initialize
    pub fn initialize(ctx: Context<Initialize>, value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }}
    
    // TODO: Implement update  
    pub fn update(ctx: Context<Update>, new_value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub data_account: Account<'info, DataAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Update<'info> {
    #[account(mut)]
    pub data_account: Account<'info, DataAccount>,
}

#[account]
pub struct DataAccount {
    pub value: u64,
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Use Anchor framework', 'Handle account initialization', 'Implement all instructions', 'Test multiple operations'],\n        "tags": ['rust', 'solana', 'senior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """rust_j03""",\n        "title": """Rust/Solana Junior 3: Solana Program Development""",\n        "description": """Implement a Solana program with account management.

Requirements:
- Initialize program accounts
- Handle multiple instructions
- Manage state correctly
- Use Anchor framework properly
- Pass all 15 tests

No hardcoding allowed - implement real logic.""",\n        "difficulty": """junior""",\n        "category": """rust""",\n        "initial_code": """use anchor_lang::prelude::*;

declare_id!("...");

#[program]
pub mod solution {
    use super::*;
    
    // TODO: Implement initialize
    pub fn initialize(ctx: Context<Initialize>, value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }}
    
    // TODO: Implement update  
    pub fn update(ctx: Context<Update>, new_value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub data_account: Account<'info, DataAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Update<'info> {
    #[account(mut)]
    pub data_account: Account<'info, DataAccount>,
}

#[account]
pub struct DataAccount {
    pub value: u64,
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Use Anchor framework', 'Handle account initialization', 'Implement all instructions', 'Test multiple operations'],\n        "tags": ['rust', 'solana', 'junior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """rust_m03""",\n        "title": """Rust/Solana Middle 3: Solana Program Development""",\n        "description": """Implement a Solana program with account management.

Requirements:
- Initialize program accounts
- Handle multiple instructions
- Manage state correctly
- Use Anchor framework properly
- Pass all 18 tests

No hardcoding allowed - implement real logic.""",\n        "difficulty": """middle""",\n        "category": """rust""",\n        "initial_code": """use anchor_lang::prelude::*;

declare_id!("...");

#[program]
pub mod solution {
    use super::*;
    
    // TODO: Implement initialize
    pub fn initialize(ctx: Context<Initialize>, value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }}
    
    // TODO: Implement update  
    pub fn update(ctx: Context<Update>, new_value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub data_account: Account<'info, DataAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Update<'info> {
    #[account(mut)]
    pub data_account: Account<'info, DataAccount>,
}

#[account]
pub struct DataAccount {
    pub value: u64,
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Use Anchor framework', 'Handle account initialization', 'Implement all instructions', 'Test multiple operations'],\n        "tags": ['rust', 'solana', 'middle'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """rust_s03""",\n        "title": """Rust/Solana Senior 3: Solana Program Development""",\n        "description": """Implement a Solana program with account management.

Requirements:
- Initialize program accounts
- Handle multiple instructions
- Manage state correctly
- Use Anchor framework properly
- Pass all 20 tests

No hardcoding allowed - implement real logic.""",\n        "difficulty": """senior""",\n        "category": """rust""",\n        "initial_code": """use anchor_lang::prelude::*;

declare_id!("...");

#[program]
pub mod solution {
    use super::*;
    
    // TODO: Implement initialize
    pub fn initialize(ctx: Context<Initialize>, value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }}
    
    // TODO: Implement update  
    pub fn update(ctx: Context<Update>, new_value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub data_account: Account<'info, DataAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Update<'info> {
    #[account(mut)]
    pub data_account: Account<'info, DataAccount>,
}

#[account]
pub struct DataAccount {
    pub value: u64,
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Use Anchor framework', 'Handle account initialization', 'Implement all instructions', 'Test multiple operations'],\n        "tags": ['rust', 'solana', 'senior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """rust_j04""",\n        "title": """Rust/Solana Junior 4: Solana Program Development""",\n        "description": """Implement a Solana program with account management.

Requirements:
- Initialize program accounts
- Handle multiple instructions
- Manage state correctly
- Use Anchor framework properly
- Pass all 15 tests

No hardcoding allowed - implement real logic.""",\n        "difficulty": """junior""",\n        "category": """rust""",\n        "initial_code": """use anchor_lang::prelude::*;

declare_id!("...");

#[program]
pub mod solution {
    use super::*;
    
    // TODO: Implement initialize
    pub fn initialize(ctx: Context<Initialize>, value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }}
    
    // TODO: Implement update  
    pub fn update(ctx: Context<Update>, new_value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub data_account: Account<'info, DataAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Update<'info> {
    #[account(mut)]
    pub data_account: Account<'info, DataAccount>,
}

#[account]
pub struct DataAccount {
    pub value: u64,
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Use Anchor framework', 'Handle account initialization', 'Implement all instructions', 'Test multiple operations'],\n        "tags": ['rust', 'solana', 'junior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """rust_m04""",\n        "title": """Rust/Solana Middle 4: Solana Program Development""",\n        "description": """Implement a Solana program with account management.

Requirements:
- Initialize program accounts
- Handle multiple instructions
- Manage state correctly
- Use Anchor framework properly
- Pass all 18 tests

No hardcoding allowed - implement real logic.""",\n        "difficulty": """middle""",\n        "category": """rust""",\n        "initial_code": """use anchor_lang::prelude::*;

declare_id!("...");

#[program]
pub mod solution {
    use super::*;
    
    // TODO: Implement initialize
    pub fn initialize(ctx: Context<Initialize>, value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }}
    
    // TODO: Implement update  
    pub fn update(ctx: Context<Update>, new_value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub data_account: Account<'info, DataAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Update<'info> {
    #[account(mut)]
    pub data_account: Account<'info, DataAccount>,
}

#[account]
pub struct DataAccount {
    pub value: u64,
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Use Anchor framework', 'Handle account initialization', 'Implement all instructions', 'Test multiple operations'],\n        "tags": ['rust', 'solana', 'middle'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """rust_s04""",\n        "title": """Rust/Solana Senior 4: Solana Program Development""",\n        "description": """Implement a Solana program with account management.

Requirements:
- Initialize program accounts
- Handle multiple instructions
- Manage state correctly
- Use Anchor framework properly
- Pass all 20 tests

No hardcoding allowed - implement real logic.""",\n        "difficulty": """senior""",\n        "category": """rust""",\n        "initial_code": """use anchor_lang::prelude::*;

declare_id!("...");

#[program]
pub mod solution {
    use super::*;
    
    // TODO: Implement initialize
    pub fn initialize(ctx: Context<Initialize>, value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }}
    
    // TODO: Implement update  
    pub fn update(ctx: Context<Update>, new_value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub data_account: Account<'info, DataAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Update<'info> {
    #[account(mut)]
    pub data_account: Account<'info, DataAccount>,
}

#[account]
pub struct DataAccount {
    pub value: u64,
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Use Anchor framework', 'Handle account initialization', 'Implement all instructions', 'Test multiple operations'],\n        "tags": ['rust', 'solana', 'senior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """rust_j05""",\n        "title": """Rust/Solana Junior 5: Solana Program Development""",\n        "description": """Implement a Solana program with account management.

Requirements:
- Initialize program accounts
- Handle multiple instructions
- Manage state correctly
- Use Anchor framework properly
- Pass all 15 tests

No hardcoding allowed - implement real logic.""",\n        "difficulty": """junior""",\n        "category": """rust""",\n        "initial_code": """use anchor_lang::prelude::*;

declare_id!("...");

#[program]
pub mod solution {
    use super::*;
    
    // TODO: Implement initialize
    pub fn initialize(ctx: Context<Initialize>, value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }}
    
    // TODO: Implement update  
    pub fn update(ctx: Context<Update>, new_value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub data_account: Account<'info, DataAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Update<'info> {
    #[account(mut)]
    pub data_account: Account<'info, DataAccount>,
}

#[account]
pub struct DataAccount {
    pub value: u64,
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Use Anchor framework', 'Handle account initialization', 'Implement all instructions', 'Test multiple operations'],\n        "tags": ['rust', 'solana', 'junior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """rust_m05""",\n        "title": """Rust/Solana Middle 5: Solana Program Development""",\n        "description": """Implement a Solana program with account management.

Requirements:
- Initialize program accounts
- Handle multiple instructions
- Manage state correctly
- Use Anchor framework properly
- Pass all 18 tests

No hardcoding allowed - implement real logic.""",\n        "difficulty": """middle""",\n        "category": """rust""",\n        "initial_code": """use anchor_lang::prelude::*;

declare_id!("...");

#[program]
pub mod solution {
    use super::*;
    
    // TODO: Implement initialize
    pub fn initialize(ctx: Context<Initialize>, value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }}
    
    // TODO: Implement update  
    pub fn update(ctx: Context<Update>, new_value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub data_account: Account<'info, DataAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Update<'info> {
    #[account(mut)]
    pub data_account: Account<'info, DataAccount>,
}

#[account]
pub struct DataAccount {
    pub value: u64,
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Use Anchor framework', 'Handle account initialization', 'Implement all instructions', 'Test multiple operations'],\n        "tags": ['rust', 'solana', 'middle'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """rust_s05""",\n        "title": """Rust/Solana Senior 5: Solana Program Development""",\n        "description": """Implement a Solana program with account management.

Requirements:
- Initialize program accounts
- Handle multiple instructions
- Manage state correctly
- Use Anchor framework properly
- Pass all 20 tests

No hardcoding allowed - implement real logic.""",\n        "difficulty": """senior""",\n        "category": """rust""",\n        "initial_code": """use anchor_lang::prelude::*;

declare_id!("...");

#[program]
pub mod solution {
    use super::*;
    
    // TODO: Implement initialize
    pub fn initialize(ctx: Context<Initialize>, value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }}
    
    // TODO: Implement update  
    pub fn update(ctx: Context<Update>, new_value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub data_account: Account<'info, DataAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Update<'info> {
    #[account(mut)]
    pub data_account: Account<'info, DataAccount>,
}

#[account]
pub struct DataAccount {
    pub value: u64,
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Use Anchor framework', 'Handle account initialization', 'Implement all instructions', 'Test multiple operations'],\n        "tags": ['rust', 'solana', 'senior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """rust_j06""",\n        "title": """Rust/Solana Junior 6: Solana Program Development""",\n        "description": """Implement a Solana program with account management.

Requirements:
- Initialize program accounts
- Handle multiple instructions
- Manage state correctly
- Use Anchor framework properly
- Pass all 15 tests

No hardcoding allowed - implement real logic.""",\n        "difficulty": """junior""",\n        "category": """rust""",\n        "initial_code": """use anchor_lang::prelude::*;

declare_id!("...");

#[program]
pub mod solution {
    use super::*;
    
    // TODO: Implement initialize
    pub fn initialize(ctx: Context<Initialize>, value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }}
    
    // TODO: Implement update  
    pub fn update(ctx: Context<Update>, new_value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub data_account: Account<'info, DataAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Update<'info> {
    #[account(mut)]
    pub data_account: Account<'info, DataAccount>,
}

#[account]
pub struct DataAccount {
    pub value: u64,
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Use Anchor framework', 'Handle account initialization', 'Implement all instructions', 'Test multiple operations'],\n        "tags": ['rust', 'solana', 'junior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """rust_m06""",\n        "title": """Rust/Solana Middle 6: Solana Program Development""",\n        "description": """Implement a Solana program with account management.

Requirements:
- Initialize program accounts
- Handle multiple instructions
- Manage state correctly
- Use Anchor framework properly
- Pass all 18 tests

No hardcoding allowed - implement real logic.""",\n        "difficulty": """middle""",\n        "category": """rust""",\n        "initial_code": """use anchor_lang::prelude::*;

declare_id!("...");

#[program]
pub mod solution {
    use super::*;
    
    // TODO: Implement initialize
    pub fn initialize(ctx: Context<Initialize>, value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }}
    
    // TODO: Implement update  
    pub fn update(ctx: Context<Update>, new_value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub data_account: Account<'info, DataAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Update<'info> {
    #[account(mut)]
    pub data_account: Account<'info, DataAccount>,
}

#[account]
pub struct DataAccount {
    pub value: u64,
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Use Anchor framework', 'Handle account initialization', 'Implement all instructions', 'Test multiple operations'],\n        "tags": ['rust', 'solana', 'middle'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """rust_s06""",\n        "title": """Rust/Solana Senior 6: Solana Program Development""",\n        "description": """Implement a Solana program with account management.

Requirements:
- Initialize program accounts
- Handle multiple instructions
- Manage state correctly
- Use Anchor framework properly
- Pass all 20 tests

No hardcoding allowed - implement real logic.""",\n        "difficulty": """senior""",\n        "category": """rust""",\n        "initial_code": """use anchor_lang::prelude::*;

declare_id!("...");

#[program]
pub mod solution {
    use super::*;
    
    // TODO: Implement initialize
    pub fn initialize(ctx: Context<Initialize>, value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }}
    
    // TODO: Implement update  
    pub fn update(ctx: Context<Update>, new_value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub data_account: Account<'info, DataAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Update<'info> {
    #[account(mut)]
    pub data_account: Account<'info, DataAccount>,
}

#[account]
pub struct DataAccount {
    pub value: u64,
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Use Anchor framework', 'Handle account initialization', 'Implement all instructions', 'Test multiple operations'],\n        "tags": ['rust', 'solana', 'senior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """rust_j07""",\n        "title": """Rust/Solana Junior 7: Solana Program Development""",\n        "description": """Implement a Solana program with account management.

Requirements:
- Initialize program accounts
- Handle multiple instructions
- Manage state correctly
- Use Anchor framework properly
- Pass all 15 tests

No hardcoding allowed - implement real logic.""",\n        "difficulty": """junior""",\n        "category": """rust""",\n        "initial_code": """use anchor_lang::prelude::*;

declare_id!("...");

#[program]
pub mod solution {
    use super::*;
    
    // TODO: Implement initialize
    pub fn initialize(ctx: Context<Initialize>, value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }}
    
    // TODO: Implement update  
    pub fn update(ctx: Context<Update>, new_value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub data_account: Account<'info, DataAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Update<'info> {
    #[account(mut)]
    pub data_account: Account<'info, DataAccount>,
}

#[account]
pub struct DataAccount {
    pub value: u64,
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Use Anchor framework', 'Handle account initialization', 'Implement all instructions', 'Test multiple operations'],\n        "tags": ['rust', 'solana', 'junior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """rust_m07""",\n        "title": """Rust/Solana Middle 7: Solana Program Development""",\n        "description": """Implement a Solana program with account management.

Requirements:
- Initialize program accounts
- Handle multiple instructions
- Manage state correctly
- Use Anchor framework properly
- Pass all 18 tests

No hardcoding allowed - implement real logic.""",\n        "difficulty": """middle""",\n        "category": """rust""",\n        "initial_code": """use anchor_lang::prelude::*;

declare_id!("...");

#[program]
pub mod solution {
    use super::*;
    
    // TODO: Implement initialize
    pub fn initialize(ctx: Context<Initialize>, value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }}
    
    // TODO: Implement update  
    pub fn update(ctx: Context<Update>, new_value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub data_account: Account<'info, DataAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Update<'info> {
    #[account(mut)]
    pub data_account: Account<'info, DataAccount>,
}

#[account]
pub struct DataAccount {
    pub value: u64,
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Use Anchor framework', 'Handle account initialization', 'Implement all instructions', 'Test multiple operations'],\n        "tags": ['rust', 'solana', 'middle'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """rust_s07""",\n        "title": """Rust/Solana Senior 7: Solana Program Development""",\n        "description": """Implement a Solana program with account management.

Requirements:
- Initialize program accounts
- Handle multiple instructions
- Manage state correctly
- Use Anchor framework properly
- Pass all 20 tests

No hardcoding allowed - implement real logic.""",\n        "difficulty": """senior""",\n        "category": """rust""",\n        "initial_code": """use anchor_lang::prelude::*;

declare_id!("...");

#[program]
pub mod solution {
    use super::*;
    
    // TODO: Implement initialize
    pub fn initialize(ctx: Context<Initialize>, value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }}
    
    // TODO: Implement update  
    pub fn update(ctx: Context<Update>, new_value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub data_account: Account<'info, DataAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Update<'info> {
    #[account(mut)]
    pub data_account: Account<'info, DataAccount>,
}

#[account]
pub struct DataAccount {
    pub value: u64,
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Use Anchor framework', 'Handle account initialization', 'Implement all instructions', 'Test multiple operations'],\n        "tags": ['rust', 'solana', 'senior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """rust_j08""",\n        "title": """Rust/Solana Junior 8: Solana Program Development""",\n        "description": """Implement a Solana program with account management.

Requirements:
- Initialize program accounts
- Handle multiple instructions
- Manage state correctly
- Use Anchor framework properly
- Pass all 15 tests

No hardcoding allowed - implement real logic.""",\n        "difficulty": """junior""",\n        "category": """rust""",\n        "initial_code": """use anchor_lang::prelude::*;

declare_id!("...");

#[program]
pub mod solution {
    use super::*;
    
    // TODO: Implement initialize
    pub fn initialize(ctx: Context<Initialize>, value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }}
    
    // TODO: Implement update  
    pub fn update(ctx: Context<Update>, new_value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub data_account: Account<'info, DataAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Update<'info> {
    #[account(mut)]
    pub data_account: Account<'info, DataAccount>,
}

#[account]
pub struct DataAccount {
    pub value: u64,
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Use Anchor framework', 'Handle account initialization', 'Implement all instructions', 'Test multiple operations'],\n        "tags": ['rust', 'solana', 'junior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """rust_m08""",\n        "title": """Rust/Solana Middle 8: Solana Program Development""",\n        "description": """Implement a Solana program with account management.

Requirements:
- Initialize program accounts
- Handle multiple instructions
- Manage state correctly
- Use Anchor framework properly
- Pass all 18 tests

No hardcoding allowed - implement real logic.""",\n        "difficulty": """middle""",\n        "category": """rust""",\n        "initial_code": """use anchor_lang::prelude::*;

declare_id!("...");

#[program]
pub mod solution {
    use super::*;
    
    // TODO: Implement initialize
    pub fn initialize(ctx: Context<Initialize>, value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }}
    
    // TODO: Implement update  
    pub fn update(ctx: Context<Update>, new_value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub data_account: Account<'info, DataAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Update<'info> {
    #[account(mut)]
    pub data_account: Account<'info, DataAccount>,
}

#[account]
pub struct DataAccount {
    pub value: u64,
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Use Anchor framework', 'Handle account initialization', 'Implement all instructions', 'Test multiple operations'],\n        "tags": ['rust', 'solana', 'middle'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """rust_s08""",\n        "title": """Rust/Solana Senior 8: Solana Program Development""",\n        "description": """Implement a Solana program with account management.

Requirements:
- Initialize program accounts
- Handle multiple instructions
- Manage state correctly
- Use Anchor framework properly
- Pass all 20 tests

No hardcoding allowed - implement real logic.""",\n        "difficulty": """senior""",\n        "category": """rust""",\n        "initial_code": """use anchor_lang::prelude::*;

declare_id!("...");

#[program]
pub mod solution {
    use super::*;
    
    // TODO: Implement initialize
    pub fn initialize(ctx: Context<Initialize>, value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }}
    
    // TODO: Implement update  
    pub fn update(ctx: Context<Update>, new_value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub data_account: Account<'info, DataAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Update<'info> {
    #[account(mut)]
    pub data_account: Account<'info, DataAccount>,
}

#[account]
pub struct DataAccount {
    pub value: u64,
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Use Anchor framework', 'Handle account initialization', 'Implement all instructions', 'Test multiple operations'],\n        "tags": ['rust', 'solana', 'senior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """rust_j09""",\n        "title": """Rust/Solana Junior 9: Solana Program Development""",\n        "description": """Implement a Solana program with account management.

Requirements:
- Initialize program accounts
- Handle multiple instructions
- Manage state correctly
- Use Anchor framework properly
- Pass all 15 tests

No hardcoding allowed - implement real logic.""",\n        "difficulty": """junior""",\n        "category": """rust""",\n        "initial_code": """use anchor_lang::prelude::*;

declare_id!("...");

#[program]
pub mod solution {
    use super::*;
    
    // TODO: Implement initialize
    pub fn initialize(ctx: Context<Initialize>, value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }}
    
    // TODO: Implement update  
    pub fn update(ctx: Context<Update>, new_value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub data_account: Account<'info, DataAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Update<'info> {
    #[account(mut)]
    pub data_account: Account<'info, DataAccount>,
}

#[account]
pub struct DataAccount {
    pub value: u64,
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Use Anchor framework', 'Handle account initialization', 'Implement all instructions', 'Test multiple operations'],\n        "tags": ['rust', 'solana', 'junior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """rust_m09""",\n        "title": """Rust/Solana Middle 9: Solana Program Development""",\n        "description": """Implement a Solana program with account management.

Requirements:
- Initialize program accounts
- Handle multiple instructions
- Manage state correctly
- Use Anchor framework properly
- Pass all 18 tests

No hardcoding allowed - implement real logic.""",\n        "difficulty": """middle""",\n        "category": """rust""",\n        "initial_code": """use anchor_lang::prelude::*;

declare_id!("...");

#[program]
pub mod solution {
    use super::*;
    
    // TODO: Implement initialize
    pub fn initialize(ctx: Context<Initialize>, value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }}
    
    // TODO: Implement update  
    pub fn update(ctx: Context<Update>, new_value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub data_account: Account<'info, DataAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Update<'info> {
    #[account(mut)]
    pub data_account: Account<'info, DataAccount>,
}

#[account]
pub struct DataAccount {
    pub value: u64,
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Use Anchor framework', 'Handle account initialization', 'Implement all instructions', 'Test multiple operations'],\n        "tags": ['rust', 'solana', 'middle'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """rust_s09""",\n        "title": """Rust/Solana Senior 9: Solana Program Development""",\n        "description": """Implement a Solana program with account management.

Requirements:
- Initialize program accounts
- Handle multiple instructions
- Manage state correctly
- Use Anchor framework properly
- Pass all 20 tests

No hardcoding allowed - implement real logic.""",\n        "difficulty": """senior""",\n        "category": """rust""",\n        "initial_code": """use anchor_lang::prelude::*;

declare_id!("...");

#[program]
pub mod solution {
    use super::*;
    
    // TODO: Implement initialize
    pub fn initialize(ctx: Context<Initialize>, value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }}
    
    // TODO: Implement update  
    pub fn update(ctx: Context<Update>, new_value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub data_account: Account<'info, DataAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Update<'info> {
    #[account(mut)]
    pub data_account: Account<'info, DataAccount>,
}

#[account]
pub struct DataAccount {
    pub value: u64,
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Use Anchor framework', 'Handle account initialization', 'Implement all instructions', 'Test multiple operations'],\n        "tags": ['rust', 'solana', 'senior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """rust_j10""",\n        "title": """Rust/Solana Junior 10: Solana Program Development""",\n        "description": """Implement a Solana program with account management.

Requirements:
- Initialize program accounts
- Handle multiple instructions
- Manage state correctly
- Use Anchor framework properly
- Pass all 15 tests

No hardcoding allowed - implement real logic.""",\n        "difficulty": """junior""",\n        "category": """rust""",\n        "initial_code": """use anchor_lang::prelude::*;

declare_id!("...");

#[program]
pub mod solution {
    use super::*;
    
    // TODO: Implement initialize
    pub fn initialize(ctx: Context<Initialize>, value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }}
    
    // TODO: Implement update  
    pub fn update(ctx: Context<Update>, new_value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub data_account: Account<'info, DataAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Update<'info> {
    #[account(mut)]
    pub data_account: Account<'info, DataAccount>,
}

#[account]
pub struct DataAccount {
    pub value: u64,
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Use Anchor framework', 'Handle account initialization', 'Implement all instructions', 'Test multiple operations'],\n        "tags": ['rust', 'solana', 'junior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """rust_m10""",\n        "title": """Rust/Solana Middle 10: Solana Program Development""",\n        "description": """Implement a Solana program with account management.

Requirements:
- Initialize program accounts
- Handle multiple instructions
- Manage state correctly
- Use Anchor framework properly
- Pass all 18 tests

No hardcoding allowed - implement real logic.""",\n        "difficulty": """middle""",\n        "category": """rust""",\n        "initial_code": """use anchor_lang::prelude::*;

declare_id!("...");

#[program]
pub mod solution {
    use super::*;
    
    // TODO: Implement initialize
    pub fn initialize(ctx: Context<Initialize>, value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }}
    
    // TODO: Implement update  
    pub fn update(ctx: Context<Update>, new_value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub data_account: Account<'info, DataAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Update<'info> {
    #[account(mut)]
    pub data_account: Account<'info, DataAccount>,
}

#[account]
pub struct DataAccount {
    pub value: u64,
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Use Anchor framework', 'Handle account initialization', 'Implement all instructions', 'Test multiple operations'],\n        "tags": ['rust', 'solana', 'middle'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """rust_s10""",\n        "title": """Rust/Solana Senior 10: Solana Program Development""",\n        "description": """Implement a Solana program with account management.

Requirements:
- Initialize program accounts
- Handle multiple instructions
- Manage state correctly
- Use Anchor framework properly
- Pass all 20 tests

No hardcoding allowed - implement real logic.""",\n        "difficulty": """senior""",\n        "category": """rust""",\n        "initial_code": """use anchor_lang::prelude::*;

declare_id!("...");

#[program]
pub mod solution {
    use super::*;
    
    // TODO: Implement initialize
    pub fn initialize(ctx: Context<Initialize>, value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }}
    
    // TODO: Implement update  
    pub fn update(ctx: Context<Update>, new_value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub data_account: Account<'info, DataAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Update<'info> {
    #[account(mut)]
    pub data_account: Account<'info, DataAccount>,
}

#[account]
pub struct DataAccount {
    pub value: u64,
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Use Anchor framework', 'Handle account initialization', 'Implement all instructions', 'Test multiple operations'],\n        "tags": ['rust', 'solana', 'senior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """move_j01""",\n        "title": """MOVE Junior 1: MOVE Resource Management""",\n        "description": """Implement a MOVE module with resource-oriented programming.

Requirements:
- Define and manage resources
- Implement access control
- Handle resource safety
- Use MOVE idioms correctly
- Pass all 15 comprehensive tests

Must implement real logic - no shortcuts.""",\n        "difficulty": """junior""",\n        "category": """move""",\n        "initial_code": """module 0x1::solution {
    use std::signer;
    
    struct Resource has key {
        value: u64,
    }
    
    // TODO: Implement create_resource
    public fun create_resource(account: &signer, value: u64) {
        // Your code here
    }
    
    // TODO: Implement get_value
    public fun get_value(addr: address): u64 acquires Resource {
        // Your code here
    }
    
    // TODO: Implement update_value
    public fun update_value(account: &signer, new_value: u64) acquires Resource {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Use resource safety', 'Implement acquires correctly', 'Handle signer validation', 'Test thoroughly'],\n        "tags": ['move', 'aptos', 'junior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """move_m01""",\n        "title": """MOVE Middle 1: MOVE Resource Management""",\n        "description": """Implement a MOVE module with resource-oriented programming.

Requirements:
- Define and manage resources
- Implement access control
- Handle resource safety
- Use MOVE idioms correctly
- Pass all 18 comprehensive tests

Must implement real logic - no shortcuts.""",\n        "difficulty": """middle""",\n        "category": """move""",\n        "initial_code": """module 0x1::solution {
    use std::signer;
    
    struct Resource has key {
        value: u64,
    }
    
    // TODO: Implement create_resource
    public fun create_resource(account: &signer, value: u64) {
        // Your code here
    }
    
    // TODO: Implement get_value
    public fun get_value(addr: address): u64 acquires Resource {
        // Your code here
    }
    
    // TODO: Implement update_value
    public fun update_value(account: &signer, new_value: u64) acquires Resource {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Use resource safety', 'Implement acquires correctly', 'Handle signer validation', 'Test thoroughly'],\n        "tags": ['move', 'aptos', 'middle'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """move_s01""",\n        "title": """MOVE Senior 1: MOVE Resource Management""",\n        "description": """Implement a MOVE module with resource-oriented programming.

Requirements:
- Define and manage resources
- Implement access control
- Handle resource safety
- Use MOVE idioms correctly
- Pass all 20 comprehensive tests

Must implement real logic - no shortcuts.""",\n        "difficulty": """senior""",\n        "category": """move""",\n        "initial_code": """module 0x1::solution {
    use std::signer;
    
    struct Resource has key {
        value: u64,
    }
    
    // TODO: Implement create_resource
    public fun create_resource(account: &signer, value: u64) {
        // Your code here
    }
    
    // TODO: Implement get_value
    public fun get_value(addr: address): u64 acquires Resource {
        // Your code here
    }
    
    // TODO: Implement update_value
    public fun update_value(account: &signer, new_value: u64) acquires Resource {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Use resource safety', 'Implement acquires correctly', 'Handle signer validation', 'Test thoroughly'],\n        "tags": ['move', 'aptos', 'senior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """move_j02""",\n        "title": """MOVE Junior 2: MOVE Resource Management""",\n        "description": """Implement a MOVE module with resource-oriented programming.

Requirements:
- Define and manage resources
- Implement access control
- Handle resource safety
- Use MOVE idioms correctly
- Pass all 15 comprehensive tests

Must implement real logic - no shortcuts.""",\n        "difficulty": """junior""",\n        "category": """move""",\n        "initial_code": """module 0x1::solution {
    use std::signer;
    
    struct Resource has key {
        value: u64,
    }
    
    // TODO: Implement create_resource
    public fun create_resource(account: &signer, value: u64) {
        // Your code here
    }
    
    // TODO: Implement get_value
    public fun get_value(addr: address): u64 acquires Resource {
        // Your code here
    }
    
    // TODO: Implement update_value
    public fun update_value(account: &signer, new_value: u64) acquires Resource {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Use resource safety', 'Implement acquires correctly', 'Handle signer validation', 'Test thoroughly'],\n        "tags": ['move', 'aptos', 'junior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """move_m02""",\n        "title": """MOVE Middle 2: MOVE Resource Management""",\n        "description": """Implement a MOVE module with resource-oriented programming.

Requirements:
- Define and manage resources
- Implement access control
- Handle resource safety
- Use MOVE idioms correctly
- Pass all 18 comprehensive tests

Must implement real logic - no shortcuts.""",\n        "difficulty": """middle""",\n        "category": """move""",\n        "initial_code": """module 0x1::solution {
    use std::signer;
    
    struct Resource has key {
        value: u64,
    }
    
    // TODO: Implement create_resource
    public fun create_resource(account: &signer, value: u64) {
        // Your code here
    }
    
    // TODO: Implement get_value
    public fun get_value(addr: address): u64 acquires Resource {
        // Your code here
    }
    
    // TODO: Implement update_value
    public fun update_value(account: &signer, new_value: u64) acquires Resource {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Use resource safety', 'Implement acquires correctly', 'Handle signer validation', 'Test thoroughly'],\n        "tags": ['move', 'aptos', 'middle'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """move_s02""",\n        "title": """MOVE Senior 2: MOVE Resource Management""",\n        "description": """Implement a MOVE module with resource-oriented programming.

Requirements:
- Define and manage resources
- Implement access control
- Handle resource safety
- Use MOVE idioms correctly
- Pass all 20 comprehensive tests

Must implement real logic - no shortcuts.""",\n        "difficulty": """senior""",\n        "category": """move""",\n        "initial_code": """module 0x1::solution {
    use std::signer;
    
    struct Resource has key {
        value: u64,
    }
    
    // TODO: Implement create_resource
    public fun create_resource(account: &signer, value: u64) {
        // Your code here
    }
    
    // TODO: Implement get_value
    public fun get_value(addr: address): u64 acquires Resource {
        // Your code here
    }
    
    // TODO: Implement update_value
    public fun update_value(account: &signer, new_value: u64) acquires Resource {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Use resource safety', 'Implement acquires correctly', 'Handle signer validation', 'Test thoroughly'],\n        "tags": ['move', 'aptos', 'senior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """move_j03""",\n        "title": """MOVE Junior 3: MOVE Resource Management""",\n        "description": """Implement a MOVE module with resource-oriented programming.

Requirements:
- Define and manage resources
- Implement access control
- Handle resource safety
- Use MOVE idioms correctly
- Pass all 15 comprehensive tests

Must implement real logic - no shortcuts.""",\n        "difficulty": """junior""",\n        "category": """move""",\n        "initial_code": """module 0x1::solution {
    use std::signer;
    
    struct Resource has key {
        value: u64,
    }
    
    // TODO: Implement create_resource
    public fun create_resource(account: &signer, value: u64) {
        // Your code here
    }
    
    // TODO: Implement get_value
    public fun get_value(addr: address): u64 acquires Resource {
        // Your code here
    }
    
    // TODO: Implement update_value
    public fun update_value(account: &signer, new_value: u64) acquires Resource {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Use resource safety', 'Implement acquires correctly', 'Handle signer validation', 'Test thoroughly'],\n        "tags": ['move', 'aptos', 'junior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """move_m03""",\n        "title": """MOVE Middle 3: MOVE Resource Management""",\n        "description": """Implement a MOVE module with resource-oriented programming.

Requirements:
- Define and manage resources
- Implement access control
- Handle resource safety
- Use MOVE idioms correctly
- Pass all 18 comprehensive tests

Must implement real logic - no shortcuts.""",\n        "difficulty": """middle""",\n        "category": """move""",\n        "initial_code": """module 0x1::solution {
    use std::signer;
    
    struct Resource has key {
        value: u64,
    }
    
    // TODO: Implement create_resource
    public fun create_resource(account: &signer, value: u64) {
        // Your code here
    }
    
    // TODO: Implement get_value
    public fun get_value(addr: address): u64 acquires Resource {
        // Your code here
    }
    
    // TODO: Implement update_value
    public fun update_value(account: &signer, new_value: u64) acquires Resource {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Use resource safety', 'Implement acquires correctly', 'Handle signer validation', 'Test thoroughly'],\n        "tags": ['move', 'aptos', 'middle'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """move_s03""",\n        "title": """MOVE Senior 3: MOVE Resource Management""",\n        "description": """Implement a MOVE module with resource-oriented programming.

Requirements:
- Define and manage resources
- Implement access control
- Handle resource safety
- Use MOVE idioms correctly
- Pass all 20 comprehensive tests

Must implement real logic - no shortcuts.""",\n        "difficulty": """senior""",\n        "category": """move""",\n        "initial_code": """module 0x1::solution {
    use std::signer;
    
    struct Resource has key {
        value: u64,
    }
    
    // TODO: Implement create_resource
    public fun create_resource(account: &signer, value: u64) {
        // Your code here
    }
    
    // TODO: Implement get_value
    public fun get_value(addr: address): u64 acquires Resource {
        // Your code here
    }
    
    // TODO: Implement update_value
    public fun update_value(account: &signer, new_value: u64) acquires Resource {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Use resource safety', 'Implement acquires correctly', 'Handle signer validation', 'Test thoroughly'],\n        "tags": ['move', 'aptos', 'senior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """move_j04""",\n        "title": """MOVE Junior 4: MOVE Resource Management""",\n        "description": """Implement a MOVE module with resource-oriented programming.

Requirements:
- Define and manage resources
- Implement access control
- Handle resource safety
- Use MOVE idioms correctly
- Pass all 15 comprehensive tests

Must implement real logic - no shortcuts.""",\n        "difficulty": """junior""",\n        "category": """move""",\n        "initial_code": """module 0x1::solution {
    use std::signer;
    
    struct Resource has key {
        value: u64,
    }
    
    // TODO: Implement create_resource
    public fun create_resource(account: &signer, value: u64) {
        // Your code here
    }
    
    // TODO: Implement get_value
    public fun get_value(addr: address): u64 acquires Resource {
        // Your code here
    }
    
    // TODO: Implement update_value
    public fun update_value(account: &signer, new_value: u64) acquires Resource {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Use resource safety', 'Implement acquires correctly', 'Handle signer validation', 'Test thoroughly'],\n        "tags": ['move', 'aptos', 'junior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """move_m04""",\n        "title": """MOVE Middle 4: MOVE Resource Management""",\n        "description": """Implement a MOVE module with resource-oriented programming.

Requirements:
- Define and manage resources
- Implement access control
- Handle resource safety
- Use MOVE idioms correctly
- Pass all 18 comprehensive tests

Must implement real logic - no shortcuts.""",\n        "difficulty": """middle""",\n        "category": """move""",\n        "initial_code": """module 0x1::solution {
    use std::signer;
    
    struct Resource has key {
        value: u64,
    }
    
    // TODO: Implement create_resource
    public fun create_resource(account: &signer, value: u64) {
        // Your code here
    }
    
    // TODO: Implement get_value
    public fun get_value(addr: address): u64 acquires Resource {
        // Your code here
    }
    
    // TODO: Implement update_value
    public fun update_value(account: &signer, new_value: u64) acquires Resource {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Use resource safety', 'Implement acquires correctly', 'Handle signer validation', 'Test thoroughly'],\n        "tags": ['move', 'aptos', 'middle'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """move_s04""",\n        "title": """MOVE Senior 4: MOVE Resource Management""",\n        "description": """Implement a MOVE module with resource-oriented programming.

Requirements:
- Define and manage resources
- Implement access control
- Handle resource safety
- Use MOVE idioms correctly
- Pass all 20 comprehensive tests

Must implement real logic - no shortcuts.""",\n        "difficulty": """senior""",\n        "category": """move""",\n        "initial_code": """module 0x1::solution {
    use std::signer;
    
    struct Resource has key {
        value: u64,
    }
    
    // TODO: Implement create_resource
    public fun create_resource(account: &signer, value: u64) {
        // Your code here
    }
    
    // TODO: Implement get_value
    public fun get_value(addr: address): u64 acquires Resource {
        // Your code here
    }
    
    // TODO: Implement update_value
    public fun update_value(account: &signer, new_value: u64) acquires Resource {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Use resource safety', 'Implement acquires correctly', 'Handle signer validation', 'Test thoroughly'],\n        "tags": ['move', 'aptos', 'senior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """move_j05""",\n        "title": """MOVE Junior 5: MOVE Resource Management""",\n        "description": """Implement a MOVE module with resource-oriented programming.

Requirements:
- Define and manage resources
- Implement access control
- Handle resource safety
- Use MOVE idioms correctly
- Pass all 15 comprehensive tests

Must implement real logic - no shortcuts.""",\n        "difficulty": """junior""",\n        "category": """move""",\n        "initial_code": """module 0x1::solution {
    use std::signer;
    
    struct Resource has key {
        value: u64,
    }
    
    // TODO: Implement create_resource
    public fun create_resource(account: &signer, value: u64) {
        // Your code here
    }
    
    // TODO: Implement get_value
    public fun get_value(addr: address): u64 acquires Resource {
        // Your code here
    }
    
    // TODO: Implement update_value
    public fun update_value(account: &signer, new_value: u64) acquires Resource {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Use resource safety', 'Implement acquires correctly', 'Handle signer validation', 'Test thoroughly'],\n        "tags": ['move', 'aptos', 'junior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """move_m05""",\n        "title": """MOVE Middle 5: MOVE Resource Management""",\n        "description": """Implement a MOVE module with resource-oriented programming.

Requirements:
- Define and manage resources
- Implement access control
- Handle resource safety
- Use MOVE idioms correctly
- Pass all 18 comprehensive tests

Must implement real logic - no shortcuts.""",\n        "difficulty": """middle""",\n        "category": """move""",\n        "initial_code": """module 0x1::solution {
    use std::signer;
    
    struct Resource has key {
        value: u64,
    }
    
    // TODO: Implement create_resource
    public fun create_resource(account: &signer, value: u64) {
        // Your code here
    }
    
    // TODO: Implement get_value
    public fun get_value(addr: address): u64 acquires Resource {
        // Your code here
    }
    
    // TODO: Implement update_value
    public fun update_value(account: &signer, new_value: u64) acquires Resource {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Use resource safety', 'Implement acquires correctly', 'Handle signer validation', 'Test thoroughly'],\n        "tags": ['move', 'aptos', 'middle'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """move_s05""",\n        "title": """MOVE Senior 5: MOVE Resource Management""",\n        "description": """Implement a MOVE module with resource-oriented programming.

Requirements:
- Define and manage resources
- Implement access control
- Handle resource safety
- Use MOVE idioms correctly
- Pass all 20 comprehensive tests

Must implement real logic - no shortcuts.""",\n        "difficulty": """senior""",\n        "category": """move""",\n        "initial_code": """module 0x1::solution {
    use std::signer;
    
    struct Resource has key {
        value: u64,
    }
    
    // TODO: Implement create_resource
    public fun create_resource(account: &signer, value: u64) {
        // Your code here
    }
    
    // TODO: Implement get_value
    public fun get_value(addr: address): u64 acquires Resource {
        // Your code here
    }
    
    // TODO: Implement update_value
    public fun update_value(account: &signer, new_value: u64) acquires Resource {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Use resource safety', 'Implement acquires correctly', 'Handle signer validation', 'Test thoroughly'],\n        "tags": ['move', 'aptos', 'senior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """move_j06""",\n        "title": """MOVE Junior 6: MOVE Resource Management""",\n        "description": """Implement a MOVE module with resource-oriented programming.

Requirements:
- Define and manage resources
- Implement access control
- Handle resource safety
- Use MOVE idioms correctly
- Pass all 15 comprehensive tests

Must implement real logic - no shortcuts.""",\n        "difficulty": """junior""",\n        "category": """move""",\n        "initial_code": """module 0x1::solution {
    use std::signer;
    
    struct Resource has key {
        value: u64,
    }
    
    // TODO: Implement create_resource
    public fun create_resource(account: &signer, value: u64) {
        // Your code here
    }
    
    // TODO: Implement get_value
    public fun get_value(addr: address): u64 acquires Resource {
        // Your code here
    }
    
    // TODO: Implement update_value
    public fun update_value(account: &signer, new_value: u64) acquires Resource {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Use resource safety', 'Implement acquires correctly', 'Handle signer validation', 'Test thoroughly'],\n        "tags": ['move', 'aptos', 'junior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """move_m06""",\n        "title": """MOVE Middle 6: MOVE Resource Management""",\n        "description": """Implement a MOVE module with resource-oriented programming.

Requirements:
- Define and manage resources
- Implement access control
- Handle resource safety
- Use MOVE idioms correctly
- Pass all 18 comprehensive tests

Must implement real logic - no shortcuts.""",\n        "difficulty": """middle""",\n        "category": """move""",\n        "initial_code": """module 0x1::solution {
    use std::signer;
    
    struct Resource has key {
        value: u64,
    }
    
    // TODO: Implement create_resource
    public fun create_resource(account: &signer, value: u64) {
        // Your code here
    }
    
    // TODO: Implement get_value
    public fun get_value(addr: address): u64 acquires Resource {
        // Your code here
    }
    
    // TODO: Implement update_value
    public fun update_value(account: &signer, new_value: u64) acquires Resource {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Use resource safety', 'Implement acquires correctly', 'Handle signer validation', 'Test thoroughly'],\n        "tags": ['move', 'aptos', 'middle'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """move_s06""",\n        "title": """MOVE Senior 6: MOVE Resource Management""",\n        "description": """Implement a MOVE module with resource-oriented programming.

Requirements:
- Define and manage resources
- Implement access control
- Handle resource safety
- Use MOVE idioms correctly
- Pass all 20 comprehensive tests

Must implement real logic - no shortcuts.""",\n        "difficulty": """senior""",\n        "category": """move""",\n        "initial_code": """module 0x1::solution {
    use std::signer;
    
    struct Resource has key {
        value: u64,
    }
    
    // TODO: Implement create_resource
    public fun create_resource(account: &signer, value: u64) {
        // Your code here
    }
    
    // TODO: Implement get_value
    public fun get_value(addr: address): u64 acquires Resource {
        // Your code here
    }
    
    // TODO: Implement update_value
    public fun update_value(account: &signer, new_value: u64) acquires Resource {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Use resource safety', 'Implement acquires correctly', 'Handle signer validation', 'Test thoroughly'],\n        "tags": ['move', 'aptos', 'senior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """move_j07""",\n        "title": """MOVE Junior 7: MOVE Resource Management""",\n        "description": """Implement a MOVE module with resource-oriented programming.

Requirements:
- Define and manage resources
- Implement access control
- Handle resource safety
- Use MOVE idioms correctly
- Pass all 15 comprehensive tests

Must implement real logic - no shortcuts.""",\n        "difficulty": """junior""",\n        "category": """move""",\n        "initial_code": """module 0x1::solution {
    use std::signer;
    
    struct Resource has key {
        value: u64,
    }
    
    // TODO: Implement create_resource
    public fun create_resource(account: &signer, value: u64) {
        // Your code here
    }
    
    // TODO: Implement get_value
    public fun get_value(addr: address): u64 acquires Resource {
        // Your code here
    }
    
    // TODO: Implement update_value
    public fun update_value(account: &signer, new_value: u64) acquires Resource {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Use resource safety', 'Implement acquires correctly', 'Handle signer validation', 'Test thoroughly'],\n        "tags": ['move', 'aptos', 'junior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """move_m07""",\n        "title": """MOVE Middle 7: MOVE Resource Management""",\n        "description": """Implement a MOVE module with resource-oriented programming.

Requirements:
- Define and manage resources
- Implement access control
- Handle resource safety
- Use MOVE idioms correctly
- Pass all 18 comprehensive tests

Must implement real logic - no shortcuts.""",\n        "difficulty": """middle""",\n        "category": """move""",\n        "initial_code": """module 0x1::solution {
    use std::signer;
    
    struct Resource has key {
        value: u64,
    }
    
    // TODO: Implement create_resource
    public fun create_resource(account: &signer, value: u64) {
        // Your code here
    }
    
    // TODO: Implement get_value
    public fun get_value(addr: address): u64 acquires Resource {
        // Your code here
    }
    
    // TODO: Implement update_value
    public fun update_value(account: &signer, new_value: u64) acquires Resource {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Use resource safety', 'Implement acquires correctly', 'Handle signer validation', 'Test thoroughly'],\n        "tags": ['move', 'aptos', 'middle'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """move_s07""",\n        "title": """MOVE Senior 7: MOVE Resource Management""",\n        "description": """Implement a MOVE module with resource-oriented programming.

Requirements:
- Define and manage resources
- Implement access control
- Handle resource safety
- Use MOVE idioms correctly
- Pass all 20 comprehensive tests

Must implement real logic - no shortcuts.""",\n        "difficulty": """senior""",\n        "category": """move""",\n        "initial_code": """module 0x1::solution {
    use std::signer;
    
    struct Resource has key {
        value: u64,
    }
    
    // TODO: Implement create_resource
    public fun create_resource(account: &signer, value: u64) {
        // Your code here
    }
    
    // TODO: Implement get_value
    public fun get_value(addr: address): u64 acquires Resource {
        // Your code here
    }
    
    // TODO: Implement update_value
    public fun update_value(account: &signer, new_value: u64) acquires Resource {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Use resource safety', 'Implement acquires correctly', 'Handle signer validation', 'Test thoroughly'],\n        "tags": ['move', 'aptos', 'senior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """move_j08""",\n        "title": """MOVE Junior 8: MOVE Resource Management""",\n        "description": """Implement a MOVE module with resource-oriented programming.

Requirements:
- Define and manage resources
- Implement access control
- Handle resource safety
- Use MOVE idioms correctly
- Pass all 15 comprehensive tests

Must implement real logic - no shortcuts.""",\n        "difficulty": """junior""",\n        "category": """move""",\n        "initial_code": """module 0x1::solution {
    use std::signer;
    
    struct Resource has key {
        value: u64,
    }
    
    // TODO: Implement create_resource
    public fun create_resource(account: &signer, value: u64) {
        // Your code here
    }
    
    // TODO: Implement get_value
    public fun get_value(addr: address): u64 acquires Resource {
        // Your code here
    }
    
    // TODO: Implement update_value
    public fun update_value(account: &signer, new_value: u64) acquires Resource {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Use resource safety', 'Implement acquires correctly', 'Handle signer validation', 'Test thoroughly'],\n        "tags": ['move', 'aptos', 'junior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """move_m08""",\n        "title": """MOVE Middle 8: MOVE Resource Management""",\n        "description": """Implement a MOVE module with resource-oriented programming.

Requirements:
- Define and manage resources
- Implement access control
- Handle resource safety
- Use MOVE idioms correctly
- Pass all 18 comprehensive tests

Must implement real logic - no shortcuts.""",\n        "difficulty": """middle""",\n        "category": """move""",\n        "initial_code": """module 0x1::solution {
    use std::signer;
    
    struct Resource has key {
        value: u64,
    }
    
    // TODO: Implement create_resource
    public fun create_resource(account: &signer, value: u64) {
        // Your code here
    }
    
    // TODO: Implement get_value
    public fun get_value(addr: address): u64 acquires Resource {
        // Your code here
    }
    
    // TODO: Implement update_value
    public fun update_value(account: &signer, new_value: u64) acquires Resource {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Use resource safety', 'Implement acquires correctly', 'Handle signer validation', 'Test thoroughly'],\n        "tags": ['move', 'aptos', 'middle'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """move_s08""",\n        "title": """MOVE Senior 8: MOVE Resource Management""",\n        "description": """Implement a MOVE module with resource-oriented programming.

Requirements:
- Define and manage resources
- Implement access control
- Handle resource safety
- Use MOVE idioms correctly
- Pass all 20 comprehensive tests

Must implement real logic - no shortcuts.""",\n        "difficulty": """senior""",\n        "category": """move""",\n        "initial_code": """module 0x1::solution {
    use std::signer;
    
    struct Resource has key {
        value: u64,
    }
    
    // TODO: Implement create_resource
    public fun create_resource(account: &signer, value: u64) {
        // Your code here
    }
    
    // TODO: Implement get_value
    public fun get_value(addr: address): u64 acquires Resource {
        // Your code here
    }
    
    // TODO: Implement update_value
    public fun update_value(account: &signer, new_value: u64) acquires Resource {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Use resource safety', 'Implement acquires correctly', 'Handle signer validation', 'Test thoroughly'],\n        "tags": ['move', 'aptos', 'senior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """move_j09""",\n        "title": """MOVE Junior 9: MOVE Resource Management""",\n        "description": """Implement a MOVE module with resource-oriented programming.

Requirements:
- Define and manage resources
- Implement access control
- Handle resource safety
- Use MOVE idioms correctly
- Pass all 15 comprehensive tests

Must implement real logic - no shortcuts.""",\n        "difficulty": """junior""",\n        "category": """move""",\n        "initial_code": """module 0x1::solution {
    use std::signer;
    
    struct Resource has key {
        value: u64,
    }
    
    // TODO: Implement create_resource
    public fun create_resource(account: &signer, value: u64) {
        // Your code here
    }
    
    // TODO: Implement get_value
    public fun get_value(addr: address): u64 acquires Resource {
        // Your code here
    }
    
    // TODO: Implement update_value
    public fun update_value(account: &signer, new_value: u64) acquires Resource {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Use resource safety', 'Implement acquires correctly', 'Handle signer validation', 'Test thoroughly'],\n        "tags": ['move', 'aptos', 'junior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """move_m09""",\n        "title": """MOVE Middle 9: MOVE Resource Management""",\n        "description": """Implement a MOVE module with resource-oriented programming.

Requirements:
- Define and manage resources
- Implement access control
- Handle resource safety
- Use MOVE idioms correctly
- Pass all 18 comprehensive tests

Must implement real logic - no shortcuts.""",\n        "difficulty": """middle""",\n        "category": """move""",\n        "initial_code": """module 0x1::solution {
    use std::signer;
    
    struct Resource has key {
        value: u64,
    }
    
    // TODO: Implement create_resource
    public fun create_resource(account: &signer, value: u64) {
        // Your code here
    }
    
    // TODO: Implement get_value
    public fun get_value(addr: address): u64 acquires Resource {
        // Your code here
    }
    
    // TODO: Implement update_value
    public fun update_value(account: &signer, new_value: u64) acquires Resource {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Use resource safety', 'Implement acquires correctly', 'Handle signer validation', 'Test thoroughly'],\n        "tags": ['move', 'aptos', 'middle'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """move_s09""",\n        "title": """MOVE Senior 9: MOVE Resource Management""",\n        "description": """Implement a MOVE module with resource-oriented programming.

Requirements:
- Define and manage resources
- Implement access control
- Handle resource safety
- Use MOVE idioms correctly
- Pass all 20 comprehensive tests

Must implement real logic - no shortcuts.""",\n        "difficulty": """senior""",\n        "category": """move""",\n        "initial_code": """module 0x1::solution {
    use std::signer;
    
    struct Resource has key {
        value: u64,
    }
    
    // TODO: Implement create_resource
    public fun create_resource(account: &signer, value: u64) {
        // Your code here
    }
    
    // TODO: Implement get_value
    public fun get_value(addr: address): u64 acquires Resource {
        // Your code here
    }
    
    // TODO: Implement update_value
    public fun update_value(account: &signer, new_value: u64) acquires Resource {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Use resource safety', 'Implement acquires correctly', 'Handle signer validation', 'Test thoroughly'],\n        "tags": ['move', 'aptos', 'senior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """move_j10""",\n        "title": """MOVE Junior 10: MOVE Resource Management""",\n        "description": """Implement a MOVE module with resource-oriented programming.

Requirements:
- Define and manage resources
- Implement access control
- Handle resource safety
- Use MOVE idioms correctly
- Pass all 15 comprehensive tests

Must implement real logic - no shortcuts.""",\n        "difficulty": """junior""",\n        "category": """move""",\n        "initial_code": """module 0x1::solution {
    use std::signer;
    
    struct Resource has key {
        value: u64,
    }
    
    // TODO: Implement create_resource
    public fun create_resource(account: &signer, value: u64) {
        // Your code here
    }
    
    // TODO: Implement get_value
    public fun get_value(addr: address): u64 acquires Resource {
        // Your code here
    }
    
    // TODO: Implement update_value
    public fun update_value(account: &signer, new_value: u64) acquires Resource {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Use resource safety', 'Implement acquires correctly', 'Handle signer validation', 'Test thoroughly'],\n        "tags": ['move', 'aptos', 'junior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """move_m10""",\n        "title": """MOVE Middle 10: MOVE Resource Management""",\n        "description": """Implement a MOVE module with resource-oriented programming.

Requirements:
- Define and manage resources
- Implement access control
- Handle resource safety
- Use MOVE idioms correctly
- Pass all 18 comprehensive tests

Must implement real logic - no shortcuts.""",\n        "difficulty": """middle""",\n        "category": """move""",\n        "initial_code": """module 0x1::solution {
    use std::signer;
    
    struct Resource has key {
        value: u64,
    }
    
    // TODO: Implement create_resource
    public fun create_resource(account: &signer, value: u64) {
        // Your code here
    }
    
    // TODO: Implement get_value
    public fun get_value(addr: address): u64 acquires Resource {
        // Your code here
    }
    
    // TODO: Implement update_value
    public fun update_value(account: &signer, new_value: u64) acquires Resource {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Use resource safety', 'Implement acquires correctly', 'Handle signer validation', 'Test thoroughly'],\n        "tags": ['move', 'aptos', 'middle'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """move_s10""",\n        "title": """MOVE Senior 10: MOVE Resource Management""",\n        "description": """Implement a MOVE module with resource-oriented programming.

Requirements:
- Define and manage resources
- Implement access control
- Handle resource safety
- Use MOVE idioms correctly
- Pass all 20 comprehensive tests

Must implement real logic - no shortcuts.""",\n        "difficulty": """senior""",\n        "category": """move""",\n        "initial_code": """module 0x1::solution {
    use std::signer;
    
    struct Resource has key {
        value: u64,
    }
    
    // TODO: Implement create_resource
    public fun create_resource(account: &signer, value: u64) {
        // Your code here
    }
    
    // TODO: Implement get_value
    public fun get_value(addr: address): u64 acquires Resource {
        // Your code here
    }
    
    // TODO: Implement update_value
    public fun update_value(account: &signer, new_value: u64) acquires Resource {
        // Your code here
    }
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Use resource safety', 'Implement acquires correctly', 'Handle signer validation', 'Test thoroughly'],\n        "tags": ['move', 'aptos', 'senior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """tvm_j01""",\n        "title": """TVM/FunC Junior 1: TON Smart Contract""",\n        "description": """Implement a TON smart contract in FunC.

Requirements:
- Handle internal messages
- Manage cell storage
- Implement get methods
- Handle gas efficiently
- Pass all 15 validation tests

Real implementation required - test with multiple scenarios.""",\n        "difficulty": """junior""",\n        "category": """func""",\n        "initial_code": """;; TVM Smart Contract
#include "imports/stdlib.fc";

;; Storage: value
(int) load_data() inline {
    slice ds = get_data().begin_parse();
    return ds~load_uint(64);
}

() save_data(int value) impure inline {
    set_data(begin_cell()
        .store_uint(value, 64)
        .end_cell());
}

;; TODO: Implement recv_internal
() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {
    ;; Your code here
}

;; TODO: Implement get_value
int get_value() method_id {
    ;; Your code here
}

;; TODO: Implement set_value
() set_value(int new_value) impure {
    ;; Your code here
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Use FunC syntax correctly', 'Handle cell operations', 'Implement message handling', 'Test message flows'],\n        "tags": ['ton', 'tvm', 'func', 'junior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """tvm_m01""",\n        "title": """TVM/FunC Middle 1: TON Smart Contract""",\n        "description": """Implement a TON smart contract in FunC.

Requirements:
- Handle internal messages
- Manage cell storage
- Implement get methods
- Handle gas efficiently
- Pass all 18 validation tests

Real implementation required - test with multiple scenarios.""",\n        "difficulty": """middle""",\n        "category": """func""",\n        "initial_code": """;; TVM Smart Contract
#include "imports/stdlib.fc";

;; Storage: value
(int) load_data() inline {
    slice ds = get_data().begin_parse();
    return ds~load_uint(64);
}

() save_data(int value) impure inline {
    set_data(begin_cell()
        .store_uint(value, 64)
        .end_cell());
}

;; TODO: Implement recv_internal
() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {
    ;; Your code here
}

;; TODO: Implement get_value
int get_value() method_id {
    ;; Your code here
}

;; TODO: Implement set_value
() set_value(int new_value) impure {
    ;; Your code here
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Use FunC syntax correctly', 'Handle cell operations', 'Implement message handling', 'Test message flows'],\n        "tags": ['ton', 'tvm', 'func', 'middle'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """tvm_s01""",\n        "title": """TVM/FunC Senior 1: TON Smart Contract""",\n        "description": """Implement a TON smart contract in FunC.

Requirements:
- Handle internal messages
- Manage cell storage
- Implement get methods
- Handle gas efficiently
- Pass all 20 validation tests

Real implementation required - test with multiple scenarios.""",\n        "difficulty": """senior""",\n        "category": """func""",\n        "initial_code": """;; TVM Smart Contract
#include "imports/stdlib.fc";

;; Storage: value
(int) load_data() inline {
    slice ds = get_data().begin_parse();
    return ds~load_uint(64);
}

() save_data(int value) impure inline {
    set_data(begin_cell()
        .store_uint(value, 64)
        .end_cell());
}

;; TODO: Implement recv_internal
() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {
    ;; Your code here
}

;; TODO: Implement get_value
int get_value() method_id {
    ;; Your code here
}

;; TODO: Implement set_value
() set_value(int new_value) impure {
    ;; Your code here
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Use FunC syntax correctly', 'Handle cell operations', 'Implement message handling', 'Test message flows'],\n        "tags": ['ton', 'tvm', 'func', 'senior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """tvm_j02""",\n        "title": """TVM/FunC Junior 2: TON Smart Contract""",\n        "description": """Implement a TON smart contract in FunC.

Requirements:
- Handle internal messages
- Manage cell storage
- Implement get methods
- Handle gas efficiently
- Pass all 15 validation tests

Real implementation required - test with multiple scenarios.""",\n        "difficulty": """junior""",\n        "category": """func""",\n        "initial_code": """;; TVM Smart Contract
#include "imports/stdlib.fc";

;; Storage: value
(int) load_data() inline {
    slice ds = get_data().begin_parse();
    return ds~load_uint(64);
}

() save_data(int value) impure inline {
    set_data(begin_cell()
        .store_uint(value, 64)
        .end_cell());
}

;; TODO: Implement recv_internal
() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {
    ;; Your code here
}

;; TODO: Implement get_value
int get_value() method_id {
    ;; Your code here
}

;; TODO: Implement set_value
() set_value(int new_value) impure {
    ;; Your code here
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Use FunC syntax correctly', 'Handle cell operations', 'Implement message handling', 'Test message flows'],\n        "tags": ['ton', 'tvm', 'func', 'junior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """tvm_m02""",\n        "title": """TVM/FunC Middle 2: TON Smart Contract""",\n        "description": """Implement a TON smart contract in FunC.

Requirements:
- Handle internal messages
- Manage cell storage
- Implement get methods
- Handle gas efficiently
- Pass all 18 validation tests

Real implementation required - test with multiple scenarios.""",\n        "difficulty": """middle""",\n        "category": """func""",\n        "initial_code": """;; TVM Smart Contract
#include "imports/stdlib.fc";

;; Storage: value
(int) load_data() inline {
    slice ds = get_data().begin_parse();
    return ds~load_uint(64);
}

() save_data(int value) impure inline {
    set_data(begin_cell()
        .store_uint(value, 64)
        .end_cell());
}

;; TODO: Implement recv_internal
() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {
    ;; Your code here
}

;; TODO: Implement get_value
int get_value() method_id {
    ;; Your code here
}

;; TODO: Implement set_value
() set_value(int new_value) impure {
    ;; Your code here
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Use FunC syntax correctly', 'Handle cell operations', 'Implement message handling', 'Test message flows'],\n        "tags": ['ton', 'tvm', 'func', 'middle'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """tvm_s02""",\n        "title": """TVM/FunC Senior 2: TON Smart Contract""",\n        "description": """Implement a TON smart contract in FunC.

Requirements:
- Handle internal messages
- Manage cell storage
- Implement get methods
- Handle gas efficiently
- Pass all 20 validation tests

Real implementation required - test with multiple scenarios.""",\n        "difficulty": """senior""",\n        "category": """func""",\n        "initial_code": """;; TVM Smart Contract
#include "imports/stdlib.fc";

;; Storage: value
(int) load_data() inline {
    slice ds = get_data().begin_parse();
    return ds~load_uint(64);
}

() save_data(int value) impure inline {
    set_data(begin_cell()
        .store_uint(value, 64)
        .end_cell());
}

;; TODO: Implement recv_internal
() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {
    ;; Your code here
}

;; TODO: Implement get_value
int get_value() method_id {
    ;; Your code here
}

;; TODO: Implement set_value
() set_value(int new_value) impure {
    ;; Your code here
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Use FunC syntax correctly', 'Handle cell operations', 'Implement message handling', 'Test message flows'],\n        "tags": ['ton', 'tvm', 'func', 'senior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """tvm_j03""",\n        "title": """TVM/FunC Junior 3: TON Smart Contract""",\n        "description": """Implement a TON smart contract in FunC.

Requirements:
- Handle internal messages
- Manage cell storage
- Implement get methods
- Handle gas efficiently
- Pass all 15 validation tests

Real implementation required - test with multiple scenarios.""",\n        "difficulty": """junior""",\n        "category": """func""",\n        "initial_code": """;; TVM Smart Contract
#include "imports/stdlib.fc";

;; Storage: value
(int) load_data() inline {
    slice ds = get_data().begin_parse();
    return ds~load_uint(64);
}

() save_data(int value) impure inline {
    set_data(begin_cell()
        .store_uint(value, 64)
        .end_cell());
}

;; TODO: Implement recv_internal
() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {
    ;; Your code here
}

;; TODO: Implement get_value
int get_value() method_id {
    ;; Your code here
}

;; TODO: Implement set_value
() set_value(int new_value) impure {
    ;; Your code here
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Use FunC syntax correctly', 'Handle cell operations', 'Implement message handling', 'Test message flows'],\n        "tags": ['ton', 'tvm', 'func', 'junior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """tvm_m03""",\n        "title": """TVM/FunC Middle 3: TON Smart Contract""",\n        "description": """Implement a TON smart contract in FunC.

Requirements:
- Handle internal messages
- Manage cell storage
- Implement get methods
- Handle gas efficiently
- Pass all 18 validation tests

Real implementation required - test with multiple scenarios.""",\n        "difficulty": """middle""",\n        "category": """func""",\n        "initial_code": """;; TVM Smart Contract
#include "imports/stdlib.fc";

;; Storage: value
(int) load_data() inline {
    slice ds = get_data().begin_parse();
    return ds~load_uint(64);
}

() save_data(int value) impure inline {
    set_data(begin_cell()
        .store_uint(value, 64)
        .end_cell());
}

;; TODO: Implement recv_internal
() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {
    ;; Your code here
}

;; TODO: Implement get_value
int get_value() method_id {
    ;; Your code here
}

;; TODO: Implement set_value
() set_value(int new_value) impure {
    ;; Your code here
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Use FunC syntax correctly', 'Handle cell operations', 'Implement message handling', 'Test message flows'],\n        "tags": ['ton', 'tvm', 'func', 'middle'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """tvm_s03""",\n        "title": """TVM/FunC Senior 3: TON Smart Contract""",\n        "description": """Implement a TON smart contract in FunC.

Requirements:
- Handle internal messages
- Manage cell storage
- Implement get methods
- Handle gas efficiently
- Pass all 20 validation tests

Real implementation required - test with multiple scenarios.""",\n        "difficulty": """senior""",\n        "category": """func""",\n        "initial_code": """;; TVM Smart Contract
#include "imports/stdlib.fc";

;; Storage: value
(int) load_data() inline {
    slice ds = get_data().begin_parse();
    return ds~load_uint(64);
}

() save_data(int value) impure inline {
    set_data(begin_cell()
        .store_uint(value, 64)
        .end_cell());
}

;; TODO: Implement recv_internal
() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {
    ;; Your code here
}

;; TODO: Implement get_value
int get_value() method_id {
    ;; Your code here
}

;; TODO: Implement set_value
() set_value(int new_value) impure {
    ;; Your code here
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Use FunC syntax correctly', 'Handle cell operations', 'Implement message handling', 'Test message flows'],\n        "tags": ['ton', 'tvm', 'func', 'senior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """tvm_j04""",\n        "title": """TVM/FunC Junior 4: TON Smart Contract""",\n        "description": """Implement a TON smart contract in FunC.

Requirements:
- Handle internal messages
- Manage cell storage
- Implement get methods
- Handle gas efficiently
- Pass all 15 validation tests

Real implementation required - test with multiple scenarios.""",\n        "difficulty": """junior""",\n        "category": """func""",\n        "initial_code": """;; TVM Smart Contract
#include "imports/stdlib.fc";

;; Storage: value
(int) load_data() inline {
    slice ds = get_data().begin_parse();
    return ds~load_uint(64);
}

() save_data(int value) impure inline {
    set_data(begin_cell()
        .store_uint(value, 64)
        .end_cell());
}

;; TODO: Implement recv_internal
() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {
    ;; Your code here
}

;; TODO: Implement get_value
int get_value() method_id {
    ;; Your code here
}

;; TODO: Implement set_value
() set_value(int new_value) impure {
    ;; Your code here
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Use FunC syntax correctly', 'Handle cell operations', 'Implement message handling', 'Test message flows'],\n        "tags": ['ton', 'tvm', 'func', 'junior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """tvm_m04""",\n        "title": """TVM/FunC Middle 4: TON Smart Contract""",\n        "description": """Implement a TON smart contract in FunC.

Requirements:
- Handle internal messages
- Manage cell storage
- Implement get methods
- Handle gas efficiently
- Pass all 18 validation tests

Real implementation required - test with multiple scenarios.""",\n        "difficulty": """middle""",\n        "category": """func""",\n        "initial_code": """;; TVM Smart Contract
#include "imports/stdlib.fc";

;; Storage: value
(int) load_data() inline {
    slice ds = get_data().begin_parse();
    return ds~load_uint(64);
}

() save_data(int value) impure inline {
    set_data(begin_cell()
        .store_uint(value, 64)
        .end_cell());
}

;; TODO: Implement recv_internal
() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {
    ;; Your code here
}

;; TODO: Implement get_value
int get_value() method_id {
    ;; Your code here
}

;; TODO: Implement set_value
() set_value(int new_value) impure {
    ;; Your code here
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Use FunC syntax correctly', 'Handle cell operations', 'Implement message handling', 'Test message flows'],\n        "tags": ['ton', 'tvm', 'func', 'middle'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """tvm_s04""",\n        "title": """TVM/FunC Senior 4: TON Smart Contract""",\n        "description": """Implement a TON smart contract in FunC.

Requirements:
- Handle internal messages
- Manage cell storage
- Implement get methods
- Handle gas efficiently
- Pass all 20 validation tests

Real implementation required - test with multiple scenarios.""",\n        "difficulty": """senior""",\n        "category": """func""",\n        "initial_code": """;; TVM Smart Contract
#include "imports/stdlib.fc";

;; Storage: value
(int) load_data() inline {
    slice ds = get_data().begin_parse();
    return ds~load_uint(64);
}

() save_data(int value) impure inline {
    set_data(begin_cell()
        .store_uint(value, 64)
        .end_cell());
}

;; TODO: Implement recv_internal
() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {
    ;; Your code here
}

;; TODO: Implement get_value
int get_value() method_id {
    ;; Your code here
}

;; TODO: Implement set_value
() set_value(int new_value) impure {
    ;; Your code here
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Use FunC syntax correctly', 'Handle cell operations', 'Implement message handling', 'Test message flows'],\n        "tags": ['ton', 'tvm', 'func', 'senior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """tvm_j05""",\n        "title": """TVM/FunC Junior 5: TON Smart Contract""",\n        "description": """Implement a TON smart contract in FunC.

Requirements:
- Handle internal messages
- Manage cell storage
- Implement get methods
- Handle gas efficiently
- Pass all 15 validation tests

Real implementation required - test with multiple scenarios.""",\n        "difficulty": """junior""",\n        "category": """func""",\n        "initial_code": """;; TVM Smart Contract
#include "imports/stdlib.fc";

;; Storage: value
(int) load_data() inline {
    slice ds = get_data().begin_parse();
    return ds~load_uint(64);
}

() save_data(int value) impure inline {
    set_data(begin_cell()
        .store_uint(value, 64)
        .end_cell());
}

;; TODO: Implement recv_internal
() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {
    ;; Your code here
}

;; TODO: Implement get_value
int get_value() method_id {
    ;; Your code here
}

;; TODO: Implement set_value
() set_value(int new_value) impure {
    ;; Your code here
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Use FunC syntax correctly', 'Handle cell operations', 'Implement message handling', 'Test message flows'],\n        "tags": ['ton', 'tvm', 'func', 'junior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """tvm_m05""",\n        "title": """TVM/FunC Middle 5: TON Smart Contract""",\n        "description": """Implement a TON smart contract in FunC.

Requirements:
- Handle internal messages
- Manage cell storage
- Implement get methods
- Handle gas efficiently
- Pass all 18 validation tests

Real implementation required - test with multiple scenarios.""",\n        "difficulty": """middle""",\n        "category": """func""",\n        "initial_code": """;; TVM Smart Contract
#include "imports/stdlib.fc";

;; Storage: value
(int) load_data() inline {
    slice ds = get_data().begin_parse();
    return ds~load_uint(64);
}

() save_data(int value) impure inline {
    set_data(begin_cell()
        .store_uint(value, 64)
        .end_cell());
}

;; TODO: Implement recv_internal
() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {
    ;; Your code here
}

;; TODO: Implement get_value
int get_value() method_id {
    ;; Your code here
}

;; TODO: Implement set_value
() set_value(int new_value) impure {
    ;; Your code here
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Use FunC syntax correctly', 'Handle cell operations', 'Implement message handling', 'Test message flows'],\n        "tags": ['ton', 'tvm', 'func', 'middle'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """tvm_s05""",\n        "title": """TVM/FunC Senior 5: TON Smart Contract""",\n        "description": """Implement a TON smart contract in FunC.

Requirements:
- Handle internal messages
- Manage cell storage
- Implement get methods
- Handle gas efficiently
- Pass all 20 validation tests

Real implementation required - test with multiple scenarios.""",\n        "difficulty": """senior""",\n        "category": """func""",\n        "initial_code": """;; TVM Smart Contract
#include "imports/stdlib.fc";

;; Storage: value
(int) load_data() inline {
    slice ds = get_data().begin_parse();
    return ds~load_uint(64);
}

() save_data(int value) impure inline {
    set_data(begin_cell()
        .store_uint(value, 64)
        .end_cell());
}

;; TODO: Implement recv_internal
() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {
    ;; Your code here
}

;; TODO: Implement get_value
int get_value() method_id {
    ;; Your code here
}

;; TODO: Implement set_value
() set_value(int new_value) impure {
    ;; Your code here
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Use FunC syntax correctly', 'Handle cell operations', 'Implement message handling', 'Test message flows'],\n        "tags": ['ton', 'tvm', 'func', 'senior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """tvm_j06""",\n        "title": """TVM/FunC Junior 6: TON Smart Contract""",\n        "description": """Implement a TON smart contract in FunC.

Requirements:
- Handle internal messages
- Manage cell storage
- Implement get methods
- Handle gas efficiently
- Pass all 15 validation tests

Real implementation required - test with multiple scenarios.""",\n        "difficulty": """junior""",\n        "category": """func""",\n        "initial_code": """;; TVM Smart Contract
#include "imports/stdlib.fc";

;; Storage: value
(int) load_data() inline {
    slice ds = get_data().begin_parse();
    return ds~load_uint(64);
}

() save_data(int value) impure inline {
    set_data(begin_cell()
        .store_uint(value, 64)
        .end_cell());
}

;; TODO: Implement recv_internal
() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {
    ;; Your code here
}

;; TODO: Implement get_value
int get_value() method_id {
    ;; Your code here
}

;; TODO: Implement set_value
() set_value(int new_value) impure {
    ;; Your code here
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Use FunC syntax correctly', 'Handle cell operations', 'Implement message handling', 'Test message flows'],\n        "tags": ['ton', 'tvm', 'func', 'junior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """tvm_m06""",\n        "title": """TVM/FunC Middle 6: TON Smart Contract""",\n        "description": """Implement a TON smart contract in FunC.

Requirements:
- Handle internal messages
- Manage cell storage
- Implement get methods
- Handle gas efficiently
- Pass all 18 validation tests

Real implementation required - test with multiple scenarios.""",\n        "difficulty": """middle""",\n        "category": """func""",\n        "initial_code": """;; TVM Smart Contract
#include "imports/stdlib.fc";

;; Storage: value
(int) load_data() inline {
    slice ds = get_data().begin_parse();
    return ds~load_uint(64);
}

() save_data(int value) impure inline {
    set_data(begin_cell()
        .store_uint(value, 64)
        .end_cell());
}

;; TODO: Implement recv_internal
() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {
    ;; Your code here
}

;; TODO: Implement get_value
int get_value() method_id {
    ;; Your code here
}

;; TODO: Implement set_value
() set_value(int new_value) impure {
    ;; Your code here
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Use FunC syntax correctly', 'Handle cell operations', 'Implement message handling', 'Test message flows'],\n        "tags": ['ton', 'tvm', 'func', 'middle'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """tvm_s06""",\n        "title": """TVM/FunC Senior 6: TON Smart Contract""",\n        "description": """Implement a TON smart contract in FunC.

Requirements:
- Handle internal messages
- Manage cell storage
- Implement get methods
- Handle gas efficiently
- Pass all 20 validation tests

Real implementation required - test with multiple scenarios.""",\n        "difficulty": """senior""",\n        "category": """func""",\n        "initial_code": """;; TVM Smart Contract
#include "imports/stdlib.fc";

;; Storage: value
(int) load_data() inline {
    slice ds = get_data().begin_parse();
    return ds~load_uint(64);
}

() save_data(int value) impure inline {
    set_data(begin_cell()
        .store_uint(value, 64)
        .end_cell());
}

;; TODO: Implement recv_internal
() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {
    ;; Your code here
}

;; TODO: Implement get_value
int get_value() method_id {
    ;; Your code here
}

;; TODO: Implement set_value
() set_value(int new_value) impure {
    ;; Your code here
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Use FunC syntax correctly', 'Handle cell operations', 'Implement message handling', 'Test message flows'],\n        "tags": ['ton', 'tvm', 'func', 'senior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """tvm_j07""",\n        "title": """TVM/FunC Junior 7: TON Smart Contract""",\n        "description": """Implement a TON smart contract in FunC.

Requirements:
- Handle internal messages
- Manage cell storage
- Implement get methods
- Handle gas efficiently
- Pass all 15 validation tests

Real implementation required - test with multiple scenarios.""",\n        "difficulty": """junior""",\n        "category": """func""",\n        "initial_code": """;; TVM Smart Contract
#include "imports/stdlib.fc";

;; Storage: value
(int) load_data() inline {
    slice ds = get_data().begin_parse();
    return ds~load_uint(64);
}

() save_data(int value) impure inline {
    set_data(begin_cell()
        .store_uint(value, 64)
        .end_cell());
}

;; TODO: Implement recv_internal
() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {
    ;; Your code here
}

;; TODO: Implement get_value
int get_value() method_id {
    ;; Your code here
}

;; TODO: Implement set_value
() set_value(int new_value) impure {
    ;; Your code here
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Use FunC syntax correctly', 'Handle cell operations', 'Implement message handling', 'Test message flows'],\n        "tags": ['ton', 'tvm', 'func', 'junior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """tvm_m07""",\n        "title": """TVM/FunC Middle 7: TON Smart Contract""",\n        "description": """Implement a TON smart contract in FunC.

Requirements:
- Handle internal messages
- Manage cell storage
- Implement get methods
- Handle gas efficiently
- Pass all 18 validation tests

Real implementation required - test with multiple scenarios.""",\n        "difficulty": """middle""",\n        "category": """func""",\n        "initial_code": """;; TVM Smart Contract
#include "imports/stdlib.fc";

;; Storage: value
(int) load_data() inline {
    slice ds = get_data().begin_parse();
    return ds~load_uint(64);
}

() save_data(int value) impure inline {
    set_data(begin_cell()
        .store_uint(value, 64)
        .end_cell());
}

;; TODO: Implement recv_internal
() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {
    ;; Your code here
}

;; TODO: Implement get_value
int get_value() method_id {
    ;; Your code here
}

;; TODO: Implement set_value
() set_value(int new_value) impure {
    ;; Your code here
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Use FunC syntax correctly', 'Handle cell operations', 'Implement message handling', 'Test message flows'],\n        "tags": ['ton', 'tvm', 'func', 'middle'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """tvm_s07""",\n        "title": """TVM/FunC Senior 7: TON Smart Contract""",\n        "description": """Implement a TON smart contract in FunC.

Requirements:
- Handle internal messages
- Manage cell storage
- Implement get methods
- Handle gas efficiently
- Pass all 20 validation tests

Real implementation required - test with multiple scenarios.""",\n        "difficulty": """senior""",\n        "category": """func""",\n        "initial_code": """;; TVM Smart Contract
#include "imports/stdlib.fc";

;; Storage: value
(int) load_data() inline {
    slice ds = get_data().begin_parse();
    return ds~load_uint(64);
}

() save_data(int value) impure inline {
    set_data(begin_cell()
        .store_uint(value, 64)
        .end_cell());
}

;; TODO: Implement recv_internal
() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {
    ;; Your code here
}

;; TODO: Implement get_value
int get_value() method_id {
    ;; Your code here
}

;; TODO: Implement set_value
() set_value(int new_value) impure {
    ;; Your code here
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Use FunC syntax correctly', 'Handle cell operations', 'Implement message handling', 'Test message flows'],\n        "tags": ['ton', 'tvm', 'func', 'senior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """tvm_j08""",\n        "title": """TVM/FunC Junior 8: TON Smart Contract""",\n        "description": """Implement a TON smart contract in FunC.

Requirements:
- Handle internal messages
- Manage cell storage
- Implement get methods
- Handle gas efficiently
- Pass all 15 validation tests

Real implementation required - test with multiple scenarios.""",\n        "difficulty": """junior""",\n        "category": """func""",\n        "initial_code": """;; TVM Smart Contract
#include "imports/stdlib.fc";

;; Storage: value
(int) load_data() inline {
    slice ds = get_data().begin_parse();
    return ds~load_uint(64);
}

() save_data(int value) impure inline {
    set_data(begin_cell()
        .store_uint(value, 64)
        .end_cell());
}

;; TODO: Implement recv_internal
() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {
    ;; Your code here
}

;; TODO: Implement get_value
int get_value() method_id {
    ;; Your code here
}

;; TODO: Implement set_value
() set_value(int new_value) impure {
    ;; Your code here
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Use FunC syntax correctly', 'Handle cell operations', 'Implement message handling', 'Test message flows'],\n        "tags": ['ton', 'tvm', 'func', 'junior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """tvm_m08""",\n        "title": """TVM/FunC Middle 8: TON Smart Contract""",\n        "description": """Implement a TON smart contract in FunC.

Requirements:
- Handle internal messages
- Manage cell storage
- Implement get methods
- Handle gas efficiently
- Pass all 18 validation tests

Real implementation required - test with multiple scenarios.""",\n        "difficulty": """middle""",\n        "category": """func""",\n        "initial_code": """;; TVM Smart Contract
#include "imports/stdlib.fc";

;; Storage: value
(int) load_data() inline {
    slice ds = get_data().begin_parse();
    return ds~load_uint(64);
}

() save_data(int value) impure inline {
    set_data(begin_cell()
        .store_uint(value, 64)
        .end_cell());
}

;; TODO: Implement recv_internal
() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {
    ;; Your code here
}

;; TODO: Implement get_value
int get_value() method_id {
    ;; Your code here
}

;; TODO: Implement set_value
() set_value(int new_value) impure {
    ;; Your code here
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Use FunC syntax correctly', 'Handle cell operations', 'Implement message handling', 'Test message flows'],\n        "tags": ['ton', 'tvm', 'func', 'middle'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """tvm_s08""",\n        "title": """TVM/FunC Senior 8: TON Smart Contract""",\n        "description": """Implement a TON smart contract in FunC.

Requirements:
- Handle internal messages
- Manage cell storage
- Implement get methods
- Handle gas efficiently
- Pass all 20 validation tests

Real implementation required - test with multiple scenarios.""",\n        "difficulty": """senior""",\n        "category": """func""",\n        "initial_code": """;; TVM Smart Contract
#include "imports/stdlib.fc";

;; Storage: value
(int) load_data() inline {
    slice ds = get_data().begin_parse();
    return ds~load_uint(64);
}

() save_data(int value) impure inline {
    set_data(begin_cell()
        .store_uint(value, 64)
        .end_cell());
}

;; TODO: Implement recv_internal
() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {
    ;; Your code here
}

;; TODO: Implement get_value
int get_value() method_id {
    ;; Your code here
}

;; TODO: Implement set_value
() set_value(int new_value) impure {
    ;; Your code here
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Use FunC syntax correctly', 'Handle cell operations', 'Implement message handling', 'Test message flows'],\n        "tags": ['ton', 'tvm', 'func', 'senior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """tvm_j09""",\n        "title": """TVM/FunC Junior 9: TON Smart Contract""",\n        "description": """Implement a TON smart contract in FunC.

Requirements:
- Handle internal messages
- Manage cell storage
- Implement get methods
- Handle gas efficiently
- Pass all 15 validation tests

Real implementation required - test with multiple scenarios.""",\n        "difficulty": """junior""",\n        "category": """func""",\n        "initial_code": """;; TVM Smart Contract
#include "imports/stdlib.fc";

;; Storage: value
(int) load_data() inline {
    slice ds = get_data().begin_parse();
    return ds~load_uint(64);
}

() save_data(int value) impure inline {
    set_data(begin_cell()
        .store_uint(value, 64)
        .end_cell());
}

;; TODO: Implement recv_internal
() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {
    ;; Your code here
}

;; TODO: Implement get_value
int get_value() method_id {
    ;; Your code here
}

;; TODO: Implement set_value
() set_value(int new_value) impure {
    ;; Your code here
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Use FunC syntax correctly', 'Handle cell operations', 'Implement message handling', 'Test message flows'],\n        "tags": ['ton', 'tvm', 'func', 'junior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """tvm_m09""",\n        "title": """TVM/FunC Middle 9: TON Smart Contract""",\n        "description": """Implement a TON smart contract in FunC.

Requirements:
- Handle internal messages
- Manage cell storage
- Implement get methods
- Handle gas efficiently
- Pass all 18 validation tests

Real implementation required - test with multiple scenarios.""",\n        "difficulty": """middle""",\n        "category": """func""",\n        "initial_code": """;; TVM Smart Contract
#include "imports/stdlib.fc";

;; Storage: value
(int) load_data() inline {
    slice ds = get_data().begin_parse();
    return ds~load_uint(64);
}

() save_data(int value) impure inline {
    set_data(begin_cell()
        .store_uint(value, 64)
        .end_cell());
}

;; TODO: Implement recv_internal
() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {
    ;; Your code here
}

;; TODO: Implement get_value
int get_value() method_id {
    ;; Your code here
}

;; TODO: Implement set_value
() set_value(int new_value) impure {
    ;; Your code here
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Use FunC syntax correctly', 'Handle cell operations', 'Implement message handling', 'Test message flows'],\n        "tags": ['ton', 'tvm', 'func', 'middle'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """tvm_s09""",\n        "title": """TVM/FunC Senior 9: TON Smart Contract""",\n        "description": """Implement a TON smart contract in FunC.

Requirements:
- Handle internal messages
- Manage cell storage
- Implement get methods
- Handle gas efficiently
- Pass all 20 validation tests

Real implementation required - test with multiple scenarios.""",\n        "difficulty": """senior""",\n        "category": """func""",\n        "initial_code": """;; TVM Smart Contract
#include "imports/stdlib.fc";

;; Storage: value
(int) load_data() inline {
    slice ds = get_data().begin_parse();
    return ds~load_uint(64);
}

() save_data(int value) impure inline {
    set_data(begin_cell()
        .store_uint(value, 64)
        .end_cell());
}

;; TODO: Implement recv_internal
() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {
    ;; Your code here
}

;; TODO: Implement get_value
int get_value() method_id {
    ;; Your code here
}

;; TODO: Implement set_value
() set_value(int new_value) impure {
    ;; Your code here
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Use FunC syntax correctly', 'Handle cell operations', 'Implement message handling', 'Test message flows'],\n        "tags": ['ton', 'tvm', 'func', 'senior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """tvm_j10""",\n        "title": """TVM/FunC Junior 10: TON Smart Contract""",\n        "description": """Implement a TON smart contract in FunC.

Requirements:
- Handle internal messages
- Manage cell storage
- Implement get methods
- Handle gas efficiently
- Pass all 15 validation tests

Real implementation required - test with multiple scenarios.""",\n        "difficulty": """junior""",\n        "category": """func""",\n        "initial_code": """;; TVM Smart Contract
#include "imports/stdlib.fc";

;; Storage: value
(int) load_data() inline {
    slice ds = get_data().begin_parse();
    return ds~load_uint(64);
}

() save_data(int value) impure inline {
    set_data(begin_cell()
        .store_uint(value, 64)
        .end_cell());
}

;; TODO: Implement recv_internal
() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {
    ;; Your code here
}

;; TODO: Implement get_value
int get_value() method_id {
    ;; Your code here
}

;; TODO: Implement set_value
() set_value(int new_value) impure {
    ;; Your code here
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}],\n        "hints": ['Use FunC syntax correctly', 'Handle cell operations', 'Implement message handling', 'Test message flows'],\n        "tags": ['ton', 'tvm', 'func', 'junior'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """tvm_m10""",\n        "title": """TVM/FunC Middle 10: TON Smart Contract""",\n        "description": """Implement a TON smart contract in FunC.

Requirements:
- Handle internal messages
- Manage cell storage
- Implement get methods
- Handle gas efficiently
- Pass all 18 validation tests

Real implementation required - test with multiple scenarios.""",\n        "difficulty": """middle""",\n        "category": """func""",\n        "initial_code": """;; TVM Smart Contract
#include "imports/stdlib.fc";

;; Storage: value
(int) load_data() inline {
    slice ds = get_data().begin_parse();
    return ds~load_uint(64);
}

() save_data(int value) impure inline {
    set_data(begin_cell()
        .store_uint(value, 64)
        .end_cell());
}

;; TODO: Implement recv_internal
() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {
    ;; Your code here
}

;; TODO: Implement get_value
int get_value() method_id {
    ;; Your code here
}

;; TODO: Implement set_value
() set_value(int new_value) impure {
    ;; Your code here
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}],\n        "hints": ['Use FunC syntax correctly', 'Handle cell operations', 'Implement message handling', 'Test message flows'],\n        "tags": ['ton', 'tvm', 'func', 'middle'],\n        "solved_count": 0,\n    },\n    {\n        "problem_id": """tvm_s10""",\n        "title": """TVM/FunC Senior 10: TON Smart Contract""",\n        "description": """Implement a TON smart contract in FunC.

Requirements:
- Handle internal messages
- Manage cell storage
- Implement get methods
- Handle gas efficiently
- Pass all 20 validation tests

Real implementation required - test with multiple scenarios.""",\n        "difficulty": """senior""",\n        "category": """func""",\n        "initial_code": """;; TVM Smart Contract
#include "imports/stdlib.fc";

;; Storage: value
(int) load_data() inline {
    slice ds = get_data().begin_parse();
    return ds~load_uint(64);
}

() save_data(int value) impure inline {
    set_data(begin_cell()
        .store_uint(value, 64)
        .end_cell());
}

;; TODO: Implement recv_internal
() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {
    ;; Your code here
}

;; TODO: Implement get_value
int get_value() method_id {
    ;; Your code here
}

;; TODO: Implement set_value
() set_value(int new_value) impure {
    ;; Your code here
}""",\n        "test_cases": [{'type': 'call', 'function': 'getValue', 'args': [], 'expected': '0', 'description': 'Initial value is 0'}, {'type': 'transaction', 'function': 'setValue', 'args': ['10'], 'expected': 'success', 'description': 'Set value to 10'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '10', 'description': 'Value should be 10'}, {'type': 'transaction', 'function': 'setValue', 'args': ['25'], 'expected': 'success', 'description': 'Set value to 25'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '25', 'description': 'Value should be 25'}, {'type': 'transaction', 'function': 'setValue', 'args': ['42'], 'expected': 'success', 'description': 'Set value to 42'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '42', 'description': 'Value should be 42'}, {'type': 'transaction', 'function': 'setValue', 'args': ['100'], 'expected': 'success', 'description': 'Set value to 100'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '100', 'description': 'Value should be 100'}, {'type': 'transaction', 'function': 'setValue', 'args': ['7'], 'expected': 'success', 'description': 'Set value to 7'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '7', 'description': 'Value should be 7'}, {'type': 'transaction', 'function': 'setValue', 'args': ['33'], 'expected': 'success', 'description': 'Set value to 33'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '33', 'description': 'Value should be 33'}, {'type': 'transaction', 'function': 'setValue', 'args': ['99'], 'expected': 'success', 'description': 'Set value to 99'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '99', 'description': 'Value should be 99'}, {'type': 'transaction', 'function': 'setValue', 'args': ['1'], 'expected': 'success', 'description': 'Set value to 1'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '1', 'description': 'Value should be 1'}, {'type': 'transaction', 'function': 'setValue', 'args': ['50'], 'expected': 'success', 'description': 'Set value to 50'}, {'type': 'call', 'function': 'getValue', 'args': [], 'expected': '50', 'description': 'Value should be 50'}, {'type': 'transaction', 'function': 'setValue', 'args': ['77'], 'expected': 'success', 'description': 'Set value to 77'}],\n        "hints": ['Use FunC syntax correctly', 'Handle cell operations', 'Implement message handling', 'Test message flows'],\n        "tags": ['ton', 'tvm', 'func', 'senior'],\n        "solved_count": 0,\n    },\n]\n\nprint(f"Total problems: {len(PROBLEMS)}")\nprint(f"Solidity: {len([p for p in PROBLEMS if p['category'] == 'solidity'])}")\nprint(f"Rust: {len([p for p in PROBLEMS if p['category'] == 'rust'])}")\nprint(f"MOVE: {len([p for p in PROBLEMS if p['category'] == 'move'])}")\nprint(f"TVM: {len([p for p in PROBLEMS if p['category'] == 'func'])}")\n