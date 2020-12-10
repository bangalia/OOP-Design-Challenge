from cupcake import Cupcake
from brownie import Brownie
from icecream import Ice_Cream

class Bakery:


    def __init__(self,greeting, customer, order):
        self.greeting = greeting
        self.order = []
    
    def welcome(self):
        greeting = "Hello and welcome to the bakery"
        return greeting
    
    def leave(self):
        goodbye = "Thank you, come again!"
        return goodbye

    def add_cupcake(self):
        choice = int(input("Would you like to add a cupcake, brownie, or ice cream? Type 1 for cupcake, Type 2 for brownie, Type 3 for ice cream:"))

        while (choice != 1) or (choice != 2) or (choice != 3):
            choice = int(input("Those aren't ready yet. \n Would you like to add a cupcake, brownie, or ice cream? Type 1 for cupcake, Type 2 for brownie, Type 3 for ice cream:"))
        
        flavor = input("What flavor would you like? \n")
        icing = input("What icing would you like? \n")
        topping = input("What topping would you like? \n")

        if choice == 2:
            addin = input("What would you like to add in? \n")
            pieces = input("How many squares would you like this cut into? \n")
            return Brownie(flavor, icing, addin, pieces)

        elif choice == 3:
            drizzle = input("What kind of drizzle would you like? \n")
            container = input("Would you like a container or a cone? \n")
            return Ice_Cream(flavor, topping, drizzle, container)
        else:
            return Cupcake(flavor, icing, topping)
    
    def append_cupcake(self, cupcake):
        self.order.append(cupcake)
    
    def add_brownie(self):
        flavor = input("What flavor brownie would you like? \n")
        icing = input("What kind of icing would you like? \n")
        addin = input("What addin what you like? \n")
        pieces = input("How many squares? \n")

        return Brownie(flavor, icing, addin, pieces)
    
    def append_brownie(self, brownie):
        user_brownie = self.add_brownie()
        self.order.append(user_brownie)
    
    def add_icecream(self):
        flavor = input("What flavor ice cream would you like? \n")
        topping = input("What topping would you like? \n")
        drizzle = input("What kind of drizzle would you like? \n")
        container = input("Would you like a cup or a cone? \n")

        return Ice_Cream(flavor, topping, drizzle, container)

    def append_icecream(self,icecream):
        user_icecream = self.add_icecream()
        self.order.append(user_icecream)


    if __name__ == "__main__":
        #bakery = Bakery()
        print(welcome)
        customer1 = Bakery("Anita")
        cupcake1 = Cupcake("Vanilla", "Caramel", "Sprinkles")
        brownie1 = Brownie("Red velvet", "Cream Cheese", "Walnuts", "9")
        icecream1 = Ice_Cream("Vanilla", "Oreos", "Chocolate", "Cone")
        bakery.append_cupcake(cupcake1)
        bakery.append_brownie(brownie1)

