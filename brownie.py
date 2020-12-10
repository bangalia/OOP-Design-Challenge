from cupcake import Cupcake

class Brownie:
    def __init__(self, flavor, icing, addin, pieces):
        Cupcake.__init__(self, flavor, icing)
        self.flavor = flavor
        self.icing = icing
        self.addin = addin
        self.pieces = pieces
    
    def add_brownie(self):
        return Brownie(self.flavor, self.icing, self.addin, self.pieces)
        

#if __name__ == "__main__":
    #Running this file in the terminal creates a brownie
    #brownie = Brownie("Red velvet", "Cream cheese", "Walnuts", "9")
    #print(f"You chose {brownie.flavor} with {brownie.icing} with {brownie.addin} cut into {brownie.pieces} squares")
    
    

