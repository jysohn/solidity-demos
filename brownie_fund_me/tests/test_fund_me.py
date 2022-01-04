from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account
from scripts.deploy import deploy_fund_me
from brownie import network, accounts, exceptions
import pytest

def test_can_fund_and_withdraw():
    # can pass below if statement to only test in local networks
    account = get_account()
    fund_me = deploy_fund_me()
    tx = fund_me.fund({"from": account, "value": 10})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 10
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0

def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing")
    not_owner = accounts.add()
    fund_me = deploy_fund_me()
    # verify exception is thrown with illegal withdraw
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": not_owner})