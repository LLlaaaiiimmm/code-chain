"""
Test script for the enhanced code validator
"""
import asyncio
from code_validator import code_validator

# Test 1: Simple Solidity contract that should pass
CORRECT_GREETING = """
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Greeting {
    string private greeting;
    address public owner;
    
    constructor() {
        owner = msg.sender;
    }
    
    function setGreeting(string memory _greeting) public {
        require(msg.sender == owner, "Only owner");
        greeting = _greeting;
    }
    
    function getGreeting() public view returns (string memory) {
        return greeting;
    }
}
"""

# Test 2: Wrong contract (missing implementation)
WRONG_GREETING = """
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Greeting {
    string private greeting;
    address public owner;
    
    constructor() {
        owner = msg.sender;
    }
    
    function setGreeting(string memory _greeting) public {
        // TODO: Implement
    }
    
    function getGreeting() public view returns (string memory) {
        // TODO: Implement
    }
}
"""

# Test problem definition with new test_cases format
test_problem = {
    "problem_id": "sol_001",
    "title": "Hello Blockchain",
    "difficulty": "junior",
    "category": "solidity",
    "test_cases": [
        {
            "type": "state",
            "variable": "owner",
            "expected": "<deployer>",
            "description": "Owner should be set to deployer"
        },
        {
            "type": "transaction",
            "function": "setGreeting",
            "args": ["Hello, CodeChain!"],
            "expected": "success",
            "description": "Should set greeting successfully"
        },
        {
            "type": "call",
            "function": "getGreeting",
            "args": [],
            "expected": "Hello, CodeChain!",
            "description": "Should return correct greeting"
        }
    ]
}

async def test_validator():
    print("=" * 80)
    print("TESTING ENHANCED CODE VALIDATOR")
    print("=" * 80)
    
    # Test 1: Correct implementation
    print("\n📝 TEST 1: Correct Implementation")
    print("-" * 80)
    all_passed, test_results, gas, error = await code_validator.validate_submission(
        code=CORRECT_GREETING,
        problem=test_problem,
        language="solidity"
    )
    
    print(f"✅ All Passed: {all_passed}")
    print(f"⛽ Gas Used: {gas}")
    print(f"❌ Error: {error if error else 'None'}")
    print("\nTest Results:")
    for result in test_results:
        status = "✅" if result["passed"] else "❌"
        print(f"  {status} Test {result['test_id']}: {result.get('description', result.get('input', 'N/A'))}")
        if result.get("error"):
            print(f"      Error: {result['error']}")
        if result.get("actual"):
            print(f"      Got: {result['actual']}, Expected: {result.get('expected', 'N/A')}")
    
    # Test 2: Wrong implementation
    print("\n" + "=" * 80)
    print("📝 TEST 2: Wrong Implementation (should fail)")
    print("-" * 80)
    all_passed2, test_results2, gas2, error2 = await code_validator.validate_submission(
        code=WRONG_GREETING,
        problem=test_problem,
        language="solidity"
    )
    
    print(f"✅ All Passed: {all_passed2}")
    print(f"⛽ Gas Used: {gas2}")
    print(f"❌ Error: {error2 if error2 else 'None'}")
    print("\nTest Results:")
    for result in test_results2:
        status = "✅" if result["passed"] else "❌"
        print(f"  {status} Test {result['test_id']}: {result.get('description', result.get('input', 'N/A'))}")
        if result.get("error"):
            print(f"      Error: {result['error']}")
        if result.get("actual"):
            print(f"      Got: {result['actual']}, Expected: {result.get('expected', 'N/A')}")
    
    print("\n" + "=" * 80)
    print("TESTING COMPLETE")
    print("=" * 80)

if __name__ == "__main__":
    asyncio.run(test_validator())
