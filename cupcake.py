from toppings import Toppings

class Cupcake:
    def __init__(self,flavor,icing, topping):

        self.flavor = flavor
        self.icing = icing
        self.topping = topping
    

    def order_chocolate(self):
        return f"You order a {self.flavor} cupcake with {self.icing} with {self.topping}"

    def order_vanilla(self):
        return f"You ordered a {self.flavor} cupcake {self.icing}"
    
    @classmethod
    def alternate(cls,newdessert):
        return f"I don't like cupcakes, may I have a {newdessert}?"


    #if __name == "main":
        # Running this file from terminal will run this code
        # cupcake = Cupcake("Vanilla", "Chocolate")
        #return f"You chose a {cupcake.favor} cupcake with {cupcake.icing}"