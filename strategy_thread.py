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
            if cur_price >= ma_price * buy_trigger_ratio:
                if self.btc_market.trigger_buy():
                    print(get_timestamp(),"trigger_buy", "cur_price:", cur_price, "ma_price:", ma_price)
            elif cur_price < ma_price and self.btc_market.has_buy_trigger():
                self.btc_market.buy(size)
                time.sleep(1)
                self.btc_market.set_buy_stop_loss(ma_price, size, target_profit, stop_loss)
                self.btc_market.buy_trigger_status = False
            elif cur_price > ma_price and self.btc_market.has_sell_trigger():
                self.btc_market.sell(size)
                time.sleep(1)
                self.btc_market.set_sell_stop_loss(ma_price, size, target_profit, stop_loss)
                self.btc_market.sell_trigger_status = False
            elif cur_price < ma_price * sell_trigger_ratio:
                if self.btc_market.trigger_sell():
                    print(get_timestamp(),"trigger_sell", "cur_price:", cur_price, "ma_price:", ma_price)

            time.sleep(1)