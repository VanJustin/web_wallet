#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json

url = "http://localhost:6332"
headers = {'content-type': 'application/json'}

def get_result(payload):
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()
    return json.dumps(response)

def get_all_address():
    payload = {
        "method": "getalladdress",
        "params": {},
        "jsonrpc": "2.0",
        "id": 1,
    }
    content = json.loads(get_result(payload))
    content=content["result"]
    address_arr=[]
    for (v) in content:
        address=v.split("-")[2]
        address_arr.append(address)
    return address_arr

def make_a_new_address():
    payload = {
        "method": "getnewaddress",
        "params": {},
        "jsonrpc": "2.0",
        "id": 1,
    }
    content = json.loads(get_result(payload))
    content=content["result"]
    return content

def get_balance_all():
    method="getbalance"
    payload = {
        "method": method,
        "params": {},
        "jsonrpc": "2.0",
        "id": 1,
    }
    content = json.loads(get_result(payload))
    pending=(content["result"]["base"]["pending"])/1000000
    stable=(content["result"]["base"]["stable"])/1000000
    balance=pending+stable
    return {"balance":balance,"pending":pending,"stable":stable}

def get_balance_of(address):
    method="getaddressbalance"
    payload = {
        "method": method,
        "params": {},
        "jsonrpc": "2.0",
        "id": 1,
    }
    content = json.loads(get_result(payload))
    pending=(content["result"]["base"]["pending"])/1000000
    stable=(content["result"]["base"]["stable"])/1000000
    balance=pending+stable
    return {"balance":balance,"pending":pending,"stable":stable}


def check_address(address):
    payload = {
        "method": "checkAddress",
        "params": [address],
        "jsonrpc": "2.0",
        "id": 1,
    }
    content = json.loads(get_result(payload))
    if "error" in content:
        return False
    else:
        return True


def pay(address,amount,msg):
    # MN to notes
    amount=int(amount)*1000000
    payload = {
        "method": "sendtoaddresswithmessage",
        "params": [address,amount,msg],
        "jsonrpc": "2.0",
        "id": 1,
    }
    content = json.loads(get_result(payload))
    if "error" in content:
        return False
    else:
        content=content["result"]
        return content
