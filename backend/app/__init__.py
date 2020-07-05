from hashlib import new
import os
import random
import requests

from flask import Flask, jsonify, request, make_response
from pusher import Pusher

from backend.blockchain.Blockchain import Blockchain
from backend.blockchain.Block import Block

app = Flask(__name__)
blockchain = Blockchain()

pusher = Pusher(
    app_id="1030757",
    key="946520f9393b1be332a1",
    secret="92cd1926b0c512469bd2",
    cluster="us3",
    ssl=True
)


@app.route('/')
def route_default():
    return 'Welcome to the blockchain!'


@app.route('/blockchain')
def route_blockchain():
    return jsonify(blockchain.to_json())


@app.route('/blockchain/mine')
def route_blockchain_mine():
    data = 'Test transaction data'

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

    message = ''

    try:
        blockchain.replace_chain(new_blockchain)
        message = 'Replaced blockchain'
    except Exception as e:
        message = f'Did not replace chain: {e}'

    response_data = {'message': message, 'code': 'SUCCESS'}

    return make_response(jsonify(response_data), 201)


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


app.run(port=PORT)
