import os
import random

import requests
from decouple import config
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from pusher import Pusher

from backend.blockchain.block import Block
from backend.blockchain.blockchain import Blockchain
from backend.wallet.transaction import Transaction
from backend.wallet.transaction_pool import TransactionPool
from backend.wallet.wallet import Wallet

app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': 'http://localhost:3000'}})

pusher = Pusher(
    app_id=config('APP_ID'),
    key=config('KEY'),
    secret=config('SECRET'),
    cluster="us3",
    ssl=True
)

blockchain = Blockchain()
wallet = Wallet()
transaction_pool = TransactionPool()


@app.route('/')
def route_default():
    return 'Py-blockchain!'


@app.route('/blockchain')
def route_blockchain():
    return jsonify(blockchain.to_json())


@app.route('/blockchain/mine')
def route_blockchain_mine():
    data = transaction_pool.get_transactions()

    data.append(Transaction.reward_transaction(wallet).to_json())

    blockchain.add_block(data)

    block = blockchain.chain[-1]

    pusher.trigger('blockchain', 'block-added', block.to_json())

    return jsonify(block.to_json())


@app.route('/blockchain/replace', methods=['POST'])
def route_blockchain_replace():
    data = request.get_json()

    block = Block.from_json(data)
    new_blockchain = blockchain.chain[:]
    new_blockchain.append(block)

    try:
        blockchain.replace_chain(new_blockchain)
        message = 'Replaced blockchain'
    except Exception as e:
        message = f'Did not replace chain: {e}'

    response_data = {'message': message, 'code': 'SUCCESS'}

    return make_response(jsonify(response_data), 201)


@app.route('/blockchain/length')
def route_blockchain_length():
    return jsonify(len(blockchain.chain))


@app.route('/transaction/new', methods=['POST'])
def route_create_transaction():
    data = request.get_json()

    transaction = wallet.create_transaction(blockchain, data['amount'], data['recipient'], transaction_pool)

    pusher.trigger('blockchain', 'transaction-created', transaction.to_json())

    return jsonify(transaction.to_json())


@app.route('/transactions')
def route_transactions():
    return jsonify(transaction_pool.get_transactions())


@app.route('/wallet/info')
def route_wallet_info():
    return jsonify({'wallet_address': wallet.address, 'balance': wallet.balance})


ROOT_PORT = 5000
PORT = ROOT_PORT

if os.environ.get('PEER') == 'True':
    PORT = random.randint(5001, 6000)

    result = requests.get(f'http://localhost:{ROOT_PORT}/blockchain')
    new_blockchain = Blockchain.from_json(result.json())

    try:
        blockchain.replace_chain(new_blockchain.chain)
        print('Synchronized the local blockchain')
    except Exception as e:
        print(f'Synchronization error: {e}')


for i in range(10):
    blockchain.add_block([
        Transaction.new_transaction(Wallet(), Wallet().address, random.randrange(10, 40, 10)).to_json(),
        Transaction.new_transaction(Wallet(), Wallet().address, random.randrange(10, 40, 10)).to_json()
    ])


app.run(port=PORT)
