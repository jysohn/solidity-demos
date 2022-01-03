from brownie import FundMe
from scripts.helpful_scripts import get_account

def fund():
    fund_me = FundMe[-1]
    account = get_account()
    print("Funding")
    fund_me.fund({"from": account, "value": 100})

def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    print("Withdrawing")
    fund_me.withdraw({"from": account})

def main():
    fund()
    withdraw()