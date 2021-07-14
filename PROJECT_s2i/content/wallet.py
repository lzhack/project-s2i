from web3 import Web3

w3 = Web3(Web3.HTTPProvider('')) # <---- ENDPOINT ROPSTEN INFURIA
account = w3.eth.account.create()
privateKey = account.privateKey.hex()
address = account.address

print (f"Your address: {address}\nYour key: {privateKey}")