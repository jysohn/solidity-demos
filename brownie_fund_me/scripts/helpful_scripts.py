from brownie import network, config, accounts, MockV3Aggregator
from dotenv import load_dotenv
load_dotenv()
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]

DECIMALS = 18
STARTING_PRICE = 2000

def get_account():
    if(network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    # only deploy if haven't yet
    if (len(MockV3Aggregator) <= 0):
        MockV3Aggregator.deploy(
            DECIMALS, 
            Web3.toWei(STARTING_PRICE, "ether"), 
            {"from": get_account()}
            )
        # use the most recently deployed
    print("Mocks Deployed!")