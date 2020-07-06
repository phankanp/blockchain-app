import pytest

from backend.wallet.transaction import Transaction
from backend.wallet.wallet import Wallet


def test_transaction():
    """
    Test and verify transaction after creation
    """
    sender_wallet = Wallet()
    recipient = 'recipient'
    amount = 50

    transaction = Transaction().create_transaction(sender_wallet, recipient, amount)

    assert transaction.outputs['sender_amount'] == sender_wallet.balance - amount
    assert transaction.outputs['recipient_amount'] == amount
    assert transaction.input['amount'] == sender_wallet.balance
    assert Transaction.verify_transaction(transaction) is True


def test_invalid_transaction():
    """
    Test invalid transaction by providing invalid amount to recipient
    """
    sender_wallet = Wallet()
    recipient = 'recipient'
    amount = 50

    transaction = Transaction().create_transaction(sender_wallet, recipient, amount)

    transaction.outputs['recipient_amount'] = 51
    assert Transaction.verify_transaction(transaction) is False


def test_invalid_balance():
    """
    Test exception when transaction amount exceeds senders wallet balance
    """
    sender_wallet = Wallet()
    recipient = 'recipient'
    amount = 200

    with pytest.raises(Exception):
        Transaction().create_transaction(sender_wallet, recipient, amount)


def test_update_transaction_new_recipient():
    """
    Test update transaction with a new recipient
    """
    sender_wallet = Wallet()
    recipient = 'recipient'
    amount = 50

    transaction = Transaction().create_transaction(sender_wallet, recipient, amount)

    new_amount = 30
    new_recipient = 'new-address'

    transaction = transaction.update(sender_wallet, new_recipient, new_amount)

    assert transaction.outputs['recipient_address'] == new_recipient
    assert transaction.outputs['recipient_amount'] == new_amount
    assert transaction.outputs['sender_amount'] == sender_wallet.balance - amount - new_amount


def test_update_transaction_same_recipient():
    """
    Test update transaction with the same recipient
    """
    sender_wallet = Wallet()
    recipient = 'recipient'
    amount = 50

    transaction = Transaction().create_transaction(sender_wallet, recipient, amount)

    new_amount = 30
    new_recipient = 'recipient'

    transaction = transaction.update(sender_wallet, new_recipient, new_amount)

    assert transaction.outputs['recipient_address'] == new_recipient
    assert transaction.outputs['recipient_amount'] == new_amount
    assert transaction.outputs['sender_amount'] == sender_wallet.balance - amount - new_amount
