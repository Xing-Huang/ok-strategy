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
import numpy
import datetime


# 单个合约持仓信息
# result = swapAPI.get_specific_position('')
# 所有币种合约账户信息
# result = swapAPI.get_accounts()
# 单个币种合约账户信息
# result = swapAPI.get_coin_account('')
# 获取某个合约的用户配置
# result = swapAPI.get_settings('')
# 设定某个合约的杠杆
# result = swapAPI.set_leverage(instrument_id='', leverage='', side='')
# 账单流水查询
# result = swapAPI.get_ledger(instrument_id='', after='', before='', limit='', type='')
# 下单
# result = swapAPI.take_order(instrument_id='', type='', price='', size='', client_oid='', order_type='0', match_price='0')
# 批量下单
# result = swapAPI.take_orders('', [
#     {'client_oid': '', 'type': '', 'price': '', 'size': ''},
#     {'client_oid': '', 'type': '', 'price': '', 'size': ''}
# ])
# 撤单
# result = swapAPI.revoke_order(instrument_id='', order_id='', client_oid='')
# 批量撤单
# result = swapAPI.revoke_orders(instrument_id='', ids=['', ''], client_oids=['', ''])
# 修改订单
# result = swapAPI.amend_order(instrument_id='', cancel_on_fail='', order_id='', client_oid='', request_id='', new_size='', new_price='')
# 批量修改订单
# result = swapAPI.amend_batch_orders(instrument_id='', amend_data=[
#     {'cancel_on_fail': '', 'order_id': '', 'client_oid': '', 'request_id': '', 'new_size': '', 'new_price': ''},
#     {'cancel_on_fail': '', 'order_id': '', 'client_oid': '', 'request_id': '', 'new_size': '', 'new_price': ''}
# ])
# 获取所有订单列表
# result = swapAPI.get_order_list(instrument_id='', state='', after='', before='', limit='')
# 获取订单信息
# result = swapAPI.get_order_info(instrument_id='', order_id='', client_oid='')
# 获取成交明细
# result = swapAPI.get_fills(instrument_id='', order_id='', after='', before='', limit='')
# 获取合约挂单冻结数量
# result = swapAPI.get_holds_amount('')
# 委托策略下单
# result = swapAPI.take_order_algo(instrument_id='', type='', order_type='', size='', trigger_price='', algo_price='', algo_type='')
# 委托策略撤单
# result = swapAPI.cancel_algos(instrument_id='', algo_ids=[''], order_type='')
# 获取委托单列表
# result = swapAPI.get_order_algos(instrument_id='', order_type='', status='', algo_id='', before='', after='', limit='')
# 获取账户手续费费率
# result = swapAPI.get_trade_fee()
# 市价全平
# result = swapAPI.close_position(instrument_id='', direction='')
# 撤销所有平仓挂单
# result = swapAPI.cancel_all(instrument_id='', direction='')
# 公共-获取合约信息
# result = swapAPI.get_instruments()
# 公共-获取深度数据
# result = swapAPI.get_depth(instrument_id='', size='', depth='')
# 公共-获取全部ticker信息
# result = swapAPI.get_ticker()
# 公共-获取某个ticker信息
# result = swapAPI.get_specific_ticker('')
# 公共-获取成交数据
# result = swapAPI.get_trades(instrument_id='', after='', before='', limit='')
# 公共-获取K线数据
# result = swapAPI.get_kline(instrument_id='', start='', end='', granularity='')
# 公共-获取指数信息
# result = swapAPI.get_index('')
# 公共-获取法币汇率
# result = swapAPI.get_rate()
# 公共-获取平台总持仓量
# result = swapAPI.get_holds('')
# 公共-获取当前限价
# result = swapAPI.get_limit('')
# 公共-获取强平单
# result = swapAPI.get_liquidation(instrument_id='', status='', froms='', to='', limit='')
# 公共-获取合约资金费率
# result = swapAPI.get_funding_time('')
# 公共-获取合约标记价格
# result = swapAPI.get_mark_price('')
# 公共-获取合约历史资金费率
# result = swapAPI.get_historical_funding_rate(instrument_id='', limit='')
# 公共-获取历史K线数据
# result = swapAPI.get_history_kline(instrument_id='', start='', end='', granularity='')

