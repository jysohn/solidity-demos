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
Run .py using Brownie (automatically runs Ganache CLI locally)
```sh
brownie run scripts/<script_name>.py
```
View Brownie accounts
```sh
brownie accounts list
```
View Brownie networks
```sh
brownie networks list
```
Run Brownie network (see below for how to add networks)
```sh
brownie run scripts/<script_name>.py --network rinkeby
```
Create or delete Brownie accounts
```sh
brownie accounts <new | delete> <account name>
```
Run all of the test functions in /tests
```sh
brownie test <-s for verbose>
```
Run only specified test function (e.g. test_store())
```sh
brownie test -k test_store
```
Run Python for debugging (allows variable calls)
```sh
brownie test --pdb
```
Run Brownie console for direct calls
```sh
brownie console
```
# Linking Ganache UI onto Brownie
To link Ganache UI with Brownie, simply run with UI open
```sh
brownie run scripts/<script_name>.py
```
To add new network to Brownie (in this case, ganache-local to Ethereum)
```sh
brownie networks add Ethereum ganache-local host=http://127.0.0.1:8545 chainid=1337
```
