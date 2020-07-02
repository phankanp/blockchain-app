import time

from generate_hash import generate_hash


class Block:
    """
    Block: Container to store transaction data
    Store information about transactions on blockchain
    """

    def __init__(self, index, timestamp, previous_hash, hash, data):
        """
        Block object constructor
        :param index: Unique ID of block
        :param timestamp: Time of creation
        :param previous_hash: Hash of previous block in chain
        :param hash: Hash of block
        :param data: Data to store in block
        """
        self.index = index
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.hash = hash
        self.data = data

    @staticmethod
    def mine_block(previous_block, data):
        """
        Mines a block using the previous block and given data
        :param previous_block: Previous block in the chain, which new block will be a part of
        :param data: Data to be in mined block
        :return: Mined block
        """
        index = previous_block.index + 1
        timestamp = time.time_ns()
        last_hash = previous_block.hash
        hash = generate_hash(index, timestamp, last_hash, data)

        return Block(index, timestamp, last_hash, hash, data)

    @staticmethod
    def generate_genesis():
        """
        :return: First block (genesis block) of chain
        """
        return Block(0, time.time_ns(), 'genesis_last_hash', 'genesis_hash', [1])

    def __repr__(self):
        """
        :return: String representation of Block object
        """
        return (
            'Block('
            f'timestamp: {self.index}, '
            f'timestamp: {self.timestamp}, '
            f'last_hash: {self.previous_hash}, '
            f'hash: {self.hash}, '
            f'data: {self.data})'
        )

    def main(self):
        pass

    if __name__ == '__main__':
        main()
