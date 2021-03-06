import json
import uuid
import hashlib

from ellipticcurve.ecdsa import Ecdsa
from ellipticcurve.privateKey import PrivateKey
from ellipticcurve.publicKey import PublicKey


class WalletUtil:

    @staticmethod
    def id():
        """
        Generates unique id for transactions
        """
        return str(uuid.uuid4())

    @staticmethod
    def generate_wallet_address(public_key):
        """
        Generates a wallet's address from public key
        :param public_key:
        :return:
        """
        address = (hashlib.sha256(PublicKey.fromPem(public_key).toDer().encode()).hexdigest())[0:8]

        return address

    @staticmethod
    def generate_keypair():
        """
        Generates private key using provided cryptography standard and backend
        """
        private_key = PrivateKey()

        return private_key

    @staticmethod
    def serialize_public_key(public_key):
        """
        Serializes public key
        """
        return PublicKey.toPem(public_key)

    @staticmethod
    def deserialize_public_key(public_key):
        """
        Deserializes public key
        """
        return PublicKey.fromPem(public_key)

    @staticmethod
    def sign(key_pair, data):
        """
        Generates transaction signature
        """
        message = json.dumps(data)
        signature = Ecdsa.sign(message, key_pair)

        return signature.toBase64()

    @staticmethod
    def verify_signature(public_key, signature, data):
        """
        Verifies transaction signature
        """
        message = json.dumps(data)

        try:
            Ecdsa.verify(message, signature, public_key)
            return True
        except Exception as e:
            return False
