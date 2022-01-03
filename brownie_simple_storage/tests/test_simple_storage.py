from brownie import SimpleStorage, accounts, config, network

def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # Assert
    assert starting_value == expected

def get_account():
    if(network.show_active() == "development"):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def test_store():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    simple_storage.store(5, {"from": account})
    new_value = simple_storage.retrieve()
    expected = 5
    assert new_value == expected