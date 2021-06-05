import urllib3
import json
import datetime
import logging
from config import *

HTTP = urllib3.PoolManager()

class PriceResponse:
    def __init__(self,data):
        self.base_unit = data['base_unit']
        self.quote_unit = data['quote_unit']
        self.low = data['low']
        self.high = data['high']
        self.last = data['last']
        self.open = data['open']
        self.volume = data['volume']
        self.sell = data['sell']
        self.buy = data['buy']
        self.name = data['name']
        self.at = data['at']

 
def fetch_tickers_list():
    '''
        Function to fetch the available crypto tickers
    '''
    try:
        response = HTTP.request('GET',URL_TICKERS,headers=HEADERS)
        data = json.loads(response.data)
        return list(data.keys())
    except Exception as ex:
        logging.debug(ex)
    return []

def fetch_price_by_ticker(ticker):
    '''
        Function to fetch crypto price by ticker
        ticker : Ticker as provided by WazirX
    '''
    try:
        response = HTTP.request('GET',URL_TICKERS,headers=HEADERS)
        data = json.loads(response.data)[ticker.lower()]
        return PriceResponse(data)        
    except Exception as ex:
        logging.debug(ex)
    return None

