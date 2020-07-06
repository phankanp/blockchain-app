from backend.wallet.transaction import Transaction


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

    def valid_transactions(self):
        """
        Validates and returns transactions based on total input/output amounts and signatures
        """
        transactions = []

        for transaction in self.transactions:
            transaction_total = transaction['recipient_amount'] + ['sender_amount']

            if transaction_total != transaction.input['amount']:
                continue

            if not Transaction.verify_transaction(transaction):
                continue

            transactions.append(transaction.to_json())

    def clear_transaction(self):
        """
        Clears transaction pool
        """
        self.transactions = {}
