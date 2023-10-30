import requests
response = requests.get("https://api.bitflyer.jp/v1/ticker/")
print(response.json())


## 買い注文 ↓
import hashlib
import hmac
import requests
import datetime
import json

# import secret key
with open('secret/api_key.json') as f:
    key_dict = json.load(f)


# your key

import ccxt
from pprint import pprint

bitflyer = ccxt.bitflyer()
bitflyer.apiKey = key_dict['API_KEY']
bitflyer.secret = key_dict['API_SECRET']

collateral = bitflyer.private_get_getcollateral()
pprint( collateral )


# 買い注文の場合

bitflyer = ccxt.bitflyer()

order = bitflyer.create_order(
	symbol = 'BTC/JPY',
	type='limit',
	side='buy',
	price= 'your price',
	amount='0.01',
	params = { "product_code" : "FX_BTC_JPY" })

pprint( order )