from cupcake import Cupcake
from brownie import Brownie
from icecream import Ice_Cream

class Bakery:
    def __init__(self,greeting):
        self.greeting = greeting
        #self.goodbye = goodbye

    def welcome(self,greeting):
        greeting = "Hello and welcome to the Bakery!"
        print(greeting)

    def add_cupcake(self):
        choice = int(input("Would you like to add a cupcake, brownie, or ice cream? Type 1 for cupcake, Type 2 for brownie, Type 3 for ice cream:"))

        while (choice != 1) or (choice != 2) or (choice != 3):
            choice = int(
              input("Those aren't ready yet. \n Would you like to add a cupcake, brownie, or ice cream? Type 1 for cupcake, Type 2 for brownie, Type 3 for ice cream:")  
            )
        
        flavor = input("What flavor would you like? \n")
        icing = input("What icing would you like? \n")
        toppings = input("What topping would you like? \n")

        if choice == 2:
            addin = input("What would you like to add in? \n")
            pieces = input("How many squares would you like this cut into? \n")
            return Brownie(flavor, icing, addin, pieces)

        elif choice == 3:
            drizzle = input("What kind of drizzle would you like? \n")
            container = input("Would you like a container or a cone? \n")
            return Ice_Cream(flavor, toppings, drizzle, container)
        else:
            return Cupcake(flavor, icing)
        