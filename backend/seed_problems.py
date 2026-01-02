from datetime import datetime, timezone

# Comprehensive problem set for CodeChain platform
# Covers: Solidity (Ethereum), Rust (Solana), FunC (TON), and general blockchain concepts

PROBLEMS = [
    # ============== SOLIDITY PROBLEMS ==============
    # Junior Level
    {
        "problem_id": "sol_001",
        "title": "Hello Blockchain",
        "description": """Write a simple smart contract that stores and retrieves a greeting message.

Requirements:
- Create a state variable to store the greeting
- Implement `setGreeting(string memory _greeting)` function
- Implement `getGreeting()` view function that returns the greeting
- Only the contract owner should be able to set the greeting""",
        "difficulty": "junior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Greeting {
    string private greeting;
    address public owner;
    
    constructor() {
        owner = msg.sender;
    }
    
    // TODO: Implement setGreeting function
    function setGreeting(string memory _greeting) public {
        // Your code here
    }
    
    // TODO: Implement getGreeting function
    function getGreeting() public view returns (string memory) {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "state",
                "variable": "owner",
                "expected": "<deployer>",
                "description": "Owner should be set to deployer"
            },
            {
                "type": "transaction",
                "function": "setGreeting",
                "args": ["Hello, CodeChain!"],
                "expected": "success",
                "description": "Should set greeting successfully"
            },
            {
                "type": "call",
                "function": "getGreeting",
                "args": [],
                "expected": "Hello, CodeChain!",
                "description": "Should return correct greeting"
            }
        ],
        "hints": [
            "Use a string state variable to store the greeting",
            "Use require() to check if msg.sender is the owner",
            "Don't forget the 'memory' keyword for string parameters"
        ],
        "tags": ["basics", "storage", "access-control"],
        "solved_count": 1250
    },
    {
        "problem_id": "sol_002",
        "title": "Simple ERC20 Token",
        "description": """Create a basic ERC20-like token contract with essential functions.

Requirements:
- Implement a mapping to track balances
- Implement mint() function (only owner)
- Implement transfer(address to, uint256 amount) function
- Implement balanceOf(address account) view function
- Emit Transfer events""",
        "difficulty": "junior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleToken {
    string public name = "CodeChain Token";
    string public symbol = "CCT";
    uint8 public decimals = 18;
    uint256 public totalSupply;
    
    mapping(address => uint256) public balances;
    address public owner;
    
    event Transfer(address indexed from, address indexed to, uint256 value);
    
    constructor() {
        owner = msg.sender;
    }
    
    // TODO: Implement mint function
    function mint(address to, uint256 amount) public {
        // Your code here
    }
    
    // TODO: Implement transfer function  
    function transfer(address to, uint256 amount) public returns (bool) {
        // Your code here
    }
    
    // TODO: Implement balanceOf function
    function balanceOf(address account) public view returns (uint256) {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "state",
                "variable": "owner",
                "expected": "<deployer>",
                "description": "Owner should be deployer"
            },
            {
                "type": "call",
                "function": "name",
                "args": [],
                "expected": "CodeChain Token",
                "description": "Should have correct name"
            },
            {
                "type": "transaction",
                "function": "mint",
                "args": ["0x1234567890123456789012345678901234567890", 1000],
                "expected": "success",
                "description": "Mint 1000 tokens"
            },
            {
                "type": "call",
                "function": "totalSupply",
                "args": [],
                "expected": "1000",
                "description": "Total supply should be 1000"
            }
        ],
        "hints": [
            "Check for sufficient balance before transfer",
            "Update both sender and receiver balances",
            "Emit Transfer event after successful transfer"
        ],
        "tags": ["token", "erc20", "mapping", "events"],
        "solved_count": 890
    },
    {
        "problem_id": "sol_003",
        "title": "Multi-Signature Wallet",
        "description": """Implement a multi-signature wallet that requires multiple confirmations.

Requirements:
- Store list of owners and required confirmations
- Implement submitTransaction() to propose a transaction
- Implement confirmTransaction() for owners to approve
- Implement executeTransaction() when threshold is met
- Track transaction status""",
        "difficulty": "middle",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MultiSigWallet {
    address[] public owners;
    uint256 public required;
    
    struct Transaction {
        address to;
        uint256 value;
        bytes data;
        bool executed;
        uint256 confirmations;
    }
    
    mapping(uint256 => Transaction) public transactions;
    mapping(uint256 => mapping(address => bool)) public confirmations;
    uint256 public transactionCount;
    
    // TODO: Implement your solution
}""",
        "test_cases": [
            {
                "type": "call",
                "function": "required",
                "args": [],
                "expected": "2",
                "description": "Should require 2 confirmations"
            }
        ],
        "hints": [
            "Use modifiers to check if caller is an owner",
            "Track confirmations in a nested mapping",
            "Execute only when confirmations >= required"
        ],
        "tags": ["multi-sig", "security", "patterns"],
        "solved_count": 456
    },
    {
        "problem_id": "sol_004",
        "title": "Reentrancy Attack Protection",
        "description": """Implement a secure withdrawal pattern protected against reentrancy attacks.

Requirements:
- Implement deposit() function
- Implement withdraw() function with reentrancy protection
- Use checks-effects-interactions pattern
- Add nonReentrant modifier
- Emit events for deposits and withdrawals""",
        "difficulty": "middle",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SecureVault {
    mapping(address => uint256) public balances;
    bool private locked;
    
    event Deposit(address indexed user, uint256 amount);
    event Withdrawal(address indexed user, uint256 amount);
    
    modifier nonReentrant() {
        // TODO: Implement reentrancy guard
        _;
    }
    
    function deposit() public payable {
        // TODO: Implement secure deposit
    }
    
    function withdraw() public nonReentrant {
        // TODO: Implement secure withdrawal
        // Remember: Checks -> Effects -> Interactions
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "deposit",
                "args": [],
                "expected": "success",
                "description": "Should accept deposits"
            },
            {"input": "withdraw()", "expected": "balance = 0, eth sent"},
            {"input": "reentrancy attack", "expected": "reverted"}
        ],
        "hints": [
            "Update state BEFORE external calls",
            "Use require() to check balance > 0",
            "Set locked = true at start of function"
        ],
        "tags": ["security", "reentrancy", "patterns", "important"],
        "solved_count": 523
    },
    {
        "problem_id": "sol_005",
        "title": "Gas Optimization Challenge",
        "description": """Optimize the given contract to reduce gas consumption by at least 30%.

Original gas cost: ~85,000
Target gas cost: <60,000

Techniques to use:
- Storage packing
- Use appropriate data types
- Minimize storage writes
- Use calldata instead of memory where possible""",
        "difficulty": "senior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// UNOPTIMIZED VERSION - Gas: ~85,000
contract Unoptimized {
    struct User {
        uint256 id;
        uint256 balance;
        uint256 lastUpdate;
        bool isActive;
        address wallet;
    }
    
    User[] public users;
    
    function addUser(uint256 id, uint256 balance, address wallet) public {
        User memory user = User({
            id: id,
            balance: balance,
            lastUpdate: block.timestamp,
            isActive: true,
            wallet: wallet
        });
        users.push(user);
    }
}

// TODO: Create optimized version below
contract Optimized {
    // Your optimized code here
}""",
        "test_cases": [
            {"input": "addUser(1, 1000, address)", "expected": "gas < 60000"}
        ],
        "hints": [
            "Pack struct fields: use uint128, uint64, uint32 instead of uint256",
            "Order struct fields by size for optimal packing",
            "Consider using uint32 for timestamps",
            "Use storage pointer instead of memory for temporary variables"
        ],
        "tags": ["optimization", "gas", "advanced", "storage-packing"],
        "solved_count": 234
    },
    {
        "problem_id": "sol_006",
        "title": "Upgradeable Proxy Pattern",
        "description": """Implement an upgradeable smart contract using the proxy pattern.

Requirements:
- Create a Proxy contract that delegates calls
- Create an Implementation contract with business logic
- Implement upgrade mechanism (only owner)
- Preserve storage layout across upgrades
- Use delegatecall properly""",
        "difficulty": "senior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Proxy {
    address public implementation;
    address public admin;
    
    constructor(address _implementation) {
        implementation = _implementation;
        admin = msg.sender;
    }
    
    // TODO: Implement fallback with delegatecall
    fallback() external payable {
        // Your code here
    }
    
    // TODO: Implement upgrade function
    function upgradeTo(address newImplementation) public {
        // Your code here
    }
}

contract ImplementationV1 {
    // Storage layout must be preserved
    address public implementation;
    address public admin;
    uint256 public value;
    
    // TODO: Implement business logic
}""",
        "test_cases": [
            {"input": "proxy.setValue(42)", "expected": "value = 42 in proxy storage"},
            {"input": "proxy.upgradeTo(v2)", "expected": "implementation updated"},
            {"input": "proxy.getValue()", "expected": "42 (storage preserved)"}
        ],
        "hints": [
            "Use delegatecall in fallback function",
            "Storage slots must match between proxy and implementation",
            "Use assembly for delegatecall return data"
        ],
        "tags": ["proxy", "upgradeable", "advanced", "architecture"],
        "solved_count": 178
    },
    {
        "problem_id": "sol_007",
        "title": "Flash Loan Arbitrage",
        "description": """Implement a flash loan contract that performs arbitrage between two DEXes.

Requirements:
- Borrow tokens via flash loan
- Swap on DEX1 at lower price
- Swap on DEX2 at higher price
- Repay loan with fee
- Keep profit
- Ensure atomicity (all or nothing)""",
        "difficulty": "expert",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IFlashLoanProvider {
    function flashLoan(uint256 amount, bytes calldata data) external;
}

interface IDEX {
    function swap(address tokenIn, address tokenOut, uint256 amountIn) external returns (uint256);
}

contract FlashArbitrage {
    IFlashLoanProvider public loanProvider;
    IDEX public dex1;
    IDEX public dex2;
    address public tokenA;
    address public tokenB;
    
    constructor(
        address _provider,
        address _dex1,
        address _dex2,
        address _tokenA,
        address _tokenB
    ) {
        loanProvider = IFlashLoanProvider(_provider);
        dex1 = IDEX(_dex1);
        dex2 = IDEX(_dex2);
        tokenA = _tokenA;
        tokenB = _tokenB;
    }
    
    // TODO: Implement executeArbitrage
    function executeArbitrage(uint256 amount) external {
        // Your code here
    }
    
    // TODO: Implement flash loan callback
    function onFlashLoan(uint256 amount, uint256 fee, bytes calldata data) external {
        // Your code here
        // 1. Verify caller is loan provider
        // 2. Perform arbitrage swaps
        // 3. Calculate profit
        // 4. Repay loan + fee
    }
}""",
        "test_cases": [
            {"input": "executeArbitrage(1000e18)", "expected": "profit > 0"},
            {"input": "price difference insufficient", "expected": "reverted"}
        ],
        "hints": [
            "Check price difference BEFORE taking loan",
            "Calculate exact amounts for each swap",
            "Approve tokens for DEX contracts",
            "Ensure profit > loan fee"
        ],
        "tags": ["defi", "flash-loan", "arbitrage", "expert"],
        "solved_count": 67
    },
    {
        "problem_id": "sol_008",
        "title": "MEV-Resistant DEX",
        "description": """Design a DEX order matching system resistant to MEV (Maximal Extractable Value) attacks.

Requirements:
- Implement commit-reveal scheme for orders
- Add price impact protection
- Implement slippage limits
- Protect against frontrunning
- Add time-weighted average price (TWAP) oracle""",
        "difficulty": "expert",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MEVResistantDEX {
    struct Order {
        bytes32 commitment;
        address trader;
        uint256 commitTime;
        bool revealed;
    }
    
    mapping(bytes32 => Order) public orders;
    uint256 public constant COMMIT_DELAY = 2; // blocks
    
    // TODO: Implement commit-reveal pattern
    function commitOrder(bytes32 commitment) public {
        // Your code here
    }
    
    function revealOrder(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut,
        bytes32 salt
    ) public {
        // Your code here
        // Verify commitment matches reveal
        // Check time delay
        // Execute swap with protections
    }
    
    // TODO: Implement TWAP oracle
    // TODO: Implement slippage protection
}""",
        "test_cases": [
            {"input": "commitOrder(hash)", "expected": "committed"},
            {"input": "revealOrder(...) before delay", "expected": "reverted"},
            {"input": "revealOrder(...) after delay", "expected": "executed with protection"}
        ],
        "hints": [
            "Hash order params with salt for commitment",
            "Use block.number for timing",
            "Calculate price impact before execution",
            "Store historical prices for TWAP"
        ],
        "tags": ["mev", "dex", "advanced-security", "expert"],
        "solved_count": 34
    },

    # ============== RUST (SOLANA) PROBLEMS ==============
    {
        "problem_id": "rust_001",
        "title": "Solana Hello World",
        "description": """Create a basic Solana program that stores and retrieves a message.

Requirements:
- Use Anchor framework
- Create an account to store data
- Implement initialize instruction
- Implement set_message instruction
- Handle account validation""",
        "difficulty": "junior",
        "category": "rust",
        "initial_code": """use anchor_lang::prelude::*;

declare_id!("YourProgramIDHere");

#[program]
pub mod hello_solana {
    use super::*;

    // TODO: Implement initialize function
    pub fn initialize(ctx: Context<Initialize>) -> Result<()> {
        // Your code here
        Ok(())
    }

    // TODO: Implement set_message function
    pub fn set_message(ctx: Context<SetMessage>, message: String) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    // TODO: Define accounts
}

#[derive(Accounts)]
pub struct SetMessage<'info> {
    // TODO: Define accounts
}

#[account]
pub struct MessageAccount {
    // TODO: Define data structure
}""",
        "test_cases": [
            {"input": "initialize()", "expected": "account created"},
            {"input": "set_message('Hello Solana')", "expected": "message stored"}
        ],
        "hints": [
            "Use #[account(init)] for account creation",
            "Define payer and system_program",
            "Use String type for message storage"
        ],
        "tags": ["solana", "anchor", "basics"],
        "solved_count": 456
    },
    {
        "problem_id": "rust_002",
        "title": "Solana Token Transfer",
        "description": """Implement a program for SPL token transfers with validation.

Requirements:
- Transfer SPL tokens between accounts
- Validate token accounts
- Check sufficient balance
- Use Token Program correctly
- Handle PDA (Program Derived Address)""",
        "difficulty": "middle",
        "category": "rust",
        "initial_code": """use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Transfer};

declare_id!("YourProgramIDHere");

#[program]
pub mod token_transfer {
    use super::*;

    pub fn transfer_tokens(
        ctx: Context<TransferTokens>,
        amount: u64
    ) -> Result<()> {
        // TODO: Implement token transfer with validation
        Ok(())
    }
}

#[derive(Accounts)]
pub struct TransferTokens<'info> {
    // TODO: Define token accounts and validation
}""",
        "test_cases": [
            {"input": "transfer_tokens(1000)", "expected": "transferred"},
            {"input": "transfer_tokens(excessive_amount)", "expected": "error: insufficient balance"}
        ],
        "hints": [
            "Use anchor_spl::token::Transfer",
            "Validate token account ownership",
            "Use CpiContext for cross-program invocation"
        ],
        "tags": ["solana", "spl-token", "cpi"],
        "solved_count": 312
    },
    {
        "problem_id": "rust_003",
        "title": "Solana Staking Pool",
        "description": """Create a staking program where users can stake tokens and earn rewards.

Requirements:
- Implement stake() and unstake() functions
- Calculate rewards based on time staked
- Use PDA for vault account
- Handle reward distribution
- Prevent reentrancy""",
        "difficulty": "senior",
        "category": "rust",
        "initial_code": """use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount};

declare_id!("YourProgramIDHere");

#[program]
pub mod staking_pool {
    use super::*;

    // TODO: Implement staking logic
    pub fn stake(ctx: Context<Stake>, amount: u64) -> Result<()> {
        // Your code here
        Ok(())
    }

    pub fn unstake(ctx: Context<Unstake>) -> Result<()> {
        // Your code here
        Ok(())
    }

    pub fn claim_rewards(ctx: Context<ClaimRewards>) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[account]
pub struct StakeAccount {
    // TODO: Define staking data
}

#[account]
pub struct PoolAccount {
    // TODO: Define pool data
}""",
        "test_cases": [
            {"input": "stake(1000)", "expected": "staked, timestamp recorded"},
            {"input": "wait 30 days", "expected": "rewards accumulated"},
            {"input": "claim_rewards()", "expected": "rewards paid"}
        ],
        "hints": [
            "Use Clock sysvar for timestamps",
            "Calculate rewards: amount * time * rate",
            "Use seeds for PDA derivation"
        ],
        "tags": ["solana", "staking", "defi", "advanced"],
        "solved_count": 145
    },
    {
        "problem_id": "rust_004",
        "title": "Solana NFT Marketplace",
        "description": """Build an NFT marketplace with listing, buying, and royalty features.

Requirements:
- List NFT for sale
- Buy NFT with SOL
- Handle royalty payments
- Cancel listing
- Use Metaplex standard""",
        "difficulty": "expert",
        "category": "rust",
        "initial_code": """use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount};

declare_id!("YourProgramIDHere");

#[program]
pub mod nft_marketplace {
    use super::*;

    pub fn list_nft(ctx: Context<ListNFT>, price: u64) -> Result<()> {
        // TODO: Implement listing logic
        Ok(())
    }

    pub fn buy_nft(ctx: Context<BuyNFT>) -> Result<()> {
        // TODO: Implement buy logic with royalty
        Ok(())
    }

    pub fn cancel_listing(ctx: Context<CancelListing>) -> Result<()> {
        // TODO: Implement cancel logic
        Ok(())
    }
}

#[account]
pub struct Listing {
    seller: Pubkey,
    nft_mint: Pubkey,
    price: u64,
    created_at: i64,
}""",
        "test_cases": [
            {"input": "list_nft(price)", "expected": "listed"},
            {"input": "buy_nft()", "expected": "transferred, royalties paid"}
        ],
        "hints": [
            "Store listing in PDA",
            "Calculate royalty from metadata",
            "Transfer NFT after payment received"
        ],
        "tags": ["solana", "nft", "marketplace", "metaplex"],
        "solved_count": 89
    },

    # ============== FUNC (TON) PROBLEMS ==============
    {
        "problem_id": "ton_001",
        "title": "TON Counter Contract",
        "description": """Create a simple counter smart contract on TON blockchain.

Requirements:
- Store counter value
- Implement increment() function
- Implement get_counter() getter
- Handle internal messages
- Return counter value""",
        "difficulty": "junior",
        "category": "func",
        "initial_code": """() recv_internal(int msg_value, cell in_msg, slice in_msg_body) impure {
    ;; TODO: Parse incoming message
    ;; TODO: Handle increment command
}

int get_counter() method_id {
    ;; TODO: Return current counter value
}

() increment() impure {
    ;; TODO: Increment counter
}""",
        "test_cases": [
            {"input": "increment()", "expected": "counter = 1"},
            {"input": "increment()", "expected": "counter = 2"},
            {"input": "get_counter()", "expected": "2"}
        ],
        "hints": [
            "Use get_data() and set_data() for storage",
            "Parse integer from cell",
            "Store counter in c4 register"
        ],
        "tags": ["ton", "func", "basics"],
        "solved_count": 234
    },
    {
        "problem_id": "ton_002",
        "title": "TON Wallet",
        "description": """Implement a simple wallet contract that can send and receive TON.

Requirements:
- Accept incoming transfers
- Send outgoing transfers (owner only)
- Track balance
- Implement seqno for replay protection
- Handle multiple operations""",
        "difficulty": "middle",
        "category": "func",
        "initial_code": """#include "stdlib.fc";

() recv_internal(int msg_value, cell in_msg_full, slice in_msg_body) impure {
    ;; TODO: Accept and process incoming messages
}

() recv_external(slice in_msg) impure {
    ;; TODO: Handle external messages (sends)
    ;; TODO: Verify signature
    ;; TODO: Check seqno
}

int seqno() method_id {
    ;; TODO: Return current sequence number
}""",
        "test_cases": [
            {"input": "send_ton(dest, amount)", "expected": "sent, seqno++"},
            {"input": "replay_attack", "expected": "rejected"}
        ],
        "hints": [
            "Use check_signature() for verification",
            "Increment seqno after each operation",
            "Use send_raw_message() for sends"
        ],
        "tags": ["ton", "wallet", "security"],
        "solved_count": 167
    },
    {
        "problem_id": "ton_003",
        "title": "TON Jetton (Token)",
        "description": """Implement a fungible token (Jetton) on TON following the standard.

