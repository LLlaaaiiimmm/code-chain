from datetime import datetime, timezone

"""
CodeChain Platform - Complete Problem Set 2025
120 Problems: 30 Solidity + 30 Rust/Solana + 30 MOVE + 30 TVM/FunC
All problems have solved_count = 0
Multiple tests per problem to prevent hardcoding
"""

PROBLEMS = []

# ============================================
# SOLIDITY PROBLEMS (30)
# ============================================

# Helper function to create Solidity problem
def create_sol_problem(pid, title, desc, level, code, tests, tags):
    return {
        "problem_id": pid,
        "title": title,
        "description": desc,
        "difficulty": level,
        "category": "solidity",
        "initial_code": code,
        "test_cases": tests,
        "hints": ["Implement all functions correctly", "Test with multiple values", "Avoid hardcoding results"],
        "tags": tags,
        "solved_count": 0
    }

# Junior Solidity (10)
for i in range(1, 11):
    PROBLEMS.append(create_sol_problem(
        f"sol_j{i:02d}",
        f"Solidity Basic {i}: Counter and Storage",
        f"""Task {i}: Create a contract with state management.
        
Requirements:
- Store a value
- Implement setValue(uint256) to update it
- Implement getValue() to read it  
- Implement increment() to add 1
- Implement reset() to set to 0

All functions must work correctly with multiple calls.""",
        "junior",
        f"""// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Task{i} {{
    uint256 private value;
    
    // TODO: Implement setValue
    function setValue(uint256 _value) public {{
        // Your code here
    }}
    
    // TODO: Implement getValue  
    function getValue() public view returns (uint256) {{
        // Your code here
    }}
    
    // TODO: Implement increment
    function increment() public {{
        // Your code here
    }}
    
    // TODO: Implement reset
    function reset() public {{
        // Your code here
    }}
}}""",
        [
            {"type": "call", "function": "getValue", "args": [], "expected": "0", "description": "Initial value is 0"},
            {"type": "transaction", "function": "setValue", "args": ["42"], "expected": "success", "description": "Set to 42"},
            {"type": "call", "function": "getValue", "args": [], "expected": "42", "description": "Should return 42"},
            {"type": "transaction", "function": "increment", "args": [], "expected": "success", "description": "Increment by 1"},
            {"type": "call", "function": "getValue", "args": [], "expected": "43", "description": "Should return 43"},
            {"type": "transaction", "function": "setValue", "args": ["100"], "expected": "success", "description": "Set to 100"},
            {"type": "call", "function": "getValue", "args": [], "expected": "100", "description": "Should return 100"},
            {"type": "transaction", "function": "reset", "args": [], "expected": "success", "description": "Reset to 0"},
            {"type": "call", "function": "getValue", "args": [], "expected": "0", "description": "Should return 0"},
        ],
        ["basics", "storage"]
    ))

