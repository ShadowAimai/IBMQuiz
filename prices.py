from collections import deque
import numpy as np

class prices(object):

    def __init__(self, list_size):
        self.inner_queue = deque(maxlen=list_size)
        self.list_size = list_size

    def add_price(self, new_price):

        if len(self.inner_queue) > 0:

            previous_price = self.inner_queue[-1]

            average_new_price = (new_price.bid + new_price.ask) / 2
            average_previous_price = (previous_price.bid + previous_price.ask) / 2

            if average_new_price > average_previous_price:
                print("Buy")

            if average_new_price < average_previous_price:
                print("Sell")

            if average_new_price == average_previous_price:
                print("Without change")


        self.inner_queue.append(new_price)

        if len(self.inner_queue) == self.list_size:
            self.calculate_average()

    def calculate_average(self):

        mean_bid = np.mean([c.bid for c in self.inner_queue])
        mean_ask = np.mean([c.ask for c in self.inner_queue])

        list_average = (mean_bid + mean_ask) / 2

        print("List average: " + str(list_average))
        