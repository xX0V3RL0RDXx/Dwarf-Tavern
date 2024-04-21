import random as rng


class Dwarf:
    beers = 0
    drunkenness = 0

    def __init__(self, name):
        self.name = name
        self.money = rng.randint(0, 40)
        self.introduce()
        DwarfList.append(self)

    def drinks(self, amount=1):
        if amount > self.beers:
            print(f'{self.name}: I don\'t have {amount} beers. I have {self.beers} beers.')
            return

        self.drunkenness += amount
        self.beers = 0
        print(f'{self.name} is {self.drunkenness} level of drunkenness')

    def introduce(self):
        print("hello i am", self.name, "and I have:", self.money)

    def buying_drinks(self):

        if self.money >= 2:
            self.beers += 1
            self.money -= 2
            print(f'{self.name} said: Give me a drink, bartender!')
            print(f'I have {self.beers} beers!')
        else:
            print(f'{self.name} said: Ulrich, take care of me! I\'m very poor. I have {self.money} in my pocket.')
        print('\n')

# List of dwarfs names; will be used to generate the dwarfs/dwarves
DwarfNameList = []
DwarfList = []

try:
    file = open("dwarfes.txt", "r")
    for each_line in file:
        DwarfNameList.append(each_line.rstrip())
except:
    print('It\'s looks like dragon burn down the Tavern, sorry ;(.')

# Loop for creation dwarfs
for each_dwarf in DwarfNameList:
    print(each_dwarf)
    Dwarf(each_dwarf)