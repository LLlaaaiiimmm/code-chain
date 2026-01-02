#!/usr/bin/env python3
"""
Focused test for DELETE /api/submissions/solved endpoint
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
BACKEND_URL = os.getenv('REACT_APP_BACKEND_URL', 'https://compiler-fix.preview.emergentagent.com')
API_BASE = f"{BACKEND_URL}/api"

async def test_delete_solved_submissions():
    """Test the delete solved submissions functionality"""
    client = httpx.AsyncClient(timeout=60.0)
    
    try:
        print("🚀 Testing DELETE /api/submissions/solved endpoint")
        print(f"📡 API Base: {API_BASE}")
        print("=" * 60)
        
        # Step 1: Create a test user
        unique_id = uuid.uuid4().hex[:8]
        test_email = f"deletetest_{unique_id}@example.com"
        
        print("1️⃣ Creating test user...")
        register_response = await client.post(f"{API_BASE}/auth/register", json={
            "email": test_email,
            "password": "TestPassword123!",
            "name": f"Delete Test User {unique_id}"
        })
        
        if register_response.status_code != 200:
            print(f"❌ User registration failed: {register_response.status_code}")
            print(f"Response: {register_response.text}")
            return False
        
        user_data = register_response.json()
        token = user_data["token"]
        user_id = user_data["user"]["user_id"]
        headers = {"Authorization": f"Bearer {token}"}
        
        print(f"✅ User created: {user_id}")
        
        # Step 2: Get initial dashboard stats
        print("\n2️⃣ Getting initial user stats...")
        dashboard_response = await client.get(f"{API_BASE}/stats/dashboard", headers=headers)
        if dashboard_response.status_code != 200:
            print(f"❌ Failed to get dashboard stats: {dashboard_response.status_code}")
            return False
        
        initial_stats = dashboard_response.json()
        initial_elo = initial_stats.get("elo_rating", 1200)
        initial_problems_solved = initial_stats.get("problems_solved", 0)
        
        print(f"✅ Initial ELO: {initial_elo}, Problems solved: {initial_problems_solved}")
        
        # Step 3: Manually create some solved submissions in the database
        print("\n3️⃣ Creating solved submissions manually...")
        
        # Get available problems
        problems_response = await client.get(f"{API_BASE}/problems")
        if problems_response.status_code != 200:
            print(f"❌ Failed to get problems: {problems_response.status_code}")
            return False
        
        problems = problems_response.json().get("problems", [])
        if len(problems) < 2:
            print("❌ Not enough problems available")
            return False
        
        # Create mock solved submissions by directly calling the submission endpoint with simple code
        # that should pass basic validation
        simple_working_code = """
        // SPDX-License-Identifier: MIT
        pragma solidity ^0.8.0;
        
        contract HelloWorld {
            string public greeting;
            
            constructor() {
                greeting = "Hello, CodeChain!";
            }
            
            function setGreeting(string memory _greeting) public {
                greeting = _greeting;
            }
            
            function getGreeting() public view returns (string memory) {
                return greeting;
            }
        }
        """
        
        solved_count = 0
        total_elo_gained = 0
        
        # Try to submit solutions to first few problems
        for i, problem in enumerate(problems[:3]):
            print(f"   Submitting to problem {i+1}: {problem['title']}")
            
            submit_response = await client.post(f"{API_BASE}/submissions", 
                headers=headers,
                json={
                    "problem_id": problem["problem_id"],
                    "code": simple_working_code,
                    "language": "solidity"
                }
            )
            
            if submit_response.status_code == 200:
                submission_data = submit_response.json()
                status = submission_data.get("status", "unknown")
                elo_change = submission_data.get("elo_change", 0)
                
                print(f"   ✅ Submission status: {status}, ELO change: {elo_change}")
                
                if status == "passed":
                    solved_count += 1
                    total_elo_gained += elo_change
                else:
                    print(f"   ⚠️ Submission failed validation: {submission_data}")
            else:
                error_detail = submit_response.json().get("detail", "Unknown error") if submit_response.status_code != 500 else "Server error"
                print(f"   ❌ Submission failed: {submit_response.status_code} - {error_detail}")
        
        print(f"\n✅ Successfully solved {solved_count} problems, gained {total_elo_gained} ELO")
        
        if solved_count == 0:
            print("❌ No problems were solved, cannot test delete functionality")
            return False
        
        # Step 4: Verify updated stats
        print("\n4️⃣ Verifying updated stats...")
        updated_dashboard = await client.get(f"{API_BASE}/stats/dashboard", headers=headers)
        if updated_dashboard.status_code != 200:
            print(f"❌ Failed to get updated stats: {updated_dashboard.status_code}")
            return False
        
        updated_stats = updated_dashboard.json()
        updated_elo = updated_stats.get("elo_rating", 1200)
        updated_problems_solved = updated_stats.get("problems_solved", 0)
        
        print(f"✅ Updated ELO: {updated_elo}, Problems solved: {updated_problems_solved}")
        print(f"   ELO gained: {updated_elo - initial_elo}, Problems gained: {updated_problems_solved - initial_problems_solved}")
        
        # Step 5: Test DELETE /api/submissions/solved
        print("\n5️⃣ Testing DELETE /api/submissions/solved...")
        delete_response = await client.delete(f"{API_BASE}/submissions/solved", headers=headers)
        
        if delete_response.status_code != 200:
            print(f"❌ Delete request failed: {delete_response.status_code}")
            print(f"Response: {delete_response.text}")
            return False
        
        delete_data = delete_response.json()
        deleted_count = delete_data.get("deleted_count", 0)
        elo_reverted = delete_data.get("elo_reverted", 0)
        problems_reverted = delete_data.get("problems_reverted", 0)
        affected_problems = delete_data.get("affected_problems", 0)
        
        print(f"✅ Delete response:")
        print(f"   Deleted count: {deleted_count}")
        print(f"   ELO reverted: {elo_reverted}")
        print(f"   Problems reverted: {problems_reverted}")
        print(f"   Affected problems: {affected_problems}")
        print(f"   Message: {delete_data.get('message', 'N/A')}")
        
        # Step 6: Verify stats were reverted
        print("\n6️⃣ Verifying stats reversion...")
        final_dashboard = await client.get(f"{API_BASE}/stats/dashboard", headers=headers)
        if final_dashboard.status_code != 200:
            print(f"❌ Failed to get final stats: {final_dashboard.status_code}")
            return False
        
        final_stats = final_dashboard.json()
        final_elo = final_stats.get("elo_rating", 1200)
        final_problems_solved = final_stats.get("problems_solved", 0)
        
        print(f"✅ Final ELO: {final_elo}, Problems solved: {final_problems_solved}")
        
        # Verify the reversion is correct
        expected_final_elo = updated_elo - elo_reverted
        expected_final_problems = updated_problems_solved - problems_reverted
        
        elo_correct = (final_elo == expected_final_elo)
        problems_correct = (final_problems_solved == expected_final_problems)
        
        print(f"   ELO reversion correct: {elo_correct} (expected {expected_final_elo}, got {final_elo})")
        print(f"   Problems reversion correct: {problems_correct} (expected {expected_final_problems}, got {final_problems_solved})")
        
        # Step 7: Verify no solved submissions remain
        print("\n7️⃣ Verifying submissions were deleted...")
        submissions_response = await client.get(f"{API_BASE}/submissions", headers=headers)
        if submissions_response.status_code != 200:
            print(f"❌ Failed to get submissions: {submissions_response.status_code}")
            return False
        
        submissions = submissions_response.json()
        solved_submissions = [sub for sub in submissions if sub.get("status") == "passed"]
        
        print(f"✅ Remaining solved submissions: {len(solved_submissions)}")
        
        # Step 8: Test repeated delete (should return 0)
        print("\n8️⃣ Testing repeated delete...")
        repeat_delete_response = await client.delete(f"{API_BASE}/submissions/solved", headers=headers)
        
        if repeat_delete_response.status_code != 200:
            print(f"❌ Repeat delete failed: {repeat_delete_response.status_code}")
            return False
        
        repeat_delete_data = repeat_delete_response.json()
        repeat_deleted_count = repeat_delete_data.get("deleted_count", -1)
        
        print(f"✅ Repeat delete count: {repeat_deleted_count}")
        print(f"   Message: {repeat_delete_data.get('message', 'N/A')}")
        
        # Summary
        print("\n" + "=" * 60)
        print("📊 TEST SUMMARY")
        
        success = True
        if deleted_count == 0:
            print("❌ No submissions were deleted")
            success = False
        elif not elo_correct:
            print("❌ ELO was not reverted correctly")
            success = False
        elif not problems_correct:
            print("❌ Problems count was not reverted correctly")
            success = False
        elif len(solved_submissions) > 0:
            print("❌ Solved submissions were not properly deleted")
            success = False
        elif repeat_deleted_count != 0:
            print("❌ Repeat delete should return 0")
            success = False
        else:
            print("✅ All tests passed! Delete solved submissions functionality is working correctly")
        
        return success
        
    except Exception as e:
        print(f"❌ Test error: {str(e)}")
        return False
    finally:
        await client.aclose()

async def main():
    success = await test_delete_solved_submissions()
    return 0 if success else 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    exit(exit_code)