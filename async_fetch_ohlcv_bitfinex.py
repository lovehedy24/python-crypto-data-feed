from async_fetch_ohlcv import start_fetch_ohlcv

currency_type = ['ETH/USDT','BTC/USDT','LTC/USDT','NEO/USDT','XRP/USDT','EOS/USDT']
currency = currency_type*5
exchange_name = ['bitfinex']*len(currency)
timeframe = ['5m']*len(currency_type) + ['15m']*len(currency_type) + ['30m']*len(currency_type) + ['1h']*len(currency_type) + ['1d']*len(currency_type)
start = ['2013-01-01 00:00:00']*len(currency)
start_fetch_ohlcv(exchange_name,currency,timeframe,start)