# Middle Solidity (10)
for i in range(1, 11):
    PROBLEMS.append(create_sol_problem(
        f"sol_m{i:02d}",
        f"Solidity Intermediate {i}: Mappings and Arrays",
        f"""Task {i}: Implement a contract with mappings and dynamic arrays.
        
Requirements:
- mapping(address => uint256) balances
- uint256[] public numbers array
- function addNumber(uint256) adds to array
- function getNumber(uint) returns number at index
- function setBalance(address, uint256) sets balance
- function getBalance(address) returns balance
- function getSum() returns sum of all numbers

Test with multiple operations to verify correctness.""",
        "middle",
        f"""// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Task{i} {{
    mapping(address => uint256) public balances;
    uint256[] public numbers;
    
    // TODO: Implement all functions
    function addNumber(uint256 num) public {{
        // Your code
    }}
    
    function getNumber(uint256 index) public view returns (uint256) {{
        // Your code
    }}
    
    function setBalance(address addr, uint256 amount) public {{
        // Your code
    }}
    
    function getBalance(address addr) public view returns (uint256) {{
        // Your code
    }}
    
    function getSum() public view returns (uint256) {{
        // Your code
    }}
    
    function getCount() public view returns (uint256) {{
        return numbers.length;
    }}
}}""",
        [
            {"type": "call", "function": "getCount", "args": [], "expected": "0", "description": "Initial count 0"},
            {"type": "transaction", "function": "addNumber", "args": ["10"], "expected": "success", "description": "Add 10"},
            {"type": "call", "function": "getSum", "args": [], "expected": "10", "description": "Sum is 10"},
            {"type": "transaction", "function": "addNumber", "args": ["20"], "expected": "success", "description": "Add 20"},
            {"type": "call", "function": "getSum", "args": [], "expected": "30", "description": "Sum is 30"},
            {"type": "transaction", "function": "addNumber", "args": ["15"], "expected": "success", "description": "Add 15"},
            {"type": "call", "function": "getCount", "args": [], "expected": "3", "description": "Count is 3"},
            {"type": "call", "function": "getSum", "args": [], "expected": "45", "description": "Sum is 45"},
            {"type": "call", "function": "getNumber", "args": ["1"], "expected": "20", "description": "Index 1 is 20"},
        ],
        ["intermediate", "mappings", "arrays"]
    ))

# Senior Solidity (5)
for i in range(1, 6):
    PROBLEMS.append(create_sol_problem(
        f"sol_s{i:02d}",
        f"Solidity Advanced {i}: Token and DeFi",
        f"""Task {i}: Implement advanced DeFi functionality.
        
Requirements:
- ERC20-like token with transfer, approve, transferFrom
- Staking mechanism with rewards
- Time-based logic
- Event emissions
- Complex state management

Must handle edge cases and multiple scenarios.""",
        "senior",
        f"""// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DeFiTask{i} {{
    mapping(address => uint256) public balances;
    mapping(address => mapping(address => uint256)) public allowances;
    uint256 public totalSupply;
    
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    
    constructor() {{
        totalSupply = 1000000;
        balances[msg.sender] = totalSupply;
    }}
    
    // TODO: Implement transfer
    function transfer(address to, uint256 amount) public returns (bool) {{
        // Your code
    }}
    
    // TODO: Implement approve
    function approve(address spender, uint256 amount) public returns (bool) {{
        // Your code
    }}
    
    // TODO: Implement transferFrom
    function transferFrom(address from, address to, uint256 amount) public returns (bool) {{
        // Your code
    }}
}}""",
        [
            {"type": "call", "function": "balances", "args": ["<deployer>"], "expected": "1000000", "description": "Initial supply"},
            {"type": "transaction", "function": "transfer", "args": ["0x0000000000000000000000000000000000000001", "1000"], "expected": "success", "description": "Transfer 1000"},
            {"type": "call", "function": "balances", "args": ["<deployer>"], "expected": "999000", "description": "Balance decreased"},
            {"type": "transaction", "function": "transfer", "args": ["0x0000000000000000000000000000000000000002", "500"], "expected": "success", "description": "Transfer 500"},
            {"type": "call", "function": "balances", "args": ["<deployer>"], "expected": "998500", "description": "Balance 998500"},
        ],
        ["advanced", "defi", "erc20"]
    ))

