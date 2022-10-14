// SPDX-License-Identifier: MIT
pragma solidity 0.8.13;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

contract Token is ERC20, ERC20Burnable, Ownable, Pausable {
    // state variables
    uint256 public taxPercentage;

    constructor(uint256 initialSupply) ERC20("ProxyToken", "PT") {
        _mint(msg.sender, initialSupply);
        taxPercentage = 10;
    }

    // Public functions

    function pause() public onlyOwner {
        _pause();
    }

    function unpause() public onlyOwner {
        _unpause();
    }

    function burn(uint256 amount) public virtual override whenNotPaused {
        _burn(_msgSender(), amount);
    }

    function transfer(address to, uint256 amount)
        public
        virtual
        override
        whenNotPaused
        returns (bool)
    {
        amount = _payTax(amount);
        return super.transfer(to, amount);
    }

    function allowance(address owner, address spender)
        public
        view
        virtual
        override
        whenNotPaused
        returns (uint256)
    {
        return super.allowance(owner, spender);
    }

    function approve(address spender, uint256 amount)
        public
        virtual
        override
        whenNotPaused
        returns (bool)
    {
        return super.approve(spender, amount);
    }

    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public virtual override whenNotPaused returns (bool) {
        amount = _payTax(amount);
        return super.transferFrom(from, to, amount);
    }

    function increaseAllowance(address spender, uint256 addedValue)
        public
        virtual
        override
        whenNotPaused
        returns (bool)
    {
        return super.increaseAllowance(spender, addedValue);
    }

    function decreaseAllowance(address spender, uint256 subtractedValue)
        public
        virtual
        override
        whenNotPaused
        returns (bool)
    {
        return super.decreaseAllowance(spender, subtractedValue);
    }

    // Internal functions

    // Pays taxes to the owner of the contract
    // The tax is calculated as sales tax
    function _payTax(uint256 amount) internal virtual returns (uint256) {
        uint256 tax = amount * (taxPercentage / 100);
        _transfer(msg.sender, owner(), tax);
        amount = amount - tax;
        return amount;
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }
}
