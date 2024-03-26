import random as rng

# List of dwarfs names
DwarfList = []

file = open("dwarfes.txt", "r")

for each_line in file:
    DwarfList.append(each_line.rstrip())


class Dwarf:
    beers = 0
    drunkenness = 0

    def __init__(self, name):
        self.name = name
        self.money = rng.randint(0, 40)
        self.introduce()

    def drinks(self, amount=1):
        if amount > self.beers:
            print(f'I don\'t have {amount} beers. I have {self.beers} beers.')
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

def party_time():
    print("Party Time! Everyone Drinks!\n")
    a.drinks()
    b.drinks()
    c.drinks()


# def beer_round(drinkers):

""" A heart of simulations. Here all event's will happen. """


def eventManeger(turn):
    while True:
        turn += 1
        print(turn)
        if turn % 6 == 0:
            a.buying_drinks()
            b.buying_drinks()
            c.buying_drinks()
            party_time()

        user_continues = input("continue?Y/N")
        if user_continues != "Y":
            exit()

# Loop for creation dwarfs
# TO DO
# for balls in DwarfList:
#     x = balls
#     Dwarf(DwarfList[x])
#     buying_drinks()

a = Dwarf(DwarfList[0])
b = Dwarf(DwarfList[1])
c = Dwarf(DwarfList[2])

eventManeger(0)

# if there is a error with file
# except:
# print('It\'s looks like dragon burn down the Tavern, sorry')






