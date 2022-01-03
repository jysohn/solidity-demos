from brownie import SimpleStorage, accounts

def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # Assert
    assert starting_value == expected

def test_store():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    simple_storage.store(5, {"from": account})
    new_value = simple_storage.retrieve()
    expected = 5
    assert new_value == expected