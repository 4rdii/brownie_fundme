from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIROMENTS,
)


def deploy_fund_me():
    account = get_account()
    # pass the price feed address to our fund me local contract
    # if we are on a presistent network like rinkeby use associated address
    # otherwise deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIROMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        price_feed_address = deploy_mocks()
    print("Deploying fundme contract...")
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
