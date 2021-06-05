# Following URLs were taken from: https://github.com/WazirX/wazirx-api 
URL_MARKET_STATUS = 'https://api.wazirx.com/api/v2/market-status'
URL_TICKERS = 'https://api.wazirx.com/api/v2/tickers'
URL_MARKET_DEPTH = 'https://api.wazirx.com/api/v2/depth?market='

# TODO:Update as per your user_agent if the following does not work
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
HEADERS = {
    'User-Agent':USER_AGENT,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}