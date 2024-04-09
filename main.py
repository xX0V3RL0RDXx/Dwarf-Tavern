import random as rng

# List of dwarfs names; will be used to generate the dwarfs/dwarves
DwarfNameList = []
DwarfList = []

file = open("dwarfes.txt", "r")

for each_line in file:
    DwarfNameList.append(each_line.rstrip())

EventList = []

file = open("events.txt", "r")

for each_line in file:
    EventList.append(each_line.rstrip())
EventWeightedList = []

file = open("eventsweighted.txt", "r")

for each_line in file:
    EventWeightedList.append(each_line.rstrip())

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
    for dwarf in DwarfList:
        dwarf.drinks()


# def beer_round(drinkers):
def puke():
    sick_dwarf = rng.choice(DwarfList)
    print(sick_dwarf.name, "is feeling sick")
    val = sick_dwarf.drunkenness
    print("his level of drunkness is:", val)
    if val >= 0:
        if rng.randint(100 * val / (val + 1), 100) == 100:
            print(sick_dwarf, "has puked xD")
def another_one():
    x = rng.choice(DwarfList)
    x.buying_drinks()
    x.drinks()

def oh_a_penny():
    x = rng.choice(DwarfList)
    print(x.name, "found a coin!")
    x.money += 1
""" A heart of simulations. Here all event's will happen. """


def eventManager(turn):
    while True:
        turn += 1
        weight = 0
        print("turn:", turn)
        while weight < 3:
            x = rng.randint(0, len(EventList) - 1)
            print("event:", str(EventList[x]))
            event = EventList[x]
            event
            weight += int(EventWeightedList[x])

        if turn % 6 == 0:
            for dwarf in DwarfList:
                dwarf.buying_drinks()
            party_time()

        user_continues = input("continue?Y/N")
        if user_continues != "Y":
            exit()

# Loop for creation dwarfs
for each_dwarf in DwarfNameList:
    print(each_dwarf)
    Dwarf(each_dwarf)
# TO DO
# for balls in DwarfList:
#     x = balls
#     Dwarf(DwarfList[x])
#     buying_drinks()

#creation of EventDict
#event manager will use it
EventDict = {}
EventDict["name"] = EventList
EventDict["eventweights"] = EventWeightedList
'''
a = Dwarf(DwarfList[0])
b = Dwarf(DwarfList[1])
c = Dwarf(DwarfList[2])
'''
eventManager(0)

# if there is a error with file
# except:
# print('It\'s looks like dragon burn down the Tavern, sorry')






