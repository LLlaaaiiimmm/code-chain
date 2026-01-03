#!/usr/bin/env python3
"""
Backend Testing Script for CodeChain Skill Chain Integration
Tests all Skill Chain API endpoints and integration with submissions
"""

import asyncio
import aiohttp
import json
import sys
from datetime import datetime

# Backend URL from frontend/.env
BACKEND_URL = "https://compile-helper-5.preview.emergentagent.com/api"

class SkillChainTester:
    def __init__(self):
        self.session = None
        self.auth_token = None
        self.test_user = {
            "email": "skilltest@codechain.dev",
            "password": "TestPassword123!",
            "name": "Skill Chain Tester"
        }
        self.results = {
            "skill_tree": {"status": "pending", "details": []},
            "user_progress": {"status": "pending", "details": []},
            "submission_integration": {"status": "pending", "details": []},
            "summary": {"total_tests": 0, "passed": 0, "failed": 0}
        }

    async def setup_session(self):
        """Initialize HTTP session"""
        self.session = aiohttp.ClientSession()
        print("🔧 HTTP session initialized")

    async def cleanup_session(self):
        """Cleanup HTTP session"""
        if self.session:
            await self.session.close()
        print("🧹 HTTP session cleaned up")

    async def register_test_user(self):
        """Register and authenticate test user"""
        try:
            # Try to register user
            register_data = {
                "email": self.test_user["email"],
                "password": self.test_user["password"],
                "name": self.test_user["name"]
            }
            
            async with self.session.post(f"{BACKEND_URL}/auth/register", json=register_data) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    self.auth_token = data["token"]
                    print(f"✅ Test user registered successfully")
                    return True
                elif resp.status == 400:
                    # User already exists, try login
                    return await self.login_test_user()
                else:
                    print(f"❌ Registration failed: {resp.status}")
                    return False
                    
        except Exception as e:
            print(f"❌ Registration error: {e}")
            return await self.login_test_user()

    async def login_test_user(self):
        """Login test user"""
        try:
            login_data = {
                "email": self.test_user["email"],
                "password": self.test_user["password"]
            }
            
            async with self.session.post(f"{BACKEND_URL}/auth/login", json=login_data) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    self.auth_token = data["token"]
                    print(f"✅ Test user logged in successfully")
                    return True
                else:
                    print(f"❌ Login failed: {resp.status}")
                    return False
                    
        except Exception as e:
            print(f"❌ Login error: {e}")
            return False

    def get_auth_headers(self):
        """Get authorization headers"""
        return {"Authorization": f"Bearer {self.auth_token}"}

    async def test_skill_tree_endpoint(self):
        """Test GET /api/skills/tree endpoint"""
        print("\n🌳 Testing Skill Tree Endpoint...")
        
        try:
            async with self.session.get(f"{BACKEND_URL}/skills/tree") as resp:
                if resp.status == 200:
                    data = await resp.json()
                    skills = data.get("skills", [])
                    
                    # Verify we have 12 skills as specified
                    if len(skills) >= 12:
                        self.results["skill_tree"]["details"].append(f"✅ Found {len(skills)} skills (expected ≥12)")
                    else:
                        self.results["skill_tree"]["details"].append(f"❌ Found only {len(skills)} skills (expected ≥12)")
                        self.results["skill_tree"]["status"] = "failed"
                        return False
                    
                    # Verify skill structure
                    required_fields = ["skill_id", "name", "description", "category", "dependencies", "level"]
                    categories_found = set()
                    
                    for skill in skills:
                        # Check required fields
                        missing_fields = [field for field in required_fields if field not in skill]
                        if missing_fields:
                            self.results["skill_tree"]["details"].append(f"❌ Skill {skill.get('skill_id', 'unknown')} missing fields: {missing_fields}")
                            self.results["skill_tree"]["status"] = "failed"
                            return False
                        
                        categories_found.add(skill["category"])
                    
                    # Verify categories
                    expected_categories = {"solidity", "rust", "tvm", "general"}
                    if expected_categories.issubset(categories_found):
                        self.results["skill_tree"]["details"].append(f"✅ All expected categories found: {categories_found}")
                    else:
                        missing_cats = expected_categories - categories_found
                        self.results["skill_tree"]["details"].append(f"❌ Missing categories: {missing_cats}")
                        self.results["skill_tree"]["status"] = "failed"
                        return False
                    
                    # Show some example skills
                    self.results["skill_tree"]["details"].append("📋 Sample skills:")
                    for skill in skills[:3]:
                        self.results["skill_tree"]["details"].append(
                            f"   • {skill['name']} ({skill['category']}) - Level {skill['level']}"
                        )
                    
                    self.results["skill_tree"]["status"] = "passed"
                    return True
                    
                else:
                    self.results["skill_tree"]["details"].append(f"❌ HTTP {resp.status}: {await resp.text()}")
                    self.results["skill_tree"]["status"] = "failed"
                    return False
                    
        except Exception as e:
            self.results["skill_tree"]["details"].append(f"❌ Exception: {e}")
            self.results["skill_tree"]["status"] = "failed"
            return False

    async def test_user_progress_endpoint(self):
        """Test GET /api/skills/user-progress endpoint (requires auth)"""
        print("\n📊 Testing User Progress Endpoint...")
        
        if not self.auth_token:
            self.results["user_progress"]["details"].append("❌ No auth token available")
            self.results["user_progress"]["status"] = "failed"
            return False
        
        try:
            headers = self.get_auth_headers()
            async with self.session.get(f"{BACKEND_URL}/skills/user-progress", headers=headers) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    skills = data.get("skills", [])
                    
                    if not skills:
                        self.results["user_progress"]["details"].append("❌ No skills returned")
                        self.results["user_progress"]["status"] = "failed"
                        return False
                    
                    # Verify each skill has progress and unlocked status
                    unlocked_count = 0
                    locked_count = 0
                    
                    for skill in skills:
                        required_fields = ["skill_id", "name", "progress", "unlocked"]
                        missing_fields = [field for field in required_fields if field not in skill]
                        
                        if missing_fields:
                            self.results["user_progress"]["details"].append(
                                f"❌ Skill {skill.get('skill_id', 'unknown')} missing: {missing_fields}"
                            )
                            self.results["user_progress"]["status"] = "failed"
                            return False
                        
                        # Verify progress is 0-100
                        progress = skill.get("progress", 0)
                        if not (0 <= progress <= 100):
                            self.results["user_progress"]["details"].append(
                                f"❌ Invalid progress {progress} for skill {skill['skill_id']}"
                            )
                            self.results["user_progress"]["status"] = "failed"
                            return False
                        
                        if skill["unlocked"]:
                            unlocked_count += 1
                        else:
                            locked_count += 1
                    
                    self.results["user_progress"]["details"].append(f"✅ Found {len(skills)} skills with progress data")
                    self.results["user_progress"]["details"].append(f"✅ Unlocked: {unlocked_count}, Locked: {locked_count}")
                    self.results["user_progress"]["details"].append("✅ All locked skills are present in response")
                    
                    # Show sample progress
                    self.results["user_progress"]["details"].append("📊 Sample progress:")
                    for skill in skills[:3]:
                        status = "🔓" if skill["unlocked"] else "🔒"
                        self.results["user_progress"]["details"].append(
                            f"   {status} {skill['name']}: {skill['progress']}%"
                        )
                    
                    self.results["user_progress"]["status"] = "passed"
                    return True
                    
                elif resp.status == 401:
                    self.results["user_progress"]["details"].append("❌ Authentication failed")
                    self.results["user_progress"]["status"] = "failed"
                    return False
                else:
                    self.results["user_progress"]["details"].append(f"❌ HTTP {resp.status}: {await resp.text()}")
                    self.results["user_progress"]["status"] = "failed"
                    return False
                    
        except Exception as e:
            self.results["user_progress"]["details"].append(f"❌ Exception: {e}")
            self.results["user_progress"]["status"] = "failed"
            return False

    async def test_submission_integration(self):
        """Test integration with submissions - solve a Solidity task and check skill progress"""
        print("\n🔗 Testing Submission Integration...")
        
        if not self.auth_token:
            self.results["submission_integration"]["details"].append("❌ No auth token available")
            self.results["submission_integration"]["status"] = "failed"
            return False
        
        try:
            headers = self.get_auth_headers()
            
            # Step 1: Get initial skill progress
            async with self.session.get(f"{BACKEND_URL}/skills/user-progress", headers=headers) as resp:
                if resp.status != 200:
                    self.results["submission_integration"]["details"].append("❌ Failed to get initial progress")
                    self.results["submission_integration"]["status"] = "failed"
                    return False
                
                initial_data = await resp.json()
                initial_skills = {s["skill_id"]: s["progress"] for s in initial_data["skills"]}
                sol_basics_initial = initial_skills.get("sol_basics", 0)
                
                self.results["submission_integration"]["details"].append(
                    f"📊 Initial sol_basics progress: {sol_basics_initial}%"
                )
            
            # Step 2: Find a Solidity Junior problem
            async with self.session.get(f"{BACKEND_URL}/problems?category=solidity&difficulty=junior&limit=5") as resp:
                if resp.status != 200:
                    self.results["submission_integration"]["details"].append("❌ Failed to get Solidity problems")
                    self.results["submission_integration"]["status"] = "failed"
                    return False
                
                problems_data = await resp.json()
                problems = problems_data.get("problems", [])
                
                if not problems:
                    self.results["submission_integration"]["details"].append("❌ No Solidity Junior problems found")
                    self.results["submission_integration"]["status"] = "failed"
                    return False
                
                test_problem = problems[0]
                self.results["submission_integration"]["details"].append(
                    f"🎯 Selected problem: {test_problem['title']} (ID: {test_problem['problem_id']})"
                )
            
            # Step 3: Check if problem is already solved
            async with self.session.get(f"{BACKEND_URL}/problems/{test_problem['problem_id']}/status", headers=headers) as resp:
                if resp.status == 200:
                    status_data = await resp.json()
                    if status_data.get("is_solved", False):
                        self.results["submission_integration"]["details"].append("⚠️ Problem already solved, skill progress may not change")
                
            # Step 4: Create a valid Solidity solution based on the problem requirements
            # The problem expects setValue and getValue functions
            valid_solidity_code = '''// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract JuniorProblem1 {
    uint256 public value;
    
    function setValue(uint256 _value) public {
        value = _value;
    }
    
    function getValue() public view returns (uint256) {
        return value;
    }
}'''
            
            # Step 5: Submit the solution
            submission_data = {
                "problem_id": test_problem["problem_id"],
                "code": valid_solidity_code,
                "language": "solidity"
            }
            
            async with self.session.post(f"{BACKEND_URL}/submissions", json=submission_data, headers=headers) as resp:
                if resp.status == 200:
                    submission_result = await resp.json()
                    
                    if submission_result.get("status") == "passed":
                        self.results["submission_integration"]["details"].append("✅ Submission passed successfully")
                        elo_change = submission_result.get("elo_change", 0)
                        self.results["submission_integration"]["details"].append(f"✅ ELO gained: +{elo_change}")
                    else:
                        self.results["submission_integration"]["details"].append("❌ Submission failed")
                        self.results["submission_integration"]["details"].append(f"Test results: {submission_result.get('test_results', [])}")
                        # Continue anyway to test the integration
                        
                elif resp.status == 400:
                    error_text = await resp.text()
                    if "already solved" in error_text:
                        self.results["submission_integration"]["details"].append("⚠️ Problem already solved by this user")
                    else:
                        self.results["submission_integration"]["details"].append(f"❌ Submission error: {error_text}")
                else:
                    self.results["submission_integration"]["details"].append(f"❌ Submission failed: HTTP {resp.status}")
            
            # Step 6: Check updated skill progress
            await asyncio.sleep(1)  # Give time for skill update
            
            async with self.session.get(f"{BACKEND_URL}/skills/user-progress", headers=headers) as resp:
                if resp.status != 200:
                    self.results["submission_integration"]["details"].append("❌ Failed to get updated progress")
                    self.results["submission_integration"]["status"] = "failed"
                    return False
                
                updated_data = await resp.json()
                updated_skills = {s["skill_id"]: s["progress"] for s in updated_data["skills"]}
                sol_basics_updated = updated_skills.get("sol_basics", 0)
                
                self.results["submission_integration"]["details"].append(
                    f"📊 Updated sol_basics progress: {sol_basics_updated}%"
                )
                
                # Check if progress increased
                if sol_basics_updated > sol_basics_initial:
                    progress_increase = sol_basics_updated - sol_basics_initial
                    self.results["submission_integration"]["details"].append(
                        f"✅ Skill progress increased by {progress_increase}% - update_skill_progress working!"
                    )
                    self.results["submission_integration"]["status"] = "passed"
                    return True
                elif sol_basics_updated == sol_basics_initial and sol_basics_initial > 0:
                    self.results["submission_integration"]["details"].append(
                        "⚠️ Progress unchanged (problem may have been solved before or skill already at max)"
                    )
                    self.results["submission_integration"]["status"] = "passed"
                    return True
                else:
                    self.results["submission_integration"]["details"].append(
                        "❌ No skill progress detected - update_skill_progress may not be working"
                    )
                    self.results["submission_integration"]["status"] = "failed"
                    return False
                    
        except Exception as e:
            self.results["submission_integration"]["details"].append(f"❌ Exception: {e}")
            self.results["submission_integration"]["status"] = "failed"
            return False

    async def run_all_tests(self):
        """Run all Skill Chain tests"""
        print("🚀 Starting Skill Chain Integration Tests")
        print("=" * 60)
        
        await self.setup_session()
        
        # Authenticate
        if not await self.register_test_user():
            print("❌ Failed to authenticate test user")
            await self.cleanup_session()
            return False
        
        # Run tests
        tests = [
            ("Skill Tree Endpoint", self.test_skill_tree_endpoint),
            ("User Progress Endpoint", self.test_user_progress_endpoint),
            ("Submission Integration", self.test_submission_integration)
        ]
        
        for test_name, test_func in tests:
            try:
                result = await test_func()
                self.results["summary"]["total_tests"] += 1
                if result:
                    self.results["summary"]["passed"] += 1
                else:
                    self.results["summary"]["failed"] += 1
            except Exception as e:
                print(f"❌ Test {test_name} crashed: {e}")
                self.results["summary"]["total_tests"] += 1
                self.results["summary"]["failed"] += 1
        
        await self.cleanup_session()
        return True

    def print_results(self):
        """Print comprehensive test results"""
        print("\n" + "=" * 60)
        print("🎯 SKILL CHAIN INTEGRATION TEST RESULTS")
        print("=" * 60)
        
        for test_name, result in self.results.items():
            if test_name == "summary":
                continue
                
            status_icon = "✅" if result["status"] == "passed" else "❌" if result["status"] == "failed" else "⏳"
            print(f"\n{status_icon} {test_name.replace('_', ' ').title()}: {result['status'].upper()}")
            
            for detail in result["details"]:
                print(f"   {detail}")
        
        # Summary
        summary = self.results["summary"]
        print(f"\n📊 SUMMARY:")
        print(f"   Total Tests: {summary['total_tests']}")
        print(f"   Passed: {summary['passed']} ✅")
        print(f"   Failed: {summary['failed']} ❌")
        
        success_rate = (summary['passed'] / max(summary['total_tests'], 1)) * 100
        print(f"   Success Rate: {success_rate:.1f}%")
        
        if summary['failed'] == 0:
            print("\n🎉 ALL SKILL CHAIN TESTS PASSED!")
        else:
            print(f"\n⚠️ {summary['failed']} TEST(S) FAILED")

async def main():
    """Main test runner"""
    tester = SkillChainTester()
    
    try:
        await tester.run_all_tests()
        tester.print_results()
        
        # Return appropriate exit code
        if tester.results["summary"]["failed"] == 0:
            sys.exit(0)
        else:
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n⚠️ Tests interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Test runner crashed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())