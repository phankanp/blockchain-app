import time

from backend.config import MINING_REWARD, MINING_REWARD_INPUT
from backend.util.chain_util import ChainUtil


class Transaction:

    def __init__(self):
        self.id = ChainUtil.id(),
        self.input = None,
        self.outputs = None

    @staticmethod
    def create_transaction(sender_wallet, recipient, amount):
        """
        Create a new transaction
        """
        if amount > sender_wallet.balance:
            raise Exception('Amount exceeds balance')

        return Transaction.create_outputs(
            sender_wallet,
            {
                'recipient_amount': amount,
                'recipient_address': recipient,
                'sender_amount': sender_wallet.balance - amount,
                'sender_address': sender_wallet.public_key
            }
        )

    @staticmethod
    def create_outputs(sender_wallet, outputs):
        """
        Creates transaction object and sets outputs
        """
        transaction = Transaction()

        transaction.outputs = outputs

        Transaction.sign_transaction(transaction, sender_wallet)

        return transaction

    @staticmethod
    def sign_transaction(transaction, sender_wallet):
        """
        Creates input and signs outputs
        """
        transaction.input = {
            'timestamp': time.time_ns(),
            'amount': sender_wallet.balance,
            'address': sender_wallet.public_key,
            'signature': sender_wallet.sign(transaction.outputs)
        }

    @staticmethod
    def verify_transaction(transaction):
        """
        Deserializes public keys and verifies transaction signature
        """
        return ChainUtil.verify_signature(
            ChainUtil.deserialize_public_key(transaction.input['address']),
            transaction.input['signature'],
            transaction.outputs,
        )

    @staticmethod
    def valid_transactions(transaction):
        """
        Validates transaction based on total input/output amounts and signatures
        """
        if transaction.input['address'] == MINING_REWARD_INPUT:
            if transaction.outputs['recipient_address'] != MINING_REWARD:
                raise Exception('Invalid mining reward')

        transaction_total = transaction['recipient_amount'] + ['sender_amount']

        if transaction_total != transaction.input['amount']:
            raise Exception('Invalid transaction total')

        if not Transaction.verify_transaction(transaction):
            raise Exception('Invalid signature')

    def update(self, sender_wallet, recipient, amount):
        """
        Updates transaction with new recipient or amount
        """
        if amount > self.outputs['sender_amount']:
            raise Exception(f'Amount {amount} exceeds balance')

        if recipient in self.outputs:
            self.outputs['recipient_amount'] += amount
        else:
            self.outputs['recipient_address'] = recipient
            self.outputs['recipient_amount'] = amount

        self.outputs['sender_amount'] -= amount

        Transaction.sign_transaction(self, sender_wallet)

        return self

    @staticmethod
    def reward_transaction(miner_wallet):
        transaction = Transaction()
        transaction.input = {
            'address': MINING_REWARD_INPUT
        }
        transaction.outputs = {
            'recipient_amount': MINING_REWARD,
            'recipient_address': miner_wallet.public_key
        }

        return transaction

    def to_json(self):
        """
        Serialize the transaction.
        """
        return self.__dict__
