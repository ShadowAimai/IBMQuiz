class Price:
    data: int
    bid: float
    ask: float

    def __init__(self, data, bid, ask):
        self.data = data
        self.bid = bid
        self.ask = ask

    def average(self):
        return (self.bid + self.ask) / 2