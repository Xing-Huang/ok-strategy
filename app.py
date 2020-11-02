from flask import Flask

from const import *
from strategy_thread import StrategyThread

app = Flask(__name__)

strategy_thread = StrategyThread(pair=pair, api_key=api_key, secret_key=secret_key, passphrase=passphrase)


@app.route("/")
def index():
    ret = {}
    btc_market = strategy_thread.btc_market
    ret["kline_data"] = btc_market.kline_data
    ret["ma_price"] = btc_market.get_ma_price(granularity, interval)
    ret["buy_trigger"] = btc_market.buy_trigger_status
    ret["sell_trigger"] = btc_market.sell_trigger_status
    ret["buy_order"] = btc_market.get_buy_info()
    ret["sell_order"] = btc_market.get_sell_info()
    ret["order_history"] = btc_market.get_order_algos()
    return ret

if __name__ == "__main__":
    strategy_thread.setDaemon(True)
    strategy_thread.start()

    app.run(host="0.0.0.0", port=9000, debug=False)



