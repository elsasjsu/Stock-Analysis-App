from stock_class import Stock
from stock_data import get_stock_data

def fetch_stocks(symbols):
    stocks = []
    for symbol in symbols:
        data = get_stock_data(symbol)
        stocks.append(Stock(symbol, data))
    return stocks
