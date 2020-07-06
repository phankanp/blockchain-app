from backend.blockchain.block import GENESIS_DATA
from backend.blockchain.blockchain import Blockchain


def test_blockchain_instance():
    blockchain = Blockchain()

    assert isinstance(blockchain, Blockchain)
    assert blockchain.chain[0].hash == GENESIS_DATA['hash']


def test_add_block():
    blockchain = Blockchain()
    data = '123'
    blockchain.add_block(data)

    assert isinstance(blockchain, Blockchain)
    assert blockchain.chain[-1].data == data
