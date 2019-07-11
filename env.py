import pybitflyer
import os
from os.path import join, dirname
from dotenv import load_dotenv

# .env ファイルを参照
load_dotenv(join(dirname(__file__), '.env'))

# ここで実際の値を得ています
key = os.environ.get('API_KEY')
secret = os.environ.get('API_SECRET')

API  = pybitflyer.API(api_key=key, api_secret=secret)
SIZE = 0.01

def sashine_buy(api, size, price, product_code = "FX_BTC_JPY", child_order_type = "LIMIT", minute_to_expire = 100, time_in_force = "GTC"):
    buy = api.sendchildorder(product_code=product_code, child_order_type=child_order_type,
                                     side="BUY",size=size, minute_to_expire=minute_to_expire, time_in_force=time_in_force, price = price)


def sashine_sell(api, size, price, product_code = "FX_BTC_JPY", child_order_type = "LIMIT", minute_to_expire = 100, time_in_force = "GTC"):
    buy = api.sendchildorder(product_code=product_code, child_order_type=child_order_type,
                                     side="SELL",size=size, minute_to_expire=minute_to_expire, time_in_force=time_in_force,price = price)

def roop (price_low,price_high,interval):
    for p in range(price_low,price_high,interval):
        sashine_buy(api = API, size = SIZE , price = p)
         
roop(int(input('low')),int(input('high')),int(input('interval')))

