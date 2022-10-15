# TEST 1: Is the token ERC-20 Token (test all ERC-20 functions)
# TEST 2: Is the token burnable
# TEST 3: Is the token pausable
# TEST 4: Is the tax functioning as intended

import pytest
from brownie import reverts
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
def test_burn():
    pass


# transfer function
def test_transfer():
    pass


# allowance function

# approve function

# transferFrom function

# increaseAllowance function

# decreaseAllowance function

# _payTax function
