# from eth_account.messages import encode_defunct
from web3 import Web3
# from web3.types import TxReceipt

def sendTransaction(message):
    w3 = Web3(Web3.HTTPProvider('')) # <---- ENDPOINT ROPSTEN INFURIA
    address = '' # <---- ADDRESS
    privateKey = '' # <---- PKEY
    nonce = w3.eth.getTransactionCount(address)
    gasPrice = w3.eth.gasPrice
    value = w3.toWei(0, 'ether')
    signedTx = w3.eth.account.signTransaction(dict(
        nonce=nonce,
        gasPrice=gasPrice,
        gas=100000,
        to='0x0000000000000000000000000000000000000000',
        value=value,
        data=message.encode('utf-8'),
    ), privateKey)

    tx = w3.eth.sendRawTransaction(signedTx.rawTransaction)
    txId = w3.toHex(tx)
    return txId