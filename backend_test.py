#!/usr/bin/env python3

import requests
import sys
import json
from datetime import datetime
import time

class CodeChainAPITester:
    def __init__(self, base_url="https://web3-academy-4.preview.emergentagent.com"):
        self.base_url = base_url
        self.api_url = f"{base_url}/api"
        self.token = None
        self.user_id = None
        self.tests_run = 0
        self.tests_passed = 0
        self.failed_tests = []
        self.session = requests.Session()
        
        # Test user credentials
        self.test_email = f"test_user_{int(time.time())}@example.com"
        self.test_password = "TestPass123!"
        self.test_name = "Test User"

    def log_test(self, name, success, details=""):
        """Log test result"""
        self.tests_run += 1
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} - {name}")
        if details:
            print(f"    {details}")
        
        if success:
            self.tests_passed += 1
        else:
            self.failed_tests.append({"name": name, "details": details})

    def test_health_check(self):
        """Test if backend is accessible"""
        try:
            response = self.session.get(f"{self.base_url}/", timeout=10)
            success = response.status_code in [200, 404]  # 404 is ok for root endpoint
            self.log_test("Backend Health Check", success, f"Status: {response.status_code}")
            return success
        except Exception as e:
            self.log_test("Backend Health Check", False, f"Error: {str(e)}")
            return False

    def test_register(self):
        """Test user registration"""
        try:
            data = {
                "email": self.test_email,
                "password": self.test_password,
                "name": self.test_name
            }
            response = self.session.post(f"{self.api_url}/auth/register", json=data, timeout=10)
            
            if response.status_code == 200:
                result = response.json()
                self.token = result.get("token")
                self.user_id = result.get("user", {}).get("user_id")
                success = bool(self.token and self.user_id)
                self.log_test("User Registration", success, f"Token: {'✓' if self.token else '✗'}, User ID: {self.user_id}")
                return success
            else:
                self.log_test("User Registration", False, f"Status: {response.status_code}, Response: {response.text[:200]}")
                return False
        except Exception as e:
            self.log_test("User Registration", False, f"Error: {str(e)}")
            return False

    def test_login(self):
        """Test user login"""
        try:
            data = {
                "email": self.test_email,
                "password": self.test_password
            }
            response = self.session.post(f"{self.api_url}/auth/login", json=data, timeout=10)
            
            if response.status_code == 200:
                result = response.json()
                token = result.get("token")
                user_id = result.get("user", {}).get("user_id")
                success = bool(token and user_id)
                self.log_test("User Login", success, f"Token: {'✓' if token else '✗'}")
                return success
            else:
                self.log_test("User Login", False, f"Status: {response.status_code}, Response: {response.text[:200]}")
                return False
        except Exception as e:
            self.log_test("User Login", False, f"Error: {str(e)}")
            return False

    def test_auth_me(self):
        """Test getting current user info"""
        if not self.token:
            self.log_test("Auth Me", False, "No token available")
            return False
            
        try:
            headers = {"Authorization": f"Bearer {self.token}"}
            response = self.session.get(f"{self.api_url}/auth/me", headers=headers, timeout=10)
            
            success = response.status_code == 200
            if success:
                user_data = response.json()
                has_required_fields = all(field in user_data for field in ["user_id", "email", "name"])
                success = has_required_fields
                self.log_test("Auth Me", success, f"User data: {user_data.get('name', 'N/A')}")
            else:
                self.log_test("Auth Me", False, f"Status: {response.status_code}")
            return success
        except Exception as e:
            self.log_test("Auth Me", False, f"Error: {str(e)}")
            return False

    def test_problems_list(self):
        """Test getting problems list"""
        try:
            response = self.session.get(f"{self.api_url}/problems", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                has_problems = "problems" in data and isinstance(data["problems"], list)
                has_total = "total" in data
                success = has_problems and has_total
                self.log_test("Problems List", success, f"Found {len(data.get('problems', []))} problems, Total: {data.get('total', 0)}")
                return success
            else:
                self.log_test("Problems List", False, f"Status: {response.status_code}")
                return False
        except Exception as e:
            self.log_test("Problems List", False, f"Error: {str(e)}")
            return False

    def test_problems_filters(self):
        """Test problems with filters"""
        try:
            # Test difficulty filter
            response = self.session.get(f"{self.api_url}/problems?difficulty=junior", timeout=10)
            success = response.status_code == 200
            
            if success:
                data = response.json()
                junior_count = len(data.get("problems", []))
                self.log_test("Problems Filter (Difficulty)", success, f"Junior problems: {junior_count}")
            else:
                self.log_test("Problems Filter (Difficulty)", False, f"Status: {response.status_code}")
            
            # Test category filter
            response = self.session.get(f"{self.api_url}/problems?category=solidity", timeout=10)
            success = response.status_code == 200
            
            if success:
                data = response.json()
                solidity_count = len(data.get("problems", []))
                self.log_test("Problems Filter (Category)", success, f"Solidity problems: {solidity_count}")
            else:
                self.log_test("Problems Filter (Category)", False, f"Status: {response.status_code}")
                
            return success
        except Exception as e:
            self.log_test("Problems Filter", False, f"Error: {str(e)}")
            return False

    def test_single_problem(self):
        """Test getting a single problem"""
        try:
            # First get problems list to get a problem ID
            response = self.session.get(f"{self.api_url}/problems", timeout=10)
            if response.status_code != 200:
                self.log_test("Single Problem", False, "Could not get problems list")
                return False
                
            problems = response.json().get("problems", [])
            if not problems:
                self.log_test("Single Problem", False, "No problems available")
                return False
                
            problem_id = problems[0]["problem_id"]
            
            # Test getting single problem
            response = self.session.get(f"{self.api_url}/problems/{problem_id}", timeout=10)
            success = response.status_code == 200
            
            if success:
                problem = response.json()
                has_required_fields = all(field in problem for field in ["problem_id", "title", "description", "difficulty"])
                success = has_required_fields
                self.log_test("Single Problem", success, f"Problem: {problem.get('title', 'N/A')}")
            else:
                self.log_test("Single Problem", False, f"Status: {response.status_code}")
            return success
        except Exception as e:
            self.log_test("Single Problem", False, f"Error: {str(e)}")
            return False

    def test_submission(self):
        """Test code submission"""
        if not self.token:
            self.log_test("Code Submission", False, "No token available")
            return False
            
        try:
            # Get a problem first
            response = self.session.get(f"{self.api_url}/problems", timeout=10)
            if response.status_code != 200:
                self.log_test("Code Submission", False, "Could not get problems")
                return False
                
            problems = response.json().get("problems", [])
            if not problems:
                self.log_test("Code Submission", False, "No problems available")
                return False
                
            problem_id = problems[0]["problem_id"]
            
            # Submit code
            headers = {"Authorization": f"Bearer {self.token}"}
            data = {
                "problem_id": problem_id,
                "code": "// Test submission\ncontract Test { function test() public {} }",
                "language": "solidity"
            }
            
            response = self.session.post(f"{self.api_url}/submissions", json=data, headers=headers, timeout=15)
            success = response.status_code == 200
            
            if success:
                result = response.json()
                has_required_fields = all(field in result for field in ["submission_id", "status", "test_results"])
                success = has_required_fields
                self.log_test("Code Submission", success, f"Status: {result.get('status', 'N/A')}, Tests: {len(result.get('test_results', []))}")
            else:
                self.log_test("Code Submission", False, f"Status: {response.status_code}, Response: {response.text[:200]}")
            return success
        except Exception as e:
            self.log_test("Code Submission", False, f"Error: {str(e)}")
            return False

    def test_leaderboard(self):
        """Test leaderboard endpoint"""
        try:
            response = self.session.get(f"{self.api_url}/leaderboard", timeout=10)
            success = response.status_code == 200
            
            if success:
                leaderboard = response.json()
                is_list = isinstance(leaderboard, list)
                success = is_list
                self.log_test("Leaderboard", success, f"Found {len(leaderboard) if is_list else 0} entries")
            else:
                self.log_test("Leaderboard", False, f"Status: {response.status_code}")
            return success
        except Exception as e:
            self.log_test("Leaderboard", False, f"Error: {str(e)}")
            return False

    def test_hackathons(self):
        """Test hackathons endpoint"""
        try:
            response = self.session.get(f"{self.api_url}/hackathons", timeout=10)
            success = response.status_code == 200
            
            if success:
                hackathons = response.json()
                is_list = isinstance(hackathons, list)
                success = is_list
                self.log_test("Hackathons", success, f"Found {len(hackathons) if is_list else 0} hackathons")
            else:
                self.log_test("Hackathons", False, f"Status: {response.status_code}")
            return success
        except Exception as e:
            self.log_test("Hackathons", False, f"Error: {str(e)}")
            return False

    def test_dashboard_stats(self):
        """Test dashboard stats endpoint"""
        if not self.token:
            self.log_test("Dashboard Stats", False, "No token available")
            return False
            
        try:
            headers = {"Authorization": f"Bearer {self.token}"}
            response = self.session.get(f"{self.api_url}/stats/dashboard", headers=headers, timeout=10)
            success = response.status_code == 200
            
            if success:
                stats = response.json()
                has_required_fields = all(field in stats for field in ["elo_rating", "problems_solved", "rank"])
                success = has_required_fields
                self.log_test("Dashboard Stats", success, f"ELO: {stats.get('elo_rating', 'N/A')}, Solved: {stats.get('problems_solved', 'N/A')}")
            else:
                self.log_test("Dashboard Stats", False, f"Status: {response.status_code}")
            return success
        except Exception as e:
            self.log_test("Dashboard Stats", False, f"Error: {str(e)}")
            return False

    def test_seed_data(self):
        """Test seed data endpoint"""
        try:
            response = self.session.post(f"{self.api_url}/seed", timeout=15)
            success = response.status_code == 200
            
            if success:
                result = response.json()
                has_message = "message" in result
                success = has_message
                self.log_test("Seed Data", success, f"Message: {result.get('message', 'N/A')}")
            else:
                self.log_test("Seed Data", False, f"Status: {response.status_code}")
            return success
        except Exception as e:
            self.log_test("Seed Data", False, f"Error: {str(e)}")
            return False

    def run_all_tests(self):
        """Run all backend tests"""
        print("🚀 Starting CodeChain Backend API Tests")
        print(f"📍 Testing: {self.base_url}")
        print("=" * 60)
        
        # Basic connectivity
        if not self.test_health_check():
            print("❌ Backend not accessible, stopping tests")
            return False
            
        # Seed data first
        self.test_seed_data()
        
        # Authentication flow
        auth_success = self.test_register()
        if auth_success:
            self.test_login()
            self.test_auth_me()
            
        # Public endpoints
        self.test_problems_list()
        self.test_problems_filters()
        self.test_single_problem()
        self.test_leaderboard()
        self.test_hackathons()
        
        # Protected endpoints
        if auth_success:
            self.test_submission()
            self.test_dashboard_stats()
        
        # Summary
        print("=" * 60)
        print(f"📊 Test Results: {self.tests_passed}/{self.tests_run} passed")
        success_rate = (self.tests_passed / self.tests_run * 100) if self.tests_run > 0 else 0
        print(f"📈 Success Rate: {success_rate:.1f}%")
        
        if self.failed_tests:
            print("\n❌ Failed Tests:")
            for test in self.failed_tests:
                print(f"  - {test['name']}: {test['details']}")
        
        return success_rate >= 80  # Consider 80%+ success rate as passing

def main():
    tester = CodeChainAPITester()
    success = tester.run_all_tests()
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())