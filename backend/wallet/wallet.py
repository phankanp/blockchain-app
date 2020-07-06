import json

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec

from backend.config import INITIAL_BALANCE
from backend.util.chain_util import ChainUtil


class Wallet:
    """
    Miners wallet which holds public/private keys and balance
    """

    def __init__(self):
        self.balance = INITIAL_BALANCE
        self.key_pair = ChainUtil.generate_keypair()
        self.public_key = ChainUtil.serialize_public_key(self.key_pair.public_key())

    def __repr__(self):
        """
        Return string representation of Wallet object
        """
        return (
            'Wallet('
            f'balance: {self.balance}, '
            f'public_key: {str(self.public_key)})'
        )

    def sign(self, data):
        """
        Generates transaction signature
        """
        return self.key_pair.sign(
            json.dumps(data).encode('utf-8'),
            ec.ECDSA(hashes.SHA256())
        )
