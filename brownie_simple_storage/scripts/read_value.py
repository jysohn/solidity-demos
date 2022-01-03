from brownie import SimpleStorage, accounts, config


def read_contract():
    # -1 for most recent deployment
    deployment_number = -1
    simple_storage = SimpleStorage[deployment_number]
    print(simple_storage.retrieve())

def main():
    read_contract()