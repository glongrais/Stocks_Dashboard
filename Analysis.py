import yfinance as yf

def get_total_value(data, quantity):
    total = 0
    for s in data:
        total += data[s].history(period='5d').iloc[-1]['Close']*quantity[s]

    return int(total)

def get_portfolio_performance(data, quantity, pru):
    total = get_total_value(data, quantity)
    bought = 0.0
    for s in quantity:
        bought += quantity[s] * pru[s]
    
    return int((float(total*100)/bought)-100)