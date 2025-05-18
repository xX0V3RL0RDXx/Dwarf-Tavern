class Tavern:
    """
      This class describes a Tavern.
      A tavern has a name and an amount of beer in its stockpile.
    """

    def __init__(self, name, supplyofbeer):
        self.tavernName = name
        # how many beers a dwarfs can buy before the tavern runs out of beer
        self.tavernSupplyOfBeer = supplyofbeer
        self.opening()

    def opening(self):
        """
        Method that introduces the tavern and shows how much beer it has.
        """
        print(f"The tavern {self.tavernName} is open! There is {self.tavernSupplyOfBeer} beer's in stockpiles."
              f"\nBeer flows. Don’t ask — just drink!")

