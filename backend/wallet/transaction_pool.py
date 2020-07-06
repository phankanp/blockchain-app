from backend.wallet.transaction import Transaction
from backend.config import MINING_REWARD, MINING_REWARD_INPUT


class TransactionPool:
    """
    Class represents a collection of transactions
    """
    def __init__(self):
        self.transactions = {}

    def add_transaction(self, transaction):
        """
        Adds transaction to pool or updated existing transaction
        """
        self.transactions[transaction.id] = transaction

    def existing_transaction(self, address):

        for transaction in self.transactions.values():
            if transaction.input['address'] == address:
                return transaction


    def clear_transaction(self):
        """
        Clears transaction pool
        """
        self.transactions = {}