# Expert Solidity (5)
for i in range(1, 6):
    PROBLEMS.append(create_sol_problem(
        f"sol_e{i:02d}",
        f"Solidity Expert {i}: Security and Optimization",
        f"""Task {i}: Expert-level contract with security patterns.
        
Requirements:
- Reentrancy guards
- Access control
- Gas optimization
- Complex logic
- Security best practices
- Multiple modifiers

Implement all security measures correctly.""",
        "expert",
        f"""// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SecureContract{i} {{
    address public owner;
    mapping(address => uint256) public deposits;
    bool private locked;
    
    constructor() {{
        owner = msg.sender;
    }}
    
    modifier onlyOwner() {{
        require(msg.sender == owner, "Not owner");
        _;
    }}
    
    modifier nonReentrant() {{
        require(!locked, "Reentrant call");
        locked = true;
        _;
        locked = false;
    }}
    
    // TODO: Implement secure deposit
    function deposit() public payable {{
        deposits[msg.sender] += msg.value;
    }}
    
    // TODO: Implement secure withdraw with reentrancy guard
    function withdraw() public nonReentrant {{
        // Your code
    }}
    
    function getBalance() public view returns (uint256) {{
        return deposits[msg.sender];
    }}
}}""",
        [
            {"type": "call", "function": "getBalance", "args": [], "expected": "0", "description": "Initial 0"},
            {"type": "transaction", "function": "deposit", "args": [], "value": "1000000000000000000", "expected": "success", "description": "Deposit 1 ETH"},
            {"type": "call", "function": "getBalance", "args": [], "expected": "1000000000000000000", "description": "Balance 1 ETH"},
        ],
        ["expert", "security", "reentrancy"]
    ))


# ============================================
# RUST/SOLANA PROBLEMS (30)
# ============================================

# Junior Rust (10)
for i in range(1, 11):
    PROBLEMS.append({
        "problem_id": f"rust_j{i:02d}",
        "title": f"Rust/Solana Basic {i}: Program Accounts",
        "description": f"""Task {i}: Implement a basic Solana program with account management.
        
Requirements:
- Initialize program account
- Store and update data
- Handle multiple instructions
- Validate account ownership
- Implement basic PDA operations

Test with multiple transactions to ensure correctness.""",
        "difficulty": "junior",
        "category": "rust",
        "initial_code": f"""// Solana Program Task {i}
use anchor_lang::prelude::*;

declare_id!("...");

#[program]
pub mod task_{i} {{
    use super::*;
    
    // TODO: Implement initialize
    pub fn initialize(ctx: Context<Initialize>, value: u64) -> Result<()> {{
        // Your code here
        Ok(())
    }}
    
    // TODO: Implement update
    pub fn update(ctx: Context<Update>, new_value: u64) -> Result<()> {{
        // Your code here
        Ok(())
    }}
}}

#[derive(Accounts)]
pub struct Initialize<'info> {{
    #[account(init, payer = user, space = 8 + 8)]
    pub data_account: Account<'info, DataAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}}

#[derive(Accounts)]
pub struct Update<'info> {{
    #[account(mut)]
    pub data_account: Account<'info, DataAccount>,
}}

#[account]
pub struct DataAccount {{
    pub value: u64,
}}""",
        "test_cases": [
            {"input": "initialize with value 10", "expected": "account created with value 10", "description": "Test init"},
            {"input": "update to 20", "expected": "value updated to 20", "description": "Test update"},
            {"input": "update to 35", "expected": "value updated to 35", "description": "Multiple updates work"},
            {"input": "read value", "expected": "35", "description": "Read returns correct value"},
        ],
        "hints": ["Use Anchor framework", "Handle account initialization", "Test multiple operations"],
        "tags": ["solana", "rust", "basics"],
        "solved_count": 0
    })

