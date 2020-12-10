from cupcake import Cupcake

class Ice_Cream(Cupcake):
    def __init__(self, flavor, toppings, drizzle, container):
        super.__init__(flavor,toppings)
        self.drizzle = drizzle
        self.container = container

        if container is None:
            self.container = input("Would you like a cone or a cup?")
        else:
            self.container = container

        return