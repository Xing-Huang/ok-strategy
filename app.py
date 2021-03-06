import time
from flask import Flask

from const import *
from strategy_thread import StrategyThread

app = Flask(__name__)

strategy_thread = StrategyThread(pair=pair, api_key=api_key, secret_key=secret_key, passphrase=passphrase)

@app.route("/")
def index():
    ret = {}
    btc_market = strategy_thread.btc_market
    ret["ma_price"] = btc_market.get_ma_price(granularity, interval)
    ret["cur_price"] = btc_market.get_mark_price()
    ret["buy_trigger"] = btc_market.buy_trigger_status
    ret["sell_trigger"] = btc_market.sell_trigger_status
    ret["buy_order"] = btc_market.has_buy_order()
    ret["sell_order"] = btc_market.has_sell_order()
    ret["leverage"] = btc_market.leverage
    ret["trade_detail"] = btc_market.get_trade_detail()
    return ret

@app.route("/buy")
def buy():
    btc_market = strategy_thread.btc_market
    cur_price = btc_market.get_mark_price()
    btc_market.buy_trigger_status = True
    btc_market.buy(size=size)
    time.sleep(0.5)
    btc_market.set_buy_stop_loss(cur_price, size, target_profit, stop_loss)
    btc_market.buy_trigger_status = False

    return "success"

@app.route("/sell")
def sell():
    btc_market = strategy_thread.btc_market
    cur_price = btc_market.get_mark_price()
    btc_market.sell_trigger_status = True

    btc_market.sell(size=size)
    time.sleep(0.5)
    btc_market.set_sell_stop_loss(cur_price, size, target_profit, stop_loss)
    btc_market.sell_trigger_status = False

    return "success"

if __name__ == "__main__":
    strategy_thread.setDaemon(True)
    strategy_thread.start()

    app.run(host="0.0.0.0", port=8000, debug=False)



