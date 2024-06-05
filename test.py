import json

json_data = '{"id":"BTC-CLP","name":"btc-clp","base_currency":"BTC","quote_currency":"CLP","minimum_order_amount":["0.00002","BTC"],"disabled":false,"illiquid":false,"rpo_disabled":null,"taker_fee":0.8,"maker_fee":0.4,"max_orders_per_minute":100,"maker_discount_percentage":"0.0","taker_discount_percentage":"0.0"}'
data = json.loads(json_data)

taker_fee = data['taker_fee']
maker_fee = data['maker_fee']

print("Taker Fee: ", taker_fee)
print("Maker Fee: ", maker_fee)

bid_price = 0.00002
ask_price = 100

spread = ask_price - bid_price

print("Spread for market BTC-CLP: ", spread)
