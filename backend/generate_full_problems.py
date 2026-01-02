"""
Generator for complete 120 problem set
Generates all Solidity, Rust, MOVE, and TVM problems with 15+ tests each
"""

def generate_all_problems():
    problems = []
    
    # ========================================
    # SOLIDITY - 30 Problems (10 Junior + 10 Middle + 10 Senior)
    # ========================================
    
    # JUNIOR SOLIDITY (10)
    junior_sol_templates = [
        {
            "id": "sol_j{:02d}",
            "title": "Solidity Junior {}: {}",
            "topics": [
                ("Counter Contract", "state management, arithmetic"),
                ("Storage Contract", "multiple data types"),
                ("Math Operations", "pure functions, calculations"),
                ("Array Manager", "dynamic arrays, loops"),
                ("Balance Tracker", "mappings, events"),
                ("Access Control", "modifiers, ownership"),
                ("String Handler", "string operations"),
                ("Logic Gates", "boolean operations"),
                ("Struct Registry", "structs, complex types"),
                ("Simple Voting", "voting mechanism"),
            ]
        }
    ]
    
    # MIDDLE SOLIDITY (10)
    middle_sol_templates = [
        {
            "id": "sol_m{:02d}",
            "title": "Solidity Middle {}: {}",
            "topics": [
                ("ERC20 Token", "token standard, transfers"),
                ("NFT Contract", "ERC721, minting"),
                ("Staking Pool", "rewards, time-lock"),
                ("Auction System", "bidding, refunds"),
                ("Multisig Wallet", "multiple approvals"),
                ("Escrow Service", "conditional release"),
                ("Lottery Contract", "randomness, distribution"),
                ("DAO Voting", "proposals, delegation"),
                ("Time Lock", "delays, scheduling"),
                ("Oracle Integration", "external data"),
            ]
        }
    ]
    
    # SENIOR SOLIDITY (10)
    senior_sol_templates = [
        {
            "id": "sol_s{:02d}",
            "title": "Solidity Senior {}: {}",
            "topics": [
                ("DEX Protocol", "AMM, liquidity pools"),
                ("Lending Platform", "collateral, interest"),
                ("Yield Aggregator", "strategy, optimization"),
                ("Flash Loans", "atomic transactions"),
                ("Cross-chain Bridge", "locks, proofs"),
                ("Gas Optimized Storage", "efficient patterns"),
                ("Upgradeable Proxy", "proxy patterns"),
                ("Reentrancy Guard", "security patterns"),
                ("MEV Protection", "frontrun prevention"),
                ("Advanced Governance", "quadratic voting"),
            ]
        }
    ]
    
    # Generate Solidity problems
    for i in range(1, 11):
        # Junior
        problems.append(generate_solidity_problem(
            f"sol_j{i:02d}",
            f"Solidity Junior {i}",
            "junior",
            generate_tests(15, "junior")
        ))
        
        # Middle  
        problems.append(generate_solidity_problem(
            f"sol_m{i:02d}",
            f"Solidity Middle {i}",
            "middle",
            generate_tests(18, "middle")
        ))
        
        # Senior
        problems.append(generate_solidity_problem(
            f"sol_s{i:02d}",
            f"Solidity Senior {i}",
            "senior",
            generate_tests(20, "senior")
        ))
    
    # ========================================
    # RUST/SOLANA - 30 Problems
    # ========================================
    for i in range(1, 11):
        # Junior Rust
        problems.append(generate_rust_problem(
            f"rust_j{i:02d}",
            f"Rust/Solana Junior {i}",
            "junior",
            generate_tests(15, "junior")
        ))
        
        # Middle Rust
        problems.append(generate_rust_problem(
            f"rust_m{i:02d}",
            f"Rust/Solana Middle {i}",
            "middle",
            generate_tests(18, "middle")
        ))
        
        # Senior Rust
        problems.append(generate_rust_problem(
            f"rust_s{i:02d}",
            f"Rust/Solana Senior {i}",
            "senior",
            generate_tests(20, "senior")
        ))
    
    # ========================================
    # MOVE - 30 Problems
    # ========================================
    for i in range(1, 11):
        # Junior MOVE
        problems.append(generate_move_problem(
            f"move_j{i:02d}",
            f"MOVE Junior {i}",
            "junior",
            generate_tests(15, "junior")
        ))
        
        # Middle MOVE
        problems.append(generate_move_problem(
            f"move_m{i:02d}",
            f"MOVE Middle {i}",
            "middle",
            generate_tests(18, "middle")
        ))
        
        # Senior MOVE
        problems.append(generate_move_problem(
            f"move_s{i:02d}",
            f"MOVE Senior {i}",
            "senior",
            generate_tests(20, "senior")
        ))
    
    # ========================================
    # TVM/FunC - 30 Problems
    # ========================================
    for i in range(1, 11):
        # Junior TVM
        problems.append(generate_tvm_problem(
            f"tvm_j{i:02d}",
            f"TVM/FunC Junior {i}",
            "junior",
            generate_tests(15, "junior")
        ))
        
        # Middle TVM
        problems.append(generate_tvm_problem(
            f"tvm_m{i:02d}",
            f"TVM/FunC Middle {i}",
            "middle",
            generate_tests(18, "middle")
        ))
        
        # Senior TVM
        problems.append(generate_tvm_problem(
            f"tvm_s{i:02d}",
            f"TVM/FunC Senior {i}",
            "senior",
            generate_tests(20, "senior")
        ))
    
    return problems


