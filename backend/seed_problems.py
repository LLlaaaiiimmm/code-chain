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
]

def get_problems():
    """Return all problems with created_at timestamp"""
    for problem in PROBLEMS:
        problem["created_at"] = datetime.now(timezone.utc).isoformat()
    return PROBLEMS
