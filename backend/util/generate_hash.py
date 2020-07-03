import hashlib
import json


def generate_hash(block):
    """
    Generate hexa hash from block object properties
    """
    block_string = json.dumps(block.__dict__, sort_keys=True)
    return hashlib.sha256(block_string.encode()).hexdigest()