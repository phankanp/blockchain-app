from backend.blockchain.block import Block
from backend.util.generate_hash import generate_hash


def test_generate_hash():
    block = Block.generate_genesis()
    assert generate_hash(block) == generate_hash(block)
    assert generate_hash(block) == 'a65ae033a322f80df233c856ae2cbb2677b16a69eebeda4c95b3cea25a86092d'
