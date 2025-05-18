from dwarf import *
from tavern import *

def method_resolver(event):
    """
    Method that triggers events based on the given event name.
    """
    if event == "puke()":
        puke()
    elif event == "party_time()":
        party_time()
    elif event == "another_one()":
        another_one()
    elif event == "oh_a_penny()":
        oh_a_penny()
    print("-----------------------------------------------")
def eventManager(turnToPlay):
    """
    The heart of the simulation. This function runs all events.

    It starts the simulation and keeps track of turns. Each turn has a 'weight' —
    the number of random events that can happen during that turn.

    After every 5 turns, the Event Manager will ask whether you'd like to continue.
    """
    turn = 0
    while True:
        turn += 1
        weight = 0
        print("\n\nturn:", turn)
        while weight < 3:
            x = rng.randint(0, len(EventList) - 1)
            print("event:", str(EventList[x]))
            event = EventList[x]
            method_resolver(event)
            weight += int(EventWeightedList[x])
        if turnToPlay == turn:
            print("Turn", turn)
            print("Many beers were drunk, many songs were sung... and now the simulation ends."
                  " Is anyone still upright? (I highly doubt it.)")
            exit()
        if turn%5 == 0:
            print("\nEnd of turn: ", turn)
            user_continues = input("continue? Y/N ")
            if user_continues.upper() == "N":
                exit()


EventList = []
file = open("events.txt", "r")
for each_line in file:
    EventList.append(each_line.rstrip())

EventWeightedList = []
file = open("eventsweighted.txt", "r")
for each_line in file:
    EventWeightedList.append(each_line.rstrip())

""" Definition of all events are here."""


def party_time():
    """
    Every dwarf buys beer — if they have money, of course —
    and drinks like there's no tomorrow! - if they have beer, of course...
    """
    print("Party Time! Everyone Drinks!")
    for dwarf in DwarfList:
        dwarf.buying_drinks()
        dwarf.drinks()


def puke():
    """
    Event that chooses a random dwarf from DwarfList and checks if they will puke.

    The higher the level of drunkenness, the higher the chance the dwarf will puke.

    A nasty function, if I may be honest...
    """
    sick_dwarf = rng.choice(DwarfList)
    print(sick_dwarf.name, "is feeling sick")
    val = sick_dwarf.drunkenness
    print("his level of drunkness is:", val)
    if val > 0:
        if rng.randint(100 * val // (val + 1), 100) >= 95:
            print(sick_dwarf.name, "has puked")
            sick_dwarf.drunkenness = sick_dwarf.drunkenness - 1


def another_one():
    """
    Event where a random dwarf buys drinks for themselves and drinks.
    """
    x = rng.choice(DwarfList)
    x.buying_drinks()
    x.drinks()


def oh_a_penny():
    """
    A random dwarf from DwarfList finds a coin. Will they spend it wisely?
    """
    x = rng.choice(DwarfList)
    print(x.name, "found a coin!")
    x.money += 1

