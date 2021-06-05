import urllib3
import json
import logging
from config import *
from response import *


def fetch_tickers_list():
    '''
        Function to fetch the available crypto tickers
    '''
    try:
        response = HTTP.request('GET',URL_TICKERS,headers=HEADERS)
        data = json.loads(response.data)
        return list(data.keys())
    except Exception as ex:
        logging.error(ex)
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
        logging.error(ex)
    return None


def fetch_market_status():
    '''
        Function to fetch crypto market status
    '''
    try:
        response = HTTP.request('GET',URL_MARKET_STATUS,headers=HEADERS)
        data = json.loads(response.data)
        return MarketStatusResponse(data)        
    except Exception as ex:
        logging.error(ex)
    return None


def fetch_market_depth(market):
    '''
        Function to fetch crypto market depth by market ticker
    '''
    try:
        response = HTTP.request('GET',f'{URL_MARKET_DEPTH}{market}',headers=HEADERS)
        data = json.loads(response.data)        
        return MarketDepthResponse(data)        
    except Exception as ex:
        logging.error(ex)
    return None


HTTP = urllib3.PoolManager()
logging.basicConfig(filename=PATH_LOG_ERROR, encoding='utf-8', level=logging.ERROR)