# ÏLUN KINEM!

---
### What is this?

This is **dwarf tavern simulator**. It's a silly project from 2 computer sciences students. Inspiration for us was a game **Dwarf Fortress** (we recomend you to play it).
Program will simulate a tavern where there is some pack of dwarfs who wants to party. 

The entire simulation operates on a turn-based system.
During one turn, something can happen. For example, dwarfs are happy, so they do what they love to do - they `DRINK!`

---
### How does it work?
There are some steps before the simulation will start.

###  First step
The program contains a txt file in which you enter, one by one on separate lines, the names of the dwarves participating in the simulation (feel free to make changes in this file). Once program open file, names of dwarf will be added to `dwarfs_list` array.
If there is a problem with the file, you will receive an error message. **(Beware the Bad Dragon!)**

Remember, dwarves don't drink alone! So, if there is a single dwarf in the tavern, he can't drink and simulation will end.

### Second step
After creating a list of dwarfs, we are creating objects of the class Dwarf with variables.

```python
class Dwarf:
    #TO DO
```
### Parameters of dwarf

The amount of money is generated randomly, but you can also set it manually. Money is needed for buying `beers`. Two pieces of gold are needed to buy one goblet of beer.

---
### Starting the simulation

>*Here, at **The Strike Earth** Tavern, some dwarfs gather together after work to drink beer and spend a lovely time with friends.*

From, this point the simulation begins. Like we just said, simulation operate on turn-based system.
Each turn there is a chance to start random event.

#### There are events such as:
- `party_time()` - dwarfs are soo happy that they start to drink. Every one drinks. 
- `whip()` - You can hear in the distance an army of orcs marching day and night. 
- 

**For every 5 turns**, the program will pause the simulation for you so you can see what just happened. To resume the simulation, simply press the `enter` key.

---
### But when it ends?
The simulation will end either when you reach a maximum number of turns that you chose at the beginning or when the tavern runs out of beer (which the dwarfs will not like).
