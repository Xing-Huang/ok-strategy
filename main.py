import numpy


value = {"buy_order":None,"buy_trigger":False,"kline_data":[["2020-11-03T04:00:00.000Z","13365.2","13435","13255","13427.6","563885","5638.85"],["2020-11-03T00:00:00.000Z","13511.8","13605.3","13292.4","13365.2","960722","9607.22"],["2020-11-02T20:00:00.000Z","13519","13666.2","13482.8","13522.1","406035","4060.35"],["2020-11-02T16:00:00.000Z","13467.8","13523","13422.8","13514.9","282512","2825.12"],["2020-11-02T12:00:00.000Z","13381.1","13500","13152.7","13474.4","1284707","12847.07"],["2020-11-02T08:00:00.000Z","13698.7","13698.7","13322.7","13385.4","1255206","12552.06"],["2020-11-02T04:00:00.000Z","13655.3","13723.4","13606","13698.7","313628","3136.28"],["2020-11-02T00:00:00.000Z","13754.1","13803.1","13610.1","13651.4","600428","6004.28"],["2020-11-01T20:00:00.000Z","13764","13830","13625.2","13754.1","281855","2818.55"],["2020-11-01T16:00:00.000Z","13740.8","13797.7","13708.6","13764.7","188159","1881.59"],["2020-11-01T12:00:00.000Z","13644","13798.9","13611.2","13740.7","479495","4794.95"],["2020-11-01T08:00:00.000Z","13758.4","13778.8","13600.1","13645.3","493459","4934.59"],["2020-11-01T04:00:00.000Z","13667.2","13778.3","13592.5","13757.5","489235","4892.35"],["2020-11-01T00:00:00.000Z","13754.5","13859.2","13607.5","13668.8","621775","6217.75"],["2020-10-31T20:00:00.000Z","13748.4","13849.7","13715.1","13758.2","201290","2012.9"],["2020-10-31T16:00:00.000Z","13824.8","13854","13660","13749.3","358652","3586.52"],["2020-10-31T12:00:00.000Z","13913.7","13918.9","13715","13824.8","624169","6241.69"],["2020-10-31T08:00:00.000Z","13556.1","14100","13520.5","13913.8","2488507","24885.07"],["2020-10-31T04:00:00.000Z","13472.8","13599.8","13430.1","13556","477552","4775.52"],["2020-10-31T00:00:00.000Z","13540","13723.7","13391.3","13472.9","1019002","10190.02"],["2020-10-30T20:00:00.000Z","13516.2","13649","13450.9","13539.9","425727","4257.27"],["2020-10-30T16:00:00.000Z","13522.7","13555","13436.4","13514.3","407889","4078.89"],["2020-10-30T12:00:00.000Z","13335.2","13533.9","13208.6","13522.7","958819","9588.19"],["2020-10-30T08:00:00.000Z","13209.9","13358","13138.5","13332.5","975009","9750.09"],["2020-10-30T04:00:00.000Z","13421.6","13484.2","13105","13209.9","1367241","13672.41"],["2020-10-30T00:00:00.000Z","13436","13645","13324.7","13422.7","888602","8886.02"],["2020-10-29T20:00:00.000Z","13473.2","13527.9","13373.5","13436","357951","3579.51"],["2020-10-29T16:00:00.000Z","13408.2","13619.7","13375","13473.2","932600","9326"],["2020-10-29T12:00:00.000Z","13031.1","13450.7","12962","13409.9","1714792","17147.92"],["2020-10-29T08:00:00.000Z","13125","13195.1","13031.1","13031.1","836919","8369.19"]],"ma_price":13551.266666666666,"order_history":{"orderStrategyVOS":[{"algo_id":"623376148652003328","contract_val":"0.0100","created_at":"2020-11-01T22:36:07.803Z","instrument_id":"","last_fill_px":"","leverage":"90.00","margin_for_unfilled":"0.00","modifyTime":"","multiply":"1","order_id":"623378562968883201","order_side":"3","order_type":"5","real_amount":"","real_price":"","size":"38.00","sl_price":"0.0","sl_trigger_price":"13690.0","sl_trigger_type":"2","status":"2","timestamp":"2020-11-01T22:40:55.611Z","tp_price":"0.0","tp_trigger_price":"13780.0","tp_trigger_type":"2","trigger_side":"2","type":"3","unitAmount":"0.0100"},{"algo_id":"622977161751072769","contract_val":"0.0100","created_at":"2020-11-01T09:23:24.858Z","instrument_id":"","last_fill_px":"","leverage":"100.00","margin_for_unfilled":"0.00","modifyTime":"","multiply":"1","order_id":"622994397370945536","order_side":"3","order_type":"5","real_amount":"","real_price":"","size":"40.00","sl_price":"0.0","sl_trigger_price":"13635.0","sl_trigger_type":"2","status":"2","timestamp":"2020-11-01T09:57:39.503Z","tp_price":"0.0","tp_trigger_price":"13850.0","tp_trigger_type":"2","trigger_side":"2","type":"3","unitAmount":"0.0100"},{"algo_id":"620123776580489220","contract_val":"0.0100","created_at":"2020-10-28T10:54:14.839Z","instrument_id":"","last_fill_px":"","leverage":"80.00","margin_for_unfilled":"0.00","modifyTime":"","multiply":"1","order_id":"620131286020427781","order_side":"3","order_type":"5","real_amount":"","real_price":"","size":"25.00","sl_price":"0.0","sl_trigger_price":"13700.0","sl_trigger_type":"2","status":"2","timestamp":"2020-10-28T11:09:10.032Z","tp_price":"0.0","tp_trigger_price":"13450.0","tp_trigger_type":"2","trigger_side":"1","type":"4","unitAmount":"0.0100"}]},"sell_order":None,"sell_trigger":True}

kline_data = value.get("kline_data")
data = [float(data[4]) for data in kline_data]
s = 0
for d in data:
    s += d
print(s/30)

# print(data)
# print(numpy.mean(data))
# value = [ for data in k]