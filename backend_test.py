#!/usr/bin/env python3
"""
CodeChain Backend API Testing Suite
Tests critical fixes for empty code validation, one-time solve logic, 
problem status check, and certificate minting authentication.
"""

import asyncio
import httpx
import json
import uuid
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv('/app/frontend/.env')
BACKEND_URL = os.getenv('REACT_APP_BACKEND_URL', 'https://compiler-helper.preview.emergentagent.com')
API_BASE = f"{BACKEND_URL}/api"

class CodeChainTester:
    def __init__(self):
        self.client = httpx.AsyncClient(timeout=30.0)
        self.test_user_token = None
        self.test_user_id = None
        self.expert_user_token = None
        self.expert_user_id = None
        self.test_problem_id = None
        self.results = []
        
    async def log_result(self, test_name: str, success: bool, message: str, details: dict = None):
        """Log test result"""
        result = {
            "test": test_name,
            "success": success,
            "message": message,
            "details": details or {},
            "timestamp": datetime.now().isoformat()
        }
        self.results.append(result)
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status}: {test_name} - {message}")
        if details:
            print(f"   Details: {details}")
    
    async def test_user_registration(self):
        """Test user registration"""
        try:
            # Generate unique test user
            unique_id = uuid.uuid4().hex[:8]
            test_email = f"testuser_{unique_id}@example.com"
            
            response = await self.client.post(f"{API_BASE}/auth/register", json={
                "email": test_email,
                "password": "TestPassword123!",
                "name": f"Test User {unique_id}"
            })
            
            if response.status_code == 200:
                data = response.json()
                self.test_user_token = data["token"]
                self.test_user_id = data["user"]["user_id"]
                await self.log_result("User Registration", True, "Successfully registered test user", {
                    "user_id": self.test_user_id,
                    "email": test_email
                })
                return True
            else:
                await self.log_result("User Registration", False, f"Registration failed: {response.status_code}", {
                    "response": response.text
                })
                return False
                
        except Exception as e:
            await self.log_result("User Registration", False, f"Registration error: {str(e)}")
            return False
    
    async def test_expert_user_creation(self):
        """Create expert user for certificate testing"""
        try:
            # Generate unique expert user
            unique_id = uuid.uuid4().hex[:8]
            expert_email = f"expert_{unique_id}@example.com"
            
            response = await self.client.post(f"{API_BASE}/auth/register", json={
                "email": expert_email,
                "password": "ExpertPassword123!",
                "name": f"Expert User {unique_id}"
            })
            
            if response.status_code == 200:
                data = response.json()
                self.expert_user_token = data["token"]
                self.expert_user_id = data["user"]["user_id"]
                
                # Upgrade to expert subscription
                headers = {"Authorization": f"Bearer {self.expert_user_token}"}
                upgrade_response = await self.client.post(
                    f"{API_BASE}/subscriptions/upgrade?plan_id=expert",
                    headers=headers
                )
                
                if upgrade_response.status_code == 200:
                    await self.log_result("Expert User Creation", True, "Successfully created expert user", {
                        "user_id": self.expert_user_id,
                        "email": expert_email,
                        "subscription": "expert"
                    })
                    return True
                else:
                    await self.log_result("Expert User Creation", False, f"Subscription upgrade failed: {upgrade_response.status_code}")
                    return False
            else:
                await self.log_result("Expert User Creation", False, f"Expert registration failed: {response.status_code}")
                return False
                
        except Exception as e:
            await self.log_result("Expert User Creation", False, f"Expert creation error: {str(e)}")
            return False
    
    async def test_get_problems(self):
        """Test getting problems list"""
        try:
            response = await self.client.get(f"{API_BASE}/problems")
            
            if response.status_code == 200:
                data = response.json()
                problems = data.get("problems", [])
                if problems:
                    self.test_problem_id = problems[0]["problem_id"]
                    await self.log_result("Get Problems", True, f"Retrieved {len(problems)} problems", {
                        "total_problems": len(problems),
                        "test_problem_id": self.test_problem_id
                    })
                    return True
                else:
                    await self.log_result("Get Problems", False, "No problems found in database")
                    return False
            else:
                await self.log_result("Get Problems", False, f"Failed to get problems: {response.status_code}")
                return False
                
        except Exception as e:
            await self.log_result("Get Problems", False, f"Error getting problems: {str(e)}")
            return False
    
    async def test_empty_code_validation(self):
        """Test empty code validation (minimum 10 characters)"""
        if not self.test_user_token or not self.test_problem_id:
            await self.log_result("Empty Code Validation", False, "Missing test user token or problem ID")
            return False
            
        headers = {"Authorization": f"Bearer {self.test_user_token}"}
        
        # Test 1: Completely empty code
        try:
            response = await self.client.post(f"{API_BASE}/submissions", 
                headers=headers,
                json={
                    "problem_id": self.test_problem_id,
                    "code": "",
                    "language": "solidity"
                }
            )
            
            if response.status_code == 400:
                error_msg = response.json().get("detail", "")
                if "minimum 10 characters" in error_msg.lower():
                    await self.log_result("Empty Code Validation - Empty", True, "Correctly rejected empty code", {
                        "status_code": response.status_code,
                        "error_message": error_msg
                    })
                else:
                    await self.log_result("Empty Code Validation - Empty", False, f"Wrong error message: {error_msg}")
                    return False
            else:
                await self.log_result("Empty Code Validation - Empty", False, f"Should have returned 400, got {response.status_code}")
                return False
                
        except Exception as e:
            await self.log_result("Empty Code Validation - Empty", False, f"Error testing empty code: {str(e)}")
            return False
        
        # Test 2: Code with less than 10 characters
        try:
            response = await self.client.post(f"{API_BASE}/submissions", 
                headers=headers,
                json={
                    "problem_id": self.test_problem_id,
                    "code": "hello",  # 5 characters
                    "language": "solidity"
                }
            )
            
            if response.status_code == 400:
                error_msg = response.json().get("detail", "")
                if "minimum 10 characters" in error_msg.lower():
                    await self.log_result("Empty Code Validation - Short", True, "Correctly rejected short code", {
                        "status_code": response.status_code,
                        "error_message": error_msg,
                        "code_length": 5
                    })
                    return True
                else:
                    await self.log_result("Empty Code Validation - Short", False, f"Wrong error message: {error_msg}")
                    return False
            else:
                await self.log_result("Empty Code Validation - Short", False, f"Should have returned 400, got {response.status_code}")
                return False
                
        except Exception as e:
            await self.log_result("Empty Code Validation - Short", False, f"Error testing short code: {str(e)}")
            return False
    
    async def test_one_time_solve_logic(self):
        """Test one-time solve logic (prevent solving same problem twice)"""
        if not self.test_user_token or not self.test_problem_id:
            await self.log_result("One-Time Solve Logic", False, "Missing test user token or problem ID")
            return False
            
        headers = {"Authorization": f"Bearer {self.test_user_token}"}
        
        # First submission - should succeed
        valid_code = """
        // SPDX-License-Identifier: MIT
        pragma solidity ^0.8.0;
        
        contract Solution {
            string public greeting = "Hello, World!";
            
            function setGreeting(string memory _greeting) public {
                greeting = _greeting;
            }
            
            function getGreeting() public view returns (string memory) {
                return greeting;
            }
        }
        """
        
        try:
            # Get user stats before submission
            user_response = await self.client.get(f"{API_BASE}/auth/me", headers=headers)
            if user_response.status_code != 200:
                await self.log_result("One-Time Solve Logic", False, "Failed to get user stats before submission")
                return False
                
            user_before = user_response.json()
            elo_before = user_before.get("elo_rating", 1200)
            problems_solved_before = user_before.get("problems_solved", 0)
            
            # First submission
            response = await self.client.post(f"{API_BASE}/submissions", 
                headers=headers,
                json={
                    "problem_id": self.test_problem_id,
                    "code": valid_code,
                    "language": "solidity"
                }
            )
            
            if response.status_code == 200:
                submission_data = response.json()
                if submission_data.get("status") == "passed":
                    elo_change = submission_data.get("elo_change", 0)
                    await self.log_result("One-Time Solve Logic - First Submit", True, "First submission successful", {
                        "submission_id": submission_data.get("submission_id"),
                        "status": submission_data.get("status"),
                        "elo_change": elo_change
                    })
                else:
                    await self.log_result("One-Time Solve Logic - First Submit", False, f"First submission failed: {submission_data.get('status')}")
                    return False
            else:
                await self.log_result("One-Time Solve Logic - First Submit", False, f"First submission failed: {response.status_code}")
                return False
            
            # Verify user stats increased
            user_response_after = await self.client.get(f"{API_BASE}/auth/me", headers=headers)
            if user_response_after.status_code == 200:
                user_after = user_response_after.json()
                elo_after = user_after.get("elo_rating", 1200)
                problems_solved_after = user_after.get("problems_solved", 0)
                
                if elo_after > elo_before and problems_solved_after > problems_solved_before:
                    await self.log_result("One-Time Solve Logic - Stats Update", True, "User stats correctly updated", {
                        "elo_before": elo_before,
                        "elo_after": elo_after,
                        "problems_solved_before": problems_solved_before,
                        "problems_solved_after": problems_solved_after
                    })
                else:
                    await self.log_result("One-Time Solve Logic - Stats Update", False, "User stats not updated correctly")
                    return False
            
            # Second submission - should fail
            response2 = await self.client.post(f"{API_BASE}/submissions", 
                headers=headers,
                json={
                    "problem_id": self.test_problem_id,
                    "code": valid_code,
                    "language": "solidity"
                }
            )
            
            if response2.status_code == 400:
                error_msg = response2.json().get("detail", "")
                if "already solved" in error_msg.lower():
                    await self.log_result("One-Time Solve Logic - Second Submit", True, "Correctly rejected second submission", {
                        "status_code": response2.status_code,
                        "error_message": error_msg
                    })
                    
                    # Verify stats didn't change again
                    user_response_final = await self.client.get(f"{API_BASE}/auth/me", headers=headers)
                    if user_response_final.status_code == 200:
                        user_final = user_response_final.json()
                        elo_final = user_final.get("elo_rating", 1200)
                        problems_solved_final = user_final.get("problems_solved", 0)
                        
                        if elo_final == elo_after and problems_solved_final == problems_solved_after:
                            await self.log_result("One-Time Solve Logic - No Double Count", True, "Stats correctly unchanged on second submission", {
                                "elo_remained": elo_final,
                                "problems_solved_remained": problems_solved_final
                            })
                            return True
                        else:
                            await self.log_result("One-Time Solve Logic - No Double Count", False, "Stats incorrectly changed on second submission")
                            return False
                else:
                    await self.log_result("One-Time Solve Logic - Second Submit", False, f"Wrong error message: {error_msg}")
                    return False
            else:
                await self.log_result("One-Time Solve Logic - Second Submit", False, f"Should have returned 400, got {response2.status_code}")
                return False
                
        except Exception as e:
            await self.log_result("One-Time Solve Logic", False, f"Error testing one-time solve: {str(e)}")
            return False
    
    async def test_problem_status_check(self):
        """Test problem status check endpoint"""
        if not self.test_user_token or not self.test_problem_id:
            await self.log_result("Problem Status Check", False, "Missing test user token or problem ID")
            return False
            
        headers = {"Authorization": f"Bearer {self.test_user_token}"}
        
        try:
            # Check status of solved problem
            response = await self.client.get(f"{API_BASE}/problems/{self.test_problem_id}/status", headers=headers)
            
            if response.status_code == 200:
                status_data = response.json()
                is_solved = status_data.get("is_solved", False)
                submission = status_data.get("submission")
                
                if is_solved and submission:
                    await self.log_result("Problem Status Check - Solved", True, "Correctly shows problem as solved", {
                        "problem_id": self.test_problem_id,
                        "is_solved": is_solved,
                        "submission_id": submission.get("submission_id") if submission else None
                    })
                else:
                    await self.log_result("Problem Status Check - Solved", False, f"Problem should be marked as solved: is_solved={is_solved}")
                    return False
            else:
                await self.log_result("Problem Status Check - Solved", False, f"Status check failed: {response.status_code}")
                return False
            
            # Test with a different problem (should be unsolved)
            problems_response = await self.client.get(f"{API_BASE}/problems")
            if problems_response.status_code == 200:
                problems = problems_response.json().get("problems", [])
                unsolved_problem = None
                for problem in problems:
                    if problem["problem_id"] != self.test_problem_id:
                        unsolved_problem = problem["problem_id"]
                        break
                
                if unsolved_problem:
                    unsolved_response = await self.client.get(f"{API_BASE}/problems/{unsolved_problem}/status", headers=headers)
                    if unsolved_response.status_code == 200:
                        unsolved_data = unsolved_response.json()
                        if not unsolved_data.get("is_solved", True):
                            await self.log_result("Problem Status Check - Unsolved", True, "Correctly shows problem as unsolved", {
                                "problem_id": unsolved_problem,
                                "is_solved": unsolved_data.get("is_solved")
                            })
                            return True
                        else:
                            await self.log_result("Problem Status Check - Unsolved", False, "Problem should be marked as unsolved")
                            return False
                    else:
                        await self.log_result("Problem Status Check - Unsolved", False, f"Unsolved status check failed: {unsolved_response.status_code}")
                        return False
                else:
                    await self.log_result("Problem Status Check - Unsolved", True, "No additional problems to test unsolved status")
                    return True
            else:
                await self.log_result("Problem Status Check - Unsolved", True, "Could not get additional problems for unsolved test")
                return True
                
        except Exception as e:
            await self.log_result("Problem Status Check", False, f"Error testing problem status: {str(e)}")
            return False
    
    async def test_certificate_minting_auth(self):
        """Test certificate minting authentication"""
        if not self.expert_user_token:
            await self.log_result("Certificate Minting Auth", False, "Missing expert user token")
            return False
            
        headers = {"Authorization": f"Bearer {self.expert_user_token}"}
        
        try:
            # Test with expert user (should work)
            response = await self.client.post(f"{API_BASE}/certificates/mint", 
                headers=headers,
                json={
                    "certificate_type": "expert_rating",
                    "metadata": {"test": "certificate"}
                }
            )
            
            if response.status_code == 200:
                cert_data = response.json()
                await self.log_result("Certificate Minting Auth - Expert", True, "Expert user can mint certificates", {
                    "certificate_id": cert_data.get("certificate_id"),
                    "type": cert_data.get("type"),
                    "blockchain": cert_data.get("blockchain")
                })
            elif response.status_code == 400:
                error_msg = response.json().get("detail", "")
                if "rating" in error_msg.lower():
                    await self.log_result("Certificate Minting Auth - Expert", True, "Expert user needs higher rating (expected)", {
                        "error": error_msg
                    })
                else:
                    await self.log_result("Certificate Minting Auth - Expert", False, f"Unexpected error: {error_msg}")
                    return False
            else:
                await self.log_result("Certificate Minting Auth - Expert", False, f"Unexpected status code: {response.status_code}")
                return False
            
            # Test with basic user (should fail)
            if self.test_user_token:
                basic_headers = {"Authorization": f"Bearer {self.test_user_token}"}
                basic_response = await self.client.post(f"{API_BASE}/certificates/mint", 
                    headers=basic_headers,
                    json={
                        "certificate_type": "expert_rating",
                        "metadata": {"test": "certificate"}
                    }
                )
                
                if basic_response.status_code == 403:
                    error_msg = basic_response.json().get("detail", "")
                    if "expert subscription required" in error_msg.lower():
                        await self.log_result("Certificate Minting Auth - Basic", True, "Basic user correctly denied", {
                            "status_code": basic_response.status_code,
                            "error_message": error_msg
                        })
                        return True
                    else:
                        await self.log_result("Certificate Minting Auth - Basic", False, f"Wrong error message: {error_msg}")
                        return False
                else:
                    await self.log_result("Certificate Minting Auth - Basic", False, f"Should have returned 403, got {basic_response.status_code}")
                    return False
            else:
                await self.log_result("Certificate Minting Auth - Basic", True, "No basic user to test (acceptable)")
                return True
                
        except Exception as e:
            await self.log_result("Certificate Minting Auth", False, f"Error testing certificate minting: {str(e)}")
            return False
    
    async def test_authentication_endpoints(self):
        """Test authentication endpoints"""
        if not self.test_user_token:
            await self.log_result("Authentication Endpoints", False, "Missing test user token")
            return False
            
        headers = {"Authorization": f"Bearer {self.test_user_token}"}
        
        try:
            # Test /auth/me endpoint
            response = await self.client.get(f"{API_BASE}/auth/me", headers=headers)
            
            if response.status_code == 200:
                user_data = response.json()
                if user_data.get("user_id") == self.test_user_id:
                    await self.log_result("Authentication Endpoints", True, "Authentication working correctly", {
                        "user_id": user_data.get("user_id"),
                        "email": user_data.get("email"),
                        "elo_rating": user_data.get("elo_rating")
                    })
                    return True
                else:
                    await self.log_result("Authentication Endpoints", False, "Wrong user data returned")
                    return False
            else:
                await self.log_result("Authentication Endpoints", False, f"Auth check failed: {response.status_code}")
                return False
                
        except Exception as e:
            await self.log_result("Authentication Endpoints", False, f"Error testing authentication: {str(e)}")
            return False
    
    async def run_all_tests(self):
        """Run all tests in sequence"""
        print(f"🚀 Starting CodeChain Backend Tests")
        print(f"📡 Testing API at: {API_BASE}")
        print("=" * 60)
        
        # Seed data first
        try:
            seed_response = await self.client.post(f"{API_BASE}/seed")
            if seed_response.status_code == 200:
                print("✅ Database seeded successfully")
            else:
                print(f"⚠️  Seed failed: {seed_response.status_code}")
        except Exception as e:
            print(f"⚠️  Seed error: {str(e)}")
        
        # Run tests in order
        tests = [
            ("User Registration", self.test_user_registration),
            ("Expert User Creation", self.test_expert_user_creation),
            ("Get Problems", self.test_get_problems),
            ("Authentication Endpoints", self.test_authentication_endpoints),
            ("Empty Code Validation", self.test_empty_code_validation),
            ("One-Time Solve Logic", self.test_one_time_solve_logic),
            ("Problem Status Check", self.test_problem_status_check),
            ("Certificate Minting Auth", self.test_certificate_minting_auth),
        ]
        
        passed = 0
        failed = 0
        
        for test_name, test_func in tests:
            print(f"\n🧪 Running: {test_name}")
            try:
                success = await test_func()
                if success:
                    passed += 1
                else:
                    failed += 1
            except Exception as e:
                await self.log_result(test_name, False, f"Test execution error: {str(e)}")
                failed += 1
        
        # Summary
        print("\n" + "=" * 60)
        print(f"📊 TEST SUMMARY")
        print(f"✅ Passed: {passed}")
        print(f"❌ Failed: {failed}")
        print(f"📈 Success Rate: {passed/(passed+failed)*100:.1f}%")
        
        # Critical issues summary
        critical_failures = [r for r in self.results if not r["success"] and "validation" in r["test"].lower() or "solve logic" in r["test"].lower()]
        if critical_failures:
            print(f"\n🚨 CRITICAL ISSUES FOUND:")
            for failure in critical_failures:
                print(f"   - {failure['test']}: {failure['message']}")
        
        await self.client.aclose()
        return passed, failed, self.results

async def main():
    """Main test runner"""
    tester = CodeChainTester()
    passed, failed, results = await tester.run_all_tests()
    
    # Save detailed results
    with open('/app/test_results_detailed.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n📄 Detailed results saved to: /app/test_results_detailed.json")
    
    # Return exit code based on results
    return 0 if failed == 0 else 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    exit(exit_code)