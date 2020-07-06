import time

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
