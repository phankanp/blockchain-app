from backend.util.generate_hash import generate_hash
from backend.blockchain.Block import Block


def test_generate_hash():
    assert generate_hash(1, '2', [3]) == generate_hash(1, [3], '2')
    assert Block.generate_genesis().hash == '3d676e303d254e846fe8196df400983037e32458bf5d08a77609836a9b3b2869'
