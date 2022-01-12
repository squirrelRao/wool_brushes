# coding=UTF-8
import time
import sys
import json
import datetime
import requests
from web3 import Web3,HTTPProvider,IPCProvider
from net_client import NetClient

class GetPreSale:

    def __init__(self,bsc_key):
	self.provider = 'https://data-seed-prebsc-1-s1.binance.org:8545'
	self.bsc_api_key = bsc_key
        self.bsc_api_key = '14QZBS4UY6VJ5G1J9MT4RCP9KG8YGFBCX9'
        self.contract_address = ''
        self.abi = ''

    def get_contract_abi(self,address):
        self.contract_address = address
        url = "https://api-testnet.bscscan.com/api?module=contract&action=getabi&address="+address+"&apikey="+self.bsc_api_key
        print(url)
        net_client = NetClient()
        res = net_client.get(url)
        self.abi = res["result"]
        return self.abi

    def get(self,url,headers={},res_type="json"):
        self.session = requests.Session()
        self.session.headers.update(headers)
        print(url)
        res = self.session.get(url)
        self.session.close()
        if res_type =="json":
            return res.json()
        elif res_type == "text":
            return res.text
        else:
            return res.content

    def post(self,url,data,header={'Content-Type':'application/json'},res_type="json"):
        data = json.dumps(data) 
        self.session = requests.Session()
        print("url:"+url)
        res = self.session.post(url,data = data,headers = header,timeout=60)
        self.session.close()
        if res_type == "json":
            return res.json()
        elif res_type == "text":
            return res.text
        else:
            return res.content


def main():
    a = GetPreSale("14QZBS4UY6VJ5G1J9MT4RCP9KG8YGFBCX9")
    abi = a.get_contract_abi("0xADFb5176A09D894BeeB952e8E258272BDCdb8590")
    print(abi)

main()
