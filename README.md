# ERC-20 Token

## Features:

* Fixed supply
* Burnable
* Pausable
* Transfer tax

## What is ERC20, Ethereum Request for Comment, number 20?

ERC-20 is the technical standard for fungible tokens created using the Ethereum blockchain. A fungible token is one that is interchangeable with another token, in other words, they have a property that makes each Token be exactly the same (in type and value) as another Token. For example, an ERC-20 Token acts just like the ETH, meaning that 1 Token is and will always be equal to all the other Tokens. This makes ERC20 tokens useful for things like a medium of exchange currency, voting rights, staking, and more.

### Tokens can represent virtually anything in Ethereum:
* reputation points in an online platform
* skills of a character in a game
* lottery tickets
* financial assets like a share in a company
* a fiat currency like USD
* an ounce of gold
* and more...

### Contents of the Standard

ERC-20 contains several functions and events that a token must implement. Keep in mind that this standard also governs actions that smart contracts take for the tokens being created. The minimum of functions and information needed in an ERC-20 compliant token are:

* **TotalSupply:** The total number of tokens that will ever be issued
* **BalanceOf:** The account balance of a token owner's account
* **Transfer:** Automatically executes transfers of a specified number of tokens to a specified address for transactions using the token
* **TransferFrom:** Automatically executes transfers of a specified number of tokens from a specified address using the token
* **Approve:** Allows a spender to withdraw a set number of tokens from a specified account, up to a specific amount
* **Allowance:** Returns a set number of tokens from a spender to the owner
* **Transfer:** An event triggered when a transfer is successful (an event)
* **Approval:** A log of an approved event (an event)

These code functions and events are integral for user/token implementation. More specifically, they assist in determining the number of tokens in circulation, storing and returning balances, making transfer and withdrawal requests, granting approval, and agreeing to automated transfers. This set of functions and signals ensures that Ethereum tokens of different types will all uniformly perform in any place within the Ethereum ecosystem. In addition, ERC-20-compliant tokens can be used interchangeably.
