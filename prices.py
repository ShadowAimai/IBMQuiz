from collections import deque
import numpy as np

class prices(object):

    def __init__(self, list_size):
        self.inner_queue = deque(maxlen=list_size)
        self.list_size = list_size

    def add_price(self, new_price):

        if len(self.inner_queue) > 0:

            previous_price = self.inner_queue[-1]

            average_new_price = new_price.average()
            average_previous_price = previous_price.average()

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

        mean = np.mean([c.average() for c in self.inner_queue])

        print("List average: " + str(mean))
        