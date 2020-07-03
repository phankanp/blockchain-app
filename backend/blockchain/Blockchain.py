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
        if len(chain) <= self.chain:
            raise Exception('Incoming chain must be longer than current chain')
        elif not Blockchain.is_valid_chain(chain):
            raise Exception('Incoming chain is invalid')

        self.chain = chain

def main(self):
    pass


if __name__ == '__main__':
    main()
