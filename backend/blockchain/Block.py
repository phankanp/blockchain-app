import time

from backend.constants import MINE_RATE, DIFFICULTY
from backend.util.generate_hash import generate_hash
from backend.util.hex_to_binary import hex_to_binary

GENESIS_DATA = {
    'index': 0,
    'timestamp': 1,
    'previous_hash': 'genesis_last_hash',
    'hash': 'genesis_hash',
    'data': [],
    'difficulty': DIFFICULTY,
    'nonce': 'genesis_nonce'
}


class Block:
    """
    Block: Container to store transaction data
    Store information about transactions on blockchain
    """

    def __init__(self, index, timestamp, previous_hash, hash, data, difficulty, nonce):
        """
        Block object constructor
        """
        self.index = index
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.hash = hash
        self.data = data
        self.difficulty = difficulty
        self.nonce = nonce

    @staticmethod
    def mine_block(previous_block, data):
        """
        Mines a block using the previous block and given data
        """
        index = previous_block.index + 1
        timestamp = time.time_ns()
        previous_hash = previous_block.hash
        difficulty = Block.adjust_difficulty(previous_block, timestamp)
        nonce = 0

        mined_block = Block(index, timestamp, previous_hash, '', data, difficulty, nonce)
        hash = Block.proof_of_work(previous_block, mined_block)
        mined_block.hash = hash

        return mined_block

    @staticmethod
    def proof_of_work(previous_block, block):
        """
        Continuously generates a new hash using different nonce values until hash meets difficulty requirements
        """
        hash = generate_hash(block)

        while not hex_to_binary(hash).startswith('0' * block.difficulty):
            block.nonce += 1
            block.timestamp = time.time_ns()
            block.difficulty = Block.adjust_difficulty(previous_block, block.timestamp)
            hash = generate_hash(block)

        return hash

    @staticmethod
    def is_valid_proof(block, block_hash):
        """
        Checks if block hash is valid and meets difficulty requirements
        """
        validate_block = Block(
            block.index,
            block.timestamp,
            block.previous_hash,
            '',
            block.data,
            block.difficulty,
            block.nonce)

        return hex_to_binary(block_hash).startswith('0' * block.difficulty) and block_hash == generate_hash(
            validate_block)

    @staticmethod
    def adjust_difficulty(previous_block, timestamp):
        """
        Utility function to adjust difficulty
        """
        difficulty = previous_block.difficulty

        if previous_block.timestamp + MINE_RATE > timestamp:
            difficulty += 1
        else:
            difficulty -= 1

        return difficulty

    @staticmethod
    def generate_genesis():
        """
        Return first block (genesis block) of chain
        """
        return Block(**GENESIS_DATA)

    def __repr__(self):
        """
        Return string representation of Block object
        """
        return (
            'Block('
            f'timestamp: {self.index}, '
            f'timestamp: {self.timestamp}, '
            f'last_hash: {self.previous_hash}, '
            f'hash: {self.hash}, '
            f'data: {self.data},'
            f'difficulty: {self.difficulty}, '
            f'nonce: {self.nonce})'
        )

    def to_json(self):
        """
        Serialize blockchain into dictionary
        """
        return self.__dict__

def main():
    genesis_block = Block.generate_genesis()
    block = Block.mine_block(genesis_block, 'foo')
    print(block)


if __name__ == '__main__':
    main()
