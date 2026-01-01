"""
Code validation and testing system for CodeChain platform
Supports: Solidity, Rust/Solana, FunC/TON, General Cryptography
"""

import re
import json
import hashlib
from typing import Dict, List, Any, Tuple
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
        """Validate Solidity smart contract"""
        
        test_results = []
        total_gas = 0
        
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
            # Parse compilation error
            test_results.append({
                "test_id": 0,
                "input": "Compilation",
                "expected": "Success",
                "passed": False,
                "gas_used": 0,
                "error": f"Compilation failed: {error_msg}"
            })
            return False, test_results, 0, f"Compilation error: {error_msg}"
        
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
                "error": f"Deployment failed: {error_msg}"
            })
            return False, test_results, 0, f"Deployment error: {error_msg}"
        
        # Step 3: Run test cases
        test_cases = problem.get("test_cases", [])
        all_passed = True
        
        for i, test_case in enumerate(test_cases):
            test_input = test_case.get("input", "")
            expected = test_case.get("expected", "")
            
            try:
                result = self._execute_test_case(
                    contract_instance, 
                    test_input, 
                    expected,
                    self.account
                )
                
                test_results.append({
                    "test_id": i + 1,
                    "input": test_input,
                    "expected": expected,
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
                    "input": test_input,
                    "expected": expected,
                    "passed": False,
                    "gas_used": 0,
                    "error": str(e)
                })
                all_passed = False
        
        return all_passed, test_results, total_gas, None
    
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
        """Validate Rust/Solana program"""
        
        test_results = []
        
        # For MVP, we'll do basic syntax checking
        # In production, this would use Solana's testing framework
        
        # Check for required imports
        required_patterns = [
            r"use anchor_lang::prelude::\*;",
            r"#\[program\]",
            r"pub mod \w+",
        ]
        
        all_passed = True
        
        for i, pattern in enumerate(required_patterns):
            if re.search(pattern, code):
                test_results.append({
                    "test_id": i + 1,
                    "input": f"Pattern check: {pattern}",
                    "expected": "Found",
                    "passed": True,
                    "gas_used": 0,
                    "error": None
                })
            else:
                test_results.append({
                    "test_id": i + 1,
                    "input": f"Pattern check: {pattern}",
                    "expected": "Found",
                    "passed": False,
                    "gas_used": 0,
                    "error": f"Missing required pattern: {pattern}"
                })
                all_passed = False
        
        # Check for common Rust errors
        if "TODO" in code and len([line for line in code.split('\n') if 'TODO' in line]) > 2:
            test_results.append({
                "test_id": len(test_results) + 1,
                "input": "Implementation check",
                "expected": "Complete",
                "passed": False,
                "gas_used": 0,
                "error": "Too many TODO comments - implementation incomplete"
            })
            all_passed = False
        
        return all_passed, test_results, 0, None if all_passed else "Rust validation failed"
    
    async def _validate_func(
        self, 
        code: str, 
        problem: Dict[str, Any]
    ) -> Tuple[bool, List[Dict], int, str]:
        """Validate FunC/TON contract"""
        
        test_results = []
        
        # Basic FunC syntax checks
        required_patterns = [
            r"recv_internal",
            r"method_id",
        ]
        
        all_passed = True
        
        for i, pattern in enumerate(required_patterns):
            if re.search(pattern, code):
                test_results.append({
                    "test_id": i + 1,
                    "input": f"Pattern check: {pattern}",
                    "expected": "Found",
                    "passed": True,
                    "gas_used": 0,
                    "error": None
                })
            else:
                test_results.append({
                    "test_id": i + 1,
                    "input": f"Pattern check: {pattern}",
                    "expected": "Found",
                    "passed": False,
                    "gas_used": 0,
                    "error": f"Missing required FunC pattern: {pattern}"
                })
                all_passed = False
        
        return all_passed, test_results, 0, None if all_passed else "FunC validation failed"
    
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
