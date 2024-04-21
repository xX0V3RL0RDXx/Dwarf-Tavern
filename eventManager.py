from dwarf import *

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


EventList = []
file = open("events.txt", "r")

for each_line in file:
    EventList.append(each_line.rstrip())
EventWeightedList = []

file = open("eventsweighted.txt", "r")

for each_line in file:
    EventWeightedList.append(each_line.rstrip())

""" All events and all functions will be here."""


def party_time():
    print("Party Time! Everyone Drinks!\n")
    for dwarf in DwarfList:
        dwarf.drinks()


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

