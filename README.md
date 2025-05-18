# ÏLUN KINEM!

### What is this?

This is a **Dwarf Tavern Simulator** — a silly project by two computer science students.  
We drew inspiration from the legendary game **Dwarf Fortress** (which we *highly* recommend playing!).

The program simulates a rowdy tavern where a bunch of dwarves gather to do what they do best: **DRINK!**

The entire simulation operates on a turn-based system.  
During each turn, something may happen — and if the dwarves are happy, you know what that means... they `DRINK!`

---

## How does it work?

There are a few steps before the simulation begins.

---
### 🚪 First Step: Opening the Tavern
At the beginning of the program, the **first step** is creating a `tavern` using the **dwarf.py** file.
The created tavern is stored in TavernList.
Currently, the program supports only one tavern, but this will change in the future 🧙‍♂️
```python
TavernList = [Tavern("The Strike Earth", 50)]
```
The tavern requires two parameters:

- `tavernName` — a string describing the name of the tavern

- `tavernSupplyOfBeer` — an integer describing the amount of beer in stockpiles.
### 🧾 Second Step: The Guest List

The program uses a `.txt` file where you list the names of the dwarves — one per line.  
Once the program reads the file, it adds those names to the `dwarfs_list` array.

If there is a problem with the file, you will receive an error message. **(Beware the Bad Dragon!)**

```python

# Load dwarf names from file
try:
    with open("dwarves.txt", "r") as file:
        for each_line in file:
            DwarfNameList.append(each_line.strip())
    if len(DwarfNameList) == 1:
        print("Only one dwarf? What is this, an elf poetry night?! Get more drinkers in here!")
        exit()
    elif len(DwarfNameList) == 0:
        print(
            "The chairs are stacked, the mugs are dry... Not a single dwarf showed up. Even the rats are disappointed.")
        exit()
except FileNotFoundError:
    print("Looks like a dragon burned down the tavern... What a shame.")
    exit()
# Create Dwarf instances
for each_dwarf in DwarfNameList:
    Dwarf(each_dwarf)

```


Remember, **dwarves don't drink alone!** So, if there is a single dwarf in the tavern, he can't drink and simulation will end.

---

### ⛏ Second Step: Creating the Dwarves

Each name becomes a **Dwarf object**, with the following properties:

```python
self.name = name
self.money = rng.randint(0, 40)
self.beers = 0
self.drunkenness = 0
```
Where:
- `name` — the dwarf’s name, taken from the file

- `money` — the amount of gold a dwarf starts with

- `beers` — how many beers the dwarf currently holds

- `drunkenness` — the dwarf’s current level of intoxication

The amount of money is generated randomly, but you can also set it manually for all dwarves. Money is needed for buying beers. Two pieces of gold are needed to buy one goblet of beer.

After creating each dwarf, they kindly introduce themselves by using `introduce()` method.

```txt
Greetings, I'm Fosdrod Runeshaper and I have 8 coins in my pocket. 

```
---

### 🍻 Starting the Simulation

> *Welcome to **The Strike Earth Tavern**, where hardworking dwarves unwind with cold beer and warm company.*


In fail main.py there is a line 
```python
    turnsToPlay = 20
    eventManager(turnsToPlay)
```

The variable turnsToPlay determines after how many turns the simulation will end.
The method eventManager runs the simulation for the specified number of turns.

From this point, **the simulation begins**.

Each turn, a `random event` might occur...

---

### 🎲 Possible Events

- `party_time()` - Every dwarf buys beer — if they have money, of course —
    and drinks like there's no tomorrow! - if they have beer, of course...
- `another_one()` - Only one beer? GIVE ME ANOTHER ONE NOW!
 (Simply put, one dwarf buys a drink and then drinks it...)
- `oh_a_penny()` - One lucky dwarf finds a coin. Will they spend it wisely?
- `puke()` - Event that chooses a random dwarf and checks if they will puke.

**Every 5 turns**, the simulation pauses so you can enjoy the chaos.
Just press Enter to keep going, or if you wanna end the simulation (okay, rude), press `N` and then Enter.

---

### ⏳ How Does It End?

The simulation ends if:

- You reach the **maximum number of turns**, or
- The **tavern runs out of beer** (uh-oh... let’s hope the dwarves don’t notice.)

---

### 🔮 What Does the Future Hold?

More events.
More dwarves.
More taverns.
And a whole lot of good old-fashioned BEER.
(Maybe even graphics… who knows?)

---
 
### 📯 Send a Raven (Or Just Email Us)
If you have any questions for us, feel free to reach out:

- [Oliwier Gramala](https://www.linkedin.com/in/oliwiergramala/), olivier.gramala@gmail.com
- [Filip Mielewczyk](https://www.linkedin.com/in/filmie240/), filip.mielewczyk11@gmail.com
