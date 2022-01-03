from brownie import accounts, config, SimpleStorage, network
import os


def deploy_simple_storage():
    #account = accounts[0]
    #print(account)

    #account = accounts.load("rinkeby-account")
    #print(account)

    #account = accounts.add(os.getenv("PRIVATE_KEY"))
    #print(account)

    #account = accounts.add(config["wallets"]["from_key"])
    #print(account)

    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)

    new_value = 5
    txn = simple_storage.store(new_value, {"from": account})
    txn.wait(1)
    stored_value = simple_storage.retrieve()
    print(stored_value)

def get_account():
    if(network.show_active() == "development"):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def main():
    deploy_simple_storage()