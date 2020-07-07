import json
import uuid

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.utils import (
    encode_dss_signature,
    decode_dss_signature
)


class WalletUtil:

    @staticmethod
    def generate_keypair():
        """
        Generates private key using provided cryptography standard and backend
        """
        return ec.generate_private_key(
            ec.SECP256K1(),
            default_backend()
        )

    @staticmethod
    def serialize_public_key(public_key):
        """
        Serializes public key
        """
        return public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode('utf-8')

    @staticmethod
    def deserialize_public_key(public_key):
        """
        Deserializes public key
        """
        deserialized_public_key = serialization.load_pem_public_key(
            public_key.encode('utf-8'),
            default_backend()
        )

        return deserialized_public_key

    @staticmethod
    def id():
        """
        Generates unique id for transactions
        """
        return str(uuid.uuid4())

    @staticmethod
    def sign(key_pair, data):
        """
        Generates transaction signature
        """
        return decode_dss_signature(key_pair.sign(
            json.dumps(data).encode('utf-8'),
            ec.ECDSA(hashes.SHA256())
        ))

    @staticmethod
    def verify_signature(public_key, signature, data):
        """
        Verifies transaction signature
        """
        try:
            public_key.verify(
                encode_dss_signature(signature),
                json.dumps(data).encode('utf-8'),
                ec.ECDSA(hashes.SHA256())
            )
            return True
        except InvalidSignature:
            return False
