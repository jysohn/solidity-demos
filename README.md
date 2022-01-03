# solidity-demos
Testing grounds for Solidity development

# Notes on running Ganache 
To kick off local blockchain via CLI
```sh
ganache-cli
```
To work with the same addresses
```sh
ganache-cli --deterministic
```

# Notes on running Eth-Brownie
Initialize Brownie dev environment
```sh
brownie init
```
Compile project using Brownie
```sh
brownie compile
```
Run .py using Brownie
```sh
brownie run scripts/<script_name>.py
```
View Brownie accounts
```sh
brownie accounts list
```
Create or delete Brownie accounts
```sh
brownie accounts <new | delete> <account name>
```
Run all of the test functions in /tests
```sh
brownie test
```
Run only specified test function (e.g. test_store())
```sh
brownie test -k test_store
```
Run Python for debugging (allows variable calls)
```sh
brownie test --pdb
```