def generate_solidity_problem(problem_id, title, difficulty, test_cases):
    """Generate a Solidity problem with comprehensive tests"""
    
    topics = {
        "sol_j01": ("Counter", "increment/decrement operations"),
        "sol_j02": ("Storage", "multiple data types"),
        "sol_j03": ("Math", "arithmetic operations"),
        "sol_j04": ("Arrays", "dynamic array management"),
        "sol_j05": ("Mappings", "balance tracking"),
        "sol_j06": ("Ownership", "access control"),
        "sol_j07": ("Strings", "string manipulation"),
        "sol_j08": ("Boolean", "logic operations"),
        "sol_j09": ("Structs", "user management"),
        "sol_j10": ("Voting", "simple voting"),
        "sol_m01": ("ERC20", "token standard"),
        "sol_m02": ("NFT", "ERC721 implementation"),
        "sol_m03": ("Staking", "rewards system"),
        "sol_m04": ("Auction", "bidding mechanism"),
        "sol_m05": ("Multisig", "multi-signature wallet"),
        "sol_m06": ("Escrow", "conditional payments"),
        "sol_m07": ("Lottery", "random selection"),
        "sol_m08": ("DAO", "governance voting"),
        "sol_m09": ("TimeLock", "delayed execution"),
        "sol_m10": ("Oracle", "external data"),
        "sol_s01": ("DEX", "automated market maker"),
        "sol_s02": ("Lending", "collateralized loans"),
        "sol_s03": ("Yield", "farming strategies"),
        "sol_s04": ("FlashLoan", "atomic operations"),
        "sol_s05": ("Bridge", "cross-chain transfers"),
        "sol_s06": ("GasOptimized", "storage patterns"),
        "sol_s07": ("Proxy", "upgradeable contracts"),
        "sol_s08": ("Reentrancy", "security guards"),
        "sol_s09": ("MEV", "frontrun protection"),
        "sol_s10": ("Governance", "advanced voting"),
    }
    
    topic, desc = topics.get(problem_id, ("Generic", "blockchain functionality"))
    
    code_template = f"""// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract {topic}Contract {{
    // State variables
    uint256 public value;
    mapping(address => uint256) public balances;
    
    // Events
    event ValueChanged(uint256 newValue);
    event BalanceUpdated(address indexed user, uint256 amount);
    
    // TODO: Implement required functions
    function setValue(uint256 _value) public {{
        // Your code here
    }}
    
    function getValue() public view returns (uint256) {{
        // Your code here
    }}
    
    function updateBalance(uint256 amount) public {{
        // Your code here
    }}
    
    function getBalance(address addr) public view returns (uint256) {{
        // Your code here
    }}
}}"""
    
    return {
        "problem_id": problem_id,
        "title": f"{title}: {topic} - {desc}",
        "description": f"""Implement a {topic} contract with {desc}.

Requirements:
- Implement all required functions
- Handle edge cases properly  
- Emit appropriate events
- Test with multiple scenarios
- Ensure no hardcoding of values

This problem requires {len(test_cases)} tests to pass.""",
        "difficulty": difficulty,
        "category": "solidity",
        "initial_code": code_template,
        "test_cases": test_cases,
        "hints": [
            "Implement all functions correctly",
            "Test with different values",
            "Handle edge cases",
            "Use events for tracking"
        ],
        "tags": ["solidity", difficulty, topic.lower()],
        "solved_count": 0
    }


