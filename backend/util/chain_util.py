import json
import uuid

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec


class ChainUtil:

    @staticmethod
    def generate_keypair():
        return ec.generate_private_key(
            ec.SECP256K1(),
            default_backend()
        )

    @staticmethod
    def serialize_public_key(public_key):
        return public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode('utf-8')

    @staticmethod
    def deserialize_public_key(public_key):
        deserialized_public_key = serialization.load_pem_public_key(
            public_key.encode('utf-8'),
            default_backend()
        )

        return deserialized_public_key

    @staticmethod
    def id():
        return uuid

    @staticmethod
    def verify_signature(public_key, signature, data):
        try:
            public_key.verify(
                signature,
                json.dumps(data).encode('utf-8'),
                ec.ECDSA(hashes.SHA256())
            )
            return True
        except InvalidSignature:
            return False