Requirements:
- Mint jettons
- Transfer between wallets
- Burn jettons
- Query balance
- Follow TEP-74 standard""",
        "difficulty": "senior",
        "category": "func",
        "initial_code": """#include "stdlib.fc";
#include "jetton-utils.fc";

() recv_internal(int msg_value, cell in_msg_full, slice in_msg_body) impure {
    slice cs = in_msg_full.begin_parse();
    int flags = cs~load_uint(4);
    slice sender_address = cs~load_msg_addr();
    
    int op = in_msg_body~load_uint(32);
    
    if (op == op::transfer) {
        ;; TODO: Implement transfer logic
    }
    
    if (op == op::burn) {
        ;; TODO: Implement burn logic
    }
}

(int, slice, slice, cell) get_wallet_data() method_id {
    ;; TODO: Return wallet data
}""",
        "test_cases": [
            {"input": "transfer(to, amount)", "expected": "transferred"},
            {"input": "burn(amount)", "expected": "supply decreased"}
        ],
        "hints": [
            "Follow TEP-74 Jetton standard",
            "Use jetton-wallet pattern",
            "Emit notifications for transfers"
        ],
        "tags": ["ton", "jetton", "token", "standard"],
        "solved_count": 98
    },

    # ============== GENERAL BLOCKCHAIN / CRYPTO PROBLEMS ==============
    {
        "problem_id": "crypto_001",
        "title": "Merkle Tree Verification",
        "description": """Implement a Merkle tree proof verification function.

Requirements:
- Given a leaf, root, and proof array
- Verify the leaf is part of the tree
- Compute intermediate hashes correctly
- Return true/false for valid/invalid proof""",
        "difficulty": "middle",
        "category": "cryptography",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MerkleProof {
    // TODO: Implement Merkle proof verification
    function verify(
        bytes32[] memory proof,
        bytes32 root,
        bytes32 leaf
    ) public pure returns (bool) {
        // Your code here
        // Hint: Hash pairs of nodes moving up the tree
    }
    
    // Helper: Hash two bytes32 values in sorted order
    function hashPair(bytes32 a, bytes32 b) private pure returns (bytes32) {
        // Your code here
    }
}""",
        "test_cases": [
            {"input": "verify(validProof, root, leaf)", "expected": "true"},
            {"input": "verify(invalidProof, root, leaf)", "expected": "false"}
        ],
        "hints": [
            "Sort hash pairs before hashing",
            "Use keccak256(abi.encodePacked(a, b))",
            "Iterate through proof array"
        ],
        "tags": ["cryptography", "merkle-tree", "algorithms"],
        "solved_count": 423
    },
    {
        "problem_id": "crypto_002",
        "title": "Signature Recovery",
        "description": """Implement ECDSA signature verification and address recovery.

Requirements:
- Recover signer address from signature
- Verify signature matches expected signer
- Handle message hashing correctly
- Use ecrecover properly""",
        "difficulty": "middle",
        "category": "cryptography",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SignatureVerifier {
    // TODO: Implement signature verification
    function verifySignature(
        address expectedSigner,
        bytes32 messageHash,
        uint8 v,
        bytes32 r,
        bytes32 s
    ) public pure returns (bool) {
        // Your code here
    }
    
    // TODO: Recover signer address
    function recoverSigner(
        bytes32 messageHash,
        uint8 v,
        bytes32 r,
        bytes32 s
    ) public pure returns (address) {
        // Your code here
    }
    
    // Helper: Create Ethereum signed message hash
    function getEthSignedMessageHash(bytes32 messageHash) public pure returns (bytes32) {
        // Your code here
    }
}""",
        "test_cases": [
            {"input": "recoverSigner(hash, v, r, s)", "expected": "correct_address"},
            {"input": "verifySignature(...)", "expected": "true"}
        ],
        "hints": [
            "Use ecrecover precompile",
            "Prepend '\\x19Ethereum Signed Message:\\n32'",
            "Validate v is 27 or 28"
        ],
        "tags": ["cryptography", "signatures", "ecdsa"],
        "solved_count": 345
    },
    {
        "problem_id": "crypto_003",
        "title": "Commit-Reveal Scheme",
        "description": """Implement a commit-reveal scheme for on-chain random number generation.

Requirements:
- Commit phase: hash(value + salt)
- Reveal phase: verify and use value
- Time-locked between phases
- Prevent early reveals
- Handle multiple participants""",
        "difficulty": "senior",
        "category": "cryptography",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CommitReveal {
    struct Commitment {
        bytes32 commitment;
        uint256 blockNumber;
        bool revealed;
    }
    
    mapping(address => Commitment) public commitments;
    uint256 public constant REVEAL_DELAY = 5; // blocks
    
    // TODO: Implement commit phase
    function commit(bytes32 commitment) public {
        // Your code here
    }
    
    // TODO: Implement reveal phase
    function reveal(uint256 value, bytes32 salt) public {
        // Your code here
        // Verify: keccak256(abi.encodePacked(value, salt)) == commitment
        // Check timing
    }
}""",
        "test_cases": [
            {"input": "commit(hash(42, salt))", "expected": "committed"},
            {"input": "reveal before delay", "expected": "reverted"},
            {"input": "reveal(42, salt) after delay", "expected": "revealed"}
        ],
        "hints": [
            "Store block.number at commit",
            "Verify block.number > commit_block + DELAY",
            "Check commitment hasn't been revealed"
        ],
        "tags": ["cryptography", "commit-reveal", "randomness"],
        "solved_count": 189
    },
    
    # ============== NEW SOLIDITY PROBLEMS - DEFI ==============
    {
        "problem_id": "sol_defi_001",
        "title": "Staking Contract with Rewards",
        "description": """Implement a staking contract where users can stake tokens and earn rewards over time.

Requirements:
- Allow users to stake ERC20 tokens
- Calculate rewards based on time staked
- Implement unstake with accumulated rewards
- Track total staked amount
- Prevent reentrancy attacks""",
        "difficulty": "middle",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IERC20 {
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function transfer(address to, uint256 amount) external returns (bool);
}

contract StakingContract {
    IERC20 public stakingToken;
    uint256 public rewardRate = 10; // 10% per year
    
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }
    
    mapping(address => Stake) public stakes;
    uint256 public totalStaked;
    
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    
    constructor(address _token) {
        stakingToken = IERC20(_token);
    }
    
    // TODO: Implement stake function
    function stake(uint256 amount) external {
        // Your code here
    }
    
    // TODO: Implement calculateReward function
    function calculateReward(address user) public view returns (uint256) {
        // Your code here
        // Formula: (amount * rewardRate * timeStaked) / (365 days * 100)
    }
    
    // TODO: Implement unstake function
    function unstake() external {
        // Your code here
        // Calculate and transfer reward + original stake
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "stake",
                "args": [1000],
                "expected": "success",
                "description": "Should stake tokens successfully"
            },
            {
                "type": "call",
                "function": "totalStaked",
                "args": [],
                "expected": "1000",
                "description": "Total staked should increase"
            }
        ],
        "hints": [
            "Use transferFrom to receive tokens from user",
            "Store block.timestamp when staking",
            "Calculate time difference for rewards",
            "Update state before external calls"
        ],
        "tags": ["defi", "staking", "rewards", "erc20"],
        "solved_count": 0
    },
    {
        "problem_id": "sol_defi_002",
        "title": "Simple Lending Protocol",
        "description": """Create a basic lending protocol where users can deposit collateral and borrow tokens.

Requirements:
- Deposit collateral (150% collateralization ratio)
- Borrow against collateral
- Repay loan with interest
- Liquidate undercollateralized positions
- Track health factor""",
        "difficulty": "senior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract LendingProtocol {
    struct Position {
        uint256 collateral;
        uint256 borrowed;
        uint256 borrowTimestamp;
    }
    
    mapping(address => Position) public positions;
    uint256 public constant COLLATERAL_RATIO = 150; // 150%
    uint256 public constant INTEREST_RATE = 5; // 5% per year
    uint256 public totalLiquidity;
    
    event Deposited(address indexed user, uint256 amount);
    event Borrowed(address indexed user, uint256 amount);
    event Repaid(address indexed user, uint256 amount, uint256 interest);
    event Liquidated(address indexed user, address indexed liquidator);
    
    // TODO: Implement deposit collateral
    function depositCollateral() external payable {
        // Your code here
    }
    
    // TODO: Implement borrow
    function borrow(uint256 amount) external {
        // Your code here
        // Check collateral ratio: collateral >= borrowed * 150 / 100
    }
    
    // TODO: Implement calculate interest
    function calculateInterest(address user) public view returns (uint256) {
        // Your code here
    }
    
    // TODO: Implement repay
    function repay() external payable {
        // Your code here
        // Repay borrowed + interest
    }
    
    // TODO: Implement liquidate
    function liquidate(address user) external {
        // Your code here
        // Check if position is undercollateralized
    }
    
    // TODO: Implement health factor
    function getHealthFactor(address user) public view returns (uint256) {
        // Your code here
        // healthFactor = (collateral * 100) / borrowed
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "depositCollateral",
                "args": [],
                "value": 1000,
                "expected": "success",
                "description": "Should deposit collateral"
            }
        ],
        "hints": [
            "Always check collateral ratio before borrowing",
            "Calculate interest based on time elapsed",
            "Health factor < 150 means undercollateralized",
            "Give liquidator incentive (bonus collateral)"
        ],
        "tags": ["defi", "lending", "collateral", "liquidation"],
        "solved_count": 0
    },
    {
        "problem_id": "sol_defi_003",
        "title": "Automated Market Maker (AMM)",
        "description": """Implement a simple constant product AMM (x * y = k) like Uniswap V1.

Requirements:
- Add liquidity (deposit both tokens)
- Remove liquidity (withdraw proportionally)
- Swap token A for token B
- Swap token B for token A
- Calculate output amount using x*y=k formula
- Track LP token shares""",
        "difficulty": "senior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IERC20 {
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function transfer(address to, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract SimpleAMM {
    IERC20 public tokenA;
    IERC20 public tokenB;
    
    uint256 public reserveA;
    uint256 public reserveB;
    uint256 public totalLiquidity;
    mapping(address => uint256) public liquidity;
    
    event LiquidityAdded(address indexed provider, uint256 amountA, uint256 amountB, uint256 liquidity);
    event LiquidityRemoved(address indexed provider, uint256 amountA, uint256 amountB, uint256 liquidity);
    event Swap(address indexed user, address indexed tokenIn, uint256 amountIn, uint256 amountOut);
    
    constructor(address _tokenA, address _tokenB) {
        tokenA = IERC20(_tokenA);
        tokenB = IERC20(_tokenB);
    }
    
    // TODO: Implement add liquidity
    function addLiquidity(uint256 amountA, uint256 amountB) external returns (uint256 liquidityMinted) {
        // Your code here
        // If first liquidity: liquidity = sqrt(amountA * amountB)
        // Else: liquidity = min(amountA * totalLiquidity / reserveA, amountB * totalLiquidity / reserveB)
    }
    
    // TODO: Implement remove liquidity
    function removeLiquidity(uint256 liquidityAmount) external returns (uint256 amountA, uint256 amountB) {
        // Your code here
        // amountA = liquidityAmount * reserveA / totalLiquidity
        // amountB = liquidityAmount * reserveB / totalLiquidity
    }
    
    // TODO: Implement get output amount (x*y=k)
    function getOutputAmount(uint256 inputAmount, uint256 inputReserve, uint256 outputReserve) public pure returns (uint256) {
        // Your code here
        // outputAmount = (inputAmount * outputReserve) / (inputReserve + inputAmount)
        // Apply 0.3% fee
    }
    
    // TODO: Implement swap A for B
    function swapAforB(uint256 amountAIn) external returns (uint256 amountBOut) {
        // Your code here
    }
    
    // TODO: Implement swap B for A
    function swapBforA(uint256 amountBIn) external returns (uint256 amountAOut) {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "addLiquidity",
                "args": [1000, 1000],
                "expected": "success",
                "description": "Should add initial liquidity"
            }
        ],
        "hints": [
            "Use sqrt for initial liquidity calculation",
            "Always maintain x*y=k constant product formula",
            "Apply 0.3% fee on swaps (multiply by 997/1000)",
            "Update reserves after each operation"
        ],
        "tags": ["defi", "amm", "dex", "liquidity"],
        "solved_count": 0
    },
    {
        "problem_id": "sol_defi_004",
        "title": "Yield Farming Contract",
        "description": """Create a yield farming contract where users stake LP tokens and earn reward tokens.

Requirements:
- Stake LP tokens
- Calculate rewards per block
- Distribute rewards proportionally to stake
- Implement emergency withdraw
- Track reward debt to prevent double claiming""",
        "difficulty": "expert",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IERC20 {
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function transfer(address to, uint256 amount) external returns (bool);
}

contract YieldFarm {
    IERC20 public lpToken;
    IERC20 public rewardToken;
    
    uint256 public rewardPerBlock = 10e18; // 10 tokens per block
    uint256 public lastRewardBlock;
    uint256 public accRewardPerShare; // Accumulated rewards per share, scaled by 1e12
    uint256 public totalStaked;
    
    struct UserInfo {
        uint256 amount;
        uint256 rewardDebt;
    }
    
    mapping(address => UserInfo) public userInfo;
    
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    
    constructor(address _lpToken, address _rewardToken) {
        lpToken = IERC20(_lpToken);
        rewardToken = IERC20(_rewardToken);
        lastRewardBlock = block.number;
    }
    
    // TODO: Implement update pool
    function updatePool() public {
        // Your code here
        // Calculate rewards since lastRewardBlock
        // Update accRewardPerShare
        // accRewardPerShare += (reward * 1e12) / totalStaked
    }
    
    // TODO: Implement pending rewards calculation
    function pendingReward(address _user) external view returns (uint256) {
        // Your code here
        // pending = (user.amount * accRewardPerShare / 1e12) - user.rewardDebt
    }
    
    // TODO: Implement stake
    function stake(uint256 amount) external {
        // Your code here
        // Update pool first
        // Transfer pending rewards if any
        // Update user.rewardDebt
    }
    
    // TODO: Implement withdraw
    function withdraw(uint256 amount) external {
        // Your code here
    }
    
    // TODO: Implement claim rewards
    function claimReward() external {
        // Your code here
    }
    
    // TODO: Implement emergency withdraw (no rewards)
    function emergencyWithdraw() external {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "stake",
                "args": [1000],
                "expected": "success",
                "description": "Should stake LP tokens"
            }
        ],
        "hints": [
            "Always call updatePool() before any state changes",
            "Use rewardDebt to track already claimed rewards",
            "Scale accRewardPerShare by 1e12 for precision",
            "pending = (amount * accRewardPerShare / 1e12) - rewardDebt"
        ],
        "tags": ["defi", "yield-farming", "staking", "rewards"],
        "solved_count": 0
    },
    
    # ============== NEW SOLIDITY PROBLEMS - NFT ==============
    {
        "problem_id": "sol_nft_001",
        "title": "Basic ERC721 NFT",
        "description": """Implement a basic ERC721 NFT contract with minting and metadata.

Requirements:
- Implement ERC721 interface
- Mint NFTs with auto-incrementing IDs
- Set and get token URI (metadata)
- Track token ownership
- Implement transfer functionality""",
        "difficulty": "junior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BasicNFT {
    string public name = "CodeChain NFT";
    string public symbol = "CCNFT";
    
    uint256 public tokenCounter;
    mapping(uint256 => address) public tokenOwner;
    mapping(address => uint256) public balanceOf;
    mapping(uint256 => string) public tokenURI;
    mapping(uint256 => address) public tokenApprovals;
    
    event Transfer(address indexed from, address indexed to, uint256 indexed tokenId);
    event Approval(address indexed owner, address indexed approved, uint256 indexed tokenId);
    
    // TODO: Implement mint function
    function mint(string memory _tokenURI) external returns (uint256) {
        // Your code here
        // Increment tokenCounter
        // Set owner and URI
        // Emit Transfer event
    }
    
    // TODO: Implement ownerOf function
    function ownerOf(uint256 tokenId) public view returns (address) {
        // Your code here
    }
    
    // TODO: Implement transfer function
    function transfer(address to, uint256 tokenId) external {
        // Your code here
        // Check ownership
        // Update balances
        // Emit event
    }
    
    // TODO: Implement approve function
    function approve(address to, uint256 tokenId) external {
        // Your code here
    }
    
    // TODO: Implement transferFrom function
    function transferFrom(address from, address to, uint256 tokenId) external {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "mint",
                "args": ["ipfs://QmExample"],
                "expected": "success",
                "description": "Should mint NFT successfully"
            },
            {
                "type": "call",
                "function": "tokenCounter",
                "args": [],
                "expected": "1",
                "description": "Token counter should increment"
            }
        ],
        "hints": [
            "Start tokenCounter at 0, increment before minting",
            "Check tokenOwner[tokenId] != address(0) for existence",
            "Update both sender and receiver balances",
            "Emit Transfer(address(0), to, tokenId) for minting"
        ],
        "tags": ["nft", "erc721", "tokens"],
        "solved_count": 0
    },
    {
        "problem_id": "sol_nft_002",
        "title": "ERC1155 Multi-Token",
        "description": """Implement an ERC1155 multi-token contract supporting both fungible and non-fungible tokens.

Requirements:
- Support multiple token types
- Implement batch minting
- Implement batch transfers
- Track balances per token ID
- Emit appropriate events""",
        "difficulty": "middle",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MultiToken {
    // Mapping from token ID to account balances
    mapping(uint256 => mapping(address => uint256)) public balances;
    
    // Mapping from account to operator approvals
    mapping(address => mapping(address => bool)) public operatorApprovals;
    
    event TransferSingle(address indexed operator, address indexed from, address indexed to, uint256 id, uint256 value);
    event TransferBatch(address indexed operator, address indexed from, address indexed to, uint256[] ids, uint256[] values);
    event ApprovalForAll(address indexed account, address indexed operator, bool approved);
    
    // TODO: Implement mint function
    function mint(address to, uint256 id, uint256 amount) external {
        // Your code here
    }
    
    // TODO: Implement mintBatch function
    function mintBatch(address to, uint256[] memory ids, uint256[] memory amounts) external {
        // Your code here
        // Check ids.length == amounts.length
    }
    
    // TODO: Implement balanceOf function
    function balanceOf(address account, uint256 id) external view returns (uint256) {
        // Your code here
    }
    
    // TODO: Implement safeTransferFrom function
    function safeTransferFrom(
        address from,
        address to,
        uint256 id,
        uint256 amount
    ) external {
        // Your code here
        // Check authorization (from == msg.sender or approved)
        // Check sufficient balance
    }
    
    // TODO: Implement safeBatchTransferFrom function
    function safeBatchTransferFrom(
        address from,
        address to,
        uint256[] memory ids,
        uint256[] memory amounts
    ) external {
        // Your code here
    }
    
    // TODO: Implement setApprovalForAll function
    function setApprovalForAll(address operator, bool approved) external {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "mint",
                "args": ["0x1234567890123456789012345678901234567890", 1, 100],
                "expected": "success",
                "description": "Should mint tokens"
            }
        ],
        "hints": [
            "ERC1155 allows multiple token IDs in one contract",
            "Balance is per (address, tokenId) pair",
            "Batch operations must check array lengths match",
            "Use require(from == msg.sender || operatorApprovals[from][msg.sender])"
        ],
        "tags": ["nft", "erc1155", "multi-token", "batch"],
        "solved_count": 0
    },
    {
        "problem_id": "sol_nft_003",
        "title": "NFT Marketplace",
        "description": """Create an NFT marketplace where users can list, buy, and auction NFTs.

Requirements:
- List NFT for fixed price
- Buy listed NFT
- Create auction with time limit
- Bid on auction
- Finalize auction (highest bidder wins)
- Cancel listing""",
        "difficulty": "senior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IERC721 {
    function transferFrom(address from, address to, uint256 tokenId) external;
    function ownerOf(uint256 tokenId) external view returns (address);
}

