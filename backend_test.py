#!/usr/bin/env python3
"""
Backend API Testing for CodeChain Platform
Testing Solidity Code Validation End-to-End

This script tests the complete flow:
1. User registration/login
2. Problem retrieval (sol_001 - Hello Blockchain)
3. Valid Solidity code submission
4. Invalid Solidity code submission (hardcoded answers)
5. Compilation error handling
6. ELO updates and submission tracking
"""

import requests
import json
import time
import sys
from typing import Dict, Any, Optional

# Backend URL from environment
BACKEND_URL = "https://skill-chain-dev.preview.emergentagent.com/api"

class CodeChainTester:
    def __init__(self):
        self.session = requests.Session()
        self.test_users = []
        self.user_tokens = {}  # Store tokens for reuse
        
    def log(self, message: str, level: str = "INFO"):
        """Log test messages with timestamp"""
        timestamp = time.strftime("%H:%M:%S")
        print(f"[{timestamp}] {level}: {message}")
        
    def register_user(self, email: str, password: str, name: str) -> Optional[Dict]:
        """Register a new test user"""
        try:
            response = self.session.post(f"{BACKEND_URL}/auth/register", json={
                "email": email,
                "password": password,
                "name": name
            })
            
            if response.status_code == 200:
                data = response.json()
                self.log(f"✅ User registered: {name} ({email})")
                return data
            else:
                self.log(f"❌ Registration failed: {response.status_code} - {response.text}", "ERROR")
                return None
                
        except Exception as e:
            self.log(f"❌ Registration error: {str(e)}", "ERROR")
            return None
    
    def login_user(self, email: str, password: str) -> Optional[str]:
        """Login user and return JWT token"""
        try:
            response = self.session.post(f"{BACKEND_URL}/auth/login", json={
                "email": email,
                "password": password
            })
            
            if response.status_code == 200:
                data = response.json()
                token = data.get("token")
                self.log(f"✅ User logged in: {email}")
                return token
            else:
                self.log(f"❌ Login failed: {response.status_code} - {response.text}", "ERROR")
                return None
                
        except Exception as e:
            self.log(f"❌ Login error: {str(e)}", "ERROR")
            return None
    
    def get_problems(self, token: str) -> Optional[Dict]:
        """Get list of problems"""
        try:
            headers = {"Authorization": f"Bearer {token}"}
            response = self.session.get(f"{BACKEND_URL}/problems", headers=headers)
            
            if response.status_code == 200:
                data = response.json()
                self.log(f"✅ Retrieved {len(data.get('problems', []))} problems")
                return data
            else:
                self.log(f"❌ Failed to get problems: {response.status_code} - {response.text}", "ERROR")
                return None
                
        except Exception as e:
            self.log(f"❌ Get problems error: {str(e)}", "ERROR")
            return None
    
    def get_problem_details(self, token: str, problem_id: str) -> Optional[Dict]:
        """Get specific problem details"""
        try:
            headers = {"Authorization": f"Bearer {token}"}
            response = self.session.get(f"{BACKEND_URL}/problems/{problem_id}", headers=headers)
            
            if response.status_code == 200:
                data = response.json()
                self.log(f"✅ Retrieved problem details: {problem_id}")
                return data
            else:
                self.log(f"❌ Failed to get problem {problem_id}: {response.status_code} - {response.text}", "ERROR")
                return None
                
        except Exception as e:
            self.log(f"❌ Get problem details error: {str(e)}", "ERROR")
            return None
    
    def submit_code(self, token: str, problem_id: str, code: str, language: str = "solidity") -> Optional[Dict]:
        """Submit code solution"""
        try:
            headers = {"Authorization": f"Bearer {token}"}
            response = self.session.post(f"{BACKEND_URL}/submissions", 
                headers=headers,
                json={
                    "problem_id": problem_id,
                    "code": code,
                    "language": language
                }
            )
            
            if response.status_code == 200:
                data = response.json()
                status = data.get("status", "unknown")
                self.log(f"✅ Code submitted successfully - Status: {status}")
                return data
            else:
                self.log(f"❌ Code submission failed: {response.status_code} - {response.text}", "ERROR")
                return {"error": response.text, "status_code": response.status_code}
                
        except Exception as e:
            self.log(f"❌ Submit code error: {str(e)}", "ERROR")
            return None
    
    def get_user_stats(self, token: str) -> Optional[Dict]:
        """Get user statistics"""
        try:
            headers = {"Authorization": f"Bearer {token}"}
            response = self.session.get(f"{BACKEND_URL}/auth/me", headers=headers)
            
            if response.status_code == 200:
                data = response.json()
                elo = data.get("elo_rating", 0)
                problems_solved = data.get("problems_solved", 0)
                self.log(f"✅ User stats - ELO: {elo}, Problems solved: {problems_solved}")
                return data
            else:
                self.log(f"❌ Failed to get user stats: {response.status_code} - {response.text}", "ERROR")
                return None
                
        except Exception as e:
            self.log(f"❌ Get user stats error: {str(e)}", "ERROR")
            return None
    
    def test_valid_solidity_submission(self):
        """Test 1: Valid Solidity submission for sol_001"""
        self.log("🔧 TEST 1: Valid Solidity Code Submission", "TEST")
        
        # Register and login test user with timestamp to ensure uniqueness
        timestamp = str(int(time.time()))
        user_data = self.register_user(f"testuser1_{timestamp}@test.com", "Test123!", "Test User 1")
        if not user_data:
            return False
            
        token = user_data.get("token")
        if not token:
            self.log("❌ No token received from registration", "ERROR")
            return False
        
        # Get initial user stats
        initial_stats = self.get_user_stats(token)
        if not initial_stats:
            return False
        
        initial_elo = initial_stats.get("elo_rating", 1200)
        initial_problems = initial_stats.get("problems_solved", 0)
        
        # Get problem details
        problem = self.get_problem_details(token, "sol_001")
        if not problem:
            return False
        
        self.log(f"Problem: {problem.get('title', 'Unknown')}")
        self.log(f"Difficulty: {problem.get('difficulty', 'Unknown')}")
        
        # Submit CORRECT Solidity code
        correct_code = """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract HelloBlockchain {
    string private greeting;
    address public owner;
    
    constructor() {
        owner = msg.sender;
    }
    
    function setGreeting(string memory _greeting) public {
        require(msg.sender == owner, "Only owner can set greeting");
        greeting = _greeting;
    }
    
    function getGreeting() public view returns (string memory) {
        return greeting;
    }
}"""
        
        self.log("Submitting CORRECT Solidity code...")
        submission = self.submit_code(token, "sol_001", correct_code)
        
        if not submission:
            return False
        
        # Check submission results
        status = submission.get("status")
        test_results = submission.get("test_results", [])
        gas_used = submission.get("gas_used", 0)
        elo_change = submission.get("elo_change", 0)
        
        self.log(f"Submission Status: {status}")
        self.log(f"Gas Used: {gas_used}")
        self.log(f"ELO Change: {elo_change}")
        self.log(f"Test Results: {len(test_results)} tests")
        
        # Print detailed test results
        for i, test in enumerate(test_results):
            passed = test.get("passed", False)
            description = test.get("input", f"Test {i+1}")
            error = test.get("error")
            
            if passed:
                self.log(f"  ✅ {description}")
            else:
                self.log(f"  ❌ {description}: {error}")
        
        # Verify submission passed
        if status != "passed":
            self.log(f"❌ Expected 'passed' status, got '{status}'", "ERROR")
            return False
        
        # Check ELO increase
        if elo_change <= 0:
            self.log(f"❌ Expected positive ELO change, got {elo_change}", "ERROR")
            return False
        
        # Get updated user stats
        final_stats = self.get_user_stats(token)
        if not final_stats:
            return False
        
        final_elo = final_stats.get("elo_rating", 1200)
        final_problems = final_stats.get("problems_solved", 0)
        
        # Verify stats updated
        if final_elo != initial_elo + elo_change:
            self.log(f"❌ ELO not updated correctly. Expected: {initial_elo + elo_change}, Got: {final_elo}", "ERROR")
            return False
        
        if final_problems != initial_problems + 1:
            self.log(f"❌ Problems solved not updated. Expected: {initial_problems + 1}, Got: {final_problems}", "ERROR")
            return False
        
        self.log("✅ TEST 1 PASSED: Valid Solidity code accepted, tests passed, ELO increased", "SUCCESS")
        
        # Store token for later tests
        self.user_tokens['test1_user'] = token
        
        return True
    
    def test_hardcoded_answer_rejection(self):
        """Test 2: Invalid submission with hardcoded answer"""
        self.log("🔧 TEST 2: Hardcoded Answer Rejection", "TEST")
        
        # Register and login different test user
        timestamp = str(int(time.time()))
        user_data = self.register_user(f"testuser2_{timestamp}@test.com", "Test123!", "Test User 2")
        if not user_data:
            return False
            
        token = user_data.get("token")
        if not token:
            return False
        
        # Submit HARDCODED Solidity code (should fail multiple test cases)
        hardcoded_code = """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract HelloBlockchain {
    string private greeting;
    address public owner;
    
    constructor() {
        owner = msg.sender;
    }
    
    function setGreeting(string memory _greeting) public {
        // Intentionally do nothing - don't store the greeting
    }
    
    function getGreeting() public view returns (string memory) {
        // Always return hardcoded value
        return "Hello, CodeChain!";
    }
}"""
        
        self.log("Submitting HARDCODED Solidity code (should fail)...")
        submission = self.submit_code(token, "sol_001", hardcoded_code)
        
        if not submission:
            return False
        
        # Check submission results
        status = submission.get("status")
        test_results = submission.get("test_results", [])
        
        self.log(f"Submission Status: {status}")
        self.log(f"Test Results: {len(test_results)} tests")
        
        # Print detailed test results
        passed_tests = 0
        failed_tests = 0
        
        for i, test in enumerate(test_results):
            passed = test.get("passed", False)
            description = test.get("input", f"Test {i+1}")
            expected = test.get("expected", "")
            actual = test.get("actual", "")
            error = test.get("error")
            
            if passed:
                self.log(f"  ✅ {description}")
                passed_tests += 1
            else:
                self.log(f"  ❌ {description}")
                self.log(f"      Expected: {expected}")
                self.log(f"      Actual: {actual}")
                if error:
                    self.log(f"      Error: {error}")
                failed_tests += 1
        
        # Verify submission failed
        if status != "failed":
            self.log(f"❌ Expected 'failed' status, got '{status}'", "ERROR")
            return False
        
        # Should have some failed tests (hardcoded answer won't work for all test cases)
        if failed_tests == 0:
            self.log("❌ Expected some tests to fail with hardcoded answer", "ERROR")
            return False
        
        self.log(f"✅ TEST 2 PASSED: Hardcoded answer correctly rejected ({failed_tests} tests failed)", "SUCCESS")
        return True
    
    def test_compilation_error(self):
        """Test 3: Compilation error handling"""
        self.log("🔧 TEST 3: Compilation Error Handling", "TEST")
        
        # Register and login different test user
        timestamp = str(int(time.time()))
        user_data = self.register_user(f"testuser3_{timestamp}@test.com", "Test123!", "Test User 3")
        if not user_data:
            return False
            
        token = user_data.get("token")
        if not token:
            return False
        
        # Submit code with syntax errors
        syntax_error_code = """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract HelloBlockchain {
    string private greeting
    address public owner;  // Missing semicolon above
    
    constructor() {
        owner = msg.sender;
    }
    
    function setGreeting(string memory _greeting) public {
        greeting = _greeting  // Missing semicolon
    }
    
    function getGreeting() public view returns (string memory) {
        return greeting;
    }
}"""
        
        self.log("Submitting code with SYNTAX ERRORS...")
        submission = self.submit_code(token, "sol_001", syntax_error_code)
        
        if not submission:
            return False
        
        # Check submission results
        status = submission.get("status")
        test_results = submission.get("test_results", [])
        error_message = submission.get("error_message", "")
        
        self.log(f"Submission Status: {status}")
        self.log(f"Error Message: {error_message}")
        
        # Print test results
        for i, test in enumerate(test_results):
            passed = test.get("passed", False)
            description = test.get("input", f"Test {i+1}")
            error = test.get("error", "")
            
            if passed:
                self.log(f"  ✅ {description}")
            else:
                self.log(f"  ❌ {description}: {error}")
        
        # Verify compilation failed
        if status != "failed":
            self.log(f"❌ Expected 'failed' status for syntax error, got '{status}'", "ERROR")
            return False
        
        # Should have compilation error in results
        compilation_error_found = False
        for test in test_results:
            if "compilation" in test.get("input", "").lower() or "compilation" in test.get("error", "").lower():
                compilation_error_found = True
                break
        
        if not compilation_error_found and "compilation" not in error_message.lower():
            self.log("❌ Expected compilation error to be reported", "ERROR")
            return False
        
        self.log("✅ TEST 3 PASSED: Compilation errors correctly caught and reported", "SUCCESS")
        return True
    
    def test_empty_code_validation(self):
        """Test 4: Empty code validation"""
        self.log("🔧 TEST 4: Empty Code Validation", "TEST")
        
        # Register a new user for this test
        timestamp = str(int(time.time()))
        user_data = self.register_user(f"testuser4_{timestamp}@test.com", "Test123!", "Test User 4")
        if not user_data:
            return False
            
        token = user_data.get("token")
        if not token:
            return False
        
        # Submit empty code
        self.log("Submitting EMPTY code...")
        submission = self.submit_code(token, "sol_001", "")
        
        # Should get error response
        if submission and "error" in submission:
            error_msg = submission.get("error", "")
            status_code = submission.get("status_code", 0)
            
            self.log(f"Error Response: {error_msg}")
            self.log(f"Status Code: {status_code}")
            
            if status_code == 400 and "too short" in error_msg.lower():
                self.log("✅ TEST 4 PASSED: Empty code correctly rejected", "SUCCESS")
                return True
            else:
                self.log(f"❌ Expected 400 status with 'too short' message", "ERROR")
                return False
        else:
            self.log("❌ Expected error response for empty code", "ERROR")
            return False
    
    def test_duplicate_submission_prevention(self):
        """Test 5: Prevent solving same problem twice"""
        self.log("🔧 TEST 5: Duplicate Submission Prevention", "TEST")
        
        # Use token from test 1 if available, otherwise skip
        token = self.user_tokens.get('test1_user')
        if not token:
            self.log("❌ No token from test 1 available, skipping duplicate test", "ERROR")
            return False
        
        # Try to submit solution again
        correct_code = """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract HelloBlockchain {
    string private greeting;
    address public owner;
    
    constructor() {
        owner = msg.sender;
    }
    
    function setGreeting(string memory _greeting) public {
        require(msg.sender == owner, "Only owner can set greeting");
        greeting = _greeting;
    }
    
    function getGreeting() public view returns (string memory) {
        return greeting;
    }
}"""
        
        self.log("Submitting solution to already solved problem...")
        submission = self.submit_code(token, "sol_001", correct_code)
        
        # Should get error response
        if submission and "error" in submission:
            error_msg = submission.get("error", "")
            status_code = submission.get("status_code", 0)
            
            self.log(f"Error Response: {error_msg}")
            self.log(f"Status Code: {status_code}")
            
            if status_code == 400 and "already solved" in error_msg.lower():
                self.log("✅ TEST 5 PASSED: Duplicate submission correctly prevented", "SUCCESS")
                return True
            else:
                self.log(f"❌ Expected 400 status with 'already solved' message", "ERROR")
                return False
        else:
            self.log("❌ Expected error response for duplicate submission", "ERROR")
            return False
    
    def run_all_tests(self):
        """Run all backend tests"""
        self.log("🚀 Starting CodeChain Backend API Tests", "START")
        self.log(f"Backend URL: {BACKEND_URL}")
        
        tests = [
            ("Valid Solidity Submission", self.test_valid_solidity_submission),
            ("Hardcoded Answer Rejection", self.test_hardcoded_answer_rejection),
            ("Compilation Error Handling", self.test_compilation_error),
            ("Empty Code Validation", self.test_empty_code_validation),
            ("Duplicate Submission Prevention", self.test_duplicate_submission_prevention),
        ]
        
        passed = 0
        failed = 0
        
        for test_name, test_func in tests:
            self.log(f"\n{'='*60}")
            try:
                if test_func():
                    passed += 1
                else:
                    failed += 1
                    self.log(f"❌ {test_name} FAILED", "FAIL")
            except Exception as e:
                failed += 1
                self.log(f"❌ {test_name} FAILED with exception: {str(e)}", "FAIL")
            
            time.sleep(1)  # Brief pause between tests
        
        # Final summary
        self.log(f"\n{'='*60}")
        self.log("🏁 TEST SUMMARY", "SUMMARY")
        self.log(f"✅ Passed: {passed}")
        self.log(f"❌ Failed: {failed}")
        self.log(f"📊 Success Rate: {passed}/{passed+failed} ({100*passed/(passed+failed):.1f}%)")
        
        if failed == 0:
            self.log("🎉 ALL TESTS PASSED! Solidity validation system is working correctly.", "SUCCESS")
            return True
        else:
            self.log(f"⚠️  {failed} test(s) failed. Please check the issues above.", "WARNING")
            return False

def main():
    """Main test execution"""
    tester = CodeChainTester()
    
    try:
        success = tester.run_all_tests()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        tester.log("\n🛑 Tests interrupted by user", "INFO")
        sys.exit(1)
    except Exception as e:
        tester.log(f"\n💥 Unexpected error: {str(e)}", "ERROR")
        sys.exit(1)

if __name__ == "__main__":
    main()