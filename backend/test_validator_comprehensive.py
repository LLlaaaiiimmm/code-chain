"""
More comprehensive tests for code validator
"""
import asyncio
from code_validator import code_validator

# Test: Code with syntax error
SYNTAX_ERROR_CODE = """
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Greeting {
    string private greeting
    // Missing semicolon above ^
    
    function getGreeting() public view returns (string memory) {
        return greeting;
    }
}
"""

# Test: Code that doesn't return expected value
WRONG_LOGIC_CODE = """
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Greeting {
    string private greeting;
    address public owner;
    
    constructor() {
        owner = msg.sender;
    }
    
    function setGreeting(string memory _greeting) public {
        greeting = "WRONG VALUE";  // Always sets wrong value
    }
    
    function getGreeting() public view returns (string memory) {
        return greeting;
    }
}
"""

# Test: Correct implementation
CORRECT_CODE = """
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

test_problem = {
    "problem_id": "sol_001",
    "category": "solidity",
    "test_cases": [
        {
            "type": "state",
            "variable": "owner",
            "expected": "<deployer>"
        },
        {
            "type": "transaction",
            "function": "setGreeting",
            "args": ["Hello, CodeChain!"],
            "expected": "success"
        },
        {
            "type": "call",
            "function": "getGreeting",
            "args": [],
            "expected": "Hello, CodeChain!"
        }
    ]
}

async def run_test(name, code):
    print(f"\n{'='*80}")
    print(f"📝 {name}")
    print(f"{'='*80}")
    
    all_passed, test_results, gas, error = await code_validator.validate_submission(
        code=code,
        problem=test_problem,
        language="solidity"
    )
    
    result_emoji = "✅" if all_passed else "❌"
    print(f"\n{result_emoji} Overall Result: {'PASSED' if all_passed else 'FAILED'}")
    print(f"⛽ Gas Used: {gas}")
    if error:
        print(f"❌ Error: {error[:200]}")
    
    print("\nDetailed Test Results:")
    for result in test_results:
        status = "✅" if result["passed"] else "❌"
        test_desc = result.get('description', result.get('input', 'Test'))
        print(f"  {status} Test {result['test_id']}: {test_desc}")
        
        if result.get("actual") and result.get("expected"):
            print(f"      Expected: {result['expected']}")
            print(f"      Got: {result['actual']}")
        
        if result.get("error"):
            error_msg = result['error']
            if len(error_msg) > 150:
                error_msg = error_msg[:150] + "..."
            print(f"      Error: {error_msg}")
    
    return all_passed

async def main():
    print("="*80)
    print("COMPREHENSIVE CODE VALIDATOR TESTING")
    print("="*80)
    
    # Test 1: Syntax error (should fail at compilation)
    result1 = await run_test("TEST 1: Code with Syntax Error (Should FAIL)", SYNTAX_ERROR_CODE)
    
    # Test 2: Wrong logic (should fail at test execution)
    result2 = await run_test("TEST 2: Code with Wrong Logic (Should FAIL)", WRONG_LOGIC_CODE)
    
    # Test 3: Correct implementation (should pass)
    result3 = await run_test("TEST 3: Correct Implementation (Should PASS)", CORRECT_CODE)
    
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Test 1 (Syntax Error): {'❌ Failed as expected' if not result1 else '⚠️ Unexpected pass'}")
    print(f"Test 2 (Wrong Logic): {'❌ Failed as expected' if not result2 else '⚠️ Unexpected pass'}")
    print(f"Test 3 (Correct Code): {'✅ Passed as expected' if result3 else '⚠️ Unexpected fail'}")
    
    overall = (not result1) and (not result2) and result3
    print(f"\n{'✅ ALL TESTS PASSED!' if overall else '⚠️ Some tests unexpected'}")
    print("="*80)

if __name__ == "__main__":
    asyncio.run(main())