contract NFTMarketplace {
    struct Listing {
        address seller;
        uint256 price;
        bool active;
    }
    
    struct Auction {
        address seller;
        uint256 startPrice;
        uint256 highestBid;
        address highestBidder;
        uint256 endTime;
        bool active;
    }
    
    mapping(address => mapping(uint256 => Listing)) public listings;
    mapping(address => mapping(uint256 => Auction)) public auctions;
    
    event Listed(address indexed nft, uint256 indexed tokenId, uint256 price);
    event Sold(address indexed nft, uint256 indexed tokenId, address buyer, uint256 price);
    event AuctionCreated(address indexed nft, uint256 indexed tokenId, uint256 startPrice, uint256 endTime);
    event BidPlaced(address indexed nft, uint256 indexed tokenId, address bidder, uint256 amount);
    event AuctionFinalized(address indexed nft, uint256 indexed tokenId, address winner, uint256 amount);
    
    // TODO: Implement list NFT
    function listNFT(address nftContract, uint256 tokenId, uint256 price) external {
        // Your code here
        // Check ownership
        // Transfer NFT to marketplace
        // Create listing
    }
    
    // TODO: Implement buy NFT
    function buyNFT(address nftContract, uint256 tokenId) external payable {
        // Your code here
        // Check listing active
        // Check msg.value == price
        // Transfer NFT to buyer
        // Transfer ETH to seller
    }
    
    // TODO: Implement create auction
    function createAuction(
        address nftContract,
        uint256 tokenId,
        uint256 startPrice,
        uint256 duration
    ) external {
        // Your code here
    }
    
    // TODO: Implement bid
    function bid(address nftContract, uint256 tokenId) external payable {
        // Your code here
        // Check auction active
        // Check bid > highestBid
        // Refund previous bidder
        // Update highest bid
    }
    
    // TODO: Implement finalize auction
    function finalizeAuction(address nftContract, uint256 tokenId) external {
        // Your code here
        // Check auction ended (block.timestamp > endTime)
        // Transfer NFT to winner
        // Transfer ETH to seller
    }
    
    // TODO: Implement cancel listing
    function cancelListing(address nftContract, uint256 tokenId) external {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "listNFT",
                "args": ["0x1234567890123456789012345678901234567890", 1, 1000],
                "expected": "success",
                "description": "Should list NFT"
            }
        ],
        "hints": [
            "Always verify ownership before listing",
            "Store previous bidder to refund when new bid comes",
            "Use block.timestamp for auction timing",
            "Consider marketplace fee (e.g., 2.5%)"
        ],
        "tags": ["nft", "marketplace", "auction", "defi"],
        "solved_count": 0
    },
    
    # ============== NEW SOLIDITY PROBLEMS - DAO ==============
    {
        "problem_id": "sol_dao_001",
        "title": "Simple DAO Voting",
        "description": """Create a basic DAO with proposal creation and voting mechanism.

Requirements:
- Create proposals with description
- Vote on proposals (for/against)
- Execute passed proposals
- Token-weighted voting
- Quorum requirement""",
        "difficulty": "middle",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IGovernanceToken {
    function balanceOf(address account) external view returns (uint256);
}

contract SimpleDAO {
    IGovernanceToken public governanceToken;
    
    struct Proposal {
        string description;
        uint256 forVotes;
        uint256 againstVotes;
        uint256 deadline;
        bool executed;
        mapping(address => bool) hasVoted;
    }
    
    mapping(uint256 => Proposal) public proposals;
    uint256 public proposalCount;
    
    uint256 public constant VOTING_PERIOD = 3 days;
    uint256 public constant QUORUM = 1000; // Minimum votes needed
    
    event ProposalCreated(uint256 indexed proposalId, string description);
    event Voted(uint256 indexed proposalId, address indexed voter, bool support, uint256 weight);
    event ProposalExecuted(uint256 indexed proposalId);
    
    constructor(address _token) {
        governanceToken = IGovernanceToken(_token);
    }
    
    // TODO: Implement create proposal
    function createProposal(string memory description) external returns (uint256) {
        // Your code here
        // Increment proposalCount
        // Set deadline = block.timestamp + VOTING_PERIOD
    }
    
    // TODO: Implement vote
    function vote(uint256 proposalId, bool support) external {
        // Your code here
        // Check hasn't voted
        // Check before deadline
        // Get voter's token balance
        // Add votes based on token balance
    }
    
    // TODO: Implement execute proposal
    function executeProposal(uint256 proposalId) external {
        // Your code here
        // Check voting ended
        // Check not executed
        // Check quorum reached
        // Check forVotes > againstVotes
    }
    
    // TODO: Implement get proposal state
    function getProposalState(uint256 proposalId) external view returns (string memory) {
        // Your code here
        // Return: "Active", "Passed", "Rejected", "Executed"
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "createProposal",
                "args": ["Increase rewards"],
                "expected": "success",
                "description": "Should create proposal"
            }
        ],
        "hints": [
            "Use governance token balance as voting weight",
            "Check block.timestamp against deadline",
            "Quorum = forVotes + againstVotes >= QUORUM",
            "Prevent double voting with hasVoted mapping"
        ],
        "tags": ["dao", "governance", "voting"],
        "solved_count": 0
    },
    {
        "problem_id": "sol_dao_002",
        "title": "Timelock Controller",
        "description": """Implement a timelock controller for delayed execution of DAO proposals.

Requirements:
- Queue transactions with delay
- Execute after timelock period
- Cancel queued transactions
- Multi-sig approval
- Emit events for transparency""",
        "difficulty": "senior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TimelockController {
    uint256 public constant MINIMUM_DELAY = 2 days;
    uint256 public constant MAXIMUM_DELAY = 30 days;
    
    struct Transaction {
        address target;
        uint256 value;
        bytes data;
        uint256 executeTime;
        bool executed;
        bool cancelled;
    }
    
    mapping(bytes32 => Transaction) public transactions;
    mapping(address => bool) public admins;
    
    event TransactionQueued(bytes32 indexed txId, address indexed target, uint256 value, uint256 executeTime);
    event TransactionExecuted(bytes32 indexed txId);
    event TransactionCancelled(bytes32 indexed txId);
    
    modifier onlyAdmin() {
        require(admins[msg.sender], "Not admin");
        _;
    }
    
    constructor() {
        admins[msg.sender] = true;
    }
    
    // TODO: Implement queue transaction
    function queueTransaction(
        address target,
        uint256 value,
        bytes memory data,
        uint256 delay
    ) external onlyAdmin returns (bytes32) {
        // Your code here
        // Check delay within bounds
        // Calculate txId = keccak256(abi.encode(target, value, data, executeTime))
        // Store transaction
    }
    
    // TODO: Implement execute transaction
    function executeTransaction(bytes32 txId) external payable onlyAdmin {
        // Your code here
        // Check executeTime reached
        // Check not executed/cancelled
        // Execute call
        // Mark as executed
    }
    
    // TODO: Implement cancel transaction
    function cancelTransaction(bytes32 txId) external onlyAdmin {
        // Your code here
    }
    
    // TODO: Implement get transaction ID
    function getTransactionId(
        address target,
        uint256 value,
        bytes memory data,
        uint256 executeTime
    ) public pure returns (bytes32) {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "queueTransaction",
                "args": ["0x1234567890123456789012345678901234567890", 0, "0x", 172800],
                "expected": "success",
                "description": "Should queue transaction"
            }
        ],
        "hints": [
            "Use keccak256(abi.encode(...)) for unique transaction ID",
            "Check block.timestamp >= executeTime before execution",
            "Use (bool success, ) = target.call{value: value}(data)",
            "Emit events for off-chain monitoring"
        ],
        "tags": ["dao", "timelock", "governance", "security"],
        "solved_count": 0
    },
    
    # ============== NEW SOLIDITY PROBLEMS - SECURITY ==============
    {
        "problem_id": "sol_sec_001",
        "title": "Role-Based Access Control",
        "description": """Implement a flexible role-based access control system.

Requirements:
- Define multiple roles (admin, minter, pauser)
- Grant and revoke roles
- Check if address has role
- Implement role hierarchy
- Role-based function modifiers""",
        "difficulty": "junior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AccessControl {
    bytes32 public constant ADMIN_ROLE = keccak256("ADMIN");
    bytes32 public constant MINTER_ROLE = keccak256("MINTER");
    bytes32 public constant PAUSER_ROLE = keccak256("PAUSER");
    
    mapping(bytes32 => mapping(address => bool)) public roles;
    
    event RoleGranted(bytes32 indexed role, address indexed account);
    event RoleRevoked(bytes32 indexed role, address indexed account);
    
    constructor() {
        roles[ADMIN_ROLE][msg.sender] = true;
    }
    
    // TODO: Implement grant role
    function grantRole(bytes32 role, address account) external {
        // Your code here
        // Only admin can grant roles
    }
    
    // TODO: Implement revoke role
    function revokeRole(bytes32 role, address account) external {
        // Your code here
    }
    
    // TODO: Implement has role check
    function hasRole(bytes32 role, address account) public view returns (bool) {
        // Your code here
    }
    
    // TODO: Implement modifier for role check
    modifier onlyRole(bytes32 role) {
        // Your code here
        _;
    }
    
    // Example protected function
    function mintTokens(address to, uint256 amount) external onlyRole(MINTER_ROLE) {
        // Minting logic here
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "grantRole",
                "args": ["0x9f2df0fed2c77648de5860a4cc508cd0818c85b8b8a1ab4ceeef8d981c8956a6", "0x1234567890123456789012345678901234567890"],
                "expected": "success",
                "description": "Should grant minter role"
            },
            {
                "type": "call",
                "function": "hasRole",
                "args": ["0x9f2df0fed2c77648de5860a4cc508cd0818c85b8b8a1ab4ceeef8d981c8956a6", "0x1234567890123456789012345678901234567890"],
                "expected": "true",
                "description": "Should confirm role granted"
            }
        ],
        "hints": [
            "Use keccak256 for role identifiers",
            "Check hasRole(ADMIN_ROLE, msg.sender) before granting",
            "Emit events when roles change",
            "Use modifiers for cleaner code"
        ],
        "tags": ["security", "access-control", "roles"],
        "solved_count": 0
    },
    {
        "problem_id": "sol_sec_002",
        "title": "Safe Integer Operations",
        "description": """Implement safe math operations to prevent overflow/underflow attacks.

Requirements:
- Safe addition with overflow check
- Safe subtraction with underflow check
- Safe multiplication with overflow check
- Safe division with zero check
- Revert on unsafe operations""",
        "difficulty": "junior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Note: Solidity 0.8.0+ has built-in overflow checks
// This exercise teaches the concepts used in earlier versions

library SafeMath {
    // TODO: Implement safe add
    function add(uint256 a, uint256 b) internal pure returns (uint256) {
        // Your code here
        // Check: a + b >= a
    }
    
    // TODO: Implement safe subtract
    function sub(uint256 a, uint256 b) internal pure returns (uint256) {
        // Your code here
        // Check: b <= a
    }
    
    // TODO: Implement safe multiply
    function mul(uint256 a, uint256 b) internal pure returns (uint256) {
        // Your code here
        // Check: a == 0 || (a * b) / a == b
    }
    
    // TODO: Implement safe divide
    function div(uint256 a, uint256 b) internal pure returns (uint256) {
        // Your code here
        // Check: b > 0
    }
}

contract UseSafeMath {
    using SafeMath for uint256;
    
    uint256 public value;
    
    function safeAdd(uint256 amount) external {
        value = value.add(amount);
    }
    
    function safeSub(uint256 amount) external {
        value = value.sub(amount);
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "safeAdd",
                "args": [100],
                "expected": "success",
                "description": "Should add safely"
            }
        ],
        "hints": [
            "Check result >= original for addition",
            "Check a >= b before subtraction",
            "For multiplication, check result / a == b",
            "Solidity 0.8.0+ has automatic checks"
        ],
        "tags": ["security", "math", "overflow", "underflow"],
        "solved_count": 0
    },
    {
        "problem_id": "sol_sec_003",
        "title": "Prevent Front-Running",
        "description": """Implement protection against front-running attacks using commit-reveal.

Requirements:
- Commit phase: submit hash
- Reveal phase: reveal value after delay
- Verify commitment matches reveal
- Time-lock between phases
- Track commitments per user""",
        "difficulty": "middle",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Antifrontrunning {
    struct Commitment {
        bytes32 hash;
        uint256 timestamp;
        bool revealed;
        uint256 value;
    }
    
    mapping(address => Commitment) public commitments;
    uint256 public constant REVEAL_DELAY = 10; // blocks
    
    event Committed(address indexed user, bytes32 hash);
    event Revealed(address indexed user, uint256 value);
    
    // TODO: Implement commit
    function commit(bytes32 hash) external {
        // Your code here
        // Store hash and timestamp
    }
    
    // TODO: Implement reveal
    function reveal(uint256 value, bytes32 salt) external {
        // Your code here
        // Check delay passed: block.number >= timestamp + REVEAL_DELAY
        // Verify hash: keccak256(abi.encodePacked(value, salt)) == stored hash
        // Store value and mark revealed
    }
    
    // TODO: Implement get commitment hash
    function getCommitmentHash(uint256 value, bytes32 salt) public pure returns (bytes32) {
        // Your code here
    }
    
    // Example: Use revealed value
    function useValue(uint256 expectedValue) external view returns (bool) {
        require(commitments[msg.sender].revealed, "Not revealed");
        return commitments[msg.sender].value == expectedValue;
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "commit",
                "args": ["0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"],
                "expected": "success",
                "description": "Should commit hash"
            }
        ],
        "hints": [
            "Use block.number for timing (not timestamp)",
            "Hash = keccak256(abi.encodePacked(value, salt))",
            "Salt prevents rainbow table attacks",
            "Always check revealed flag before using value"
        ],
        "tags": ["security", "front-running", "commit-reveal"],
        "solved_count": 0
    },
    
    # ============== NEW SOLIDITY PROBLEMS - GAMES ==============
    {
        "problem_id": "sol_game_001",
        "title": "Lottery Contract",
        "description": """Create a provably fair lottery system with Chainlink VRF.

Requirements:
- Players buy tickets with ETH
- Random winner selection
- Distribute prize to winner
- Time-based rounds
- Refund if minimum players not met""",
        "difficulty": "middle",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Lottery {
    address[] public players;
    address public winner;
    uint256 public ticketPrice = 0.01 ether;
    uint256 public roundEndTime;
    uint256 public constant ROUND_DURATION = 1 days;
    uint256 public constant MIN_PLAYERS = 3;
    
    enum State { OPEN, DRAWING, CLOSED }
    State public state;
    
    event TicketPurchased(address indexed player);
    event WinnerSelected(address indexed winner, uint256 prize);
    event RoundStarted(uint256 endTime);
    
    constructor() {
        state = State.OPEN;
        roundEndTime = block.timestamp + ROUND_DURATION;
        emit RoundStarted(roundEndTime);
    }
    
    // TODO: Implement buy ticket
    function buyTicket() external payable {
        // Your code here
        // Check state is OPEN
        // Check msg.value == ticketPrice
        // Check round not ended
        // Add player to array
    }
    
    // TODO: Implement draw winner (simplified random - use Chainlink VRF in production)
    function drawWinner() external {
        // Your code here
        // Check round ended
        // Check minimum players
        // Generate random index
        // Select winner
        // Transfer prize
    }
    
    // TODO: Implement refund if min players not met
    function refund() external {
        // Your code here
        // Check round ended
        // Check players < MIN_PLAYERS
        // Refund all players
    }
    
    // TODO: Implement start new round
    function startNewRound() external {
        // Your code here
    }
    
    // Helper: Get player count
    function getPlayerCount() external view returns (uint256) {
        return players.length;
    }
    
    // Note: For production use Chainlink VRF for true randomness
    function pseudoRandom() private view returns (uint256) {
        return uint256(keccak256(abi.encodePacked(block.timestamp, block.prevrandao, players.length)));
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "buyTicket",
                "args": [],
                "value": 10000000000000000,
                "expected": "success",
                "description": "Should buy ticket"
            }
        ],
        "hints": [
            "Use array to store all players (not mapping)",
            "random % players.length gives random index",
            "Use Chainlink VRF for production randomness",
            "Clear players array after each round"
        ],
        "tags": ["game", "lottery", "random"],
        "solved_count": 0
    },
    {
        "problem_id": "sol_game_002",
        "title": "Rock Paper Scissors",
        "description": """Implement a fair Rock-Paper-Scissors game using commit-reveal.

Requirements:
- Two players commit their moves
- Reveal phase after both committed
- Determine winner
- Distribute prize
- Handle draw scenarios""",
        "difficulty": "senior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract RockPaperScissors {
    enum Move { None, Rock, Paper, Scissors }
    
    struct Game {
        address player1;
        address player2;
        bytes32 commit1;
        bytes32 commit2;
        Move move1;
        Move move2;
        uint256 bet;
        bool revealed1;
        bool revealed2;
        bool active;
    }
    
    mapping(uint256 => Game) public games;
    uint256 public gameCounter;
    
    event GameCreated(uint256 indexed gameId, address indexed player1, uint256 bet);
    event PlayerJoined(uint256 indexed gameId, address indexed player2);
    event MoveRevealed(uint256 indexed gameId, address indexed player);
    event GameFinished(uint256 indexed gameId, address indexed winner, uint256 prize);
    
    // TODO: Implement create game
    function createGame(bytes32 commitment) external payable returns (uint256) {
        // Your code here
        // Store commitment and bet amount
    }
    
    // TODO: Implement join game
    function joinGame(uint256 gameId, bytes32 commitment) external payable {
        // Your code here
        // Check msg.value matches bet
        // Store second player and commitment
    }
    
    // TODO: Implement reveal move
    function revealMove(uint256 gameId, Move move, bytes32 salt) external {
        // Your code here
        // Verify commitment: keccak256(abi.encodePacked(move, salt))
        // Store revealed move
        // If both revealed, determine winner
    }
    
    // TODO: Implement determine winner
    function determineWinner(uint256 gameId) private {
        // Your code here
        // Rock beats Scissors
        // Scissors beats Paper
        // Paper beats Rock
        // Handle draw (refund both)
    }
    
    // TODO: Helper to create commitment
    function getCommitment(Move move, bytes32 salt) public pure returns (bytes32) {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "createGame",
                "args": ["0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"],
                "value": 100000000000000000,
                "expected": "success",
                "description": "Should create game"
            }
        ],
        "hints": [
            "Use commit-reveal to prevent cheating",
            "Both players must commit before any reveal",
            "Winner logic: (move1 + 1) % 3 == move2 means move1 wins",
            "Refund both players on draw"
        ],
        "tags": ["game", "commit-reveal", "pvp"],
        "solved_count": 0
    },
    
    # ============== NEW SOLIDITY PROBLEMS - ORACLE ==============
    {
        "problem_id": "sol_oracle_001",
        "title": "Price Oracle",
        "description": """Implement a decentralized price oracle with multiple data sources.

Requirements:
- Accept price updates from authorized sources
- Calculate median price from multiple sources
- Implement time-weighted average price (TWAP)
- Detect and handle stale data
- Admin controls for data sources""",
        "difficulty": "expert",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract PriceOracle {
    struct PriceData {
        uint256 price;
        uint256 timestamp;
    }
    
    struct Observation {
        uint256 timestamp;
        uint256 priceCumulative;
    }
    
    mapping(address => bool) public authorizedSources;
    mapping(address => PriceData) public latestPrices;
    address[] public sources;
    
    Observation[] public observations;
    uint256 public constant MAX_PRICE_AGE = 1 hours;
    
    event PriceUpdated(address indexed source, uint256 price, uint256 timestamp);
    event SourceAdded(address indexed source);
    event SourceRemoved(address indexed source);
    
    // TODO: Implement add data source
    function addSource(address source) external {
        // Your code here
    }
    
    // TODO: Implement update price
    function updatePrice(uint256 price) external {
        // Your code here
        // Check authorized
        // Store price with timestamp
        // Update TWAP observations
    }
    
    // TODO: Implement get median price
    function getMedianPrice() public view returns (uint256) {
        // Your code here
        // Collect all non-stale prices
        // Sort and return median
    }
    
    // TODO: Implement TWAP
    function getTWAP(uint256 period) public view returns (uint256) {
        // Your code here
        // Calculate time-weighted average over period
    }
    
    // TODO: Implement is price stale
    function isPriceStale(address source) public view returns (bool) {
        // Your code here
        // Check if timestamp > MAX_PRICE_AGE old
    }
    
    // Helper: Sort array for median
    function sort(uint256[] memory arr) private pure returns (uint256[] memory) {
        // Simple bubble sort
        uint256 n = arr.length;
        for (uint256 i = 0; i < n - 1; i++) {
            for (uint256 j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    (arr[j], arr[j + 1]) = (arr[j + 1], arr[j]);
                }
            }
        }
        return arr;
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "addSource",
                "args": ["0x1234567890123456789012345678901234567890"],
                "expected": "success",
                "description": "Should add price source"
            }
        ],
        "hints": [
            "Median = middle value in sorted array",
            "TWAP = sum(price * duration) / total_duration",
            "Check block.timestamp - priceTimestamp <= MAX_AGE",
            "Need at least 3 sources for good median"
        ],
        "tags": ["oracle", "price-feed", "defi", "advanced"],
        "solved_count": 0
    },
    
    # ============== NEW RUST/SOLANA PROBLEMS ==============
    {
        "problem_id": "rust_003",
        "title": "Solana NFT Minting",
        "description": """Create a Solana program for minting NFTs using Metaplex standard.

Requirements:
- Initialize NFT collection
- Mint individual NFTs
- Set metadata URI
- Transfer NFTs
- Track total supply""",
        "difficulty": "middle",
        "category": "rust",
        "initial_code": """use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Mint};

declare_id!("YourProgramIDHere");

#[program]
pub mod nft_minting {
    use super::*;

    // TODO: Implement initialize collection
    pub fn initialize_collection(
        ctx: Context<InitializeCollection>,
        name: String,
        symbol: String,
    ) -> Result<()> {
        // Your code here
        Ok(())
    }

    // TODO: Implement mint NFT
    pub fn mint_nft(
        ctx: Context<MintNFT>,
        uri: String,
    ) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct InitializeCollection<'info> {
    // TODO: Define accounts
    #[account(init, payer = authority, space = 8 + 200)]
    pub collection: Account<'info, Collection>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct MintNFT<'info> {
    // TODO: Define accounts
}

#[account]
pub struct Collection {
    pub authority: Pubkey,
    pub name: String,
    pub symbol: String,
    pub total_minted: u64,
}

#[account]
pub struct NFTMetadata {
    pub uri: String,
    pub mint: Pubkey,
}""",
        "test_cases": [
            {"input": "initialize_collection('CodeChain NFT', 'CCNFT')", "expected": "collection created"},
            {"input": "mint_nft('ipfs://...')", "expected": "nft minted"}
        ],
        "hints": [
            "Use Anchor's init constraint for account creation",
            "Store collection authority as Pubkey",
            "Increment total_minted counter",
            "Use Token program for actual minting"
        ],
        "tags": ["solana", "nft", "metaplex", "anchor"],
        "solved_count": 0
    },
    {
        "problem_id": "rust_004",
        "title": "Solana Staking Program",
        "description": """Implement a token staking program with time-locked rewards.

Requirements:
- Stake SPL tokens
- Calculate rewards based on time
- Unstake with rewards
- Handle multiple stakers
- Implement reward pool""",
        "difficulty": "senior",
        "category": "rust",
        "initial_code": """use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount};

declare_id!("YourProgramIDHere");

#[program]
pub mod staking {
    use super::*;

    // TODO: Implement initialize pool
    pub fn initialize_pool(ctx: Context<InitializePool>, reward_rate: u64) -> Result<()> {
        // Your code here
        Ok(())
    }

    // TODO: Implement stake
    pub fn stake(ctx: Context<Stake>, amount: u64) -> Result<()> {
        // Your code here
        // Transfer tokens to pool
        // Record stake timestamp
        Ok(())
    }

    // TODO: Implement calculate rewards
    pub fn calculate_rewards(ctx: Context<CalculateRewards>) -> Result<u64> {
        // Your code here
        // rewards = amount * time_staked * reward_rate / SECONDS_PER_YEAR
        Ok(0)
    }

    // TODO: Implement unstake
    pub fn unstake(ctx: Context<Unstake>) -> Result<()> {
        // Your code here
        // Calculate rewards
        // Transfer stake + rewards back
        Ok(())
    }
}

#[derive(Accounts)]
pub struct InitializePool<'info> {
    #[account(init, payer = authority, space = 8 + 200)]
    pub pool: Account<'info, StakingPool>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Stake<'info> {
    #[account(mut)]
    pub pool: Account<'info, StakingPool>,
    #[account(init_if_needed, payer = user, space = 8 + 200)]
    pub stake_account: Account<'info, StakeAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub token_program: Program<'info, Token>,
    pub system_program: Program<'info, System>,
}

#[account]
pub struct StakingPool {
    pub authority: Pubkey,
    pub reward_rate: u64,
    pub total_staked: u64,
}

#[account]
pub struct StakeAccount {
    pub owner: Pubkey,
    pub amount: u64,
    pub stake_timestamp: i64,
}""",
        "test_cases": [
            {"input": "initialize_pool(10)", "expected": "pool created"},
            {"input": "stake(1000)", "expected": "tokens staked"},
            {"input": "unstake() after 1 year", "expected": "tokens + 10% reward returned"}
        ],
        "hints": [
            "Use Clock::get()? for timestamps",
            "Store stake_timestamp as i64",
            "Calculate time_diff = current_time - stake_timestamp",
            "Use token::transfer for moving tokens"
        ],
        "tags": ["solana", "staking", "defi", "anchor"],
        "solved_count": 0
    },
    {
        "problem_id": "rust_005",
        "title": "Solana Escrow",
        "description": """Create an escrow program for secure peer-to-peer token swaps.

Requirements:
- Initialize escrow with terms
- Deposit tokens to escrow
- Accept/cancel escrow
- Automatic refund on timeout
- Handle PDA properly""",
        "difficulty": "senior",
        "category": "rust",
        "initial_code": """use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Transfer};

declare_id!("YourProgramIDHere");

#[program]
pub mod escrow {
    use super::*;

    // TODO: Implement initialize escrow
    pub fn initialize_escrow(
        ctx: Context<InitializeEscrow>,
        amount: u64,
        timeout: i64,
    ) -> Result<()> {
        // Your code here
        Ok(())
    }

    // TODO: Implement accept escrow
    pub fn accept_escrow(ctx: Context<AcceptEscrow>) -> Result<()> {
        // Your code here
        // Verify conditions
        // Transfer tokens to both parties
        Ok(())
    }

    // TODO: Implement cancel escrow
    pub fn cancel_escrow(ctx: Context<CancelEscrow>) -> Result<()> {
        // Your code here
        // Check timeout or initiator
        // Refund tokens
        Ok(())
    }
}

#[derive(Accounts)]
pub struct InitializeEscrow<'info> {
    #[account(init, payer = initiator, space = 8 + 300)]
    pub escrow: Account<'info, EscrowAccount>,
    #[account(mut)]
    pub initiator: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct AcceptEscrow<'info> {
    #[account(mut)]
    pub escrow: Account<'info, EscrowAccount>,
    pub acceptor: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

#[derive(Accounts)]
pub struct CancelEscrow<'info> {
    #[account(mut, close = initiator)]
    pub escrow: Account<'info, EscrowAccount>,
    pub initiator: Signer<'info>,
}

#[account]
pub struct EscrowAccount {
    pub initiator: Pubkey,
    pub acceptor: Pubkey,
    pub amount: u64,
    pub timeout: i64,
    pub is_active: bool,
}""",
        "test_cases": [
            {"input": "initialize_escrow(1000, timeout)", "expected": "escrow created"},
            {"input": "accept_escrow()", "expected": "tokens swapped"},
            {"input": "cancel_escrow() after timeout", "expected": "tokens refunded"}
        ],
        "hints": [
            "Use PDA for escrow token account",
            "Check Clock::get()?.unix_timestamp for timeout",
            "Only initiator can cancel before timeout",
            "Anyone can cancel after timeout",
            "Use close constraint to reclaim rent"
        ],
        "tags": ["solana", "escrow", "swap", "pda"],
        "solved_count": 0
    },
    {
        "problem_id": "rust_006",
        "title": "Solana DAO Voting",
        "description": """Implement a DAO voting mechanism on Solana.

Requirements:
- Create proposals
- Vote with token weight
- Calculate vote results
- Execute passed proposals
- Time-locked voting periods""",
        "difficulty": "expert",
        "category": "rust",
        "initial_code": """use anchor_lang::prelude::*;

declare_id!("YourProgramIDHere");

#[program]
pub mod dao_voting {
    use super::*;

    // TODO: Implement create proposal
    pub fn create_proposal(
        ctx: Context<CreateProposal>,
        description: String,
        voting_period: i64,
    ) -> Result<()> {
        // Your code here
        Ok(())
    }

    // TODO: Implement vote
    pub fn vote(
        ctx: Context<Vote>,
        support: bool,
    ) -> Result<()> {
        // Your code here
        // Get voter's token balance as voting weight
        // Record vote
        Ok(())
    }

    // TODO: Implement execute proposal
    pub fn execute_proposal(ctx: Context<ExecuteProposal>) -> Result<()> {
        // Your code here
        // Check voting ended
        // Check votes_for > votes_against
        // Execute
        Ok(())
    }
}

#[derive(Accounts)]
pub struct CreateProposal<'info> {
    #[account(init, payer = proposer, space = 8 + 500)]
    pub proposal: Account<'info, Proposal>,
    #[account(mut)]
    pub proposer: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Vote<'info> {
    #[account(mut)]
    pub proposal: Account<'info, Proposal>,
    pub voter: Signer<'info>,
}

#[account]
pub struct Proposal {
    pub description: String,
    pub proposer: Pubkey,
    pub votes_for: u64,
    pub votes_against: u64,
    pub end_time: i64,
    pub executed: bool,
}""",
        "test_cases": [
            {"input": "create_proposal('Increase rewards', 7_days)", "expected": "proposal created"},
            {"input": "vote(true)", "expected": "vote recorded"},
            {"input": "execute_proposal()", "expected": "proposal executed"}
        ],
        "hints": [
            "Store end_time = Clock::get()?.unix_timestamp + voting_period",
            "Use token balance as voting weight",
            "Prevent double voting with HashMap",
            "Check end_time before execution"
        ],
        "tags": ["solana", "dao", "voting", "governance"],
        "solved_count": 0
    },
    {
        "problem_id": "rust_007",
        "title": "Solana Token Vesting",
        "description": """Create a token vesting program with linear unlock schedule.

Requirements:
- Initialize vesting schedule
- Calculate unlocked amount based on time
- Claim unlocked tokens
- Support cliff period
- Handle multiple beneficiaries""",
        "difficulty": "expert",
        "category": "rust",
        "initial_code": """use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Transfer};

declare_id!("YourProgramIDHere");

#[program]
pub mod token_vesting {
    use super::*;

    // TODO: Implement create vesting
    pub fn create_vesting(
        ctx: Context<CreateVesting>,
        total_amount: u64,
        start_time: i64,
        cliff_duration: i64,
        vesting_duration: i64,
    ) -> Result<()> {
        // Your code here
        Ok(())
    }

    // TODO: Implement calculate vested amount
    pub fn calculate_vested(
        start_time: i64,
        cliff_duration: i64,
        vesting_duration: i64,
        total_amount: u64,
        current_time: i64,
    ) -> u64 {
        // Your code here
        // Before cliff: 0
        // After cliff, linear: (current_time - start_time) * total_amount / vesting_duration
        0
    }

    // TODO: Implement claim tokens
    pub fn claim(ctx: Context<Claim>) -> Result<()> {
        // Your code here
        // Calculate vested amount
        // Subtract already claimed
        // Transfer claimable amount
        Ok(())
    }
}

#[derive(Accounts)]
pub struct CreateVesting<'info> {
    #[account(init, payer = authority, space = 8 + 300)]
    pub vesting: Account<'info, VestingAccount>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub beneficiary: AccountInfo<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Claim<'info> {
    #[account(mut)]
    pub vesting: Account<'info, VestingAccount>,
    pub beneficiary: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

#[account]
pub struct VestingAccount {
    pub beneficiary: Pubkey,
    pub total_amount: u64,
    pub claimed_amount: u64,
    pub start_time: i64,
    pub cliff_duration: i64,
    pub vesting_duration: i64,
}""",
        "test_cases": [
            {"input": "create_vesting(1000, now, 30_days, 365_days)", "expected": "vesting created"},
            {"input": "claim() before cliff", "expected": "0 tokens"},
            {"input": "claim() at 50% duration", "expected": "~500 tokens"}
        ],
        "hints": [
            "Cliff: no tokens until cliff_duration passes",
            "Linear vesting: proportional to time passed",
            "Track claimed_amount to prevent double claims",
            "claimable = vested - claimed"
        ],
        "tags": ["solana", "vesting", "tokens", "time-lock"],
        "solved_count": 0
    },
    {
        "problem_id": "rust_008",
        "title": "Solana Flash Loan",
        "description": """Implement a flash loan protocol on Solana.

Requirements:
- Borrow any amount within single transaction
- Execute callback to borrower program
- Verify loan + fee repaid
- Revert if not repaid
- Track flash loan statistics""",
        "difficulty": "expert",
        "category": "rust",
        "initial_code": """use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Transfer};

declare_id!("YourProgramIDHere");

#[program]
pub mod flash_loan {
    use super::*;

    // TODO: Implement initialize pool
    pub fn initialize_pool(ctx: Context<InitializePool>, fee_rate: u64) -> Result<()> {
        // Your code here
        // fee_rate in basis points (e.g., 9 = 0.09%)
        Ok(())
    }

    // TODO: Implement flash loan
    pub fn flash_loan(
        ctx: Context<FlashLoan>,
        amount: u64,
    ) -> Result<()> {
        // Your code here
        // 1. Transfer amount to borrower
        // 2. Execute borrower callback (CPI)
        // 3. Verify repayment + fee
        // 4. If not repaid, transaction reverts
        Ok(())
    }

    // Helper: Calculate fee
    fn calculate_fee(amount: u64, fee_rate: u64) -> u64 {
        amount * fee_rate / 10000
    }
}

#[derive(Accounts)]
pub struct InitializePool<'info> {
    #[account(init, payer = authority, space = 8 + 200)]
    pub pool: Account<'info, FlashLoanPool>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct FlashLoan<'info> {
    #[account(mut)]
    pub pool: Account<'info, FlashLoanPool>,
    #[account(mut)]
    pub pool_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub borrower_token_account: Account<'info, TokenAccount>,
    pub borrower: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

#[account]
pub struct FlashLoanPool {
    pub authority: Pubkey,
    pub fee_rate: u64,
    pub total_borrowed: u64,
    pub total_fees: u64,
}""",
        "test_cases": [
            {"input": "initialize_pool(9)", "expected": "pool created with 0.09% fee"},
            {"input": "flash_loan(1000)", "expected": "loan + fee must be repaid in same tx"}
        ],
        "hints": [
            "Flash loan must complete in one transaction",
            "Use CPI (Cross-Program Invocation) for callback",
            "Check balance before and after callback",
            "Difference must be >= amount + fee"
        ],
        "tags": ["solana", "flash-loan", "defi", "advanced"],
        "solved_count": 0
    },
    
    # ============== NEW FUNC/TON PROBLEMS ==============
    {
        "problem_id": "ton_001",
        "title": "TON Simple Wallet",
        "description": """Create a basic TON wallet contract in FunC.

Requirements:
- Receive internal messages
- Send messages to other contracts
- Check sender authorization
- Store owner address
- Handle balance""",
        "difficulty": "junior",
        "category": "func",
        "initial_code": """#include "stdlib.fc";

;; Storage layout:
;; owner_address - 256 bits

() recv_internal(int msg_value, cell in_msg_full, slice in_msg_body) impure {
    ;; TODO: Implement message handler
    ;; Parse sender
    ;; Check authorization
    ;; Handle commands
}

() recv_external(slice in_msg) impure {
    ;; TODO: Implement external message handler
}

;; TODO: Implement send message
() send_message(slice dest_addr, int amount, int mode) impure {
    ;; Your code here
}

;; TODO: Implement get owner
slice get_owner() method_id {
    ;; Your code here
    ;; Load from storage
}""",
        "test_cases": [
            {"input": "deploy contract", "expected": "contract deployed"},
            {"input": "send_message(addr, 100)", "expected": "message sent"},
            {"input": "unauthorized send", "expected": "rejected"}
        ],
        "hints": [
            "Use begin_parse() for slices",
            "Use load_msg_addr() for addresses",
            "Use send_raw_message() for sending",
            "Store owner in c4 register"
        ],
        "tags": ["ton", "func", "wallet", "basics"],
        "solved_count": 0
    },
    {
        "problem_id": "ton_002",
        "title": "TON Jetton (Token)",
        "description": """Implement a TON Jetton (fungible token) contract.

Requirements:
- Mint tokens to address
- Transfer tokens between addresses
- Track balances
- Emit notifications
- Follow TEP-74 standard""",
        "difficulty": "middle",
        "category": "func",
        "initial_code": """#include "stdlib.fc";

;; Storage:
;; total_supply - 64 bits
;; admin_address - 256 bits
;; content - cell (metadata)

() recv_internal(int msg_value, cell in_msg_full, slice in_msg_body) impure {
    ;; TODO: Parse operation
    int op = in_msg_body~load_uint(32);
    
    if (op == 0x0f8a7ea5) {  ;; transfer
        ;; TODO: Implement transfer
    }
    
    if (op == 21) {  ;; mint (only admin)
        ;; TODO: Implement mint
    }
}

;; TODO: Implement get balance
int get_balance(slice owner_address) method_id {
    ;; Your code here
    return 0;
}

;; TODO: Implement get total supply
int get_total_supply() method_id {
    ;; Your code here
    return 0;
}""",
        "test_cases": [
            {"input": "mint(1000)", "expected": "tokens minted"},
            {"input": "transfer(addr, 100)", "expected": "tokens transferred"},
            {"input": "get_balance(addr)", "expected": "100"}
        ],
        "hints": [
            "Use dict for storing balances",
            "Follow TEP-74 Jetton standard",
            "Use op codes for operations",
            "Store data in c4 register"
        ],
        "tags": ["ton", "func", "jetton", "token"],
        "solved_count": 0
    },
    {
        "problem_id": "ton_003",
        "title": "TON NFT Collection",
        "description": """Create an NFT collection contract following TEP-62.

Requirements:
- Deploy NFT items
- Track collection metadata
- Implement get_nft_address_by_index
- Royalty support
- Batch operations""",
        "difficulty": "senior",
        "category": "func",
        "initial_code": """#include "stdlib.fc";

;; Storage:
;; next_item_index - 64 bits
;; collection_content - cell
;; owner_address - 256 bits

() recv_internal(int msg_value, cell in_msg_full, slice in_msg_body) impure {
    int op = in_msg_body~load_uint(32);
    
    if (op == 1) {  ;; deploy NFT
        ;; TODO: Implement NFT deployment
        ;; Calculate NFT address
        ;; Send deploy message
        ;; Increment index
    }
}

;; TODO: Implement get NFT address by index
slice get_nft_address_by_index(int index) method_id {
    ;; Your code here
    ;; Calculate deterministic address from collection + index
}

;; TODO: Implement get collection data
(int, cell, slice) get_collection_data() method_id {
    ;; Return: (next_item_index, collection_content, owner_address)
}

;; TODO: Implement get NFT content
cell get_nft_content(int index, cell individual_content) method_id {
    ;; Your code here
    ;; Combine collection content + individual content
}""",
        "test_cases": [
            {"input": "deploy_nft(metadata)", "expected": "NFT deployed"},
            {"input": "get_nft_address_by_index(0)", "expected": "correct address"},
            {"input": "get_collection_data()", "expected": "collection info"}
        ],
        "hints": [
            "Follow TEP-62 NFT standard",
            "Use STATEINIT for deterministic addresses",
            "Store collection base URI in content cell",
            "Each NFT is a separate contract"
        ],
        "tags": ["ton", "func", "nft", "collection"],
        "solved_count": 0
    },
    {
        "problem_id": "ton_004",
        "title": "TON Multisig Wallet",
        "description": """Implement a multi-signature wallet on TON.

Requirements:
- Multiple owners (k-of-n signatures)
- Submit transaction proposal
- Approve transaction
- Execute when threshold met
- Cancel transaction""",
        "difficulty": "senior",
        "category": "func",
        "initial_code": """#include "stdlib.fc";

;; Storage:
;; owners - dictionary
;; required_confirmations - 8 bits
;; transaction_count - 32 bits
;; transactions - dictionary

() recv_internal(int msg_value, cell in_msg_full, slice in_msg_body) impure {
    int op = in_msg_body~load_uint(32);
    
    if (op == 1) {  ;; submit transaction
        ;; TODO: Implement submit
    }
    
    if (op == 2) {  ;; confirm transaction
        ;; TODO: Implement confirm
        ;; Check if sender is owner
        ;; Add confirmation
        ;; Execute if threshold met
    }
    
    if (op == 3) {  ;; execute transaction
        ;; TODO: Implement execute
    }
}

;; TODO: Implement is owner
int is_owner(slice address) method_id {
    ;; Your code here
}

;; TODO: Implement get confirmations
int get_confirmations(int tx_id) method_id {
    ;; Your code here
}""",
        "test_cases": [
            {"input": "submit_transaction(dest, amount)", "expected": "tx created"},
            {"input": "confirm by owner1", "expected": "confirmation added"},
            {"input": "confirm by owner2", "expected": "tx executed"}
        ],
        "hints": [
            "Use dict for owners and transactions",
            "Store confirmations as bitmap",
            "Count bits to check threshold",
            "Use send_raw_message for execution"
        ],
        "tags": ["ton", "func", "multisig", "security"],
        "solved_count": 0
    },
    {
        "problem_id": "ton_005",
        "title": "TON DEX Swap",
        "description": """Create a simple DEX swap contract on TON.

Requirements:
- Add liquidity (provide token pairs)
- Remove liquidity
- Swap token A for token B
- Calculate output amount (constant product)
- Track LP shares""",
        "difficulty": "expert",
        "category": "func",
        "initial_code": """#include "stdlib.fc";

;; Storage:
;; reserve_a - 64 bits
;; reserve_b - 64 bits
;; total_lp_supply - 64 bits
;; lp_balances - dictionary

() recv_internal(int msg_value, cell in_msg_full, slice in_msg_body) impure {
    int op = in_msg_body~load_uint(32);
    
    if (op == 1) {  ;; add liquidity
        ;; TODO: Implement add liquidity
        ;; Calculate LP tokens to mint
        ;; Update reserves
    }
    
    if (op == 2) {  ;; swap
        ;; TODO: Implement swap
        ;; Calculate output using x*y=k
        ;; Apply 0.3% fee
        ;; Update reserves
    }
    
    if (op == 3) {  ;; remove liquidity
        ;; TODO: Implement remove liquidity
    }
}

;; TODO: Implement get reserves
(int, int) get_reserves() method_id {
    ;; Return (reserve_a, reserve_b)
}

;; TODO: Implement calculate output amount
int get_amount_out(int amount_in, int reserve_in, int reserve_out) method_id {
    ;; Your code here
    ;; Formula: (amount_in * 997 * reserve_out) / (reserve_in * 1000 + amount_in * 997)
}""",
        "test_cases": [
            {"input": "add_liquidity(1000, 1000)", "expected": "LP tokens minted"},
            {"input": "swap_a_for_b(100)", "expected": "tokens swapped"},
            {"input": "get_reserves()", "expected": "updated reserves"}
        ],
        "hints": [
            "Use x*y=k constant product formula",
            "Apply 0.3% fee: multiply by 997/1000",
            "LP tokens = sqrt(amount_a * amount_b) for first deposit",
            "Store reserves and LP supply in storage"
        ],
        "tags": ["ton", "func", "dex", "defi", "amm"],
        "solved_count": 0
    },
    
    # ============== NEW CRYPTOGRAPHY PROBLEMS ==============
    {
        "problem_id": "crypto_004",
        "title": "Hash Chain Verification",
        "description": """Implement a hash chain for sequential data verification.

Requirements:
- Create hash chain from data array
- Verify element at position
- Support efficient proofs
- Prevent tampering
- Handle large chains""",
        "difficulty": "middle",
        "category": "cryptography",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract HashChain {
    // Each element: hash(previous_hash + data)
    bytes32 public chainHead;
    uint256 public chainLength;
    
    event ElementAdded(uint256 indexed index, bytes32 hash);
    
    // TODO: Implement initialize chain
    function initializeChain(bytes32 firstHash) external {
        // Your code here
    }
    
    // TODO: Implement add element
    function addElement(bytes memory data) external returns (bytes32) {
        // Your code here
        // newHash = keccak256(abi.encodePacked(chainHead, data))
    }
    
    // TODO: Implement verify chain
    function verifyChain(
        bytes32 startHash,
        bytes[] memory data
    ) public pure returns (bytes32) {
        // Your code here
        // Recompute chain and return final hash
    }
    
    // TODO: Implement verify element at position
    function verifyElement(
        bytes32 startHash,
        bytes[] memory precedingData,
        bytes memory element
    ) public pure returns (bool) {
        // Your code here
    }
}""",
        "test_cases": [
            {"input": "initializeChain(genesis_hash)", "expected": "chain started"},
            {"input": "addElement('data1')", "expected": "element added"},
            {"input": "verifyChain(genesis, [data1, data2])", "expected": "true"}
        ],
        "hints": [
            "Hash = keccak256(abi.encodePacked(prev_hash, data))",
            "Store only the head for space efficiency",
            "To verify, recompute entire chain",
            "Each link depends on previous"
        ],
        "tags": ["cryptography", "hash-chain", "verification"],
        "solved_count": 0
    },
    {
        "problem_id": "crypto_005",
        "title": "Zero-Knowledge Proof Verifier",
        "description": """Implement a simple ZK proof verifier for age verification without revealing exact age.

Requirements:
- Prove age > threshold without revealing age
- Use commitment scheme
- Verify proof on-chain
- Prevent replay attacks
- Support multiple proofs""",
        "difficulty": "expert",
        "category": "cryptography",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AgeVerifier {
    mapping(address => bytes32) public commitments;
    mapping(bytes32 => bool) public usedProofs;
    
    event CommitmentCreated(address indexed user, bytes32 commitment);
    event ProofVerified(address indexed user, bool result);
    
    // TODO: Implement create commitment
    function createCommitment(bytes32 commitment) external {
        // Your code here
        // commitment = keccak256(abi.encodePacked(age, salt))
    }
    
    // TODO: Implement verify age > threshold
    function verifyAgeAboveThreshold(
        uint256 age,
        bytes32 salt,
        uint256 threshold
    ) external returns (bool) {
        // Your code here
        // 1. Verify commitment: keccak256(age, salt) == stored commitment
        // 2. Check age > threshold
        // 3. Don't reveal exact age
        // 4. Mark proof as used
    }
    
    // TODO: Implement check if proof used
    function isProofUsed(bytes32 proofId) external view returns (bool) {
        // Your code here
    }
}""",
        "test_cases": [
            {"input": "createCommitment(hash(25, salt))", "expected": "commitment stored"},
            {"input": "verifyAgeAboveThreshold(25, salt, 18)", "expected": "true"},
            {"input": "verify same proof again", "expected": "rejected (replay)"}
        ],
        "hints": [
            "Use commit-reveal pattern",
            "Don't store actual age on-chain",
            "Check commitment before verifying",
            "Use nonce or timestamp to prevent replay"
        ],
        "tags": ["cryptography", "zero-knowledge", "privacy", "advanced"],
        "solved_count": 0
    },
    {
        "problem_id": "crypto_006",
        "title": "Multi-Hash Verification",
        "description": """Implement a system supporting multiple hash algorithms for verification.

Requirements:
- Support SHA256, Keccak256, RIPEMD160
- Verify data against multiple hashes
- Implement hash function selector
- Compare hash outputs
- Gas-efficient implementation""",
        "difficulty": "middle",
        "category": "cryptography",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MultiHashVerifier {
    enum HashAlgorithm { KECCAK256, SHA256, RIPEMD160 }
    
    struct HashData {
        HashAlgorithm algorithm;
        bytes32 hash;
    }
    
    mapping(uint256 => HashData) public storedHashes;
    uint256 public hashCount;
    
    event HashStored(uint256 indexed id, HashAlgorithm algorithm, bytes32 hash);
    event HashVerified(uint256 indexed id, bool result);
    
    // TODO: Implement store hash
    function storeHash(HashAlgorithm algorithm, bytes memory data) external returns (uint256) {
        // Your code here
        // Calculate hash based on algorithm
        // Store and return ID
    }
    
    // TODO: Implement verify data
    function verifyData(uint256 hashId, bytes memory data) external returns (bool) {
        // Your code here
        // Recalculate hash using stored algorithm
        // Compare with stored hash
    }
    
    // TODO: Implement calculate hash
    function calculateHash(
        HashAlgorithm algorithm,
        bytes memory data
    ) public pure returns (bytes32) {
        // Your code here
        if (algorithm == HashAlgorithm.KECCAK256) {
            return keccak256(data);
        } else if (algorithm == HashAlgorithm.SHA256) {
            return sha256(data);
        } else if (algorithm == HashAlgorithm.RIPEMD160) {
            return ripemd160(data);
        }
    }
}""",
        "test_cases": [
            {"input": "storeHash(KECCAK256, 'data')", "expected": "hash stored"},
            {"input": "verifyData(id, 'data')", "expected": "true"},
            {"input": "verifyData(id, 'wrong')", "expected": "false"}
        ],
        "hints": [
            "Solidity supports keccak256, sha256, ripemd160",
            "Use enum to select algorithm",
            "RIPEMD160 returns bytes20, pad to bytes32",
            "Compare hashes with =="
        ],
        "tags": ["cryptography", "hashing", "verification"],
        "solved_count": 0
    },
    {
        "problem_id": "crypto_007",
        "title": "Threshold Signature Scheme",
        "description": """Implement a threshold signature scheme where k-of-n signatures are required.

Requirements:
- Register signers
- Collect partial signatures
- Verify threshold met
- Combine signatures
- Execute when valid""",
        "difficulty": "expert",
        "category": "cryptography",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ThresholdSignature {
    struct Message {
        bytes32 messageHash;
        uint256 signatureCount;
        mapping(address => bool) hasSigned;
        bool executed;
    }
    
    address[] public signers;
    uint256 public threshold;
    mapping(bytes32 => Message) public messages;
    
    event SignerAdded(address indexed signer);
    event MessageSigned(bytes32 indexed messageHash, address indexed signer);
    event ThresholdReached(bytes32 indexed messageHash);
    
    // TODO: Implement initialize
    function initialize(address[] memory _signers, uint256 _threshold) external {
        // Your code here
        // Check threshold <= signers.length
    }
    
    // TODO: Implement sign message
    function signMessage(bytes32 messageHash) external {
        // Your code here
        // Check sender is signer
        // Check not already signed
        // Increment signature count
    }
    
    // TODO: Implement verify threshold
    function isThresholdMet(bytes32 messageHash) public view returns (bool) {
        // Your code here
    }
    
    // TODO: Implement execute with threshold
    function executeIfThreshold(
        bytes32 messageHash,
        address target,
        bytes memory data
    ) external {
        // Your code here
        // Check threshold met
        // Check not executed
        // Execute call
    }
}""",
        "test_cases": [
            {"input": "initialize([addr1, addr2, addr3], 2)", "expected": "2-of-3 multisig"},
            {"input": "signMessage(hash) by addr1", "expected": "1 signature"},
            {"input": "signMessage(hash) by addr2", "expected": "threshold met, execute"}
        ],
        "hints": [
            "Store signers in array",
            "Use mapping to prevent double signing",
            "Count signatures per message",
            "Execute only when count >= threshold"
        ],
        "tags": ["cryptography", "signatures", "multisig", "threshold"],
        "solved_count": 0
    },

    # ============== ADDITIONAL SOLIDITY PROBLEMS (DeFi, NFT, DAO, Gaming) ==============
    # Junior Level
    {
        "problem_id": "sol_009",
        "title": "Voting Contract",
        "description": """Create a simple voting contract for proposals.

Requirements:
- Add proposals with description and vote count
- Users can vote for proposals (one vote per address)
- Track who has voted
- Get winning proposal
- Emit events for new proposals and votes""",
        "difficulty": "junior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Voting {
    struct Proposal {
        string description;
        uint256 voteCount;
    }
    
    Proposal[] public proposals;
    mapping(address => bool) public hasVoted;
    
    event ProposalAdded(uint256 indexed proposalId, string description);
    event Voted(address indexed voter, uint256 indexed proposalId);
    
    // TODO: Implement addProposal
    function addProposal(string memory description) public {
        // Your code here
    }
    
    // TODO: Implement vote
    function vote(uint256 proposalId) public {
        // Your code here
        // Check if already voted
        // Increment vote count
    }
    
    // TODO: Implement getWinner
    function getWinner() public view returns (uint256 winningProposal) {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "addProposal",
                "args": ["Proposal 1"],
                "expected": "success",
                "description": "Should add proposal"
            },
            {
                "type": "transaction",
                "function": "vote",
                "args": [0],
                "expected": "success",
                "description": "Should vote for proposal"
            }
        ],
        "hints": [
            "Use array to store proposals",
            "Use mapping to track voters",
            "Use require() to prevent double voting",
            "Loop through proposals to find winner"
        ],
        "tags": ["voting", "governance", "basics"],
        "solved_count": 0
    },
    {
        "problem_id": "sol_010",
        "title": "Escrow Service",
        "description": """Implement an escrow service for safe peer-to-peer transactions.

Requirements:
- Buyer deposits funds
- Seller can confirm delivery
- Buyer can confirm receipt and release funds
- Support refunds with seller approval
- Add dispute resolution by arbiter""",
        "difficulty": "junior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Escrow {
    enum State { AWAITING_PAYMENT, AWAITING_DELIVERY, COMPLETE, REFUNDED }
    
    struct Transaction {
        address buyer;
        address seller;
        address arbiter;
        uint256 amount;
        State state;
    }
    
    mapping(uint256 => Transaction) public transactions;
    uint256 public transactionCount;
    
    event Deposited(uint256 indexed txId, address indexed buyer, uint256 amount);
    event Released(uint256 indexed txId, address indexed seller, uint256 amount);
    event Refunded(uint256 indexed txId, address indexed buyer, uint256 amount);
    
    // TODO: Implement createTransaction
    function createTransaction(address seller, address arbiter) public payable returns (uint256) {
        // Your code here
    }
    
    // TODO: Implement release funds
    function releaseFunds(uint256 txId) public {
        // Your code here
    }
    
    // TODO: Implement refund
    function refund(uint256 txId) public {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "createTransaction",
                "args": ["0x1234567890123456789012345678901234567890", "0x2234567890123456789012345678901234567890"],
                "expected": "success",
                "description": "Create escrow transaction"
            }
        ],
        "hints": [
            "Use enum for transaction states",
            "Store transaction details in mapping",
            "Use require() to validate state transitions",
            "Transfer funds with .transfer() or .call()"
        ],
        "tags": ["escrow", "payment", "security"],
        "solved_count": 0
    },
    {
        "problem_id": "sol_011",
        "title": "ERC721 Basic NFT",
        "description": """Create a basic ERC721 NFT contract with minting and transfers.

Requirements:
- Implement ERC721 standard
- Mint new NFTs with token URI
- Transfer NFTs between addresses
- Track token ownership
- Support tokenURI for metadata""",
        "difficulty": "junior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BasicNFT {
    string public name = "CodeChain NFT";
    string public symbol = "CCNFT";
    
    mapping(uint256 => address) public ownerOf;
    mapping(address => uint256) public balanceOf;
    mapping(uint256 => string) private tokenURIs;
    uint256 public totalSupply;
    
    event Transfer(address indexed from, address indexed to, uint256 indexed tokenId);
    event Minted(address indexed to, uint256 indexed tokenId, string uri);
    
    // TODO: Implement mint
    function mint(address to, string memory uri) public returns (uint256) {
        // Your code here
    }
    
    // TODO: Implement transfer
    function transfer(address to, uint256 tokenId) public {
        // Your code here
    }
    
    // TODO: Implement tokenURI
    function tokenURI(uint256 tokenId) public view returns (string memory) {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "mint",
                "args": ["0x1234567890123456789012345678901234567890", "ipfs://QmTest"],
                "expected": "success",
                "description": "Mint new NFT"
            }
        ],
        "hints": [
            "Use mappings for ownership tracking",
            "Increment totalSupply on mint",
            "Validate ownership before transfer",
            "Store metadata URI for each token"
        ],
        "tags": ["nft", "erc721", "token"],
        "solved_count": 0
    },
    {
        "problem_id": "sol_012",
        "title": "Lottery System",
        "description": """Create a fair lottery system with random winner selection.

Requirements:
- Users can enter by paying ticket price
- Track all participants
- Random winner selection (use block data)
- Winner gets prize pool
- Owner can start new round""",
        "difficulty": "junior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Lottery {
    address public owner;
    address[] public players;
    uint256 public ticketPrice = 0.01 ether;
    
    event PlayerEntered(address indexed player);
    event WinnerSelected(address indexed winner, uint256 amount);
    
    constructor() {
        owner = msg.sender;
    }
    
    // TODO: Implement enter
    function enter() public payable {
        // Your code here
        // Check ticket price paid
        // Add player to array
    }
    
    // TODO: Implement pickWinner
    function pickWinner() public {
        // Your code here
        // Only owner can call
        // Select random winner
        // Transfer prize
        // Reset lottery
    }
    
    // TODO: Implement pseudo-random number generation
    function random() private view returns (uint256) {
        // Your code here - use block data
    }
    
    function getPrizePool() public view returns (uint256) {
        return address(this).balance;
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "enter",
                "args": [],
                "expected": "success",
                "description": "Enter lottery with payment"
            }
        ],
        "hints": [
            "Use require() to check msg.value == ticketPrice",
            "Store players in dynamic array",
            "Use keccak256 with block data for randomness (not secure for production)",
            "Clear players array after selecting winner"
        ],
        "tags": ["lottery", "random", "gaming"],
        "solved_count": 0
    },
    {
        "problem_id": "sol_013",
        "title": "Time Lock Vault",
        "description": """Create a vault that locks funds until a specific time.

Requirements:
- Deposit funds with unlock timestamp
- Cannot withdraw before unlock time
- Support multiple deposits per user
- Track total locked amount
- Emit events for deposits and withdrawals""",
        "difficulty": "junior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TimeLockVault {
    struct Deposit {
        uint256 amount;
        uint256 unlockTime;
        bool withdrawn;
    }
    
    mapping(address => Deposit[]) public deposits;
    
    event Deposited(address indexed user, uint256 amount, uint256 unlockTime);
    event Withdrawn(address indexed user, uint256 amount);
    
    // TODO: Implement deposit
    function deposit(uint256 unlockDelay) public payable {
        // Your code here
        // unlockDelay in seconds from now
    }
    
    // TODO: Implement withdraw
    function withdraw(uint256 depositIndex) public {
        // Your code here
        // Check unlock time has passed
        // Check not already withdrawn
    }
    
    // TODO: Implement getDeposits
    function getDeposits(address user) public view returns (Deposit[] memory) {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "deposit",
                "args": [3600],
                "expected": "success",
                "description": "Deposit with 1 hour lock"
            }
        ],
        "hints": [
            "Use block.timestamp for current time",
            "Store deposits in array per user",
            "Check block.timestamp >= unlockTime",
            "Mark deposit as withdrawn to prevent double withdrawal"
        ],
        "tags": ["timelock", "vault", "security"],
        "solved_count": 0
    },

    # Middle Level
    {
        "problem_id": "sol_014",
        "title": "Staking Contract",
        "description": """Implement a token staking contract with rewards.

Requirements:
- Stake tokens for rewards
- Calculate rewards based on time and amount
- Unstake tokens with accumulated rewards
- Track total staked and rewards distributed
- Support APY configuration""",
        "difficulty": "middle",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IERC20 {
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function transfer(address to, uint256 amount) external returns (bool);
}

contract Staking {
    IERC20 public stakingToken;
    IERC20 public rewardToken;
    
    uint256 public rewardRate = 100; // 100 tokens per day per 1000 staked
    uint256 public totalStaked;
    
    struct Stake {
        uint256 amount;
        uint256 timestamp;
        uint256 rewardDebt;
    }
    
    mapping(address => Stake) public stakes;
    
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    
    constructor(address _stakingToken, address _rewardToken) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
    }
    
    // TODO: Implement stake
    function stake(uint256 amount) public {
        // Your code here
    }
    
    // TODO: Implement calculateReward
    function calculateReward(address user) public view returns (uint256) {
        // Your code here
        // Calculate based on time and amount
    }
    
    // TODO: Implement unstake
    function unstake() public {
        // Your code here
        // Return staked amount + rewards
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "stake",
                "args": [1000],
                "expected": "success",
                "description": "Stake tokens"
            }
        ],
        "hints": [
            "Use transferFrom to receive tokens",
            "Calculate reward: (amount * rate * time) / denominator",
            "Use block.timestamp for timing",
            "Transfer both stake and rewards on unstake"
        ],
        "tags": ["staking", "defi", "rewards"],
        "solved_count": 0
    },
    {
        "problem_id": "sol_015",
        "title": "Airdrop Manager",
        "description": """Create an efficient airdrop distribution system.

Requirements:
- Upload list of recipients and amounts
- Batch token distribution
- Track claimed status
- Support Merkle tree for gas optimization
- Prevent double claims""",
        "difficulty": "middle",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IERC20 {
    function transfer(address to, uint256 amount) external returns (bool);
}

contract AirdropManager {
    IERC20 public token;
    address public owner;
    bytes32 public merkleRoot;
    
    mapping(address => bool) public hasClaimed;
    
    event AirdropClaimed(address indexed user, uint256 amount);
    
    constructor(address _token) {
        token = IERC20(_token);
        owner = msg.sender;
    }
    
    // TODO: Implement setMerkleRoot
    function setMerkleRoot(bytes32 _merkleRoot) public {
        // Your code here
    }
    
    // TODO: Implement claim with Merkle proof
    function claim(uint256 amount, bytes32[] calldata proof) public {
        // Your code here
        // Verify Merkle proof
        // Check not claimed
        // Transfer tokens
    }
    
    // TODO: Implement verifyProof
    function verifyProof(
        bytes32[] calldata proof,
        address user,
        uint256 amount
    ) internal view returns (bool) {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "setMerkleRoot",
                "args": ["0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"],
                "expected": "success",
                "description": "Set Merkle root"
            }
        ],
        "hints": [
            "Use bytes32 for Merkle root",
            "Verify proof by hashing up the tree",
            "Use keccak256 for hashing",
            "Mark address as claimed after distribution"
        ],
        "tags": ["airdrop", "merkle-tree", "distribution"],
        "solved_count": 0
    },
    {
        "problem_id": "sol_016",
        "title": "Crowdfunding Platform",
        "description": """Build a crowdfunding platform for project fundraising.

Requirements:
- Create campaigns with goal and deadline
- Accept contributions
- Refund if goal not met
- Release funds if goal reached
- Track campaign status""",
        "difficulty": "middle",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Crowdfunding {
    struct Campaign {
        address creator;
        uint256 goal;
        uint256 deadline;
        uint256 totalRaised;
        bool finalized;
    }
    
    mapping(uint256 => Campaign) public campaigns;
    mapping(uint256 => mapping(address => uint256)) public contributions;
    uint256 public campaignCount;
    
    event CampaignCreated(uint256 indexed campaignId, address creator, uint256 goal);
    event Contributed(uint256 indexed campaignId, address contributor, uint256 amount);
    event CampaignFinalized(uint256 indexed campaignId, bool success);
    
    // TODO: Implement createCampaign
    function createCampaign(uint256 goal, uint256 duration) public returns (uint256) {
        // Your code here
    }
    
    // TODO: Implement contribute
    function contribute(uint256 campaignId) public payable {
        // Your code here
    }
    
    // TODO: Implement finalize
    function finalize(uint256 campaignId) public {
        // Your code here
        // Check deadline passed
        // If goal met: transfer to creator
        // If goal not met: enable refunds
    }
    
    // TODO: Implement refund
    function refund(uint256 campaignId) public {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "createCampaign",
                "args": [1000000000000000000, 86400],
                "expected": "success",
                "description": "Create campaign with 1 ETH goal"
            }
        ],
        "hints": [
            "Use block.timestamp for deadline checking",
            "Store contributions per user per campaign",
            "Check deadline before accepting contributions",
            "Only allow refunds if goal not met"
        ],
        "tags": ["crowdfunding", "fundraising", "platform"],
        "solved_count": 0
    },
    {
        "problem_id": "sol_017",
        "title": "NFT Marketplace",
        "description": """Create a marketplace for buying and selling NFTs.

Requirements:
- List NFTs for sale with price
- Buy listed NFTs
- Cancel listings
- Support royalties for creators
- Track marketplace fees""",
        "difficulty": "middle",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IERC721 {
    function transferFrom(address from, address to, uint256 tokenId) external;
    function ownerOf(uint256 tokenId) external view returns (address);
}

contract NFTMarketplace {
    struct Listing {
        address seller;
        address nftContract;
        uint256 tokenId;
        uint256 price;
        bool active;
    }
    
    mapping(bytes32 => Listing) public listings;
    uint256 public feePercent = 250; // 2.5%
    
    event Listed(bytes32 indexed listingId, address seller, uint256 price);
    event Sold(bytes32 indexed listingId, address buyer, uint256 price);
    event Cancelled(bytes32 indexed listingId);
    
    // TODO: Implement listNFT
    function listNFT(
        address nftContract,
        uint256 tokenId,
        uint256 price
    ) public returns (bytes32) {
        // Your code here
    }
    
    // TODO: Implement buyNFT
    function buyNFT(bytes32 listingId) public payable {
        // Your code here
        // Calculate fees
        // Transfer NFT and funds
    }
    
    // TODO: Implement cancelListing
    function cancelListing(bytes32 listingId) public {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "listNFT",
                "args": ["0x1234567890123456789012345678901234567890", 1, 1000000000000000000],
                "expected": "success",
                "description": "List NFT for sale"
            }
        ],
        "hints": [
            "Use keccak256 to generate listing ID",
            "Calculate marketplace fee from price",
            "Use IERC721.transferFrom for NFT transfer",
            "Validate seller is owner before listing"
        ],
        "tags": ["nft", "marketplace", "trading"],
        "solved_count": 0
    },
    {
        "problem_id": "sol_018",
        "title": "Vesting Schedule",
        "description": """Implement a token vesting contract with linear release.

Requirements:
- Create vesting schedules for beneficiaries
- Linear vesting over time period
- Cliff period support
- Calculate releasable amount
- Allow beneficiaries to claim vested tokens""",
        "difficulty": "middle",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IERC20 {
    function transfer(address to, uint256 amount) external returns (bool);
}

contract TokenVesting {
    IERC20 public token;
    
    struct VestingSchedule {
        uint256 totalAmount;
        uint256 startTime;
        uint256 cliffDuration;
        uint256 duration;
        uint256 released;
    }
    
    mapping(address => VestingSchedule) public schedules;
    
    event VestingCreated(address indexed beneficiary, uint256 amount, uint256 duration);
    event TokensReleased(address indexed beneficiary, uint256 amount);
    
    constructor(address _token) {
        token = IERC20(_token);
    }
    
    // TODO: Implement createVesting
    function createVesting(
        address beneficiary,
        uint256 totalAmount,
        uint256 cliffDuration,
        uint256 duration
    ) public {
        // Your code here
    }
    
    // TODO: Implement calculateReleasable
    function calculateReleasable(address beneficiary) public view returns (uint256) {
        // Your code here
        // Linear vesting calculation
    }
    
    // TODO: Implement release
    function release() public {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "createVesting",
                "args": ["0x1234567890123456789012345678901234567890", 1000000, 2592000, 31536000],
                "expected": "success",
                "description": "Create vesting with 30-day cliff, 1-year duration"
            }
        ],
        "hints": [
            "Use block.timestamp for timing",
            "Vesting formula: (totalAmount * elapsed) / duration",
            "Check cliff period before releasing",
            "Track released amount to calculate remaining"
        ],
        "tags": ["vesting", "token-distribution", "time-based"],
        "solved_count": 0
    },
    {
        "problem_id": "sol_019",
        "title": "Price Oracle",
        "description": """Build a decentralized price oracle with data aggregation.

Requirements:
- Multiple data providers can submit prices
- Calculate median or average price
- Time-weighted average price (TWAP)
- Cooldown period between updates
- Data validity checks""",
        "difficulty": "middle",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract PriceOracle {
    struct PriceData {
        uint256 price;
        uint256 timestamp;
    }
    
    mapping(address => bool) public isProvider;
    mapping(address => PriceData) public providerPrices;
    address[] public providers;
    
    uint256 public constant UPDATE_COOLDOWN = 300; // 5 minutes
    
    event PriceUpdated(address indexed provider, uint256 price, uint256 timestamp);
    event ProviderAdded(address indexed provider);
    
    // TODO: Implement addProvider
    function addProvider(address provider) public {
        // Your code here
    }
    
    // TODO: Implement submitPrice
    function submitPrice(uint256 price) public {
        // Your code here
        // Check is provider
        // Check cooldown
    }
    
    // TODO: Implement getMedianPrice
    function getMedianPrice() public view returns (uint256) {
        // Your code here
        // Collect prices from all providers
        // Sort and return median
    }
    
    // TODO: Implement getTWAP
    function getTWAP(uint256 timeWindow) public view returns (uint256) {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "addProvider",
                "args": ["0x1234567890123456789012345678901234567890"],
                "expected": "success",
                "description": "Add price provider"
            }
        ],
        "hints": [
            "Use median to avoid outliers",
            "Store historical prices for TWAP",
            "Implement sorting algorithm",
            "Validate price freshness with timestamps"
        ],
        "tags": ["oracle", "defi", "price-feeds"],
        "solved_count": 0
    },

    # Senior Level
    {
        "problem_id": "sol_020",
        "title": "Automated Market Maker (AMM)",
        "description": """Implement a constant product AMM (x * y = k).

Requirements:
- Add liquidity and mint LP tokens
- Remove liquidity and burn LP tokens
- Swap tokens using constant product formula
- Calculate optimal swap amounts
- Handle slippage protection""",
        "difficulty": "senior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IERC20 {
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function transfer(address to, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract AMM {
    IERC20 public tokenA;
    IERC20 public tokenB;
    
    uint256 public reserveA;
    uint256 public reserveB;
    uint256 public totalLiquidity;
    
    mapping(address => uint256) public liquidity;
    
    event LiquidityAdded(address indexed provider, uint256 amountA, uint256 amountB);
    event LiquidityRemoved(address indexed provider, uint256 amountA, uint256 amountB);
    event Swapped(address indexed trader, uint256 amountIn, uint256 amountOut);
    
    constructor(address _tokenA, address _tokenB) {
        tokenA = IERC20(_tokenA);
        tokenB = IERC20(_tokenB);
    }
    
    // TODO: Implement addLiquidity
    function addLiquidity(uint256 amountA, uint256 amountB) public returns (uint256) {
        // Your code here
        // Maintain price ratio if pool not empty
        // Mint LP tokens proportional to contribution
    }
    
    // TODO: Implement removeLiquidity
    function removeLiquidity(uint256 liquidityAmount) public returns (uint256, uint256) {
        // Your code here
    }
    
    // TODO: Implement swap
    function swap(address tokenIn, uint256 amountIn, uint256 minAmountOut) public returns (uint256) {
        // Your code here
        // Use formula: amountOut = (amountIn * reserveOut) / (reserveIn + amountIn)
        // Apply 0.3% fee
    }
    
    // TODO: Implement getAmountOut
    function getAmountOut(uint256 amountIn, uint256 reserveIn, uint256 reserveOut) public pure returns (uint256) {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "addLiquidity",
                "args": [1000, 1000],
                "expected": "success",
                "description": "Add initial liquidity"
            }
        ],
        "hints": [
            "First liquidity: LP = sqrt(amountA * amountB)",
            "Subsequent: LP = min((amountA * totalLP) / reserveA, ...)",
            "Constant product: reserveA * reserveB = k",
            "Apply fee before calculating output"
        ],
        "tags": ["amm", "dex", "defi", "advanced"],
        "solved_count": 0
    },
    {
        "problem_id": "sol_021",
        "title": "Lending Protocol",
        "description": """Create a lending/borrowing protocol with collateralization.

Requirements:
- Deposit collateral
- Borrow against collateral with ratio
- Repay loans with interest
- Liquidate undercollateralized positions
- Track health factor""",
        "difficulty": "senior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IERC20 {
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function transfer(address to, uint256 amount) external returns (bool);
}

interface IPriceOracle {
    function getPrice(address token) external view returns (uint256);
}

contract LendingProtocol {
    IPriceOracle public oracle;
    
    uint256 public constant COLLATERAL_RATIO = 150; // 150%
    uint256 public constant LIQUIDATION_THRESHOLD = 120; // 120%
    uint256 public constant INTEREST_RATE = 500; // 5% APY
    
    struct Position {
        uint256 collateralAmount;
        address collateralToken;
        uint256 borrowedAmount;
        address borrowedToken;
        uint256 borrowTimestamp;
    }
    
    mapping(address => Position) public positions;
    
    event Deposited(address indexed user, address token, uint256 amount);
    event Borrowed(address indexed user, address token, uint256 amount);
    event Repaid(address indexed user, uint256 amount, uint256 interest);
    event Liquidated(address indexed user, address indexed liquidator, uint256 amount);
    
    // TODO: Implement deposit
    function deposit(address token, uint256 amount) public {
        // Your code here
    }
    
    // TODO: Implement borrow
    function borrow(address token, uint256 amount) public {
        // Your code here
        // Check collateral ratio
    }
    
    // TODO: Implement repay
    function repay() public {
        // Your code here
        // Calculate interest
    }
    
    // TODO: Implement liquidate
    function liquidate(address user) public {
        // Your code here
        // Check health factor < threshold
    }
    
    // TODO: Implement getHealthFactor
    function getHealthFactor(address user) public view returns (uint256) {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "deposit",
                "args": ["0x1234567890123456789012345678901234567890", 1000],
                "expected": "success",
                "description": "Deposit collateral"
            }
        ],
        "hints": [
            "Health factor = (collateral * price) / (borrowed * price)",
            "Interest = (borrowed * rate * time) / (365 days * 10000)",
            "Use oracle for token prices",
            "Liquidator gets bonus for liquidating"
        ],
        "tags": ["lending", "defi", "collateral", "advanced"],
        "solved_count": 0
    },
    {
        "problem_id": "sol_022",
        "title": "DAO Governance",
        "description": """Implement a complete DAO governance system with proposals and voting.

Requirements:
- Create proposals with description and execution data
- Vote with token-weighted voting power
- Quorum requirements
- Timelock for execution
- Delegate voting power""",
        "difficulty": "senior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IGovernanceToken {
    function balanceOf(address account) external view returns (uint256);
    function delegates(address account) external view returns (address);
}

