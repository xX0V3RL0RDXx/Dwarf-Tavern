import random as rng

# creation of Tavern
from tavern import *
TavernList = [Tavern("The Strike Earth", 50)]

# List of dwarf names; used to generate the dwarfs
DwarfNameList = []
DwarfList = []


class Dwarf:
    """
    This class describes a Dwarf. A dwarf has a name, a random starting amount of money (0–40),
    a number of beers they own, and a level of drunkenness.
    """

    def __init__(self, name):
        self.name = name
        self.money = rng.randint(0, 40)
        self.beers = 0
        self.drunkenness = 0
        self.introduce()
        DwarfList.append(self)

    def drinks(self, amount=1):
        """
        Dwarf drinks a given amount of beers if they have enough.
        Increases drunkenness by the number of beers consumed.
        After drinking, the number of beers is reduced accordingly.
        """
        if amount > self.beers:
            print(f"{self.name}: I don't have {amount} beers. I have only {self.beers} beers.")
            return

        self.drunkenness += amount
        self.beers -= amount
        print(f"{self.name} is now at level {self.drunkenness} of drunkenness.")

    def introduce(self):
        """
        Introduces the dwarf and shows how much money they have.
        """
        print(f"Greetings, I'm {self.name} and I have {self.money} coins in my pocket.")

    def buying_drinks(self):
        """
        Allows the dwarf to buy one beer if they have enough money.
        One drink costs 2 coins.
        """
        if self.money >= 2:
            print(f"\n{self.name} says: 'Tavern Keeper! Give me a drink!'")
            if TavernList[0].tavernSupplyOfBeer <= 0:
                print('\n!------------------------------------------------------------------------------------------------------------------!'
                      '\nThe Tavern Keeper went to fetch another barrel of beer from the storage, but when he tried to pour it, he heard only '
                      '\nthe hollow sound of an empty keg... The beer supplies were gone, and the dwarves still wanted more.'
                      '\nThe Tavern Keeper slipped out the back door, knowing there was no saving the tavern now. '
                      '\nHe would not survive the wrath of thirsty dwarves.'
                     f'\nThis is the end of {TavernList[0].tavernName}'
                      '\n!------------------------------------------------------------------------------------------------------------------!')
                exit()
            self.beers += 1
            self.money -= 2
            TavernList[0].tavernSupplyOfBeer -= 1
            print(f"I have {self.beers} beer(s) now! \nBeers in stockpile: {TavernList[0].tavernSupplyOfBeer}")
        else:
            print(f"{self.name} says: 'Ulrich, take care of me! I'm broke — only {self.money} coins left.'")



# Load dwarf names from file
try:
    with open("dwarves.txt", "r") as file:
        for each_line in file:
            DwarfNameList.append(each_line.strip())
    if len(DwarfNameList) == 1:
        print("Only one dwarf? What is this, an elf poetry night?! Get more drinkers in here!")
        exit()
    elif len(DwarfNameList) ==0:
        print("The chairs are stacked, the mugs are dry... Not a single dwarf showed up. Even the rats are disappointed.")
        exit()
except FileNotFoundError:
    print("Looks like a dragon burned down the tavern... What a shame.")
    exit()
# Create Dwarf instances
for each_dwarf in DwarfNameList:
    Dwarf(each_dwarf)
