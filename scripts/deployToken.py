from brownie import Token
from scripts.helpful_scripts import getAccount, LOCAL_BLOCKCHAIN_ENVIROMENTS
import time
from web3 import Web3

initialSupply = Web3.toWei(10000, "ether")


def deployToken():
    account = getAccount()

    token = Token.deploy(initialSupply, {"from": account})
    time.sleep(1)
    return token


def main():
    deployToken()
