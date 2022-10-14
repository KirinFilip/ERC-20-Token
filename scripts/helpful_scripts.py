from brownie import accounts, network, config

FORKED_LOCAL_ENVIROMENTS = ["mainnet-fork"]
LOCAL_BLOCKCHAIN_ENVIROMENTS = ["development", "ganache-local"]


def getAccount(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIROMENTS
        or network.show_active() in FORKED_LOCAL_ENVIROMENTS
    ):
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])
