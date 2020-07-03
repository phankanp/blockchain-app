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


def main(self):
    pass


if __name__ == '__main__':
    main()
