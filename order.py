import random
from cupcake import Cupcake
from order import Order

class Order:
    def __init(self,order_number,order_contents):
        self.order_number = order_number
        self.order_contents = order_contents

    def take_order