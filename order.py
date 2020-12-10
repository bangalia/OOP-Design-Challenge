import random
from cupcake import Cupcake
from toppings import Toppings

class Order:
    def __init(self,order_number,order_contents):
        self.order_number = order_number
        self.order_contents = order_contents
        self.toppings = list()

    def take_order(self):
        total_cost = 0
        for topping in self.toppings:
            total_cost += toppings.price
        return total_cost
    
    @staticmethod
    def loyalty(rewards):
        if rewards == "yes":
           return f"Thank you for joining our rewards program"
        else:
            return f"Okay, maybe next time!"
    
    def customerbonus(self):
        lucky_number = random.randint(0,self.order_number)
        return lucky_number