class CurrencyMarket():
    def __init__(self, pair, api_key, secret_key, passphrase):
        self.pair = pair
        self.swap_api = swap.SwapAPI(api_key, secret_key, passphrase, False)
        self.sell_trigger_status = False
        self.buy_trigger_status = False

        self.buy_client_oid = None
        self.sell_client_oid = None
        self.buy_stop_loss_id = None
        self.sell_stop_loss_id = None

        self.id = 0
        self.leverage = None

    def set_leverage(self, leverage):
        self.swap_api.set_leverage(self.pair,leverage = str(leverage), side="3")
        self.leverage = leverage

    def get_ma_price(self, granularity, interval):
        kline_data = self.get_kline_data(granularity, interval)
        close_data = [float(data[4]) for data in kline_data]
        return float(numpy.mean(close_data))

    def get_mark_price(self):
        price = self.swap_api.get_mark_price(self.pair)
        return float(price["mark_price"])

    def has_sell_order(self):
        if self.sell_stop_loss_id is None:
            return False
        info = self.swap_api.get_order_algos(self.pair, order_type="5", algo_id=self.sell_stop_loss_id)
        if info[0].get("status") in ("2"):
            self.sell_stop_loss_id = None
            return False
        return True

    def has_buy_order(self):
        if self.buy_stop_loss_id is None:
            return False
        info = self.swap_api.get_order_algos(self.pair, order_type="5", algo_id=self.buy_stop_loss_id)
        if info[0].get("status") in ("2"):
            self.buy_stop_loss_id = None
            return False
        return True

    def trigger_buy(self):
        self.buy_trigger_status = True

    def trigger_sell(self):
        self.sell_trigger_status = True

    def has_buy_trigger(self):
        return self.buy_trigger_status

    def has_sell_trigger(self):
        return self.sell_trigger_status

    def set_buy_stop_loss(self, price, size, target_profit, stop_loss):
        if self.buy_client_oid is None:
            return
        tp_trigger_price = price * (1+target_profit/self.leverage)
        tp_price = tp_trigger_price -1
        sl_trigger_price = price * (1-stop_loss/self.leverage)
        sl_price = tp_trigger_price +1
        response = self.swap_api.take_order_algo(instrument_id=self.pair, type="3", order_type='5', size=str(size),
                                     tp_trigger_type = "1", sl_trigger_type = "1",
                                      tp_trigger_price=str(tp_trigger_price), tp_price=str(tp_price),
                                      sl_trigger_price=str(sl_trigger_price), sl_price=str(sl_price))
        if response.get("error_code") != "0":
            print("error:", response)
            return
        self.buy_stop_loss_id = response["data"]["algo_id"]

    def set_sell_stop_loss(self, price, size, target_profit, stop_loss):
        tp_trigger_price = price * (1 - target_profit/self.leverage)
        tp_price = tp_trigger_price +1
        sl_trigger_price = price * (1 + stop_loss/self.leverage)
        sl_price = tp_trigger_price -1
        response = self.swap_api.take_order_algo(instrument_id=self.pair, type="4", order_type='5', size=str(size),
                                                 tp_trigger_type="1", sl_trigger_type="1",
                                                 tp_trigger_price=str(tp_trigger_price), tp_price=str(tp_price),
                                      sl_trigger_price=str(sl_trigger_price), sl_price=str(sl_price))
        if response.get("error_code") != "0":
            print("error:", response)
            return
        self.sell_stop_loss_id = response["data"]["algo_id"]

    def buy(self, size):
        client_oid = self.get_next_client_oid()
        response = self.swap_api.take_order(instrument_id=self.pair, type='1',  size=str(size), client_oid=client_oid, order_type='4', match_price='0')
        if response.get("error_code") != "0":
            print("error:", response)
            return
        self.buy_client_oid = response.get("client_oid")

    def sell(self, size):
        client_oid = self.get_next_client_oid()
        response = self.swap_api.take_order(instrument_id=self.pair, type='2',  size=str(size), client_oid=client_oid, order_type='4', match_price='0')
        if response.get("error_code") != "0":
            print("error:", response)
            return
        self.sell_client_oid = response.get("client_oid")


    def get_trade_detail(self):
        return self.swap_api.get_fills(self.pair)

    def get_next_client_oid(self):
        import random
        self.id = random.randint(1, 1000000)
        return "huang" + str(self.id)

    def get_ma_key(self, granularity, interval):
        return str(granularity) + "-" + str(interval)

    def format_time(self, t):
        t = t.isoformat("T", "milliseconds")
        return t + "Z"

    def get_kline_data(self, granularity, interval):
        cur_time = datetime.datetime.now().timestamp()
        end_time = datetime.datetime.fromtimestamp(cur_time)
        start_time = datetime.datetime.fromtimestamp(cur_time - interval)
        prices = self.swap_api.get_kline(instrument_id=self.pair, start=self.format_time(start_time), end=self.format_time(end_time), granularity=str(granularity))
        return prices


