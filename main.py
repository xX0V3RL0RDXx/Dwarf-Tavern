from eventManager import *
from dwarf import *

# creation of EventDict
# event manager will use it
EventDict = {}
EventDict["name"] = EventList
EventDict["eventweights"] = EventWeightedList

turnsToPlay = 20
eventManager(turnsToPlay)







