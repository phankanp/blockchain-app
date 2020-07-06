import json

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec

from backend.config import INITIAL_BALANCE
from backend.util.wallet_util import WalletUtil
from backend.wallet.transaction import Transaction


class Wallet:
    """
    Miners wallet which holds public/private keys and balance
    """

    def __init__(self):
        self.balance = INITIAL_BALANCE
        self.key_pair = WalletUtil.generate_keypair()
        self.public_key = WalletUtil.serialize_public_key(self.key_pair.public_key())

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

    def create_transaction(self, blockchain, amount, recipient, transaction_pool):
        """
        Creates or updates a transaction
        """
        self.balance = self.calculate_balance(blockchain)

        if amount > self.balance:
            raise Exception(f'{amount} exceeds current balance: {self.balance}')

        transaction = transaction_pool.existing_transaction(self.public_key)

        if transaction:
            transaction.update(self, recipient, amount)
        else:
            transaction = Transaction.new_transaction(self, recipient, amount)
            transaction_pool.add_transaction(transaction)

        return transaction

    def calculate_balance(self, blockchain):
        """
        Updates wallet balance with the latest transaction
        """
        balance = self.balance

        transactions = []
        wallet_transactions = []

        for block in blockchain.chain:
            for transaction in block.data:
                transactions.append(transaction)

        for transaction in transactions:
            if transaction.input['address'] == self.public_key:
                wallet_transactions.append(transaction)

        start_time = 0

        if len(wallet_transactions) > 0:
            latest_transaction = wallet_transactions[0].input['timestamp']

            for wallet_transaction in wallet_transactions:
                if wallet_transaction.input['timestamp'] > latest_transaction:
                    latest_transaction = wallet_transaction.input['timestamp']

            balance = latest_transaction.outputs['sender_amount']

            start_time = latest_transaction.input['timestamp']

        for transaction in transactions:
            if transaction.input['timestamp'] > start_time:
                if transaction.outputs['recipient_address'] == self.public_key:
                    balance += transaction.outputs['recipient_amount']

        return balance
