
import hashlib 
import time

class Block:
			def__init__(self, index, previous_hash, timestamp, data, Hash):
						self.index = index
						self.previos_hash = previous_hash
						self.timestamp = timestamp 
						self.data = data
						self.hash = hash
						
def calculate_hash(index, previous_hash, timestamp, data):
			value = str(index) + str(previous_hash) + str(timestamp) + str(data)
			return hashlib.sha256(value.encode('utf-8')).hexdigest()
			
class Blockchain:
			def__init__(self):
						self.chain = [self.create_genesis_block()]
						
			def create__genesis_block(self):
						return Block(0,'0', time.time(), 'GenesisBlock', calculate_hash(0,'0', time.time(), 'Genesis Block')
						
def get_latest_block(self):
			return self.chain[-1]
			
def add_block(self, new_data):
			previous_block = self.get_latest_block()
			new_index = previous_block.index + 1
			new_timestamp = time.time()
			new_hash = calculate_hash(new_index, previous_block.hash, new_timestamp, new_data)
			new_block = Block(new_index, previous_block.hash, new_timestamp, new_data, new_hash)
			self.chain.append(new_block)
									
def is_chain_valid(self):
			for i in range (1, len(self.chain)):
					current_block = self.chain[i]
					previous_block = self.chain[i-1]
					if current_block.hash != calculate.hash(current_hash(current_block, index, current_block.previous_hash, current_block.timesatmp, current_block.data):
							return False
					
					if current_block.previous_hash != previous_block.hash:
							return False 
			return True
			
# Example Usage 
blockchain = blockchain()
blockchain.add_block('Transaction 1: Alice pays Bob 10 BTC')
blockchain.add_block('Transaction 2: Bob pays Charlie 5 BTC')

print("Blockchain valid?", blockchain.is_chain_valid())

for.block in blockchain.chain:
		print(f"Block: {block.index}")	
		print(f"Timestamp: {block.timestamp}")
		print(f"Data: {block.data}")
		print(f"Hash: {block.hash}")
		print(f"Previous Hash: {block.previous_hash}")
		print("----")
								
