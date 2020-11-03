import time
import datetime
from threading import Thread

from const import *
from market import CurrencyMarket


def get_timestamp():
    now = datetime.datetime.now()
    t = now.isoformat("T", "milliseconds")
    return t + "Z"

class StrategyThread(Thread):
    def __init__(self, pair, api_key, secret_key, passphrase):
        Thread.__init__(self)
        self.btc_market = CurrencyMarket(pair, api_key, secret_key, passphrase)

    def run(self):
        self.btc_market.set_leverage(leverage)
        while True:
            cur_price = self.btc_market.get_mark_price()
            ma_price = self.btc_market.get_ma_price(granularity, interval)
            print(cur_price, ma_price, buy_trigger_ratio, type(cur_price), type(ma_price))
            if cur_price >= ma_price * buy_trigger_ratio:
                self.btc_market.trigger_buy()
            # elif cur_price < ma_price and self.btc_market.has_buy_trigger():
            #     self.btc_market.buy(ma_price, size, target_profit, stop_loss)
            # elif cur_price > ma_price and self.btc_market.has_sell_trigger():
            #     self.btc_market.sell(ma_price, size, target_profit, stop_loss)
            elif cur_price < ma_price * sell_trigger_ratio:
                self.btc_market.trigger_sell()
            time.sleep(1)