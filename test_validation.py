#!/usr/bin/env python3
"""
Test script to verify that empty Solidity code is properly rejected
"""
import asyncio
import sys
sys.path.append('/app/backend')

from code_validator import CodeValidator

async def test_empty_code():
    """Test that empty code with TODOs is rejected"""
    validator = CodeValidator()
    
    # Test 1: Code with TODO
    code_with_todo = """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Antifrontrunning {
    struct Commitment {
        bytes32 hash;
        uint256 timestamp;
        bool revealed;
        uint256 value;
    }
    
    mapping(address => Commitment) public commitments;
    uint256 public constant REVEAL_DELAY = 10;
    
    function commit(bytes32 hash) external {
        // TODO: Implement commit
    }
    
    function reveal(uint256 value, bytes32 salt) external {
        // TODO: Implement reveal
    }
    
    function getCommitmentHash(uint256 value, bytes32 salt) public pure returns (bytes32) {
        // TODO: Implement
    }
}"""
    
    problem = {
        "category": "solidity",
        "test_cases": []
    }
    
    print("Test 1: Code with TODO comments")
    result, test_results, gas, error = await validator.validate_submission(code_with_todo, problem, "solidity")
    print(f"  Result: {'PASS' if not result else 'FAIL'}")
    print(f"  Expected: Should be rejected (result=False)")
    print(f"  Error message: {error}")
    if test_results:
        print(f"  Test result error: {test_results[0].get('error', 'N/A')}")
    print()
    
    # Test 2: Empty function bodies
    code_with_empty_functions = """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Antifrontrunning {
    mapping(address => bytes32) public commitments;
    
    function commit(bytes32 hash) external {
    }
    
    function reveal(uint256 value, bytes32 salt) external {
    }
}"""
    
    print("Test 2: Code with empty functions")
    result, test_results, gas, error = await validator.validate_submission(code_with_empty_functions, problem, "solidity")
    print(f"  Result: {'PASS' if not result else 'FAIL'}")
    print(f"  Expected: Should be rejected (result=False)")
    print(f"  Error message: {error}")
    if test_results:
        print(f"  Test result error: {test_results[0].get('error', 'N/A')}")
    print()
    
    # Test 3: Properly implemented code (should compile)
    proper_code = """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Antifrontrunning {
    struct Commitment {
        bytes32 hash;
        uint256 timestamp;
        bool revealed;
        uint256 value;
    }
    
    mapping(address => Commitment) public commitments;
    uint256 public constant REVEAL_DELAY = 10;
    
    event Committed(address indexed user, bytes32 hash);
    event Revealed(address indexed user, uint256 value);
    
    function commit(bytes32 hash) external {
        commitments[msg.sender] = Commitment({
            hash: hash,
            timestamp: block.number,
            revealed: false,
            value: 0
        });
        emit Committed(msg.sender, hash);
    }
    
    function reveal(uint256 value, bytes32 salt) external {
        Commitment storage c = commitments[msg.sender];
        require(block.number >= c.timestamp + REVEAL_DELAY, "Delay not passed");
        require(!c.revealed, "Already revealed");
        require(keccak256(abi.encodePacked(value, salt)) == c.hash, "Invalid reveal");
        
        c.revealed = true;
        c.value = value;
        emit Revealed(msg.sender, value);
    }
    
    function getCommitmentHash(uint256 value, bytes32 salt) public pure returns (bytes32) {
        return keccak256(abi.encodePacked(value, salt));
    }
}"""
    
    print("Test 3: Properly implemented code")
    result, test_results, gas, error = await validator.validate_submission(proper_code, problem, "solidity")
    print(f"  Result: {'PASS' if result else 'FAIL'}")
    print(f"  Expected: Should compile successfully (result=True or at least compile)")
    print(f"  Error message: {error if error else 'None'}")
    if not result and test_results:
        print(f"  Test result error: {test_results[0].get('error', 'N/A')}")
    print()
    
    print("=" * 60)
    print("VALIDATION FIX TEST SUMMARY:")
    print("=" * 60)
    print("✅ Empty code with TODO should be REJECTED")
    print("✅ Code with empty functions should be REJECTED")
    print("✅ Properly implemented code should COMPILE")
    print()

if __name__ == "__main__":
    asyncio.run(test_empty_code())