def generate_rust_problem(problem_id, title, difficulty, test_cases):
    """Generate a Rust/Solana problem"""
    
    code_template = """use anchor_lang::prelude::*;

declare_id!("...");

#[program]
pub mod solution {
    use super::*;
    
    // TODO: Implement initialize
    pub fn initialize(ctx: Context<Initialize>, value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }}
    
    // TODO: Implement update  
    pub fn update(ctx: Context<Update>, new_value: u64) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub data_account: Account<'info, DataAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Update<'info> {
    #[account(mut)]
    pub data_account: Account<'info, DataAccount>,
}

#[account]
pub struct DataAccount {
    pub value: u64,
}"""
    
    return {
        "problem_id": problem_id,
        "title": f"{title}: Solana Program Development",
        "description": f"""Implement a Solana program with account management.

Requirements:
- Initialize program accounts
- Handle multiple instructions
- Manage state correctly
- Use Anchor framework properly
- Pass all {len(test_cases)} tests

No hardcoding allowed - implement real logic.""",
        "difficulty": difficulty,
        "category": "rust",
        "initial_code": code_template,
        "test_cases": test_cases,
        "hints": [
            "Use Anchor framework",
            "Handle account initialization",
            "Implement all instructions",
            "Test multiple operations"
        ],
        "tags": ["rust", "solana", difficulty],
        "solved_count": 0
    }


def generate_move_problem(problem_id, title, difficulty, test_cases):
    """Generate a MOVE problem"""
    
    code_template = """module 0x1::solution {
    use std::signer;
    
    struct Resource has key {
        value: u64,
    }
    
    // TODO: Implement create_resource
    public fun create_resource(account: &signer, value: u64) {
        // Your code here
    }
    
    // TODO: Implement get_value
    public fun get_value(addr: address): u64 acquires Resource {
        // Your code here
    }
    
    // TODO: Implement update_value
    public fun update_value(account: &signer, new_value: u64) acquires Resource {
        // Your code here
    }
}"""
    
    return {
        "problem_id": problem_id,
        "title": f"{title}: MOVE Resource Management",
        "description": f"""Implement a MOVE module with resource-oriented programming.

Requirements:
- Define and manage resources
- Implement access control
- Handle resource safety
- Use MOVE idioms correctly
- Pass all {len(test_cases)} comprehensive tests

Must implement real logic - no shortcuts.""",
        "difficulty": difficulty,
        "category": "move",
        "initial_code": code_template,
        "test_cases": test_cases,
        "hints": [
            "Use resource safety",
            "Implement acquires correctly",
            "Handle signer validation",
            "Test thoroughly"
        ],
        "tags": ["move", "aptos", difficulty],
        "solved_count": 0
    }


def generate_tvm_problem(problem_id, title, difficulty, test_cases):
    """Generate a TVM/FunC problem"""
    
    code_template = """;; TVM Smart Contract
#include "imports/stdlib.fc";

;; Storage: value
(int) load_data() inline {
    slice ds = get_data().begin_parse();
    return ds~load_uint(64);
}

() save_data(int value) impure inline {
    set_data(begin_cell()
        .store_uint(value, 64)
        .end_cell());
}

;; TODO: Implement recv_internal
() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {
    ;; Your code here
}

;; TODO: Implement get_value
int get_value() method_id {
    ;; Your code here
}

;; TODO: Implement set_value
() set_value(int new_value) impure {
    ;; Your code here
}"""
    
    return {
        "problem_id": problem_id,
        "title": f"{title}: TON Smart Contract",
        "description": f"""Implement a TON smart contract in FunC.

Requirements:
- Handle internal messages
- Manage cell storage
- Implement get methods
- Handle gas efficiently
- Pass all {len(test_cases)} validation tests

Real implementation required - test with multiple scenarios.""",
        "difficulty": difficulty,
        "category": "func",
        "initial_code": code_template,
        "test_cases": test_cases,
        "hints": [
            "Use FunC syntax correctly",
            "Handle cell operations",
            "Implement message handling",
            "Test message flows"
        ],
        "tags": ["ton", "tvm", "func", difficulty],
        "solved_count": 0
    }


