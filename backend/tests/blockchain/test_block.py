from backend.blockchain.Block import Block
from backend.blockchain.Block import GENESIS_DATA
from backend.util.hex_to_binary import hex_to_binary


def test_mine_block():
    previous_block = Block.generate_genesis()
    data = '123'

    next_block = Block.mine_block(previous_block, data)

    assert isinstance(next_block, Block)
    assert next_block.data == data
    assert previous_block.hash == next_block.previous_hash
    assert hex_to_binary(next_block.hash).startswith('0' * next_block.difficulty)


def test_genesis_block():
    genesis_block = Block.generate_genesis()

    assert isinstance(genesis_block, Block)
    for k, v in GENESIS_DATA.items():
        assert getattr(genesis_block, k) == v