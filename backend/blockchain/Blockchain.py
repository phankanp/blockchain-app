from backend.blockchain.Block import Block


class Blockchain:
    """
    Blockchain: A ledger for recording transactions
    Implemented as a list of blocks
    """

    def __init__(self):
        """
        Initializes list to store blocks
        """
        self.chain = [Block.generate_genesis()]

    def add_block(self, data):
        """
        Add block to chain list
        """
        self.chain.append(Block.mine_block(self.chain[-1], data))

    def __repr__(self):
        """
        Return string representation of Blockchain object
        """
        return f'Blockchain: {self.chain}'

    def to_json(self):
        """
        Serialize blockchain into list of blocks
        """
        block_list = []

        for block in self.chain:
            block_list.append(block.to_json())

        return block_list

    @staticmethod
    def from_json(chain_json):
        """
        Deserialize a list of serialized blocks into a Blokchain instance.
        """
        blockchain = Blockchain()

        chain = []

        for block_json in chain_json:
            chain.append(Block.from_json(block_json))

        blockchain.chain = chain

        return blockchain

    @staticmethod
    def is_valid_chain(chain):
        """
        Checks if incoming chain is valid
        """
        if chain[0] != Block.generate_genesis():
            raise Exception('First block must be genesis block')

        for i in range(1, len(chain)):
            block = chain[i]
            previous_block = chain[i - 1]
            if block.previous_hash != previous_block.hash or not Block.is_valid_proof(block, block.hash):
                return False

        return True

    def replace_chain(self, chain):
        """
        Checks if incoming chain can replace local chain
        """
        if len(chain) <= len(self.chain):
            raise Exception('Incoming chain must be longer than current chain')
        elif Blockchain.is_valid_chain(chain) == False:
            raise Exception('Incoming chain is invalid')

        self.chain = chain


def main():
    pass


if __name__ == '__main__':
    main()
