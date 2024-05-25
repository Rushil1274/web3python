from web3 import Web3


# Connect to blockchain
node_url = "https://bsc-mainnet.core.chainstack.com/6f75e59fedb7124602de2b6f8b0e1757"
web3 = Web3(Web3.HTTPProvider(node_url))

if web3.is_connected():
    print("Connection Successful")
else:
    print("Connection Failed")

# latest block
print("Latest block : ", web3.eth.block_number)

# balance
balance = web3.eth.get_balance("0xA85668FdabFD8f7B35A3c9a9f56B1F0E2d2c183b")
normal_number = web3.from_wei(balance, 'ether')
print(balance) #balance in wei
print(normal_number)

# pending transaction
pending_tx_filter = web3.eth.filter('pending')
pending_tx = pending_tx_filter.get_new_entries() # this is a list 
# print(pending_tx)

# for hash in pending_tx:
#     print(web3.to_hex(hash))
#     print(hash)

# details of transaction
detail = web3.eth.get_transaction('0xd15d5d6796a8499dd399c0c13132b8dc720f9a75a16237e579276ddbbc59b1ea')
print(detail)

info = ['from', 'to', 'value']
# info = ['value']

dictonary = dict(detail)
for key, val in dictonary.items():
    print(key, val)
    # for word in info:
    #     if key == word:
    #         print(key, val)
    #         # print(key, web3.from_wei(val, 'ether'))
