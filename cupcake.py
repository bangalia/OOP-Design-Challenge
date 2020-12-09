from toppings import Toppings

class Cupcake:
    def __init__(self,flavor,icing):

        self.flavor = flavor
        self.icing = icing
        self.toppings = list()

    def build_cupcake(self,toppings):
        self.toppings.append()