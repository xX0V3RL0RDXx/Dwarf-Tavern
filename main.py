import random as rng

# List of dwarfs names
DwarfList = []

file = open("dwarfes.txt", "r")

for each_line in file:
    DwarfList.append(file.readline().rstrip())


class Dwarf:
    # IN CAPITALISM WE LOVE MONEY
    money = 0
    # How drunk is dwarf
    drunkenness = 0

    # PLACE HOLDER
    def introduce(self):
        print("hello i am ", self.name, " and I have: ", self.money)

    # Constructor of dwarf object
    def __init__(self, name, money = None):

        self.name = name
        self.money = money

        # Append dwarf to list of dwarfs
        DwarfList.append(self)

        # Generating a money if amount of money is not inputted
        if money == None:
            self.money = rng.randint(0, 50)

        self.introduce()

    # Increase of drunkenness for single dwarf
    # amount - how many beers dwarf will drink
    def drinks(self, amount = 1):
        self.drunkenness += amount
        print(self.drunkenness)

# PARTY TIME !!! Dwarf are happy and they want to celebrate.
# Every one drinks


def party_time():
    print("Party Time! Everyone Drinks!")

'''
def beer_round(drinkers):
    drinkers =
'''

# A heart of simulations. Here all event's will happen.
def eventManeger(turns, turn):
    i = 0
    while True:
        turn += 1
        i += 1
        print(i)
        if i % 6 == 0:
            party_time()

        user_continues = input("continue?Y/N")
        if user_continues != "Y":
            exit()

turn = 0
turns = 0

# Loop for creation dwarfs
# TO DO
for balls in DwarfList:
    x = balls
    Dwarf(DwarfList[x])

eventManeger(1, turn)

# if there is a error with file
# except:
# print('It\'s looks like dragon burn down the Tavern, sorry')






