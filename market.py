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
    def __init__(self, api_key, secret_key, passphrase):
        self.swap_api = swap.SwapAPI(api_key, secret_key, passphrase, False)
        self.sell_trigger_status = False
        self.buy_trigger_status = False
        self.ma_prices = {}

    def get_ma_key(self, granularity, interval):
        return str(granularity) + "-" + str(interval)

    def get_ma_price(self, granularity, interval):
        key = self.get_ma_key(granularity, interval)
        value = self.ma_prices.get(key)
        if value is None:
            self.swap.get_kline(instrument_id='', start='', end='', granularity='')
            

    def get_cur_price(self):
        pass

    def has_sell_order(self):
        pass

    def has_buy_order(self):
        pass

    def trigger_buy(self):
        self.buy_trigger_status = True

    def trigger_sell(self):
        self.sell_trigger_status = True

    def has_buy_trigger(self):
        return self.buy_trigger_status

    def has_sell_trigger(self):
        return self.sell_trigger_status

    def buy(self):
        if self.has_buy_order():
            return

    def sell(self):
        if self.has_sell_order():
            return

