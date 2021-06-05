# Simple WazirX API Wrapper in Python

WazirX API repo can be found [here](https://github.com/WazirX/wazirx-api)

1. #### Market Tickers by WazirX
   
   **`fetch_tickers_list()`** - No params required

1. #### Fetch Price by Ticker
   
   **`fetch_price_by_ticker(ticker)`** - ticker : ticker for the crypto as provided by WazirX E.g. ethinr

1. #### Market Depth by Ticker
   
   **`fetch_market_depth(market)`** - market : ticker for the crypto market as provided by WazirX E.g. ethinr

1. #### MARKET STATUS
   
   **`fetch_market_status()`** - No params required

### Installation


```
pip install requirements.txt
```

### Implementation

```
import wazirx

wazirx.fetch_market_status()
wazirx.fetch_tickers_list()
wazirx.fetch_market_depth('ethinr')
wazirx.fetch_price_by_ticker('ethinr')
```
