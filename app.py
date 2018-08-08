# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template, request
from flask import make_response,Response
app = Flask(__name__)
import rpc,json
import os


@app.route('/',methods=['GET'])
def home():
    return render_template("index.html")

#print(rpc.getbalance("2SATGZDFDXNNJRVZ52O4J6VYTTMO2EZR"))
#print(rpc.getbalance("G35X2DSESYNWASV5YLY3UZNCBCMGAJ7R"))
@app.route('/api/address',methods=['GET'])
def get_address_all():
    return jsonify(rpc.get_all_address())

@app.route('/api/address/new',methods=['GET'])
def make_a_address(address):
    return jsonify(rpc.make_a_new_address())

@app.route('/api/address/<string:address>',methods=['GET'])
def check_address_of(address):
    return jsonify(rpc.check_address(address))

@app.route('/api/balance',methods=['GET'])
def get_balance():
    return jsonify(rpc.get_balance_all())

@app.route('/api/balance/<string:address>',methods=['GET'])
def get_balance_of(address):
    return jsonify(rpc.get_balance_of(address))

@app.route('/api/pay',methods=['POST'])
def pay():
    if request.method == 'POST':
        address=request.form.get('address')
        amount=request.form.get('amount')
        text=request.form.get('text')
        return jsonify(rpc.pay(address,amount,text))

@app.route('/api/keys')
def api_key():
    keysfile = "{0}/.config/lightwallet/keys.json".format(os.environ['HOME'])
    return jsonify(json.loads(open(keysfile).read()))

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    app.run(debug=True,host='0.0.0.0',port=port)
