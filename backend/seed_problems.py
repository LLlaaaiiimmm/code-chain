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
            }
        ],
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
]

def get_problems():
    """Return all problems with created_at timestamp"""
    for problem in PROBLEMS:
        problem["created_at"] = datetime.now(timezone.utc).isoformat()
    return PROBLEMS
