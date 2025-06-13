import datetime
from blockchain_simulation import Block, Blockchain

# Create a new blockchain
my_blockchain = Blockchain()

print("Mining block 1...")
my_blockchain.add_block(Block(1, datetime.datetime.now(), {"amount": 4, "sender": "Alice", "receiver": "Bob"}, ""))

print("Mining block 2...")
my_blockchain.add_block(Block(2, datetime.datetime.now(), {"amount": 8, "sender": "Bob", "receiver": "Charlie"}, ""))

print("Mining block 3...")
my_blockchain.add_block(Block(3, datetime.datetime.now(), {"amount": 12, "sender": "Charlie", "receiver": "David"}, ""))

print("\nBlockchain:")
for block in my_blockchain.chain:
    print(f"Index: {block.index}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Hash: {block.hash}")
    print("-" * 20)


