from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIROMENT = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIROMENTS = ["development", "ganache-local"]
DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    print(f"this is the netwrok type: {network.show_active()}")
    if network.show_active() == "ganache-local" and len(accounts) == 0:
        accounts.add(config["wallets"]["ganache_local"]["account0"])
        accounts.add(config["wallets"]["ganache_local"]["account1"])
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIROMENTS
        or network.show_active() in FORKED_LOCAL_ENVIROMENT
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"the active netwrok is{network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": accounts[0]})
    print("Mocks Deployed!")
    return MockV3Aggregator[-1].address
