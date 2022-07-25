from email.contentmanager import raw_data_manager
import yfinance as yf

raw_data = None

def load_data(stock_list):
    global raw_data
    raw_data = yf.Tickers(stock_list)

def get_raw_data():
    global raw_data
    return raw_data