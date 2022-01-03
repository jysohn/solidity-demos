from brownie import FundMe
from scripts.helpful_scripts import get_account
from dotenv import load_dotenv
load_dotenv()

def deploy_fund_me():
    account = get_account()
    fund_me = FundMe.deploy({"from": account})
    print(f"Contract deployed to {fund_me.address}")

def main():
    deploy_fund_me()