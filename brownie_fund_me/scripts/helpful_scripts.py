from brownie import network, config, accounts
from dotenv import load_dotenv
load_dotenv()

def get_account():
    if(network.show_active() == "development"):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])