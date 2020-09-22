# views_api.py is for you API endpoints that could be hit by another service

# add your dependencies here

# import json
# import requests

from flask import jsonify, request
from http import HTTPStatus

from lnbits.extensions.zap import zap_ext
from lnbits.core.crud import get_wallet_for_key, get_wallet_payments

# add your endpoints here

# Wallet ID: a9ed5d5f2f2548c3b2ab97de0c02da1e
test_wallet_id = 'a9ed5d5f2f2548c3b2ab97de0c02da1e'

@zap_ext.route("/api/v1/channelbalance", methods=["POST"])
def channel_balance():
    api_key = request.headers['X-Api-Key']
    wall = get_wallet_for_key(api_key)
    balance = int(wall.balance_msat/1000)
    response = {
        'balance': balance,
        'pending_open_balance': 0
    }
    return jsonify(response), HTTPStatus.OK