# Middle Rust (10)
for i in range(1, 11):
    PROBLEMS.append({
        "problem_id": f"rust_m{i:02d}",
        "title": f"Rust/Solana Intermediate {i}: Token Program",
        "description": f"""Task {i}: Implement SPL token operations.
        
Requirements:
- Token minting
- Token transfers
- Balance tracking
- Authority validation
- Multiple token accounts

Implement complete token functionality.""",
        "difficulty": "middle",
        "category": "rust",
        "initial_code": f"""// Token Program Task {i}
use anchor_lang::prelude::*;
use anchor_spl::token::{{self, Token, TokenAccount, Mint}};

declare_id!("...");

#[program]
pub mod token_task_{i} {{
    use super::*;
    
    // TODO: Implement mint
    pub fn mint_tokens(ctx: Context<MintTokens>, amount: u64) -> Result<()> {{
        // Your code
        Ok(())
    }}
    
    // TODO: Implement transfer
    pub fn transfer_tokens(ctx: Context<TransferTokens>, amount: u64) -> Result<()> {{
        // Your code
        Ok(())
    }}
}}

#[derive(Accounts)]
pub struct MintTokens<'info> {{
    #[account(mut)]
    pub mint: Account<'info, Mint>,
    #[account(mut)]
    pub token_account: Account<'info, TokenAccount>,
    pub authority: Signer<'info>,
    pub token_program: Program<'info, Token>,
}}

#[derive(Accounts)]
pub struct TransferTokens<'info> {{
    #[account(mut)]
    pub from: Account<'info, TokenAccount>,
    #[account(mut)]
    pub to: Account<'info, TokenAccount>,
    pub authority: Signer<'info>,
    pub token_program: Program<'info, Token>,
}}""",
        "test_cases": [
            {"input": "mint 100 tokens", "expected": "balance = 100", "description": "Mint works"},
            {"input": "transfer 30 tokens", "expected": "sender: 70, receiver: 30", "description": "Transfer works"},
            {"input": "mint 50 more", "expected": "balance = 120 (70+50)", "description": "Multiple mints"},
            {"input": "transfer 20", "expected": "correct balances", "description": "Multiple operations"},
        ],
        "hints": ["Use SPL token program", "CPI calls", "Authority checks"],
        "tags": ["solana", "tokens", "spl"],
        "solved_count": 0
    })

# Senior Rust (5)
for i in range(1, 6):
    PROBLEMS.append({
        "problem_id": f"rust_s{i:02d}",
        "title": f"Rust/Solana Advanced {i}: DeFi Protocol",
        "description": f"""Task {i}: Implement DeFi protocol with complex logic.
        
Requirements:
- Liquidity pool management
- Staking and rewards
- Complex PDA derivations
- Cross-program invocations
- State synchronization

Build complete DeFi functionality.""",
        "difficulty": "senior",
        "category": "rust",
        "initial_code": f"""// DeFi Protocol Task {i}
// TODO: Implement complete DeFi program
use anchor_lang::prelude::*;

#[program]
pub mod defi_task_{i} {{
    use super::*;
    // Implement liquidity pools, staking, rewards
}}""",
        "test_cases": [
            {"input": "add_liquidity 1000", "expected": "pool updated", "description": "Add liquidity"},
            {"input": "stake 500", "expected": "staked successfully", "description": "Staking works"},
            {"input": "calculate_rewards", "expected": "rewards > 0", "description": "Rewards calculated"},
            {"input": "withdraw rewards", "expected": "rewards claimed", "description": "Withdrawal works"},
        ],
        "hints": ["Complex state management", "Multiple CPIs", "Reward calculation"],
        "tags": ["solana", "defi", "advanced"],
        "solved_count": 0
    })

# Expert Rust (5)
for i in range(1, 6):
    PROBLEMS.append({
        "problem_id": f"rust_e{i:02d}",
        "title": f"Rust/Solana Expert {i}: Security and Optimization",
        "description": f"""Task {i}: Expert Solana program with security hardening.
        
Requirements:
- Account validation
- Reentrancy protection
- Integer overflow protection
- Access control
- Gas optimization
- Comprehensive error handling

Implement with all security best practices.""",
        "difficulty": "expert",
        "category": "rust",
        "initial_code": f"""// Secure Program Task {i}
// TODO: Implement with security patterns
use anchor_lang::prelude::*;

#[program]
pub mod secure_task_{i} {{
    use super::*;
    // Implement with security measures
}}

// Add custom errors
#[error_code]
pub enum ErrorCode {{
    Unauthorized,
    InsufficientFunds,
    InvalidAmount,
}}""",
        "test_cases": [
            {"input": "secure operation", "expected": "validated and executed", "description": "Security check"},
            {"input": "unauthorized access", "expected": "error: Unauthorized", "description": "Access control"},
            {"input": "overflow attempt", "expected": "error: overflow", "description": "Overflow protection"},
        ],
        "hints": ["Comprehensive validation", "Security first", "Error handling"],
        "tags": ["solana", "security", "expert"],
        "solved_count": 0
    })

