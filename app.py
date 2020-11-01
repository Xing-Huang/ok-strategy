import okex.account_api as account
import okex.futures_api as future
import okex.lever_api as lever
import okex.spot_api as spot
import okex.swap_api as swap
import okex.index_api as index
import okex.option_api as option
import okex.system_api as system
import okex.information_api as information
import json
import datetime

from const import *
from market import CurrencyMarket

def get_timestamp():
    now = datetime.datetime.now()
    t = now.isoformat("T", "milliseconds")
    return t + "Z"

time = get_timestamp()

if __name__ == '__main__':
    btc_market = CurrencyMarket("BTC_USDT_SWAP", api_key, secret_key, passphrase)

    while True:
        cur_price = btc_market.get_cur_price()
        ma_price = btc_market.get_ma_price(granularity, interval)
        if cur_price >= ma_price * buy_trigger_ratio:
            btc_market.trigger_buy()
        elif cur_price < ma_price and btc_market.has_buy_trigger():
            btc_market.buy()
        elif cur_price > ma_price and btc_market.has_sell_trigger():
            btc_market.sell()
        elif cur_price < ma_price * sell_trigger_ratio:
            btc_market.trigger_sell()

