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


# pause/unpause function
def test_pause_unpause(contract):
    assert contract.paused() == False
    contract.pause()
    assert contract.paused() == True
    contract.unpause()
    assert contract.paused() == False
    contract.pause()
    assert contract.paused() == True


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
    contract.approve(accounts[1], 100)
    assert contract.allowance(accounts[0], accounts[1]) == 100


def test_approve_WhenPaused(contract):
    contract.pause()
    with reverts():
        contract.approve(accounts[1], 100)

    contract.unpause()
    contract.approve(accounts[1], 100)
    assert contract.allowance(accounts[0], accounts[1]) == 100


# transferFrom function
def test_transferFrom(contract):
    contract.increaseAllowance(accounts[1], 500, {"from": accounts[0]})
    contract.transferFrom(accounts[0], accounts[2], 100, {"from": accounts[1]})
    assert contract.balanceOf(accounts[2]) == 100
    assert contract.balanceOf(accounts[1]) == 0
    assert contract.balanceOf(accounts[0]) == initialSupply - 100


def test_transferFrom_WhenPaused(contract):
    contract.increaseAllowance(accounts[1], 500, {"from": accounts[0]})
    contract.pause()
    with reverts():
        contract.transferFrom(accounts[0], accounts[2], 100, {"from": accounts[1]})

    # test when unpaused again
    contract.unpause()
    contract.transferFrom(accounts[0], accounts[2], 100, {"from": accounts[1]})
    assert contract.balanceOf(accounts[2]) == 100
    assert contract.balanceOf(accounts[1]) == 0
    assert contract.balanceOf(accounts[0]) == initialSupply - 100


# increaseAllowance function
def test_increaseAllowance(contract):
    contract.transfer(accounts[1], 1000)
    contract.increaseAllowance(accounts[1], 500, {"from": accounts[0]})
    assert contract.allowance(accounts[0], accounts[1]) == 500


def test_increaseAllowance_WhenPaused(contract):
    contract.transfer(accounts[1], 1000)
    contract.pause()
    with reverts():
        contract.increaseAllowance(accounts[1], 500, {"from": accounts[0]})

    contract.unpause()
    contract.increaseAllowance(accounts[1], 500, {"from": accounts[0]})
    assert contract.allowance(accounts[0], accounts[1]) == 500


# decreaseAllowance function
def test_decreaseAllowance(contract):
    contract.transfer(accounts[1], 1000)
    contract.increaseAllowance(accounts[1], 500, {"from": accounts[0]})
    assert contract.allowance(accounts[0], accounts[1]) == 500

    contract.decreaseAllowance(accounts[1], 250, {"from": accounts[0]})
    assert contract.allowance(accounts[0], accounts[1]) == 250


def test_decreaseAllowance_WhenPaused(contract):
    contract.transfer(accounts[1], 1000)
    contract.increaseAllowance(accounts[1], 500, {"from": accounts[0]})
    assert contract.allowance(accounts[0], accounts[1]) == 500

    contract.pause()
    with reverts():
        contract.decreaseAllowance(accounts[1], 250, {"from": accounts[0]})

    contract.unpause()
    contract.decreaseAllowance(accounts[1], 250)
    assert contract.allowance(accounts[0], accounts[1]) == 250


# _payTax function
def test_payTax(contract):
    contract.transfer(accounts[1], 1000)
    assert contract.balanceOf(accounts[1]) == 1000 - 100  # tax = 100
    assert contract.balanceOf(accounts[0]) == initialSupply - 1000 + 100  # tax = 100
