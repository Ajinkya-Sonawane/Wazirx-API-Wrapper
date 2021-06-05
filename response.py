import logging

class PriceResponse:
    def __init__(self,data) -> None:
        try:
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
        except Exception as ex:
            logging.error(ex)

class MarketStatusResponse:

    class Market:

        def __init__(self,data) -> None:
            try:
                self.type = data['type']
                self.baseMarket = data['baseMarket']
                self.quoteMarket = data['quoteMarket']
                self.status = data['status']
                if self.type.lower() == "spot":
                    self.minBuyAmount = data['minBuyAmount']
                    self.minSellAmount = data['minSellAmount']
                    self.fee = data['fee']
                    self.basePrecision = data['basePrecision']
                    self.quotePrecision = data['quotePrecision']
                    self.low = data['low']
                    self.high = data['high']
                    self.last = data['last']
                    self.open = data['open']
                    self.volume = data['volume']
                    self.sell = data['sell']
                    self.buy = data['buy']
                elif self.type.lower() == "p2p":
                    self.minBuyAmount = data['minBuyAmount']
                    self.minSellAmount = data['minSellAmount']
                    self.fee = data['fee']
                    self.maxBuyAmount = data['maxBuyAmount']
                elif self.type.lower() == "stf":
                    self.minBuyVolumne = data['minBuyVolume']
                    self.maxBuyVolumne = data['maxBuyVolume']
                    self.feePercentOnProfit = data['feePercentOnProfit']
            except Exception as ex:
                logging.error(ex)

    class Asset:

        def __init__(self,data) -> None:
            try:
                self.type = data['type']
                self.name = data['name']
                self.deposit = data['deposit']
                self.withdrawal = data['withdrawal']
                try:
                    self.minDepositAmount = data['minDepositAmount']
                except Exception as ex:
                    pass

                try:
                    self.minWithdrawAmount = data['minWithdrawAmount']
                except Exception as ex:
                    pass
                try:
                    self.maxWithdrawAmount = data['maxWithdrawAmount']
                except Exception as ex:
                    pass                
                try:
                    self.withdrawFee = data['withdrawFee']
                except Exception as ex:
                    pass
                try:
                    self.confirmations = data['confirmations']
                except Exception as ex:
                    pass                                
            except Exception as ex:
                logging.error(ex)

    def __init__(self,data) -> None:
        try:
            self.markets = [self.Market(record) for record in data['markets']]
            self.assets = [self.Asset(record) for record in data['assets']]
        except Exception as ex:
            logging.error(ex)


class MarketDepthResponse:

    class Depth:
        def __init__(self,price,volume) -> None:
            try:
                self.price = price
                self.volume = volume
            except Exception as ex:
                logging.error(ex)

    def __init__(self,data) -> None:
        try:
            self.timestamp = data['timestamp']
            self.asks = [self.Depth(price,volume) for price,volume in data['asks']]
            self.bids = [self.Depth(price,volume) for price,volume in data['bids']]
        except Exception as ex:
            logging.error(ex)