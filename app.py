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
    ret["buy_order"] = btc_market.get_buy_info()
    ret["sell_order"] = btc_market.get_sell_info()
    ret["trade_detail"] = btc_market.get_trade_detail()
    return ret

@app.route("/buy")
def buy():
    btc_market = strategy_thread.btc_market
    cur_price = btc_market.get_mark_price()
    btc_market.buy(cur_price, size=size, target_profit=target_profit, stop_loss=stop_loss)
    return "success"

@app.route("/sell")
def buy():
    btc_market = strategy_thread.btc_market
    cur_price = btc_market.get_mark_price()
    btc_market.sell(cur_price, size=size, target_profit=target_profit, stop_loss=stop_loss)
    return "success"

if __name__ == "__main__":
    strategy_thread.setDaemon(True)
    strategy_thread.start()

    app.run(host="0.0.0.0", port=8000, debug=False)



