
import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, Hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = Hash

def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        # The genesis block's previous_hash is '0' and its data is 'Genesis Block'
        return Block(0, '0', time.time(), 'Genesis Block', calculate_hash(0, '0', time.time(), 'Genesis Block'))

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_data):
        previous_block = self.get_latest_block()
        new_index = previous_block.index + 1
        new_timestamp = time.time()
        # Calculate the hash for the new block using the previous block's hash
        new_hash = calculate_hash(new_index, previous_block.hash, new_timestamp, new_data)
        new_block = Block(new_index, previous_block.hash, new_timestamp, new_data, new_hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        # Check if the chain is valid by verifying the hash and previous hash of each block
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash is correct
            if current_block.hash != calculate_hash(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.data):
                return False

            # Check if the current block's previous hash points to the previous block's hash
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

# Example Usage
blockchain = Blockchain()
blockchain.add_block('Transaction 1: Alice pays Bob 10 BTC')
blockchain.add_block('Transaction 2: Bob pays Charlie 5 BTC')

print("Blockchain valid?", blockchain.is_chain_valid())

for block in blockchain.chain:
    print(f"Block: {block.index}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Hash: {block.hash}")
    print(f"Previous Hash: {block.previous_hash}")
    print("----")
print("Blockchain valid?", blockchain.is_chain_valid())

for.block in blockchain.chain:
		print(f"Block: {block.index}")	
		print(f"Timestamp: {block.timestamp}")
		print(f"Data: {block.data}")
		print(f"Hash: {block.hash}")
		print(f"Previous Hash: {block.previous_hash}")
		print("----")
								