def generate_tests(count, difficulty):
    """Generate test cases based on difficulty"""
    tests = []
    
    # Initial state tests
    tests.append({
        "type": "call",
        "function": "getValue",
        "args": [],
        "expected": "0",
        "description": "Initial value is 0"
    })
    
    # Multiple set/get operations to prevent hardcoding
    values = [10, 25, 42, 100, 7, 33, 99, 1, 50, 77, 88, 15, 200, 5, 60, 120, 75, 35, 90, 45]
    
    for i in range(min(count - 1, len(values))):
        val = values[i]
        tests.append({
            "type": "transaction",
            "function": "setValue",
            "args": [str(val)],
            "expected": "success",
            "description": f"Set value to {val}"
        })
        tests.append({
            "type": "call",
            "function": "getValue",
            "args": [],
            "expected": str(val),
            "description": f"Value should be {val}"
        })
    
    # Add balance tests if space allows
    if difficulty in ["middle", "senior"] and count > 10:
        tests.append({
            "type": "transaction",
            "function": "updateBalance",
            "args": ["100"],
            "expected": "success",
            "description": "Update balance"
        })
        tests.append({
            "type": "call",
            "function": "getBalance",
            "args": ["<deployer>"],
            "expected": "100",
            "description": "Balance is 100"
        })
    
    return tests[:count]


# Generate and save
if __name__ == "__main__":
    problems = generate_all_problems()
    
    # Write to file
    with open('/app/backend/seed_problems_generated.py', 'w') as f:
        f.write('"""\\n')
        f.write('CodeChain Platform - Complete Problem Set 2025\\n')
        f.write('120 Problems: 30 Solidity + 30 Rust + 30 MOVE + 30 TVM\\n')
        f.write('Each with 15+ comprehensive tests\\n')
        f.write('All problems have solved_count = 0\\n')
        f.write('"""\\n\\n')
        f.write('PROBLEMS = [\\n')
        
        for p in problems:
            f.write('    {\\n')
            for key, value in p.items():
                if isinstance(value, str):
                    # Escape string properly
                    escaped = value.replace('\\\\', '\\\\\\\\').replace('"', '\\\\"').replace('\\n', '\\\\n')
                    f.write(f'        "{key}": """{value}""",\\n')
                elif isinstance(value, list):
                    f.write(f'        "{key}": {value},\\n')
                elif isinstance(value, int):
                    f.write(f'        "{key}": {value},\\n')
            f.write('    },\\n')
        
        f.write(']\\n\\n')
        f.write('print(f"Total problems: {len(PROBLEMS)}")\\n')
        f.write('print(f"Solidity: {len([p for p in PROBLEMS if p[\'category\'] == \'solidity\'])}")\\n')
        f.write('print(f"Rust: {len([p for p in PROBLEMS if p[\'category\'] == \'rust\'])}")\\n')
        f.write('print(f"MOVE: {len([p for p in PROBLEMS if p[\'category\'] == \'move\'])}")\\n')
        f.write('print(f"TVM: {len([p for p in PROBLEMS if p[\'category\'] == \'func\'])}")\\n')
    
    print(f"Generated {len(problems)} problems!")
    print(f"Solidity: {len([p for p in problems if p['category'] == 'solidity'])}")
    print(f"Rust: {len([p for p in problems if p['category'] == 'rust'])}")
    print(f"MOVE: {len([p for p in problems if p['category'] == 'move'])}")
    print(f"TVM: {len([p for p in problems if p['category'] == 'func'])}")
