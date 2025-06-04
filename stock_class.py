class Stock:
    def __init__(self, symbol, data):
        self.symbol = symbol
        self.data = data

    def get_recent_data(self, count=10):
        return self.data[:count]