# ============================================
# MOVE PROBLEMS (30)
# ============================================

# Junior MOVE (10)
for i in range(1, 11):
    PROBLEMS.append({
        "problem_id": f"move_j{i:02d}",
        "title": f"MOVE Basic {i}: Resources and Structs",
        "description": f"""Task {i}: Implement basic MOVE module with resources.
        
Requirements:
- Define resource struct
- Resource creation function
- Resource transfer function
- Access control
- Resource safety guarantees

Use MOVE's resource-oriented programming correctly.""",
        "difficulty": "junior",
        "category": "move",
        "initial_code": f"""// MOVE Module Task {i}
module 0x1::task_{i} {{
    use std::signer;
    
    struct Resource has key {{
        value: u64,
    }}
    
    // TODO: Implement create_resource
    public fun create_resource(account: &signer, value: u64) {{
        // Your code here
    }}
    
    // TODO: Implement get_value
    public fun get_value(addr: address): u64 acquires Resource {{
        // Your code here
    }}
    
    // TODO: Implement update_value
    public fun update_value(account: &signer, new_value: u64) acquires Resource {{
        // Your code here
    }}
}}""",
        "test_cases": [
            {"input": "create resource with value 10", "expected": "resource created", "description": "Creation works"},
            {"input": "get value", "expected": "10", "description": "Read works"},
            {"input": "update to 25", "expected": "value updated", "description": "Update works"},
            {"input": "get value", "expected": "25", "description": "New value correct"},
            {"input": "update to 50", "expected": "value = 50", "description": "Multiple updates"},
        ],
        "hints": ["Use 'acquires'", "Resource safety", "Signer validation"],
        "tags": ["move", "resources", "basics"],
        "solved_count": 0
    })

# Middle MOVE (10)
for i in range(1, 11):
    PROBLEMS.append({
        "problem_id": f"move_m{i:02d}",
        "title": f"MOVE Intermediate {i}: Coin Module",
        "description": f"""Task {i}: Implement fungible token in MOVE.
        
Requirements:
- Coin resource definition
- Minting capability
- Transfer functionality
- Balance tracking
- Supply management

Build complete coin module.""",
        "difficulty": "middle",
        "category": "move",
        "initial_code": f"""// Coin Module Task {i}
module 0x1::my_coin_{i} {{
    use std::signer;
    use aptos_framework::coin;
    
    struct MyCoin has key {{}}
    
    struct CoinStore has key {{
        balance: u64,
    }}
    
    // TODO: Implement initialize
    public fun initialize(account: &signer) {{
        // Your code
    }}
    
    // TODO: Implement mint
    public fun mint(account: &signer, amount: u64) {{
        // Your code
    }}
    
    // TODO: Implement transfer
    public fun transfer(from: &signer, to: address, amount: u64) {{
        // Your code
    }}
    
    // TODO: Implement balance_of
    public fun balance_of(addr: address): u64 {{
        // Your code
    }}
}}""",
        "test_cases": [
            {"input": "initialize", "expected": "coin initialized", "description": "Init works"},
            {"input": "mint 100", "expected": "balance = 100", "description": "Mint works"},
            {"input": "transfer 30", "expected": "sender: 70, receiver: 30", "description": "Transfer works"},
            {"input": "mint 50", "expected": "balance = 120", "description": "Multiple mints"},
        ],
        "hints": ["Coin framework", "Capability pattern", "Balance management"],
        "tags": ["move", "coin", "fungible"],
        "solved_count": 0
    })

