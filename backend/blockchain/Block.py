import time

from backend.util.generate_hash import generate_hash
from backend.util.hex_to_binary import hex_to_binary
from backend.constants import MINE_RATE, DIFFICULTY

GENESIS_DATA = {
    'index': 0,
    'timestamp': 1,
    'previous_hash': 'genesis_last_hash',
    'hash': generate_hash(0, 1, 'genesis_last_hash', [], DIFFICULTY, 'genesis_nonce'),
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
        hash = generate_hash(index, timestamp, previous_hash, data, difficulty, nonce)

        while not hex_to_binary(hash).startswith('0' * difficulty):
            nonce += 1
            timestamp = time.time_ns()
            difficulty = Block.adjust_difficulty(previous_block, timestamp)
            hash = generate_hash(index, timestamp, previous_hash, data, difficulty, nonce)

        return Block(index, timestamp, previous_hash, hash, data, difficulty, nonce)

    @staticmethod
    def adjust_difficulty(last_block, timestamp):
        """
        Utility function to adjust difficulty
        """
        difficulty = last_block.difficulty

        if last_block.timestamp + MINE_RATE > timestamp:
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


def main():
    genesis_block = Block.generate_genesis()
    block = Block.mine_block(genesis_block, 'foo')
    print(block)


if __name__ == '__main__':
    main()
