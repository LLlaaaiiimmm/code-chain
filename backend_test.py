#!/usr/bin/env python3
"""
Comprehensive Backend API Testing for CodeChain Platform
Tests all major endpoints including authentication, problems, submissions, etc.
"""

import requests
import json
import time
from datetime import datetime, timezone
import uuid

# Configuration
BASE_URL = "https://devchain-1.preview.emergentagent.com/api"
TEST_USER_EMAIL = f"testuser_{uuid.uuid4().hex[:8]}@example.com"
TEST_USER_PASSWORD = "TestPassword123!"
TEST_USER_NAME = "Test User"

class CodeChainAPITester:
    def __init__(self):
        self.session = requests.Session()
        self.auth_token = None
        self.user_id = None
        self.test_results = []
        
    def log_result(self, test_name, success, details="", response_data=None):
        """Log test result"""
        result = {
            "test": test_name,
            "success": success,
            "details": details,
            "timestamp": datetime.now().isoformat()
        }
        if response_data:
            result["response_data"] = response_data
        self.test_results.append(result)
        
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} {test_name}: {details}")
        
    def make_request(self, method, endpoint, **kwargs):
        """Make HTTP request with proper headers"""
        url = f"{BASE_URL}{endpoint}"
        headers = kwargs.get('headers', {})
        
        if self.auth_token:
            headers['Authorization'] = f"Bearer {self.auth_token}"
            
        kwargs['headers'] = headers
        
        try:
            response = self.session.request(method, url, **kwargs)
            return response
        except Exception as e:
            print(f"Request failed: {e}")
            return None
    
    def test_auth_register(self):
        """Test user registration"""
        data = {
            "email": TEST_USER_EMAIL,
            "password": TEST_USER_PASSWORD,
            "name": TEST_USER_NAME
        }
        
        response = self.make_request("POST", "/auth/register", json=data)
        
        if response and response.status_code == 200:
            result = response.json()
            if "token" in result and "user" in result:
                self.auth_token = result["token"]
                self.user_id = result["user"]["user_id"]
                self.log_result("Auth Register", True, 
                              f"User registered successfully with ID: {self.user_id}",
                              {"user_id": self.user_id, "email": result["user"]["email"]})
                return True
            else:
                self.log_result("Auth Register", False, "Missing token or user in response")
        else:
            error_msg = response.text if response else "No response"
            self.log_result("Auth Register", False, f"Registration failed: {error_msg}")
        return False
    
    def test_auth_login(self):
        """Test user login"""
        data = {
            "email": TEST_USER_EMAIL,
            "password": TEST_USER_PASSWORD
        }
        
        response = self.make_request("POST", "/auth/login", json=data)
        
        if response and response.status_code == 200:
            result = response.json()
            if "token" in result:
                self.auth_token = result["token"]
                self.log_result("Auth Login", True, "Login successful")
                return True
            else:
                self.log_result("Auth Login", False, "Missing token in response")
        else:
            error_msg = response.text if response else "No response"
            self.log_result("Auth Login", False, f"Login failed: {error_msg}")
        return False
    
    def test_auth_me(self):
        """Test get current user info"""
        response = self.make_request("GET", "/auth/me")
        
        if response and response.status_code == 200:
            result = response.json()
            if "user_id" in result and "email" in result:
                self.log_result("Auth Me", True, 
                              f"User info retrieved: {result['name']} ({result['email']})",
                              {"elo_rating": result.get("elo_rating"), "subscription": result.get("subscription")})
                return True
            else:
                self.log_result("Auth Me", False, "Missing user data in response")
        else:
            error_msg = response.text if response else "No response"
            self.log_result("Auth Me", False, f"Get user info failed: {error_msg}")
        return False
    
    def test_problems_list(self):
        """Test get problems list with filters"""
        # Test basic list
        response = self.make_request("GET", "/problems")
        
        if response and response.status_code == 200:
            result = response.json()
            if "problems" in result and "total" in result:
                problems_count = len(result["problems"])
                self.log_result("Problems List", True, 
                              f"Retrieved {problems_count} problems, total: {result['total']}")
                
                # Test with difficulty filter
                response_diff = self.make_request("GET", "/problems?difficulty=junior")
                if response_diff and response_diff.status_code == 200:
                    diff_result = response_diff.json()
                    junior_count = len(diff_result["problems"])
                    self.log_result("Problems Filter (Difficulty)", True, 
                                  f"Retrieved {junior_count} junior problems")
                else:
                    self.log_result("Problems Filter (Difficulty)", False, "Difficulty filter failed")
                
                # Test with category filter
                response_cat = self.make_request("GET", "/problems?category=solidity")
                if response_cat and response_cat.status_code == 200:
                    cat_result = response_cat.json()
                    solidity_count = len(cat_result["problems"])
                    self.log_result("Problems Filter (Category)", True, 
                                  f"Retrieved {solidity_count} solidity problems")
                else:
                    self.log_result("Problems Filter (Category)", False, "Category filter failed")
                
                return True
            else:
                self.log_result("Problems List", False, "Missing problems or total in response")
        else:
            error_msg = response.text if response else "No response"
            self.log_result("Problems List", False, f"Get problems failed: {error_msg}")
        return False
    
    def test_problem_detail(self):
        """Test get specific problem details"""
        # First get a problem ID
        response = self.make_request("GET", "/problems?limit=1")
        
        if response and response.status_code == 200:
            result = response.json()
            if result["problems"]:
                problem_id = result["problems"][0]["problem_id"]
                
                # Test get specific problem
                detail_response = self.make_request("GET", f"/problems/{problem_id}")
                
                if detail_response and detail_response.status_code == 200:
                    detail_result = detail_response.json()
                    if "problem_id" in detail_result and "title" in detail_result:
                        self.log_result("Problem Detail", True, 
                                      f"Retrieved problem: {detail_result['title']} ({problem_id})",
                                      {"difficulty": detail_result.get("difficulty"), 
                                       "category": detail_result.get("category")})
                        return problem_id
                    else:
                        self.log_result("Problem Detail", False, "Missing problem data in response")
                else:
                    error_msg = detail_response.text if detail_response else "No response"
                    self.log_result("Problem Detail", False, f"Get problem detail failed: {error_msg}")
            else:
                self.log_result("Problem Detail", False, "No problems available to test")
        else:
            self.log_result("Problem Detail", False, "Could not get problems list for detail test")
        return None
    
    def test_submission_create(self, problem_id):
        """Test code submission"""
        if not problem_id:
            self.log_result("Submission Create", False, "No problem ID available")
            return False
            
        # Simple valid Solidity code
        test_code = """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Solution {
    string private greeting;
    
    function setGreeting(string memory _greeting) public {
        greeting = _greeting;
    }
    
    function getGreeting() public view returns (string memory) {
        return greeting;
    }
}"""
        
        data = {
            "problem_id": problem_id,
            "code": test_code,
            "language": "solidity"
        }
        
        response = self.make_request("POST", "/submissions", json=data)
        
        if response and response.status_code == 200:
            result = response.json()
            if "submission_id" in result and "status" in result:
                self.log_result("Submission Create", True, 
                              f"Submission created: {result['submission_id']}, status: {result['status']}",
                              {"test_results": len(result.get("test_results", [])), 
                               "elo_change": result.get("elo_change")})
                return True
            else:
                self.log_result("Submission Create", False, "Missing submission data in response")
        else:
            error_msg = response.text if response else "No response"
            self.log_result("Submission Create", False, f"Submission failed: {error_msg}")
        return False
    
    def test_submissions_list(self):
        """Test get user submissions"""
        response = self.make_request("GET", "/submissions")
        
        if response and response.status_code == 200:
            result = response.json()
            if isinstance(result, list):
                submissions_count = len(result)
                self.log_result("Submissions List", True, 
                              f"Retrieved {submissions_count} user submissions")
                return True
            else:
                self.log_result("Submissions List", False, "Response is not a list")
        else:
            error_msg = response.text if response else "No response"
            self.log_result("Submissions List", False, f"Get submissions failed: {error_msg}")
        return False
    
    def test_leaderboard(self):
        """Test global leaderboard"""
        response = self.make_request("GET", "/leaderboard")
        
        if response and response.status_code == 200:
            result = response.json()
            if isinstance(result, list):
                leaderboard_count = len(result)
                self.log_result("Leaderboard", True, 
                              f"Retrieved leaderboard with {leaderboard_count} users")
                return True
            else:
                self.log_result("Leaderboard", False, "Response is not a list")
        else:
            error_msg = response.text if response else "No response"
            self.log_result("Leaderboard", False, f"Get leaderboard failed: {error_msg}")
        return False
    
    def test_subscription_plans(self):
        """Test get subscription plans"""
        response = self.make_request("GET", "/subscriptions/plans")
        
        if response and response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                plans_count = len(result)
                plan_names = [plan.get("name", "Unknown") for plan in result]
                self.log_result("Subscription Plans", True, 
                              f"Retrieved {plans_count} subscription plans: {', '.join(plan_names)}")
                return True
            else:
                self.log_result("Subscription Plans", False, "No plans in response")
        else:
            error_msg = response.text if response else "No response"
            self.log_result("Subscription Plans", False, f"Get subscription plans failed: {error_msg}")
        return False
    
    def test_subscription_current(self):
        """Test get current subscription"""
        response = self.make_request("GET", "/subscriptions/current")
        
        if response and response.status_code == 200:
            result = response.json()
            if "plan" in result:
                self.log_result("Current Subscription", True, 
                              f"Current plan: {result['plan']}, problems solved this month: {result.get('problems_solved_this_month', 0)}")
                return True
            else:
                self.log_result("Current Subscription", False, "Missing plan in response")
        else:
            error_msg = response.text if response else "No response"
            self.log_result("Current Subscription", False, f"Get current subscription failed: {error_msg}")
        return False
    
    def test_subscription_upgrade(self):
        """Test subscription upgrade"""
        response = self.make_request("POST", "/subscriptions/upgrade?plan_id=expert")
        
        if response and response.status_code == 200:
            result = response.json()
            if "subscription" in result:
                self.log_result("Subscription Upgrade", True, 
                              f"Upgraded to: {result['subscription']}")
                return True
            else:
                self.log_result("Subscription Upgrade", False, "Missing subscription in response")
        else:
            error_msg = response.text if response else "No response"
            self.log_result("Subscription Upgrade", False, f"Subscription upgrade failed: {error_msg}")
        return False
    
    def test_certificates_list(self):
        """Test get user certificates"""
        response = self.make_request("GET", "/certificates")
        
        if response and response.status_code == 200:
            result = response.json()
            if isinstance(result, list):
                certificates_count = len(result)
                self.log_result("Certificates List", True, 
                              f"Retrieved {certificates_count} certificates")
                return True
            else:
                self.log_result("Certificates List", False, "Response is not a list")
        else:
            error_msg = response.text if response else "No response"
            self.log_result("Certificates List", False, f"Get certificates failed: {error_msg}")
        return False
    
    def test_certificate_mint(self):
        """Test certificate minting"""
        data = {
            "certificate_type": "problem_master",
            "metadata": {"test": True}
        }
        
        response = self.make_request("POST", "/certificates/mint", json=data)
        
        if response and response.status_code == 200:
            result = response.json()
            if "certificate_id" in result:
                self.log_result("Certificate Mint", True, 
                              f"Certificate minted: {result['certificate_id']}, type: {result.get('type')}")
                return True
            else:
                self.log_result("Certificate Mint", False, "Missing certificate_id in response")
        elif response and response.status_code == 403:
            self.log_result("Certificate Mint", True, 
                          "Certificate minting correctly requires Expert subscription (403 expected)")
            return True
        elif response and response.status_code == 400:
            self.log_result("Certificate Mint", True, 
                          "Certificate minting correctly validates criteria (400 expected)")
            return True
        else:
            error_msg = response.text if response else "No response"
            self.log_result("Certificate Mint", False, f"Certificate minting failed: {error_msg}")
        return False
    
    def test_hackathons_list(self):
        """Test get hackathons"""
        response = self.make_request("GET", "/hackathons")
        
        if response and response.status_code == 200:
            result = response.json()
            if isinstance(result, list):
                hackathons_count = len(result)
                self.log_result("Hackathons List", True, 
                              f"Retrieved {hackathons_count} hackathons")
                
                # Test with status filter
                active_response = self.make_request("GET", "/hackathons?status=active")
                if active_response and active_response.status_code == 200:
                    active_result = active_response.json()
                    active_count = len(active_result)
                    self.log_result("Hackathons Filter (Active)", True, 
                                  f"Retrieved {active_count} active hackathons")
                
                return hackathons_count > 0
            else:
                self.log_result("Hackathons List", False, "Response is not a list")
        else:
            error_msg = response.text if response else "No response"
            self.log_result("Hackathons List", False, f"Get hackathons failed: {error_msg}")
        return False
    
    def test_hackathon_detail(self):
        """Test get specific hackathon"""
        # First get a hackathon ID
        response = self.make_request("GET", "/hackathons")
        
        if response and response.status_code == 200:
            result = response.json()
            if result and len(result) > 0:
                hackathon_id = result[0]["hackathon_id"]
                
                detail_response = self.make_request("GET", f"/hackathons/{hackathon_id}")
                
                if detail_response and detail_response.status_code == 200:
                    detail_result = detail_response.json()
                    if "hackathon_id" in detail_result:
                        self.log_result("Hackathon Detail", True, 
                                      f"Retrieved hackathon: {detail_result.get('title', 'Unknown')} ({hackathon_id})")
                        return True
                    else:
                        self.log_result("Hackathon Detail", False, "Missing hackathon data in response")
                else:
                    error_msg = detail_response.text if detail_response else "No response"
                    self.log_result("Hackathon Detail", False, f"Get hackathon detail failed: {error_msg}")
            else:
                self.log_result("Hackathon Detail", True, "No hackathons available to test (expected)")
                return True
        else:
            self.log_result("Hackathon Detail", False, "Could not get hackathons list for detail test")
        return False
    
    def test_dashboard_stats(self):
        """Test dashboard statistics"""
        response = self.make_request("GET", "/stats/dashboard")
        
        if response and response.status_code == 200:
            result = response.json()
            expected_fields = ["total_submissions", "passed_submissions", "elo_rating", "problems_solved", "rank"]
            if all(field in result for field in expected_fields):
                self.log_result("Dashboard Stats", True, 
                              f"ELO: {result['elo_rating']}, Problems: {result['problems_solved']}, Rank: {result['rank']}")
                return True
            else:
                missing = [f for f in expected_fields if f not in result]
                self.log_result("Dashboard Stats", False, f"Missing fields: {missing}")
        else:
            error_msg = response.text if response else "No response"
            self.log_result("Dashboard Stats", False, f"Get dashboard stats failed: {error_msg}")
        return False
    
    def test_global_stats(self):
        """Test global statistics"""
        response = self.make_request("GET", "/stats/global")
        
        if response and response.status_code == 200:
            result = response.json()
            expected_fields = ["total_users", "total_problems", "total_submissions", "total_hackathons"]
            if all(field in result for field in expected_fields):
                self.log_result("Global Stats", True, 
                              f"Users: {result['total_users']}, Problems: {result['total_problems']}, Submissions: {result['total_submissions']}")
                return True
            else:
                missing = [f for f in expected_fields if f not in result]
                self.log_result("Global Stats", False, f"Missing fields: {missing}")
        else:
            error_msg = response.text if response else "No response"
            self.log_result("Global Stats", False, f"Get global stats failed: {error_msg}")
        return False
    
    def run_all_tests(self):
        """Run comprehensive test suite"""
        print("🚀 Starting CodeChain Backend API Tests")
        print(f"📍 Testing against: {BASE_URL}")
        print(f"👤 Test user: {TEST_USER_EMAIL}")
        print("=" * 60)
        
        # Authentication flow
        if not self.test_auth_register():
            print("❌ Registration failed, cannot continue with authenticated tests")
            return
            
        self.test_auth_login()
        self.test_auth_me()
        
        # Problems API
        self.test_problems_list()
        problem_id = self.test_problem_detail()
        
        # Submissions (requires problem_id)
        if problem_id:
            self.test_submission_create(problem_id)
        self.test_submissions_list()
        
        # Leaderboard
        self.test_leaderboard()
        
        # Subscriptions
        self.test_subscription_plans()
        self.test_subscription_current()
        self.test_subscription_upgrade()
        
        # Certificates (test after upgrade)
        self.test_certificates_list()
        self.test_certificate_mint()
        
        # Hackathons
        self.test_hackathons_list()
        self.test_hackathon_detail()
        
        # Statistics
        self.test_dashboard_stats()
        self.test_global_stats()
        
        # Summary
        self.print_summary()
    
    def print_summary(self):
        """Print test results summary"""
        print("\n" + "=" * 60)
        print("📊 TEST RESULTS SUMMARY")
        print("=" * 60)
        
        passed = sum(1 for result in self.test_results if result["success"])
        total = len(self.test_results)
        
        print(f"✅ Passed: {passed}/{total} ({passed/total*100:.1f}%)")
        
        failed_tests = [result for result in self.test_results if not result["success"]]
        if failed_tests:
            print(f"❌ Failed: {len(failed_tests)}")
            print("\nFailed Tests:")
            for test in failed_tests:
                print(f"  • {test['test']}: {test['details']}")
        
        print(f"\n🔗 Backend URL: {BASE_URL}")
        print(f"👤 Test User ID: {self.user_id}")
        print(f"🔑 Auth Token: {'✅ Valid' if self.auth_token else '❌ Missing'}")

if __name__ == "__main__":
    tester = CodeChainAPITester()
    tester.run_all_tests()