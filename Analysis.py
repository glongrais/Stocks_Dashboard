import yfinance as yf

def get_total_value(data):
    total = 0

    for s in data:
        total += yf.Ticker(s['symbol']).history(period='5d').iloc[-1]['Close']*int(s['quantity'])

    return int(total)