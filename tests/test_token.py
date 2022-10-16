# TEST 1: Is the token ERC-20 Token (test all ERC-20 functions)
# TEST 2: Is the token burnable
# TEST 3: Is the token pausable
# TEST 4: Is the tax functioning as intended

import pytest
from brownie import accounts, reverts
from web3 import Web3
from scripts.deployToken import deployToken, initialSupply
from scripts.helpful_scripts import getAccount


@pytest.fixture
def contract():
    return deployToken()


# _mint function
## minter address
def test_minterAddress(contract):
    assert contract.owner() == getAccount()


## totalSupply
def test_mintInitialSupply(contract):
    assert contract.totalSupply() == initialSupply


# pause function
def test_pause(contract):
    contract.pause()
    assert contract.paused() == True


# unpause function
def test_unpause(contract):
    assert contract.paused() == False
    contract.pause()
    assert contract.paused() == True
    contract.unpause()
    assert contract.paused() == False


# burn function
def test_burn(contract):
    contract.burn(1000)
    assert contract.totalSupply() == initialSupply - 1000


def test_burn_WhenPaused(contract):
    contract.pause()
    with reverts():
        contract.burn(100)


# transfer function
def test_transfer(contract):
    contract.transfer(accounts[1], 100)
    assert contract.balanceOf(accounts[0]) == initialSupply - 100
    assert contract.balanceOf(accounts[1]) == 100


def test_transfer_WhenPaused(contract):
    contract.pause()
    with reverts():
        contract.transfer(accounts[1], 100)

    # test when unpaused again
    contract.unpause()
    contract.transfer(accounts[1], 100)
    assert contract.balanceOf(accounts[0]) == initialSupply - 100
    assert contract.balanceOf(accounts[1]) == 100


# allowance function
def test_allowance(contract):
    allowance = contract.allowance(contract.owner(), accounts[1])
    assert allowance == 0


def test_allowance_WhenPaused(contract):
    contract.pause()
    with reverts():
        contract.allowance(contract.owner(), accounts[1])

    # test when unpaused again
    contract.unpause()
    allowance = contract.allowance(contract.owner(), accounts[1])
    assert allowance == 0


# approve function
def test_approve(contract):
    pass


def test_approve_WhenPaused(contract):
    contract.pause()


# transferFrom function
def test_transferFrom(contract):
    pass


def test_transferFrom_WhenPaused(contract):
    contract.pause()


# increaseAllowance function
def test_increaseAllowance(contract):
    pass


def test_increaseAllowance_WhenPaused(contract):
    contract.pause()


# decreaseAllowance function
def test_decreaseAllowance(contract):
    pass


def test_decreaseAllowance_WhenPaused(contract):
    contract.pause()


# _payTax function
def test_payTax(contract):
    pass