contract DAOGovernance {
    IGovernanceToken public governanceToken;
    
    enum ProposalState { Pending, Active, Defeated, Succeeded, Executed }
    
    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 startBlock;
        uint256 endBlock;
        uint256 forVotes;
        uint256 againstVotes;
        mapping(address => bool) hasVoted;
        address target;
        bytes data;
        bool executed;
    }
    
    mapping(uint256 => Proposal) public proposals;
    uint256 public proposalCount;
    
    uint256 public constant VOTING_PERIOD = 17280; // ~3 days in blocks
    uint256 public constant QUORUM_VOTES = 100000e18; // 100k tokens
    
    event ProposalCreated(uint256 indexed proposalId, address proposer, string description);
    event Voted(uint256 indexed proposalId, address voter, bool support, uint256 votes);
    event ProposalExecuted(uint256 indexed proposalId);
    
    constructor(address _governanceToken) {
        governanceToken = IGovernanceToken(_governanceToken);
    }
    
    // TODO: Implement propose
    function propose(
        string memory description,
        address target,
        bytes memory data
    ) public returns (uint256) {
        // Your code here
    }
    
    // TODO: Implement vote
    function vote(uint256 proposalId, bool support) public {
        // Your code here
        // Get voting power from token balance
    }
    
    // TODO: Implement execute
    function execute(uint256 proposalId) public {
        // Your code here
        // Check quorum met
        // Check more for votes than against
    }
    
    // TODO: Implement getProposalState
    function getProposalState(uint256 proposalId) public view returns (ProposalState) {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "propose",
                "args": ["Increase rewards", "0x1234567890123456789012345678901234567890", "0x"],
                "expected": "success",
                "description": "Create proposal"
            }
        ],
        "hints": [
            "Use block.number for voting periods",
            "Store voting power at proposal creation",
            "Check quorum: total votes >= QUORUM_VOTES",
            "Use .call() for proposal execution"
        ],
        "tags": ["dao", "governance", "voting", "advanced"],
        "solved_count": 0
    },
    {
        "problem_id": "sol_023",
        "title": "Cross-Chain Bridge",
        "description": """Build a cross-chain token bridge with lock/mint mechanism.

Requirements:
- Lock tokens on source chain
- Mint wrapped tokens on destination chain
- Burn wrapped tokens to unlock on source
- Validator signatures for security
- Handle failed transactions""",
        "difficulty": "senior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IERC20 {
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function transfer(address to, uint256 amount) external returns (bool);
    function burn(uint256 amount) external;
    function mint(address to, uint256 amount) external;
}