# Senior MOVE (5)
for i in range(1, 6):
    PROBLEMS.append({
        "problem_id": f"move_s{i:02d}",
        "title": f"MOVE Advanced {i}: NFT and Marketplace",
        "description": f"""Task {i}: Implement NFT collection and marketplace.
        
Requirements:
- NFT token standard
- Collection management
- Marketplace listing
- Buying and selling
- Royalties

Complex MOVE patterns.""",
        "difficulty": "senior",
        "category": "move",
        "initial_code": f"""// NFT Module Task {i}
module 0x1::nft_market_{i} {{
    use std::string::String;
    use std::signer;
    
    struct NFT has key, store {{
        id: u64,
        name: String,
        creator: address,
    }}
    
    // TODO: Implement complete NFT marketplace
}}""",
        "test_cases": [
            {"input": "mint NFT", "expected": "NFT created", "description": "Minting"},
            {"input": "list for sale", "expected": "listed", "description": "Listing"},
            {"input": "buy NFT", "expected": "ownership transferred", "description": "Buying"},
        ],
        "hints": ["Token standard", "Transfer logic", "Marketplace"],
        "tags": ["move", "nft", "marketplace"],
        "solved_count": 0
    })

# Expert MOVE (5)
for i in range(1, 6):
    PROBLEMS.append({
        "problem_id": f"move_e{i:02d}",
        "title": f"MOVE Expert {i}: Complex DeFi Protocol",
        "description": f"""Task {i}: Expert MOVE implementation with formal verification.
        
Requirements:
- AMM implementation
- Liquidity pools
- Swap functionality
- Fee calculation
- Formal verification properties

Expert-level MOVE programming.""",
        "difficulty": "expert",
        "category": "move",
        "initial_code": f"""// DeFi Protocol Task {i}
module 0x1::defi_{i} {{
    // TODO: Implement AMM with formal verification
    // Ensure invariants hold
}}

spec module {{
    // Add formal verification specs
}}""",
        "test_cases": [
            {"input": "add liquidity", "expected": "pool updated", "description": "Liquidity"},
            {"input": "swap tokens", "expected": "correct amounts", "description": "Swap"},
            {"input": "remove liquidity", "expected": "funds returned", "description": "Removal"},
        ],
        "hints": ["Formal verification", "AMM formula", "Invariants"],
        "tags": ["move", "defi", "verification"],
        "solved_count": 0
    })

# ============================================
# TVM/FunC PROBLEMS (30)
# ============================================

# Junior TVM (10)
for i in range(1, 11):
    PROBLEMS.append({
        "problem_id": f"tvm_j{i:02d}",
        "title": f"TVM/FunC Basic {i}: TON Smart Contract",
        "description": f"""Task {i}: Implement basic TON smart contract.
        
Requirements:
- Handle internal messages
- Store and retrieve data
- Send messages
- Gas management
- Cell manipulation

Basic FunC programming.""",
        "difficulty": "junior",
        "category": "func",
        "initial_code": f""";; TVM Contract Task {i}
#include "imports/stdlib.fc";

;; Storage: value
(int) load_data() inline {{
    slice ds = get_data().begin_parse();
    return ds~load_uint(64);
}}

() save_data(int value) impure inline {{
    set_data(begin_cell()
        .store_uint(value, 64)
        .end_cell());
}}

;; TODO: Implement recv_internal
() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {{
    ;; Your code here
}}

;; TODO: Implement get_value
int get_value() method_id {{
    ;; Your code here
}}

;; TODO: Implement set_value  
() set_value(int new_value) impure {{
    ;; Your code here
}}""",
        "test_cases": [
            {"input": "get_value", "expected": "0", "description": "Initial value"},
            {"input": "set_value 42", "expected": "success", "description": "Set value"},
            {"input": "get_value", "expected": "42", "description": "Read value"},
            {"input": "set_value 100", "expected": "success", "description": "Update"},
            {"input": "get_value", "expected": "100", "description": "New value"},
        ],
        "hints": ["FunC syntax", "Cell operations", "Message handling"],
        "tags": ["ton", "tvm", "basics"],
        "solved_count": 0
    })

