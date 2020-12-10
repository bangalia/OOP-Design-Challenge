from toppings import Toppings

class Cupcake:
    def __init__(self,flavor,icing, topping):

        self.flavor = flavor
        self.icing = icing
        self.topping = topping
    
    def print_cupcake(self):
        print(f" You chose a {self.flavor} cupcake with {self.icing} and {self.topping}")


    def __str__(self):
        return f"""
        \n
        Flavor: {self.flavor}\n
        Icing: {self.icing}\n
        Topping: {self.topping}\n
        """

    if __name == "main":
         #Running this file from terminal will run this code
         cupcake = Cupcake("Vanilla", "Chocolate")
        return f"You chose a {cupcake.favor} cupcake with {cupcake.icing}"