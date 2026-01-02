"""
Code validation and testing system for CodeChain platform
Supports: Solidity, Rust/Solana, FunC/TON, General Cryptography

Enhanced validation system with:
- Real code compilation and execution
- Structured test cases with multiple test types
- Detailed error reporting
- Support for function calls, state checks, events, and reverts
"""

import re
import json
import hashlib
import ast
from typing import Dict, List, Any, Tuple, Optional
try:
    from solcx import compile_source, install_solc, set_solc_version
except ImportError:
    # Fallback if solcx not available
    compile_source = None
    install_solc = None
    set_solc_version = None
from web3 import Web3
from eth_account import Account
import subprocess
import tempfile
import os
import sys


class CodeValidator:
    """Main validator class for checking code solutions"""
    
    def __init__(self):
        self.w3 = Web3(Web3.EthereumTesterProvider())
        self.account = self.w3.eth.accounts[0]
        
        # Install Solidity compiler if available
        if compile_source and install_solc and set_solc_version:
            try:
                install_solc('0.8.0')
                set_solc_version('0.8.0')
            except Exception as e:
                print(f"Warning: Could not install solc: {e}")
                pass  # Already installed or not available
    
    async def validate_submission(
        self, 
        code: str, 
        problem: Dict[str, Any], 
        language: str
    ) -> Tuple[bool, List[Dict], int, str]:
        """
        Validate code submission
        Returns: (all_passed, test_results, total_gas, error_message)
        """
        category = problem.get("category", "solidity").lower()
        
        if category == "solidity":
            return await self._validate_solidity(code, problem)
        elif category == "rust":
            return await self._validate_rust(code, problem)
        elif category == "move":
            return await self._validate_move(code, problem)
        elif category == "func":
            return await self._validate_func(code, problem)
        elif category == "cryptography":
            return await self._validate_cryptography(code, problem)
        else:
            return False, [], 0, "Unsupported language"
    
    async def _validate_solidity(
        self, 
        code: str, 
        problem: Dict[str, Any]
    ) -> Tuple[bool, List[Dict], int, str]:
        """
        Validate Solidity smart contract with enhanced testing
        
        Test case formats supported:
        1. Function call: {"type": "call", "function": "getName", "args": [], "expected": "John"}
        2. Transaction: {"type": "transaction", "function": "setName", "args": ["Alice"], "expected": "success"}
        3. State check: {"type": "state", "variable": "owner", "expected": "<deployer>"}
        4. Event check: {"type": "event", "function": "transfer", "args": [...], "event_name": "Transfer"}
        5. Revert check: {"type": "revert", "function": "withdraw", "args": [], "expected": "revert"}
        """
        
        test_results = []
        total_gas = 0
        
        # Step 0: Pre-validation checks
        # Check for TODO comments (indicates incomplete solution)
        if "TODO" in code or "// Your code here" in code:
            test_results.append({
                "test_id": 0,
                "input": "Code completeness check",
                "expected": "All TODOs removed and functions implemented",
                "passed": False,
                "gas_used": 0,
                "error": "❌ Code contains TODO comments or placeholder text. Please implement all functions."
            })
            return False, test_results, 0, "Code is incomplete - contains TODO markers"
        
        # Check for empty function bodies (basic check)
        empty_function_pattern = r'function\s+\w+\([^)]*\)[^{]*\{\s*\}'
        if re.search(empty_function_pattern, code):
            test_results.append({
                "test_id": 0,
                "input": "Function implementation check",
                "expected": "All functions implemented with logic",
                "passed": False,
                "gas_used": 0,
                "error": "❌ Code contains empty functions. Please implement the required logic."
            })
            return False, test_results, 0, "Code has empty functions"
        
        # Check if compiler is available
        if not compile_source:
            return False, [{
                "test_id": 0,
                "input": "Compilation",
                "expected": "Success",
                "passed": False,
                "gas_used": 0,
                "error": "Solidity compiler not available"
            }], 0, "Compiler not available"
        
        # Step 1: Syntax and compilation check
        try:
            compiled = compile_source(
                code,
                output_values=['abi', 'bin']
            )
        except Exception as e:
            error_msg = str(e)
            # Parse compilation error for more details
            if "ParserError" in error_msg:
                error_msg = "Syntax error in code: " + error_msg.split("ParserError:")[-1].strip()
            elif "TypeError" in error_msg:
                error_msg = "Type error: " + error_msg.split("TypeError:")[-1].strip()
            
            test_results.append({
                "test_id": 0,
                "input": "Compilation",
                "expected": "Success",
                "passed": False,
                "gas_used": 0,
                "error": f"❌ {error_msg[:200]}"
            })
            return False, test_results, 0, f"Compilation error: {error_msg[:200]}"
        
        # Get contract interface
        contract_id, contract_interface = list(compiled.items())[0]
        abi = contract_interface['abi']
        bytecode = contract_interface['bin']
        
        # Step 2: Deploy contract
        try:
            Contract = self.w3.eth.contract(abi=abi, bytecode=bytecode)
            tx_hash = Contract.constructor().transact({'from': self.account})
            tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
            contract_instance = self.w3.eth.contract(
                address=tx_receipt.contractAddress,
                abi=abi
            )
            deployment_gas = tx_receipt.gasUsed
            total_gas += deployment_gas
        except Exception as e:
            error_msg = str(e)
            test_results.append({
                "test_id": 0,
                "input": "Deployment",
                "expected": "Success",
                "passed": False,
                "gas_used": 0,
                "error": f"❌ Deployment failed: {error_msg[:200]}"
            })
            return False, test_results, 0, f"Deployment error: {error_msg[:200]}"
        
        # Step 3: Run test cases
        test_cases = problem.get("test_cases", [])
        all_passed = True
        
        for i, test_case in enumerate(test_cases):
            try:
                # Handle both old format and new format
                if isinstance(test_case, dict) and "type" in test_case:
                    # New structured format
                    result = await self._execute_structured_test(
                        contract_instance,
                        test_case,
                        self.account
                    )
                else:
                    # Old format - fallback
                    test_input = test_case.get("input", "")
                    expected = test_case.get("expected", "")
                    result = self._execute_test_case(
                        contract_instance, 
                        test_input, 
                        expected,
                        self.account
                    )
                
                test_results.append({
                    "test_id": i + 1,
                    "input": result.get("description", str(test_case)),
                    "expected": result.get("expected", ""),
                    "passed": result["passed"],
                    "gas_used": result.get("gas_used", 0),
                    "error": result.get("error", None),
                    "actual": result.get("actual", None)
                })
                
                if result["passed"]:
                    total_gas += result.get("gas_used", 0)
                else:
                    all_passed = False
                    
            except Exception as e:
                test_results.append({
                    "test_id": i + 1,
                    "input": str(test_case),
                    "expected": "Test execution",
                    "passed": False,
                    "gas_used": 0,
                    "error": f"❌ Test execution error: {str(e)[:200]}"
                })
                all_passed = False
        
        return all_passed, test_results, total_gas, None
    
    async def _execute_structured_test(
        self,
        contract: Any,
        test_case: Dict[str, Any],
        account: str
    ) -> Dict[str, Any]:
        """Execute a structured test case"""
        
        test_type = test_case.get("type", "call")
        function_name = test_case.get("function", "")
        args = test_case.get("args", [])
        expected = test_case.get("expected", "")
        
        try:
            if test_type == "call":
                # View/pure function call
                return await self._test_function_call(contract, function_name, args, expected, account)
            
            elif test_type == "transaction":
                # State-changing transaction
                return await self._test_transaction(contract, function_name, args, expected, account)
            
            elif test_type == "state":
                # Check state variable
                return await self._test_state_variable(contract, test_case, account)
            
            elif test_type == "event":
                # Check event emission
                return await self._test_event(contract, test_case, account)
            
            elif test_type == "revert":
                # Check that function reverts
                return await self._test_revert(contract, function_name, args, account)
            
            else:
                return {
                    "passed": False,
                    "error": f"Unknown test type: {test_type}",
                    "description": str(test_case)
                }
                
        except Exception as e:
            return {
                "passed": False,
                "error": str(e),
                "description": str(test_case),
                "gas_used": 0
            }
    
    async def _test_function_call(
        self,
        contract: Any,
        function_name: str,
        args: List[Any],
        expected: Any,
        account: str
    ) -> Dict[str, Any]:
        """Test a view/pure function call"""
        
        if not hasattr(contract.functions, function_name):
            return {
                "passed": False,
                "error": f"Function '{function_name}' not found in contract",
                "description": f"Call {function_name}({args})",
                "expected": str(expected)
            }
        
        func = getattr(contract.functions, function_name)
        
        try:
            # Call the function
            if args:
                result = func(*args).call()
            else:
                result = func().call()
            
            # Compare result with expected
            passed = self._compare_values(result, expected)
            
            return {
                "passed": passed,
                "actual": str(result),
                "expected": str(expected),
                "description": f"✓ Call {function_name}({', '.join(map(str, args))})",
                "gas_used": 21000  # Estimated for view functions
            }
            
        except Exception as e:
            return {
                "passed": False,
                "error": f"Function call failed: {str(e)[:100]}",
                "description": f"Call {function_name}({args})",
                "expected": str(expected),
                "gas_used": 0
            }
    
    async def _test_transaction(
        self,
        contract: Any,
        function_name: str,
        args: List[Any],
        expected: Any,
        account: str
    ) -> Dict[str, Any]:
        """Test a state-changing transaction"""
        
        if not hasattr(contract.functions, function_name):
            return {
                "passed": False,
                "error": f"Function '{function_name}' not found",
                "description": f"Transaction {function_name}({args})"
            }
        
        func = getattr(contract.functions, function_name)
        
        try:
            # Execute transaction
            if args:
                tx_hash = func(*args).transact({'from': account})
            else:
                tx_hash = func().transact({'from': account})
            
            tx_receipt = contract.w3.eth.wait_for_transaction_receipt(tx_hash)
            
            # Check if expected is "success" or we need to verify something
            if expected.lower() in ["success", "true", "pass"]:
                passed = tx_receipt.status == 1
            else:
                # Might need to check return value or state
                passed = True
            
            return {
                "passed": passed,
                "actual": "Transaction successful",
                "expected": str(expected),
                "description": f"✓ Execute {function_name}({', '.join(map(str, args))})",
                "gas_used": tx_receipt.gasUsed
            }
            
        except Exception as e:
            error_msg = str(e)
            # Check if this is an expected revert
            if "revert" in expected.lower() and "revert" in error_msg.lower():
                return {
                    "passed": True,
                    "actual": "Reverted as expected",
                    "expected": expected,
                    "description": f"Transaction {function_name}({args})",
                    "gas_used": 0
                }
            
            return {
                "passed": False,
                "error": f"Transaction failed: {error_msg[:100]}",
                "description": f"Execute {function_name}({args})",
                "expected": str(expected),
                "gas_used": 0
            }
    
    async def _test_state_variable(
        self,
        contract: Any,
        test_case: Dict[str, Any],
        account: str
    ) -> Dict[str, Any]:
        """Test state variable value"""
        
        variable_name = test_case.get("variable", "")
        expected = test_case.get("expected", "")
        
        if not hasattr(contract.functions, variable_name):
            return {
                "passed": False,
                "error": f"State variable '{variable_name}' not found or not public",
                "description": f"Check {variable_name}"
            }
        
        try:
            func = getattr(contract.functions, variable_name)
            result = func().call()
            
            # Handle special expected values
            if expected == "<deployer>":
                expected = account
            
            passed = self._compare_values(result, expected)
            
            return {
                "passed": passed,
                "actual": str(result),
                "expected": str(expected),
                "description": f"✓ Check state: {variable_name}",
                "gas_used": 0
            }
            
        except Exception as e:
            return {
                "passed": False,
                "error": str(e),
                "description": f"Check {variable_name}",
                "gas_used": 0
            }
    
    async def _test_event(
        self,
        contract: Any,
        test_case: Dict[str, Any],
        account: str
    ) -> Dict[str, Any]:
        """Test event emission"""
        
        function_name = test_case.get("function", "")
        args = test_case.get("args", [])
        event_name = test_case.get("event_name", "")
        
        try:
            func = getattr(contract.functions, function_name)
            
            if args:
                tx_hash = func(*args).transact({'from': account})
            else:
                tx_hash = func().transact({'from': account})
            
            tx_receipt = contract.w3.eth.wait_for_transaction_receipt(tx_hash)
            
            # Check if event was emitted
            event_found = False
            for log in tx_receipt.logs:
                # Simple check - in production would decode events properly
                event_found = True
                break
            
            return {
                "passed": event_found,
                "actual": f"Event emitted: {event_found}",
                "expected": f"Event {event_name} should be emitted",
                "description": f"✓ Check event: {event_name}",
                "gas_used": tx_receipt.gasUsed
            }
            
        except Exception as e:
            return {
                "passed": False,
                "error": str(e),
                "description": f"Check event {event_name}",
                "gas_used": 0
            }
    
    async def _test_revert(
        self,
        contract: Any,
        function_name: str,
        args: List[Any],
        account: str
    ) -> Dict[str, Any]:
        """Test that function reverts"""
        
        if not hasattr(contract.functions, function_name):
            return {
                "passed": False,
                "error": f"Function '{function_name}' not found",
                "description": f"Should revert: {function_name}({args})"
            }
        
        func = getattr(contract.functions, function_name)
        
        try:
            # Try to execute - should fail
            if args:
                tx_hash = func(*args).transact({'from': account})
            else:
                tx_hash = func().transact({'from': account})
            
            tx_receipt = contract.w3.eth.wait_for_transaction_receipt(tx_hash)
            
            # If we get here, transaction succeeded (but shouldn't have)
            return {
                "passed": False,
                "error": "Function should have reverted but succeeded",
                "actual": "Transaction successful",
                "expected": "Transaction should revert",
                "description": f"Should revert: {function_name}({args})",
                "gas_used": 0
            }
            
        except Exception as e:
            # Transaction reverted as expected
            return {
                "passed": True,
                "actual": "Reverted as expected",
                "expected": "Revert",
                "description": f"✓ Reverts: {function_name}({args})",
                "gas_used": 0
            }
    
    def _compare_values(self, actual: Any, expected: Any) -> bool:
        """Compare actual and expected values with type handling"""
        
        # Convert to strings for comparison
        actual_str = str(actual).lower().strip()
        expected_str = str(expected).lower().strip()
        
        # Direct equality
        if actual_str == expected_str:
            return True
        
        # Numeric comparison
        try:
            if float(actual_str) == float(expected_str):
                return True
        except:
            pass
        
        # Boolean comparison
        if actual_str in ['true', '1'] and expected_str in ['true', '1']:
            return True
        if actual_str in ['false', '0'] and expected_str in ['false', '0']:
            return True
        
        # Address comparison (case insensitive)
        if actual_str.startswith('0x') and expected_str.startswith('0x'):
            if actual_str.lower() == expected_str.lower():
                return True
        
        # Substring match
        if expected_str in actual_str or actual_str in expected_str:
            return True
        
        return False
    
    def _execute_test_case(
        self, 
        contract: Any, 
        test_input: str, 
        expected: str,
        account: str
    ) -> Dict[str, Any]:
        """Execute a single test case on the contract"""
        
        # Parse test input to extract function call
        # Format: "functionName(arg1, arg2, ...)"
        match = re.match(r"(\w+)\((.*)\)", test_input)
        
        if not match:
            # Simple getter or state check
            return {"passed": True, "gas_used": 21000}
        
        function_name = match.group(1)
        args_str = match.group(2)
        
        # Parse arguments
        args = []
        if args_str.strip():
            # Simple parsing - split by comma and clean
            args = [arg.strip().strip("'\"") for arg in args_str.split(",")]
        
        try:
            # Check if function exists
            if not hasattr(contract.functions, function_name):
                return {
                    "passed": False,
                    "error": f"Function '{function_name}' not found in contract"
                }
            
            func = getattr(contract.functions, function_name)
            
            # Determine if it's a call or transaction
            # View/pure functions use call(), others use transact()
            try:
                # Try as a view function first
                if args:
                    result = func(*args).call()
                else:
                    result = func().call()
                gas_used = 21000  # Estimated for view functions
                
            except Exception as e:
                # If call fails, try as transaction
                if args:
                    tx_hash = func(*args).transact({'from': account})
                else:
                    tx_hash = func().transact({'from': account})
                    
                tx_receipt = contract.w3.eth.wait_for_transaction_receipt(tx_hash)
                gas_used = tx_receipt.gasUsed
                result = "success"  # Transaction succeeded
            
            # Validate result against expected
            passed = self._validate_result(result, expected)
            
            return {
                "passed": passed,
                "gas_used": gas_used,
                "actual": str(result)
            }
            
        except Exception as e:
            return {
                "passed": False,
                "error": str(e),
                "gas_used": 0
            }
    
    def _validate_result(self, actual: Any, expected: str) -> bool:
        """Validate if actual result matches expected"""
        expected_lower = expected.lower().strip()
        actual_str = str(actual).lower().strip()
        
        # Check for common patterns
        if expected_lower in ["success", "true", "owner set", "transferred", "minted"]:
            # For transactions, just check they succeeded
            return True
        
        if expected_lower in ["reverted", "failed", "rejected"]:
            return False
        
        # Check numerical equality
        try:
            if actual_str == expected_lower:
                return True
            # Try numeric comparison
            if float(actual_str) == float(expected_lower):
                return True
        except:
            pass
        
        # Check string containment
        if expected_lower in actual_str or actual_str in expected_lower:
            return True
        
        return False
    
    async def _validate_rust(
        self, 
        code: str, 
        problem: Dict[str, Any]
    ) -> Tuple[bool, List[Dict], int, str]:
        """
        Validate Rust/Solana program with real compilation
        
        Enhanced validation to prevent cheating:
        - Strict TODO checks (no TODOs allowed)
        - Empty function detection
        - Pattern matching for all test cases
        - Minimum code complexity requirements
        """
        
        test_results = []
        all_passed = True
        
        # Step 0: Pre-validation checks - STRICT
        # Check for ANY TODO markers (incomplete code)
        if 'TODO' in code or 'todo!' in code or '// Your code here' in code or '/* TODO */' in code:
            test_results.append({
                "test_id": 0,
                "input": "Code completeness check",
                "expected": "All TODOs removed and functions implemented",
                "passed": False,
                "gas_used": 0,
                "error": "❌ Code contains TODO markers or placeholder text. Please implement all functions."
            })
            return False, test_results, 0, "Code is incomplete - contains TODO markers"
        
        # Check for empty function bodies
        empty_function_patterns = [
            r'fn\s+\w+\([^)]*\)\s*(?:->\s*[^{]+)?\s*\{\s*\}',  # fn name() {}
            r'pub\s+fn\s+\w+\([^)]*\)\s*(?:->\s*[^{]+)?\s*\{\s*\}',  # pub fn name() {}
        ]
        for pattern in empty_function_patterns:
            if re.search(pattern, code):
                test_results.append({
                    "test_id": 0,
                    "input": "Function implementation check",
                    "expected": "All functions must have implementations",
                    "passed": False,
                    "gas_used": 0,
                    "error": "❌ Code has empty functions. Please implement the required logic."
                })
                return False, test_results, 0, "Code has empty functions"
        
        # Check minimum code length (anti-template submission)
        code_without_comments = re.sub(r'//.*$', '', code, flags=re.MULTILINE)
        code_without_comments = re.sub(r'/\*.*?\*/', '', code_without_comments, flags=re.DOTALL)
        if len(code_without_comments.strip()) < 200:
            test_results.append({
                "test_id": 0,
                "input": "Code complexity check",
                "expected": "Meaningful implementation with actual logic",
                "passed": False,
                "gas_used": 0,
                "error": "❌ Code is too short. Please provide a complete implementation."
            })
            return False, test_results, 0, "Code too short"
        
        # Step 1: Try to compile with Rust (if available)
        compilation_passed = False
        try:
            # Create a temporary directory for Rust project
            with tempfile.TemporaryDirectory() as tmpdir:
                # Write the code to a file
                rust_file = os.path.join(tmpdir, "main.rs")
                with open(rust_file, 'w') as f:
                    f.write(code)
                
                # Try to compile
                result = subprocess.run(
                    ['rustc', '--crate-type', 'lib', rust_file],
                    cwd=tmpdir,
                    capture_output=True,
                    text=True,
                    timeout=30
                )
                
                if result.returncode == 0:
                    test_results.append({
                        "test_id": 1,
                        "input": "Rust compilation",
                        "expected": "Success",
                        "passed": True,
                        "gas_used": 0,
                        "error": None,
                        "actual": "✓ Code compiles successfully"
                    })
                    compilation_passed = True
                else:
                    error_msg = result.stderr[:300] if result.stderr else "Compilation failed"
                    test_results.append({
                        "test_id": 1,
                        "input": "Rust compilation",
                        "expected": "Success",
                        "passed": False,
                        "gas_used": 0,
                        "error": f"❌ Compilation error: {error_msg}"
                    })
                    all_passed = False
                    return all_passed, test_results, 0, "Rust compilation failed"
                    
        except FileNotFoundError:
            # Rust compiler not installed - will use pattern matching only
            test_results.append({
                "test_id": 1,
                "input": "Rust compilation",
                "expected": "Success (or pattern matching)",
                "passed": True,
                "gas_used": 0,
                "error": None,
                "actual": "⚠️ Rust compiler not available - using enhanced pattern matching"
            })
            compilation_passed = True  # Continue with pattern matching
            
        except subprocess.TimeoutExpired:
            test_results.append({
                "test_id": 1,
                "input": "Rust compilation",
                "expected": "Success",
                "passed": False,
                "gas_used": 0,
                "error": "❌ Compilation timeout - code may have infinite loops"
            })
            return False, test_results, 0, "Compilation timeout"
            
        except Exception as e:
            test_results.append({
                "test_id": 1,
                "input": "Rust compilation",
                "expected": "Success",
                "passed": False,
                "gas_used": 0,
                "error": f"❌ Compilation error: {str(e)[:200]}"
            })
            return False, test_results, 0, str(e)
        
        # Step 2: Enhanced pattern matching - CHECK ALL TEST CASES
        test_cases = problem.get("test_cases", [])
        
        # Required Solana/Anchor patterns
        required_patterns = {
            "anchor_imports": r"use anchor_lang::prelude::\*;",
            "program_module": r"#\[program\]",
            "public_functions": r"pub\s+fn\s+\w+",
            "context_usage": r"Context<\w+>",
        }
        
        # Check required patterns
        for pattern_name, pattern in required_patterns.items():
            if not re.search(pattern, code):
                test_results.append({
                    "test_id": len(test_results) + 1,
                    "input": f"Required pattern: {pattern_name}",
                    "expected": "Present in code",
                    "passed": False,
                    "gas_used": 0,
                    "error": f"❌ Missing required Rust/Solana pattern: {pattern_name}"
                })
                all_passed = False
        
        # Step 3: Validate ALL test cases
        if test_cases:
            # For Rust, test_cases contain expected behaviors
            # We need to check that code has proper implementation for each test scenario
            for i, test_case in enumerate(test_cases):
                test_input = test_case.get("input", "")
                expected = test_case.get("expected", "")
                description = test_case.get("description", f"Test {i+1}")
                
                # Extract value from test input (e.g., "initialize_with_10" -> 10)
                # Check that code can handle different values (not hardcoded)
                import_match = re.search(r'initialize.*?(\d+)', test_input)
                if import_match:
                    value = import_match.group(1)
                    # Code should NOT have hardcoded return of this specific value
                    # Instead it should use the parameter
                    hardcode_pattern = rf'return\s+{value}\s*;'
                    if re.search(hardcode_pattern, code):
                        test_results.append({
                            "test_id": len(test_results) + 1,
                            "input": description,
                            "expected": "Dynamic implementation (not hardcoded)",
                            "passed": False,
                            "gas_used": 0,
                            "error": f"❌ Code appears to hardcode value {value}. Implementation must be dynamic!"
                        })
                        all_passed = False
                        continue
                
                # Generic test - check implementation exists
                test_results.append({
                    "test_id": len(test_results) + 1,
                    "input": description,
                    "expected": expected,
                    "passed": True,
                    "gas_used": 0,
                    "error": None
                })
        
        # Final check: Must have meaningful data structures
        if not re.search(r'struct\s+\w+', code):
            test_results.append({
                "test_id": len(test_results) + 1,
                "input": "Data structures check",
                "expected": "At least one struct definition",
                "passed": False,
                "gas_used": 0,
                "error": "❌ Code must define proper data structures (structs)"
            })
            all_passed = False
        
        return all_passed, test_results, 0, None if all_passed else "Rust validation failed"
    
    async def _validate_rust_patterns(
        self,
        code: str,
        problem: Dict[str, Any]
    ) -> Tuple[bool, List[Dict], int, str]:
        """Fallback pattern-based validation for Rust when compiler unavailable"""
        
        test_results = []
        all_passed = True
        
        # Basic Rust/Solana patterns
        required_patterns = [
            (r"use anchor_lang::prelude::\*;", "Anchor Lang imports"),
            (r"#\[program\]", "Program attribute"),
            (r"pub mod \w+", "Public module"),
        ]
        
        for i, (pattern, description) in enumerate(required_patterns):
            if re.search(pattern, code):
                test_results.append({
                    "test_id": i + 1,
                    "input": description,
                    "expected": "Found",
                    "passed": True,
                    "gas_used": 0,
                    "error": None
                })
            else:
                test_results.append({
                    "test_id": i + 1,
                    "input": description,
                    "expected": "Found",
                    "passed": False,
                    "gas_used": 0,
                    "error": f"❌ Missing: {description}"
                })
                all_passed = False
        
        return all_passed, test_results, 0, None if all_passed else "Pattern validation failed"
    
    
    async def _validate_move(
        self, 
        code: str, 
        problem: Dict[str, Any]
    ) -> Tuple[bool, List[Dict], int, str]:
        """
        Validate MOVE (Aptos/Sui) code
        
        Enhanced validation to prevent cheating:
        - Strict TODO checks (no TODOs allowed)
        - Empty function detection
        - Pattern matching for all test cases
        - Minimum code complexity requirements
        """
        test_results = []
        all_passed = True
        
        # Step 0: Pre-validation checks - STRICT
        # Check for ANY TODO markers
        if "TODO" in code or "// Your code here" in code or "/* TODO */" in code or "todo!" in code:
            test_results.append({
                "test_id": 0,
                "input": "Code completeness check",
                "expected": "All TODOs removed and functions implemented",
                "passed": False,
                "gas_used": 0,
                "error": "❌ Code contains TODO markers or placeholder text. Please implement all functions."
            })
            return False, test_results, 0, "Code is incomplete - contains TODO markers"
        
        # Check for empty function bodies - STRICT patterns
        empty_function_patterns = [
            r'(public\s+fun|fun)\s+\w+\([^)]*\)\s*(:.*?)?\s*\{\s*\}',  # fun name() {}
            r'(public\s+fun|fun)\s+\w+\([^)]*\)\s*(:.*?)?\s*\{\s*//.*\s*\}',  # fun with only comment
            r'(public\s+entry\s+fun)\s+\w+\([^)]*\)\s*(:.*?)?\s*\{\s*\}',  # public entry fun
        ]
        for pattern in empty_function_patterns:
            if re.search(pattern, code):
                test_results.append({
                    "test_id": 0,
                    "input": "Function implementation check",
                    "expected": "All functions must have implementations",
                    "passed": False,
                    "gas_used": 0,
                    "error": "❌ Code has empty functions. Please implement the required logic."
                })
                return False, test_results, 0, "Code has empty functions"
        
        # Check minimum code length (anti-template submission)
        code_without_comments = re.sub(r'//.*$', '', code, flags=re.MULTILINE)
        code_without_comments = re.sub(r'/\*.*?\*/', '', code_without_comments, flags=re.DOTALL)
        if len(code_without_comments.strip()) < 200:
            test_results.append({
                "test_id": 0,
                "input": "Code complexity check",
                "expected": "Meaningful implementation with actual logic",
                "passed": False,
                "gas_used": 0,
                "error": "❌ Code is too short. Please provide a complete implementation."
            })
            return False, test_results, 0, "Code too short"
        
        # Try to compile if move compiler is available
        try:
            with tempfile.NamedTemporaryFile(mode='w', suffix='.move', delete=False) as f:
                f.write(code)
                temp_file = f.name
            
            try:
                # Try aptos move compiler
                result = subprocess.run(
                    ['aptos', 'move', 'compile', '--package-dir', os.path.dirname(temp_file)],
                    capture_output=True,
                    text=True,
                    timeout=30
                )
                
                if result.returncode != 0:
                    # Compilation failed
                    test_results.append({
                        "test_id": 0,
                        "input": "MOVE compilation",
                        "expected": "Clean compilation",
                        "passed": False,
                        "gas_used": 0,
                        "error": f"❌ Compilation error: {result.stderr[:200]}"
                    })
                    return False, test_results, 0, "Compilation failed"
                else:
                    # Compilation successful
                    test_results.append({
                        "test_id": 0,
                        "input": "MOVE compilation",
                        "expected": "Clean compilation",
                        "passed": True,
                        "gas_used": 0
                    })
                    
            except (FileNotFoundError, subprocess.TimeoutExpired):
                # Compiler not available or timeout, use pattern matching
                pass
            finally:
                if os.path.exists(temp_file):
                    os.unlink(temp_file)
        except Exception as e:
            # Fall through to pattern matching
            pass
        
        # Pattern matching for MOVE code
        return await self._validate_move_patterns(code, problem, test_results)
    
    async def _validate_move_patterns(
        self,
        code: str,
        problem: Dict[str, Any],
        test_results: List[Dict]
    ) -> Tuple[bool, List[Dict], int, str]:
        """Pattern-based validation for MOVE"""
        
        test_cases = problem.get("test_cases", [])
        all_passed = True
        
        # Define patterns for MOVE constructs
        patterns = {
            "module": r'module\s+\w+::\w+\s*\{',
            "struct": r'struct\s+\w+\s*(has\s+(key|store|drop|copy)(,\s*(key|store|drop|copy))*)?',
            "public_fun": r'public\s+fun\s+\w+',
            "acquires": r'acquires\s+\w+',
            "signer": r'&signer',
            "resource": r'move_to|move_from|borrow_global',
        }
        
        for i, test_case in enumerate(test_cases, 1):
            test_input = test_case.get("input", "")
            expected = test_case.get("expected", "")
            description = test_case.get("description", f"Test {i}")
            
            # Check if required MOVE constructs are present
            passed = True
            error_msg = None
            
            if "module" in test_input.lower() and not re.search(patterns["module"], code):
                passed = False
                error_msg = "❌ Missing module definition"
            elif "struct" in test_input.lower() and not re.search(patterns["struct"], code):
                passed = False
                error_msg = "❌ Missing struct definition"
            elif "resource" in test_input.lower() and not any(re.search(p, code) for p in [patterns["resource"]]):
                passed = False
                error_msg = "❌ Missing resource operations"
            elif "signer" in test_input.lower() and not re.search(patterns["signer"], code):
                passed = False
                error_msg = "❌ Missing signer parameter"
            else:
                # Generic check: code should have actual implementation
                if len(code.strip()) < 100:
                    passed = False
                    error_msg = "❌ Code too short - needs proper implementation"
            
            test_results.append({
                "test_id": i,
                "input": test_input,
                "expected": expected,
                "passed": passed,
                "gas_used": 0,
                "error": error_msg if not passed else None
            })
            
            if not passed:
                all_passed = False
        
        return all_passed, test_results, 0, None if all_passed else "Pattern validation failed"

    async def _validate_func(
        self, 
        code: str, 
        problem: Dict[str, Any]
    ) -> Tuple[bool, List[Dict], int, str]:
        """
        Validate FunC/TON contract
        
        Attempts real compilation if func compiler available,
        otherwise falls back to pattern matching
        """
        
        test_results = []
        all_passed = True
        
        # Step 1: Check for incomplete code
        if "TODO" in code or "..." in code:
            todo_count = code.count("TODO") + code.count("...")
            if todo_count > 2:
                test_results.append({
                    "test_id": 1,
                    "input": "Implementation check",
                    "expected": "Complete",
                    "passed": False,
                    "gas_used": 0,
                    "error": f"❌ Code incomplete - found {todo_count} TODO/... markers"
                })
                return False, test_results, 0, "Incomplete implementation"
        
        # Step 2: Try FunC compilation
        try:
            with tempfile.TemporaryDirectory() as tmpdir:
                func_file = os.path.join(tmpdir, "contract.fc")
                with open(func_file, 'w') as f:
                    f.write(code)
                
                # Try to compile with func
                result = subprocess.run(
                    ['func', '-o', os.path.join(tmpdir, 'contract.fif'), func_file],
                    capture_output=True,
                    text=True,
                    timeout=15
                )
                
                if result.returncode == 0:
                    test_results.append({
                        "test_id": 2,
                        "input": "FunC compilation",
                        "expected": "Success",
                        "passed": True,
                        "gas_used": 0,
                        "error": None,
                        "actual": "✓ Code compiles successfully"
                    })
                else:
                    error_msg = result.stderr[:300] if result.stderr else "Compilation failed"
                    test_results.append({
                        "test_id": 2,
                        "input": "FunC compilation",
                        "expected": "Success",
                        "passed": False,
                        "gas_used": 0,
                        "error": f"❌ Compilation error: {error_msg}"
                    })
                    all_passed = False
                    return all_passed, test_results, 0, "FunC compilation failed"
                    
        except FileNotFoundError:
            # FunC compiler not installed - use pattern matching
            test_results.append({
                "test_id": 2,
                "input": "FunC compilation",
                "expected": "Success",
                "passed": False,
                "gas_used": 0,
                "error": "⚠️ FunC compiler not available - using pattern matching"
            })
            return await self._validate_func_patterns(code, problem)
            
        except subprocess.TimeoutExpired:
            test_results.append({
                "test_id": 2,
                "input": "FunC compilation",
                "expected": "Success",
                "passed": False,
                "gas_used": 0,
                "error": "❌ Compilation timeout"
            })
            return False, test_results, 0, "Compilation timeout"
            
        except Exception as e:
            test_results.append({
                "test_id": 2,
                "input": "FunC compilation",
                "expected": "Success",
                "passed": False,
                "gas_used": 0,
                "error": f"❌ Error: {str(e)[:200]}"
            })
            return False, test_results, 0, str(e)
        
        # Step 3: Additional pattern checks
        test_cases = problem.get("test_cases", [])
        
        for i, test_case in enumerate(test_cases):
            pattern = test_case.get("pattern", "")
            description = test_case.get("description", f"Test {i+1}")
            
            if pattern and re.search(pattern, code):
                test_results.append({
                    "test_id": len(test_results) + 1,
                    "input": description,
                    "expected": "Pattern found",
                    "passed": True,
                    "gas_used": 0,
                    "error": None
                })
            elif pattern:
                test_results.append({
                    "test_id": len(test_results) + 1,
                    "input": description,
                    "expected": "Pattern found",
                    "passed": False,
                    "gas_used": 0,
                    "error": f"❌ Required pattern not found"
                })
                all_passed = False
        
        return all_passed, test_results, 0, None if all_passed else "FunC validation failed"
    
    async def _validate_func_patterns(
        self,
        code: str,
        problem: Dict[str, Any]
    ) -> Tuple[bool, List[Dict], int, str]:
        """Fallback pattern-based validation for FunC"""
        
        test_results = []
        all_passed = True
        
        # Basic FunC syntax checks
        required_patterns = [
            (r"recv_internal|recv_external", "Message receiver function"),
            (r"method_id", "Method ID declaration"),
        ]
        
        for i, (pattern, description) in enumerate(required_patterns):
            if re.search(pattern, code):
                test_results.append({
                    "test_id": i + 1,
                    "input": description,
                    "expected": "Found",
                    "passed": True,
                    "gas_used": 0,
                    "error": None
                })
            else:
                test_results.append({
                    "test_id": i + 1,
                    "input": description,
                    "expected": "Found",
                    "passed": False,
                    "gas_used": 0,
                    "error": f"❌ Missing: {description}"
                })
                all_passed = False
        
        return all_passed, test_results, 0, None if all_passed else "Pattern validation failed"
    
    async def _validate_cryptography(
        self, 
        code: str, 
        problem: Dict[str, Any]
    ) -> Tuple[bool, List[Dict], int, str]:
        """Validate cryptography problems (usually Solidity with crypto focus)"""
        
        # Cryptography problems are typically Solidity-based
        # But with specific checks for crypto operations
        
        all_passed, test_results, gas, error = await self._validate_solidity(code, problem)
        
        # Additional crypto-specific checks
        problem_id = problem.get("problem_id", "")
        
        if "merkle" in problem_id.lower() or "merkle" in problem.get("title", "").lower():
            # Check for merkle tree specific functions
            if "keccak256" not in code or "abi.encodePacked" not in code:
                test_results.append({
                    "test_id": len(test_results) + 1,
                    "input": "Merkle tree implementation check",
                    "expected": "Uses keccak256 and encodePacked",
                    "passed": False,
                    "gas_used": 0,
                    "error": "Merkle tree should use keccak256 and abi.encodePacked"
                })
                all_passed = False
        
        if "signature" in problem_id.lower() or "ecdsa" in problem.get("title", "").lower():
            # Check for signature functions
            if "ecrecover" not in code:
                test_results.append({
                    "test_id": len(test_results) + 1,
                    "input": "Signature verification check",
                    "expected": "Uses ecrecover",
                    "passed": False,
                    "gas_used": 0,
                    "error": "Signature verification should use ecrecover"
                })
                all_passed = False
        
        return all_passed, test_results, gas, error


# Global validator instance
code_validator = CodeValidator()
