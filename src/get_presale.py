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
        self.bsc_api_key = ''
        self.contract_address = ''
        self.abi = ''

    def get_contract_abi(self,address):
        self.contract_address = address
        url = "https://api-testnet.bscscan.com/api?module=contract&action=getabi&address="+address+"&apikey="+self.bsc_api_key
        net_client = NetClient()
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36"}
        res = net_client.get(url,headers)
        if res["status"] == "1":
            self.abi = res["result"]
            return self.abi
        else:
            print(res["result"])
            return None

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
    api_key = ""
    a = GetPreSale(api_key)
    address = "0x18e4b20Bcd2C0A000D5e36Ed2df14eDc7917bEfA"
    abi = a.get_contract_abi(address)
    print(abi)

main()