# Middle TVM (10)
for i in range(1, 11):
    PROBLEMS.append({
        "problem_id": f"tvm_m{i:02d}",
        "title": f"TVM/FunC Intermediate {i}: Jetton Standard",
        "description": f"""Task {i}: Implement Jetton (TON token) contract.
        
Requirements:
- Jetton master contract
- Jetton wallet contract
- Transfer operations
- Burn and mint
- Balance tracking

Complete Jetton implementation.""",
        "difficulty": "middle",
        "category": "func",
        "initial_code": f""";; Jetton Task {i}
#include "imports/stdlib.fc";

;; TODO: Implement Jetton master
() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {{
    ;; Handle jetton operations
}}

;; TODO: Implement transfer
() transfer(slice to_address, int amount) impure {{
    ;; Your code
}}

;; TODO: Implement balance
int get_balance() method_id {{
    ;; Your code
}}""",
        "test_cases": [
            {"input": "mint 100", "expected": "balance = 100", "description": "Mint works"},
            {"input": "transfer 30", "expected": "balance = 70", "description": "Transfer works"},
            {"input": "burn 20", "expected": "balance = 50", "description": "Burn works"},
        ],
        "hints": ["Jetton standard", "Message structure", "Cell parsing"],
        "tags": ["ton", "jetton", "tokens"],
        "solved_count": 0
    })

# Senior TVM (5)
for i in range(1, 6):
    PROBLEMS.append({
        "problem_id": f"tvm_s{i:02d}",
        "title": f"TVM/FunC Advanced {i}: DEX Protocol",
        "description": f"""Task {i}: Implement DEX on TON blockchain.
        
Requirements:
- Liquidity pools
- Swap functionality
- Price oracle
- Fee distribution
- Complex message handling

Advanced TVM programming.""",
        "difficulty": "senior",
        "category": "func",
        "initial_code": f""";; DEX Protocol Task {i}
;; TODO: Implement complete DEX
#include "imports/stdlib.fc";

() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {{
    ;; Handle DEX operations
}}""",
        "test_cases": [
            {"input": "add_liquidity", "expected": "pool updated", "description": "Liquidity"},
            {"input": "swap", "expected": "tokens swapped", "description": "Swap works"},
        ],
        "hints": ["AMM logic", "Message routing", "State management"],
        "tags": ["ton", "dex", "defi"],
        "solved_count": 0
    })

# Expert TVM (5)
for i in range(1, 6):
    PROBLEMS.append({
        "problem_id": f"tvm_e{i:02d}",
        "title": f"TVM/FunC Expert {i}: Advanced Contracts",
        "description": f"""Task {i}: Expert TVM contract with optimization.
        
Requirements:
- Gas optimization
- Complex cell operations
- Sharding considerations
- Security patterns
- Advanced message handling

Expert TVM development.""",
        "difficulty": "expert",
        "category": "func",
        "initial_code": f""";; Expert Task {i}
;; TODO: Implement optimized contract
#include "imports/stdlib.fc";

() recv_internal(int msg_value, cell in_msg_cell, slice in_msg) impure {{
    ;; Optimized implementation
}}""",
        "test_cases": [
            {"input": "complex_operation", "expected": "success", "description": "Complex logic"},
            {"input": "gas_check", "expected": "< threshold", "description": "Gas optimized"},
        ],
        "hints": ["Gas optimization", "Cell efficiency", "Security"],
        "tags": ["ton", "optimization", "expert"],
        "solved_count": 0
    })

print(f"Total problems: {len(PROBLEMS)}")