contract CrossChainBridge {
    address public admin;
    mapping(address => bool) public validators;
    uint256 public requiredSignatures = 3;
    
    struct Transfer {
        address token;
        address from;
        address to;
        uint256 amount;
        uint256 nonce;
        bool processed;
    }
    
    mapping(bytes32 => Transfer) public transfers;
    mapping(bytes32 => mapping(address => bool)) public signatures;
    mapping(bytes32 => uint256) public signatureCount;
    
    event TransferInitiated(bytes32 indexed transferId, address token, address from, uint256 amount);
    event TransferCompleted(bytes32 indexed transferId, address to, uint256 amount);
    
    // TODO: Implement lock
    function lock(address token, uint256 amount, address recipient) public returns (bytes32) {
        // Your code here
        // Lock tokens on this chain
        // Generate transfer ID
    }
    
    // TODO: Implement sign
    function sign(bytes32 transferId) public {
        // Your code here
        // Validators sign to approve
    }
    
    // TODO: Implement mint
    function mint(bytes32 transferId) public {
        // Your code here
        // Check signature threshold met
        // Mint wrapped tokens
    }
    
    // TODO: Implement burn
    function burn(address token, uint256 amount) public returns (bytes32) {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "lock",
                "args": ["0x1234567890123456789012345678901234567890", 1000, "0x2234567890123456789012345678901234567890"],
                "expected": "success",
                "description": "Lock tokens for bridging"
            }
        ],
        "hints": [
            "Generate transferId with keccak256(token, from, to, amount, nonce)",
            "Use multi-sig pattern for validator consensus",
            "Store locked tokens in contract",
            "Emit events for relayers to detect"
        ],
        "tags": ["bridge", "cross-chain", "interoperability", "advanced"],
        "solved_count": 0
    },
    {
        "problem_id": "sol_024",
        "title": "Yield Farming Vault",
        "description": """Create an auto-compounding yield farming vault.

Requirements:
- Deposit LP tokens
- Auto-harvest rewards
- Auto-compound rewards back to LP
- Calculate share price
- Withdraw with proportional rewards""",
        "difficulty": "senior",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IERC20 {
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function transfer(address to, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

interface IFarm {
    function deposit(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function harvest() external returns (uint256);
}

contract YieldVault {
    IERC20 public lpToken;
    IERC20 public rewardToken;
    IFarm public farm;
    
    uint256 public totalShares;
    mapping(address => uint256) public shares;
    
    uint256 public lastHarvest;
    uint256 public constant HARVEST_INTERVAL = 4 hours;
    
    event Deposited(address indexed user, uint256 amount, uint256 shares);
    event Withdrawn(address indexed user, uint256 amount, uint256 shares);
    event Harvested(uint256 rewards);
    
    constructor(address _lpToken, address _rewardToken, address _farm) {
        lpToken = IERC20(_lpToken);
        rewardToken = IERC20(_rewardToken);
        farm = IFarm(_farm);
    }
    
    // TODO: Implement deposit
    function deposit(uint256 amount) public returns (uint256) {
        // Your code here
        // Calculate shares based on current vault value
    }
    
    // TODO: Implement withdraw
    function withdraw(uint256 shareAmount) public returns (uint256) {
        // Your code here
        // Calculate LP amount from shares
    }
    
    // TODO: Implement harvest
    function harvest() public {
        // Your code here
        // Harvest rewards from farm
        // Convert to LP and deposit back
    }
    
    // TODO: Implement getSharePrice
    function getSharePrice() public view returns (uint256) {
        // Your code here
        // Total value / total shares
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "deposit",
                "args": [1000],
                "expected": "success",
                "description": "Deposit LP tokens"
            }
        ],
        "hints": [
            "First deposit: shares = amount",
            "Subsequent: shares = (amount * totalShares) / totalValue",
            "Auto-compound increases value without changing shares",
            "Withdrawal: amount = (shares * totalValue) / totalShares"
        ],
        "tags": ["yield-farming", "defi", "auto-compound", "vault"],
        "solved_count": 0
    },

    # Expert Level
    {
        "problem_id": "sol_025",
        "title": "Options Trading Protocol",
        "description": """Implement a decentralized options trading protocol.

Requirements:
- Create call/put options with strike price and expiry
- Buy and sell options
- Exercise options when profitable
- Automatic settlement at expiry
- Collateral management""",
        "difficulty": "expert",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IERC20 {
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function transfer(address to, uint256 amount) external returns (bool);
}

interface IPriceOracle {
    function getPrice(address token) external view returns (uint256);
}

contract OptionsProtocol {
    IPriceOracle public oracle;
    
    enum OptionType { Call, Put }
    enum OptionState { Active, Exercised, Expired }
    
    struct Option {
        OptionType optionType;
        address underlying;
        address strikeToken;
        uint256 strikePrice;
        uint256 expiry;
        uint256 amount;
        address writer;
        address holder;
        OptionState state;
    }
    
    mapping(uint256 => Option) public options;
    uint256 public optionCount;
    
    event OptionCreated(uint256 indexed optionId, OptionType optionType, uint256 strikePrice);
    event OptionExercised(uint256 indexed optionId, address holder, uint256 profit);
    event OptionExpired(uint256 indexed optionId);
    
    constructor(address _oracle) {
        oracle = IPriceOracle(_oracle);
    }
    
    // TODO: Implement createOption
    function createOption(
        OptionType optionType,
        address underlying,
        address strikeToken,
        uint256 strikePrice,
        uint256 expiry,
        uint256 amount
    ) public returns (uint256) {
        // Your code here
        // Writer must provide collateral
    }
    
    // TODO: Implement buyOption
    function buyOption(uint256 optionId, uint256 premium) public {
        // Your code here
    }
    
    // TODO: Implement exerciseOption
    function exerciseOption(uint256 optionId) public {
        // Your code here
        // Check if in the money
        // Calculate profit
        // Transfer funds
    }
    
    // TODO: Implement calculateOptionValue
    function calculateOptionValue(uint256 optionId) public view returns (uint256) {
        // Your code here
        // Intrinsic value calculation
    }
    
    // TODO: Implement settleExpired
    function settleExpired(uint256 optionId) public {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "createOption",
                "args": [0, "0x1234567890123456789012345678901234567890", "0x2234567890123456789012345678901234567890", 2000, 1735689600, 100],
                "expected": "success",
                "description": "Create call option"
            }
        ],
        "hints": [
            "Call option: profit = max(currentPrice - strikePrice, 0) * amount",
            "Put option: profit = max(strikePrice - currentPrice, 0) * amount",
            "Writer must lock collateral for full exposure",
            "Use oracle for current price",
            "Check expiry with block.timestamp"
        ],
        "tags": ["options", "derivatives", "defi", "expert"],
        "solved_count": 0
    },
    {
        "problem_id": "sol_026",
        "title": "MEV Protection Layer",
        "description": """Design a MEV protection mechanism using batch auctions and fair ordering.

Requirements:
- Batch orders into discrete auctions
- Fair ordering within batches
- Price improvement from MEV capture
- Protect against frontrunning and sandwiching
- Implement threshold encryption for order privacy""",
        "difficulty": "expert",
        "category": "solidity",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MEVProtection {
    struct Order {
        address trader;
        address tokenIn;
        address tokenOut;
        uint256 amountIn;
        uint256 minAmountOut;
        bytes32 commitment;
        bool revealed;
        bool executed;
    }
    
    struct Batch {
        uint256 startBlock;
        uint256 endBlock;
        uint256 orderCount;
        mapping(uint256 => Order) orders;
        bool finalized;
    }
    
    mapping(uint256 => Batch) public batches;
    uint256 public currentBatch;
    uint256 public constant BATCH_DURATION = 5; // blocks
    
    event OrderCommitted(uint256 indexed batchId, uint256 indexed orderId, bytes32 commitment);
    event OrderRevealed(uint256 indexed batchId, uint256 indexed orderId);
    event BatchFinalized(uint256 indexed batchId, uint256 orderCount);
    
    // TODO: Implement commitOrder
    function commitOrder(bytes32 commitment) public returns (uint256) {
        // Your code here
        // Create order with commitment
        // Check batch timing
    }
    
    // TODO: Implement revealOrder
    function revealOrder(
        uint256 batchId,
        uint256 orderId,
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut,
        bytes32 salt
    ) public {
        // Your code here
        // Verify commitment
        // Can only reveal after batch commit phase
    }
    
    // TODO: Implement finalizeBatch
    function finalizeBatch(uint256 batchId) public {
        // Your code here
        // Sort orders fairly (e.g., by gas price or randomly)
        // Execute in fair order
        // Distribute any captured MEV
    }
    
    // TODO: Implement verifyCommitment
    function verifyCommitment(
        bytes32 commitment,
        address trader,
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut,
        bytes32 salt
    ) internal pure returns (bool) {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "commitOrder",
                "args": ["0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"],
                "expected": "success",
                "description": "Commit order to batch"
            }
        ],
        "hints": [
            "Use commit-reveal to hide order details",
            "Batch duration prevents immediate execution",
            "Fair ordering: random shuffle or FIFO within batch",
            "Capture MEV by executing profitable orders first, distribute gains",
            "Use VRF or block hash for randomness"
        ],
        "tags": ["mev", "protection", "fairness", "expert"],
        "solved_count": 0
    },

    # ============== ADDITIONAL RUST (SOLANA) PROBLEMS ==============
    # Junior Level
    {
        "problem_id": "rust_012",
        "title": "Solana Counter Program",
        "description": """Create a simple counter program on Solana.

Requirements:
- Initialize counter account
- Increment counter
- Decrement counter  
- Reset counter
- Get current count""",
        "difficulty": "junior",
        "category": "rust",
        "initial_code": """use anchor_lang::prelude::*;

declare_id!("CounterProgramID");

#[program]
pub mod counter {
    use super::*;

    // TODO: Implement initialize
    pub fn initialize(ctx: Context<Initialize>) -> Result<()> {
        // Your code here
        Ok(())
    }

    // TODO: Implement increment
    pub fn increment(ctx: Context<Update>) -> Result<()> {
        // Your code here
        Ok(())
    }

    // TODO: Implement decrement
    pub fn decrement(ctx: Context<Update>) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    // TODO: Define accounts
}

#[derive(Accounts)]
pub struct Update<'info> {
    // TODO: Define accounts
}

#[account]
pub struct Counter {
    // TODO: Define data structure
}""",
        "test_cases": [
            {"input": "initialize()", "expected": "counter created"},
            {"input": "increment()", "expected": "count = 1"},
            {"input": "increment()", "expected": "count = 2"},
            {"input": "decrement()", "expected": "count = 1"}
        ],
        "hints": [
            "Use #[account(init)] for initialization",
            "Store count as u64",
            "Use mut for mutable accounts",
            "Add overflow checks"
        ],
        "tags": ["solana", "anchor", "basics", "counter"],
        "solved_count": 0
    },
    {
        "problem_id": "rust_013",
        "title": "Solana NFT Minter",
        "description": """Build an NFT minting program on Solana.

Requirements:
- Mint NFT with metadata
- Use Metaplex Token Metadata standard
- Set creator royalties
- Update metadata (with authority)
- Transfer NFT""",
        "difficulty": "junior",
        "category": "rust",
        "initial_code": """use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Mint};
use mpl_token_metadata::state::{Metadata, Creator};

declare_id!("NFTMinterProgramID");

#[program]
pub mod nft_minter {
    use super::*;

    // TODO: Implement mint_nft
    pub fn mint_nft(
        ctx: Context<MintNFT>,
        name: String,
        symbol: String,
        uri: String,
    ) -> Result<()> {
        // Your code here
        // Create mint account
        // Create metadata account
        // Mint one token
        Ok(())
    }
}

#[derive(Accounts)]
pub struct MintNFT<'info> {
    // TODO: Define accounts
    // mint, token_account, metadata, etc.
}""",
        "test_cases": [
            {"input": "mint_nft('CodeChain NFT', 'CC', 'ipfs://...')", "expected": "NFT minted"},
            {"input": "check supply", "expected": "supply = 1"},
            {"input": "check decimals", "expected": "decimals = 0"}
        ],
        "hints": [
            "Use Metaplex Token Metadata program",
            "NFT: supply = 1, decimals = 0",
            "Store metadata on-chain or IPFS",
            "Set seller_fee_basis_points for royalties"
        ],
        "tags": ["solana", "nft", "metaplex", "minting"],
        "solved_count": 0
    },
    {
        "problem_id": "rust_014",
        "title": "Solana Escrow Program",
        "description": """Create an escrow program for atomic swaps on Solana.

Requirements:
- Initialize escrow with two parties
- Party A deposits tokens
- Party B can accept and complete swap
- Cancel escrow before acceptance
- Handle PDA for escrow authority""",
        "difficulty": "junior",
        "category": "rust",
        "initial_code": """use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Transfer};

declare_id!("EscrowProgramID");

#[program]
pub mod escrow {
    use super::*;

    // TODO: Implement initialize_escrow
    pub fn initialize_escrow(
        ctx: Context<InitializeEscrow>,
        expected_amount: u64,
    ) -> Result<()> {
        // Your code here
        Ok(())
    }

    // TODO: Implement exchange
    pub fn exchange(ctx: Context<Exchange>) -> Result<()> {
        // Your code here
        Ok(())
    }

    // TODO: Implement cancel
    pub fn cancel(ctx: Context<Cancel>) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct InitializeEscrow<'info> {
    // TODO: Define accounts
}

#[derive(Accounts)]
pub struct Exchange<'info> {
    // TODO: Define accounts
}

#[derive(Accounts)]
pub struct Cancel<'info> {
    // TODO: Define accounts
}

#[account]
pub struct EscrowAccount {
    // TODO: Define data structure
}""",
        "test_cases": [
            {"input": "initialize_escrow(1000)", "expected": "escrow created"},
            {"input": "exchange()", "expected": "tokens swapped"},
            {"input": "cancel()", "expected": "escrow cancelled, tokens returned"}
        ],
        "hints": [
            "Use PDA for escrow authority",
            "Seeds: [b'escrow', initializer.key().as_ref()]",
            "Transfer tokens to escrow account",
            "Use CPI for token transfers"
        ],
        "tags": ["solana", "escrow", "swap", "pda"],
        "solved_count": 0
    },

    # Middle Level
    {
        "problem_id": "rust_015",
        "title": "Solana Token Staking",
        "description": """Implement a token staking program with rewards on Solana.

Requirements:
- Stake SPL tokens
- Calculate time-based rewards
- Claim rewards
- Unstake tokens
- Track total staked""",
        "difficulty": "middle",
        "category": "rust",
        "initial_code": """use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Transfer};

declare_id!("StakingProgramID");

#[program]
pub mod staking {
    use super::*;

    // TODO: Implement stake
    pub fn stake(ctx: Context<Stake>, amount: u64) -> Result<()> {
        // Your code here
        Ok(())
    }

    // TODO: Implement claim_rewards
    pub fn claim_rewards(ctx: Context<ClaimRewards>) -> Result<()> {
        // Your code here
        // Calculate rewards based on time and amount
        Ok(())
    }

    // TODO: Implement unstake
    pub fn unstake(ctx: Context<Unstake>) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Stake<'info> {
    // TODO: Define accounts
}

#[derive(Accounts)]
pub struct ClaimRewards<'info> {
    // TODO: Define accounts
}

#[derive(Accounts)]
pub struct Unstake<'info> {
    // TODO: Define accounts
}

#[account]
pub struct StakeAccount {
    // TODO: Define data structure
    // owner, amount, stake_timestamp, etc.
}""",
        "test_cases": [
            {"input": "stake(1000)", "expected": "tokens staked"},
            {"input": "wait 1 day", "expected": "rewards accumulated"},
            {"input": "claim_rewards()", "expected": "rewards transferred"},
            {"input": "unstake()", "expected": "tokens returned"}
        ],
        "hints": [
            "Use Clock sysvar for timestamps",
            "Reward calculation: (amount * rate * time_elapsed) / time_unit",
            "Store stake_timestamp when staking",
            "Update rewards before unstaking"
        ],
        "tags": ["solana", "staking", "rewards", "defi"],
        "solved_count": 0
    },
    {
        "problem_id": "rust_016",
        "title": "Solana NFT Collection Manager",
        "description": """Build a program to manage NFT collections with minting controls.

Requirements:
- Create collection with max supply
- Mint NFTs from collection
- Enforce mint limits
- Update collection metadata
- Track minted count""",
        "difficulty": "middle",
        "category": "rust",
        "initial_code": """use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, Mint, TokenAccount};
use mpl_token_metadata::state::Collection;

declare_id!("NFTCollectionProgramID");

#[program]
pub mod nft_collection {
    use super::*;

    // TODO: Implement create_collection
    pub fn create_collection(
        ctx: Context<CreateCollection>,
        name: String,
        symbol: String,
        uri: String,
        max_supply: u64,
    ) -> Result<()> {
        // Your code here
        Ok(())
    }

    // TODO: Implement mint_from_collection
    pub fn mint_from_collection(
        ctx: Context<MintFromCollection>,
        name: String,
        uri: String,
    ) -> Result<()> {
        // Your code here
        // Check max supply not exceeded
        Ok(())
    }
}

#[derive(Accounts)]
pub struct CreateCollection<'info> {
    // TODO: Define accounts
}

#[derive(Accounts)]
pub struct MintFromCollection<'info> {
    // TODO: Define accounts
}

#[account]
pub struct CollectionAccount {
    // TODO: Define data structure
}""",
        "test_cases": [
            {"input": "create_collection('MyNFTs', 'MNFT', 'uri', 10000)", "expected": "collection created"},
            {"input": "mint_from_collection('NFT #1', 'uri1')", "expected": "NFT minted"},
            {"input": "mint when max reached", "expected": "error: max supply reached"}
        ],
        "hints": [
            "Store max_supply and minted_count",
            "Check minted_count < max_supply before minting",
            "Use Metaplex collection standard",
            "Link NFTs to collection with collection field"
        ],
        "tags": ["solana", "nft", "collection", "metaplex"],
        "solved_count": 0
    },
    {
        "problem_id": "rust_017",
        "title": "Solana Voting DAO",
        "description": """Create a DAO governance program with proposal voting.

Requirements:
- Create proposals
- Vote with token-weighted power
- Execute proposals when passed
- Quorum requirements
- Timelock for execution""",
        "difficulty": "middle",
        "category": "rust",
        "initial_code": """use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount};

declare_id!("VotingDAOProgramID");

#[program]
pub mod voting_dao {
    use super::*;

    // TODO: Implement create_proposal
    pub fn create_proposal(
        ctx: Context<CreateProposal>,
        description: String,
        execution_data: Vec<u8>,
    ) -> Result<()> {
        // Your code here
        Ok(())
    }

    // TODO: Implement vote
    pub fn vote(
        ctx: Context<Vote>,
        proposal_id: u64,
        support: bool,
    ) -> Result<()> {
        // Your code here
        // Get voting power from token balance
        Ok(())
    }

    // TODO: Implement execute_proposal
    pub fn execute_proposal(ctx: Context<ExecuteProposal>, proposal_id: u64) -> Result<()> {
        // Your code here
        // Check quorum met and votes pass
        Ok(())
    }
}

#[derive(Accounts)]
pub struct CreateProposal<'info> {
    // TODO: Define accounts
}

#[derive(Accounts)]
pub struct Vote<'info> {
    // TODO: Define accounts
}

#[derive(Accounts)]
pub struct ExecuteProposal<'info> {
    // TODO: Define accounts
}

#[account]
pub struct Proposal {
    // TODO: Define data structure
}""",
        "test_cases": [
            {"input": "create_proposal('Increase rewards', data)", "expected": "proposal created"},
            {"input": "vote(0, true)", "expected": "voted yes"},
            {"input": "execute_proposal(0)", "expected": "proposal executed"}
        ],
        "hints": [
            "Use Clock for voting periods",
            "Store for_votes and against_votes",
            "Get voting power from governance token balance",
            "Check quorum: total_votes >= required_quorum"
        ],
        "tags": ["solana", "dao", "governance", "voting"],
        "solved_count": 0
    },

    # Senior Level
    {
        "problem_id": "rust_018",
        "title": "Serum DEX Integration",
        "description": """Integrate with Serum DEX for trading on Solana.

Requirements:
- Place limit orders
- Place market orders
- Cancel orders
- Settle funds
- Query order book""",
        "difficulty": "senior",
        "category": "rust",
        "initial_code": """use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount};
use serum_dex::state::MarketState;

declare_id!("SerumIntegrationProgramID");

#[program]
pub mod serum_integration {
    use super::*;

    // TODO: Implement place_order
    pub fn place_order(
        ctx: Context<PlaceOrder>,
        side: u8, // 0 = Bid, 1 = Ask
        limit_price: u64,
        max_quantity: u64,
    ) -> Result<()> {
        // Your code here
        // CPI to Serum DEX
        Ok(())
    }

    // TODO: Implement cancel_order
    pub fn cancel_order(
        ctx: Context<CancelOrder>,
        order_id: u128,
    ) -> Result<()> {
        // Your code here
        Ok(())
    }

    // TODO: Implement settle_funds
    pub fn settle_funds(ctx: Context<SettleFunds>) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct PlaceOrder<'info> {
    // TODO: Define accounts
    // market, open_orders, etc.
}

#[derive(Accounts)]
pub struct CancelOrder<'info> {
    // TODO: Define accounts
}

#[derive(Accounts)]
pub struct SettleFunds<'info> {
    // TODO: Define accounts
}""",
        "test_cases": [
            {"input": "place_order(BID, 100, 10)", "expected": "order placed"},
            {"input": "cancel_order(order_id)", "expected": "order cancelled"},
            {"input": "settle_funds()", "expected": "funds settled"}
        ],
        "hints": [
            "Use Serum DEX program ID for CPI",
            "Open orders account tracks user's orders",
            "Settle funds after orders fill",
            "Use serum_dex crate for instructions"
        ],
        "tags": ["solana", "serum", "dex", "trading", "advanced"],
        "solved_count": 0
    },
    {
        "problem_id": "rust_019",
        "title": "Solana Token Vesting",
        "description": """Implement a token vesting program with linear release.

Requirements:
- Create vesting schedules
- Linear vesting calculation
- Cliff period support
- Release vested tokens
- Cancel vesting (return unvested)""",
        "difficulty": "senior",
        "category": "rust",
        "initial_code": """use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Transfer};

declare_id!("VestingProgramID");

#[program]
pub mod vesting {
    use super::*;

    // TODO: Implement create_vesting
    pub fn create_vesting(
        ctx: Context<CreateVesting>,
        total_amount: u64,
        start_time: i64,
        cliff_duration: i64,
        vesting_duration: i64,
    ) -> Result<()> {
        // Your code here
        Ok(())
    }

    // TODO: Implement release
    pub fn release(ctx: Context<Release>) -> Result<()> {
        // Your code here
        // Calculate vested amount
        // Transfer releasable tokens
        Ok(())
    }

    // TODO: Implement cancel_vesting
    pub fn cancel_vesting(ctx: Context<CancelVesting>) -> Result<()> {
        // Your code here
        Ok(())
    }
}

#[derive(Accounts)]
pub struct CreateVesting<'info> {
    // TODO: Define accounts
}

#[derive(Accounts)]
pub struct Release<'info> {
    // TODO: Define accounts
}

#[derive(Accounts)]
pub struct CancelVesting<'info> {
    // TODO: Define accounts
}

#[account]
pub struct VestingAccount {
    // TODO: Define data structure
}""",
        "test_cases": [
            {"input": "create_vesting(10000, now, 30days, 365days)", "expected": "vesting created"},
            {"input": "release() before cliff", "expected": "0 tokens released"},
            {"input": "release() after 6 months", "expected": "~5000 tokens released"}
        ],
        "hints": [
            "Use Clock sysvar for time",
            "Vested = (total * (now - start)) / duration",
            "Check now >= start + cliff before releasing",
            "Track released_amount to calculate remaining"
        ],
        "tags": ["solana", "vesting", "token-distribution", "timelock"],
        "solved_count": 0
    },

    # Expert Level
    {
        "problem_id": "rust_020",
        "title": "Solana Flash Loan Program",
        "description": """Build a flash loan program on Solana.

Requirements:
- Borrow any amount within transaction
- Execute custom instructions with borrowed funds
- Repay loan with fee in same transaction
- Revert if not repaid
- Support multiple tokens""",
        "difficulty": "expert",
        "category": "rust",
        "initial_code": """use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Transfer};

declare_id!("FlashLoanProgramID");

#[program]
pub mod flash_loan {
    use super::*;

    // TODO: Implement flash_loan
    pub fn flash_loan(
        ctx: Context<FlashLoan>,
        amount: u64,
        instructions: Vec<Instruction>,
    ) -> Result<()> {
        // Your code here
        // 1. Transfer loan amount to borrower
        // 2. Execute provided instructions via CPI
        // 3. Verify repayment + fee
        // 4. Revert if not repaid
        Ok(())
    }
}

#[derive(Accounts)]
pub struct FlashLoan<'info> {
    // TODO: Define accounts
    #[account(mut)]
    pub pool: Account<'info, TokenAccount>,
    #[account(mut)]
    pub borrower: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

#[derive(AnchorSerialize, AnchorDeserialize, Clone)]
pub struct Instruction {
    pub program_id: Pubkey,
    pub accounts: Vec<AccountMeta>,
    pub data: Vec<u8>,
}""",
        "test_cases": [
            {"input": "flash_loan(10000, [arbitrage_ix])", "expected": "loan executed"},
            {"input": "flash_loan without repayment", "expected": "transaction reverted"}
        ],
        "hints": [
            "Check pool balance before and after",
            "Required: balance_after >= balance_before + fee",
            "Use invoke() for CPIs to custom programs",
            "Fee calculation: amount * fee_bps / 10000",
            "All must happen in single transaction for atomicity"
        ],
        "tags": ["solana", "flash-loan", "defi", "expert", "advanced"],
        "solved_count": 0
    },

    # ============== ADDITIONAL FUNC (TON) PROBLEMS ==============
    # Junior Level
    {
        "problem_id": "func_006",
        "title": "TON Simple Wallet",
        "description": """Create a basic wallet contract on TON blockchain.

Requirements:
- Receive TON coins
- Send TON coins with owner signature
- Get balance
- Validate seqno for replay protection
- Support bounce messages""",
        "difficulty": "junior",
        "category": "func",
        "initial_code": """#include "stdlib.fc";

;; Storage: (seqno, public_key)
(int, int) load_data() inline {
    ;; TODO: Load from storage
}

() save_data(int seqno, int public_key) impure inline {
    ;; TODO: Save to storage
}

;; TODO: Implement recv_internal
() recv_internal(int msg_value, cell in_msg, slice in_msg_body) impure {
    ;; Accept incoming TON
}

;; TODO: Implement recv_external
() recv_external(slice in_msg) impure {
    ;; Verify signature and send TON
    ;; Check seqno
    ;; Send message
}

;; TODO: Implement get_seqno
int seqno() method_id {
    ;; Return current seqno
}

;; TODO: Implement get_balance
int balance() method_id {
    ;; Return contract balance
}""",
        "test_cases": [
            {"input": "send TON to wallet", "expected": "balance increased"},
            {"input": "send_from_wallet(dest, amount, seqno, signature)", "expected": "TON sent"},
            {"input": "replay same seqno", "expected": "rejected"}
        ],
        "hints": [
            "Use recv_internal for incoming messages",
            "Use recv_external for signed transactions",
            "Increment seqno after each transaction",
            "Verify signature with check_signature",
            "Use send_raw_message to send TON"
        ],
        "tags": ["ton", "func", "wallet", "basics"],
        "solved_count": 0
    },
    {
        "problem_id": "func_007",
        "title": "TON Token Contract",
        "description": """Implement a basic fungible token on TON.

Requirements:
- Mint tokens (owner only)
- Transfer tokens
- Get balance
- Get total supply
- Burn tokens""",
        "difficulty": "junior",
        "category": "func",
        "initial_code": """#include "stdlib.fc";

;; Storage: (total_supply, owner_address, balances_dict)
global int ctx_total_supply;
global int ctx_owner;
global cell ctx_balances;

() load_data() impure {
    ;; TODO: Load from storage
}

() save_data() impure {
    ;; TODO: Save to storage
}

;; TODO: Implement mint
() mint(slice to, int amount) impure {
    ;; Check sender is owner
    ;; Increase balance
    ;; Increase total supply
}

;; TODO: Implement transfer
() transfer(slice from, slice to, int amount) impure {
    ;; Check balance sufficient
    ;; Decrease from balance
    ;; Increase to balance
}

;; TODO: Implement balance_of
int balance_of(slice address) method_id {
    ;; Return balance
}

;; TODO: Implement total_supply
int total_supply() method_id {
    ;; Return total supply
}""",
        "test_cases": [
            {"input": "mint(addr, 1000)", "expected": "balance = 1000"},
            {"input": "transfer(from, to, 500)", "expected": "balances updated"},
            {"input": "total_supply()", "expected": "1000"}
        ],
        "hints": [
            "Use dict to store balances",
            "Use udict_get and udict_set for balance operations",
            "Check sender authority for mint",
            "Validate sufficient balance before transfer"
        ],
        "tags": ["ton", "func", "token", "fungible"],
        "solved_count": 0
    },

    # Middle Level
    {
        "problem_id": "func_008",
        "title": "TON Jetton Standard",
        "description": """Implement the TEP-74 Jetton standard on TON.

Requirements:
- Jetton master contract
- Jetton wallet contract
- Transfer with notification
- Burn tokens
- Get wallet address""",
        "difficulty": "middle",
        "category": "func",
        "initial_code": """#include "stdlib.fc";

;; Jetton Master Contract

;; Storage: (total_supply, admin_address, content, jetton_wallet_code)
global int ctx_total_supply;
global slice ctx_admin;
global cell ctx_content;
global cell ctx_jetton_wallet_code;

() load_data() impure {
    ;; TODO: Load storage
}

() save_data() impure {
    ;; TODO: Save storage
}

;; TODO: Implement mint
() mint(slice to, int amount, cell master_msg) impure {
    ;; Deploy or update jetton wallet
    ;; Send mint message to wallet
}

;; TODO: Implement get_wallet_address
slice get_wallet_address(slice owner) method_id {
    ;; Calculate and return jetton wallet address for owner
}

;; Jetton Wallet Contract

;; Storage: (balance, owner, jetton_master)
global int ctx_balance;
global slice ctx_owner;
global slice ctx_jetton_master;

;; TODO: Implement transfer
() transfer(slice to, int amount, slice forward_payload) impure {
    ;; Transfer tokens
    ;; Send notification if payload provided
}

;; TODO: Implement burn
() burn(int amount) impure {
    ;; Burn tokens
    ;; Notify master contract
}""",
        "test_cases": [
            {"input": "deploy master", "expected": "jetton master created"},
            {"input": "mint(user, 1000)", "expected": "jetton wallet created, balance = 1000"},
            {"input": "transfer(to, 500, payload)", "expected": "transfer with notification"}
        ],
        "hints": [
            "Use TEP-74 standard message layouts",
            "Calculate wallet address deterministically",
            "Use op codes: transfer = 0xf8a7ea5, burn = 0x595f07bc",
            "Forward payload for notifications"
        ],
        "tags": ["ton", "func", "jetton", "standard"],
        "solved_count": 0
    },
    {
        "problem_id": "func_009",
        "title": "TON NFT Collection",
        "description": """Build an NFT collection contract following TEP-62.

Requirements:
- Collection master contract
- Mint NFTs with sequential IDs
- NFT item contract
- Get NFT address by index
- Support metadata""",
        "difficulty": "middle",
        "category": "func",
        "initial_code": """#include "stdlib.fc";

;; NFT Collection Contract

;; Storage: (owner, next_item_index, content, nft_item_code, royalty_params)
global slice ctx_owner;
global int ctx_next_item_index;
global cell ctx_content;
global cell ctx_nft_item_code;

() load_data() impure {
    ;; TODO: Load storage
}

() save_data() impure {
    ;; TODO: Save storage
}

;; TODO: Implement mint_nft
() mint_nft(slice to, cell content) impure {
    ;; Deploy NFT item contract
    ;; Increment next_item_index
}

;; TODO: Implement get_nft_address_by_index
slice get_nft_address_by_index(int index) method_id {
    ;; Calculate and return NFT address
}

;; NFT Item Contract

;; Storage: (index, collection_address, owner_address, content)
global int ctx_index;
global slice ctx_collection;
global slice ctx_owner;
global cell ctx_content;

;; TODO: Implement transfer
() transfer(slice new_owner, slice response_destination) impure {
    ;; Transfer ownership
    ;; Send excess to response_destination
}

;; TODO: Implement get_nft_data
(int, int, slice, slice, cell) get_nft_data() method_id {
    ;; Return (init?, index, collection, owner, content)
}""",
        "test_cases": [
            {"input": "mint_nft(user, metadata)", "expected": "NFT #0 created"},
            {"input": "mint_nft(user, metadata)", "expected": "NFT #1 created"},
            {"input": "transfer(new_owner)", "expected": "ownership transferred"}
        ],
        "hints": [
            "Follow TEP-62 NFT standard",
            "Use TEP-64 for metadata",
            "Calculate address with create_address",
            "Op code for transfer: 0x5fcc3d14"
        ],
        "tags": ["ton", "func", "nft", "collection"],
        "solved_count": 0
    },

    # Senior Level
    {
        "problem_id": "func_010",
        "title": "TON DAO Governance",
        "description": """Create a DAO governance system on TON.

Requirements:
- Create proposals
- Vote with jetton-weighted power
- Execute proposals when passed
- Quorum and threshold requirements
- Timelock for execution""",
        "difficulty": "senior",
        "category": "func",
        "initial_code": """#include "stdlib.fc";

;; Storage: (admin, governance_token, proposal_count, proposals_dict, quorum, threshold)
global slice ctx_admin;
global slice ctx_governance_token;
global int ctx_proposal_count;
global cell ctx_proposals;
global int ctx_quorum;
global int ctx_threshold;

() load_data() impure {
    ;; TODO: Load storage
}

() save_data() impure {
    ;; TODO: Save storage
}

;; TODO: Implement create_proposal
() create_proposal(slice proposer, cell description, cell execution_data, int voting_end_time) impure {
    ;; Create new proposal
    ;; Store in proposals dict
    ;; Increment proposal_count
}

;; TODO: Implement vote
() vote(int proposal_id, slice voter, int support) impure {
    ;; Get voter's token balance
    ;; Record vote
    ;; Update vote counts
}

;; TODO: Implement execute_proposal
() execute_proposal(int proposal_id) impure {
    ;; Check voting ended
    ;; Check quorum met
    ;; Check threshold passed
    ;; Execute proposal code
}

;; TODO: Implement get_proposal_state
(int, int, int, int) get_proposal_state(int proposal_id) method_id {
    ;; Return (for_votes, against_votes, quorum_met, passed)
}""",
        "test_cases": [
            {"input": "create_proposal(data)", "expected": "proposal created"},
            {"input": "vote(0, voter, true)", "expected": "vote recorded"},
            {"input": "execute_proposal(0)", "expected": "proposal executed"}
        ],
        "hints": [
            "Query governance token contract for balance",
            "Store proposals in dict with ID as key",
            "Quorum: total_votes >= quorum_amount",
            "Threshold: for_votes > (total_votes * threshold / 100)",
            "Use now() for time checks"
        ],
        "tags": ["ton", "func", "dao", "governance"],
        "solved_count": 0
    },

    # ============== ADDITIONAL CRYPTOGRAPHY PROBLEMS ==============
    # Middle Level
    {
        "problem_id": "crypto_011",
        "title": "Merkle Tree Airdrop Verifier",
        "description": """Implement an airdrop system using Merkle trees for efficient verification.

Requirements:
- Generate Merkle root from distribution list
- Verify Merkle proofs on-chain
- Prevent double claims
- Support large airdrop lists (100k+ addresses)
- Gas-efficient verification""",
        "difficulty": "middle",
        "category": "cryptography",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IERC20 {
    function transfer(address to, uint256 amount) external returns (bool);
}

contract MerkleAirdrop {
    IERC20 public token;
    bytes32 public merkleRoot;
    mapping(address => bool) public hasClaimed;
    
    event Claimed(address indexed user, uint256 amount);
    event MerkleRootUpdated(bytes32 newRoot);
    
    constructor(address _token, bytes32 _merkleRoot) {
        token = IERC20(_token);
        merkleRoot = _merkleRoot;
    }
    
    // TODO: Implement claim
    function claim(uint256 amount, bytes32[] calldata proof) external {
        // Your code here
        // 1. Check not already claimed
        // 2. Verify Merkle proof
        // 3. Mark as claimed
        // 4. Transfer tokens
    }
    
    // TODO: Implement verifyProof
    function verifyProof(
        bytes32[] calldata proof,
        bytes32 leaf
    ) internal view returns (bool) {
        // Your code here
        // Reconstruct root from leaf and proof
        // Compare with stored merkleRoot
    }
    
    // TODO: Implement hashLeaf
    function hashLeaf(address account, uint256 amount) internal pure returns (bytes32) {
        // Your code here
        // Hash user address and amount
    }
    
    // Update Merkle root (admin only)
    function updateMerkleRoot(bytes32 newRoot) external {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "claim",
                "args": [1000, ["0x1234...", "0x5678..."]],
                "expected": "success",
                "description": "Claim with valid proof"
            }
        ],
        "hints": [
            "Leaf = keccak256(abi.encodePacked(address, amount))",
            "Proof verification: hash up the tree to root",
            "Sort hashes before hashing pairs for deterministic tree",
            "Gas cost: ~30k per claim regardless of tree size"
        ],
        "tags": ["cryptography", "merkle-tree", "airdrop", "gas-optimization"],
        "solved_count": 0
    },
    {
        "problem_id": "crypto_012",
        "title": "Ring Signature Mixer",
        "description": """Implement a privacy-preserving token mixer using ring signatures.

Requirements:
- Deposit tokens anonymously
- Withdraw to different address
- Use ring signatures for unlinkability
- Support multiple denomination pools
- Prevent double-spending""",
        "difficulty": "middle",
        "category": "cryptography",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IERC20 {
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function transfer(address to, uint256 amount) external returns (bool);
}

contract RingMixer {
    IERC20 public token;
    uint256 public denomination = 1000e18; // Fixed deposit amount
    
    mapping(bytes32 => bool) public nullifiers;
    mapping(bytes32 => bool) public commitments;
    
    bytes32[] public merkleTree;
    uint256 public nextIndex;
    
    event Deposit(bytes32 indexed commitment, uint256 leafIndex);
    event Withdrawal(address indexed to, bytes32 nullifier);
    
    constructor(address _token) {
        token = IERC20(_token);
    }
    
    // TODO: Implement deposit
    function deposit(bytes32 commitment) external {
        // Your code here
        // 1. Transfer tokens from user
        // 2. Add commitment to Merkle tree
        // 3. Store commitment
    }
    
    // TODO: Implement withdraw
    function withdraw(
        address recipient,
        bytes32 nullifier,
        bytes32 root,
        bytes32[] calldata proof,
        uint256[8] calldata ringSignature
    ) external {
        // Your code here
        // 1. Verify nullifier not used
        // 2. Verify Merkle proof
        // 3. Verify ring signature
        // 4. Mark nullifier as used
        // 5. Transfer tokens to recipient
    }
    
    // TODO: Implement verifyRingSignature
    function verifyRingSignature(
        bytes32 message,
        uint256[8] calldata signature,
        bytes32[] calldata publicKeys
    ) internal pure returns (bool) {
        // Your code here
        // Ring signature verification
    }
    
    // TODO: Implement calculateMerkleRoot
    function calculateMerkleRoot(
        bytes32 leaf,
        uint256 index,
        bytes32[] calldata proof
    ) internal pure returns (bytes32) {
        // Your code here
    }
}""",
        "test_cases": [
            {
                "type": "transaction",
                "function": "deposit",
                "args": ["0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"],
                "expected": "success",
                "description": "Anonymous deposit"
            }
        ],
        "hints": [
            "Commitment = hash(secret, nullifier)",
            "Nullifier prevents double-spending",
            "Ring signature proves membership without revealing which member",
            "Use Linkable Spontaneous Anonymous Group (LSAG) signatures",
            "Merkle tree tracks all deposits"
        ],
        "tags": ["cryptography", "privacy", "ring-signature", "mixer"],
        "solved_count": 0
    },

    # Expert Level
    {
        "problem_id": "crypto_013",
        "title": "Zero-Knowledge Proof Verifier",
        "description": """Implement a zk-SNARK verifier for private transactions.

Requirements:
- Verify zk-SNARK proofs on-chain
- Support Groth16 verification
- Verify statement without revealing witness
- Efficient pairing checks
- Support multiple circuits""",
        "difficulty": "expert",
        "category": "cryptography",
        "initial_code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

library Pairing {
    struct G1Point {
        uint256 X;
        uint256 Y;
    }
    
    struct G2Point {
        uint256[2] X;
        uint256[2] Y;
    }
    
    // TODO: Implement pairing check
    function pairing(G1Point[] memory p1, G2Point[] memory p2) internal view returns (bool) {
        // Your code here
        // Use precompiled contract for bn256 pairing
    }
}

contract ZKVerifier {
    using Pairing for *;
    
    struct VerifyingKey {
        Pairing.G1Point alpha;
        Pairing.G2Point beta;
        Pairing.G2Point gamma;
        Pairing.G2Point delta;
        Pairing.G1Point[] gammaABC;
    }
    
    struct Proof {
        Pairing.G1Point a;
        Pairing.G2Point b;
        Pairing.G1Point c;
    }
    
    VerifyingKey verifyingKey;
    
    // TODO: Implement verify
    function verify(
        uint256[] memory input,
        Proof memory proof
    ) public view returns (bool) {
        // Your code here
        // Groth16 verification:
        // e(A, B) = e(alpha, beta) * e(vk_x, gamma) * e(C, delta)
    }
    
    // TODO: Implement verifyingKeyHash
    function verifyingKeyHash() public view returns (bytes32) {
        // Your code here
    }
}

contract PrivateTransfer {
    ZKVerifier public verifier;
    
    mapping(bytes32 => bool) public nullifiers;
    mapping(bytes32 => bool) public commitments;
    
    event Deposit(bytes32 indexed commitment);
    event Withdrawal(bytes32 indexed nullifier);
    
    // TODO: Implement deposit
    function deposit(bytes32 commitment) external payable {
        // Your code here
    }
    
    // TODO: Implement withdraw
    function withdraw(
        bytes32 nullifier,
        bytes32 root,
        address recipient,
        uint256[8] calldata proof
    ) external {
        // Your code here
        // 1. Verify proof
        // 2. Check nullifier not used
        // 3. Transfer funds
    }
}""",
        "test_cases": [
            {
                "type": "call",
                "function": "verify",
                "args": [[1, 2, 3], "proof_data"],
                "expected": "true",
                "description": "Verify valid zk-SNARK proof"
            }
        ],
        "hints": [
            "Use precompiled contract at address 0x08 for pairing",
            "Groth16: 3 pairings for verification",
            "vk_x = sum of gammaABC[i] * input[i]",
            "Efficient: verify in ~250k gas",
            "Use libraries like snarkjs for proof generation"
        ],
        "tags": ["cryptography", "zero-knowledge", "zk-snark", "privacy", "expert"],
        "solved_count": 0
    },
]

def get_problems():
    """Return all problems with created_at timestamp"""
    for problem in PROBLEMS:
        problem["created_at"] = datetime.now(timezone.utc).isoformat()
    return PROBLEMS
