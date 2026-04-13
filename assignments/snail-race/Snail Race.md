# The Great Snail Race

You're going to build a snail race game in Python.

# Part 1: Constants and Variables

In Python, we use **constants** for values that never change. These are typically written in ALL_CAPS to remind us not to modify them.

You do not need to add this code to your file, but look at these constants and answer the questions below:

```python
MAX_NUM_SNAILS = 8
MAX_NAME_LENGTH = 20
FINISH_LINE = 40
```

1. What do you think each constant represents in the game?
   <br><br>
2. Why do you think the programmer chose these particular values?

<div class="page"/>

# Part 2: Input Validation with While Loops

The game uses `while True` loops to keep asking until the player enters valid input. This is a common pattern!

Add this code to `snail_race.py`. **It is test code. You will delete it after you're finished.**:

```python
while True:
    response = input("Enter a number: ")
    if response.isdecimal():
        break
    print("That's not a number!")
```

## Testing:

Run the code and try entering different inputs. Describe what happens when you enter:

- A valid number (e.g., `5`)
  <br><br>
- A non-number (e.g., `hello`)
  <br><br>
- An empty string (just press Enter)
  <br><br>

## Questions

1. What does `break` do in a loop?
   <br><br><br>
2. What would happen if you removed the `break` statement?
   <br><br><br>

**Delete the test code before moving on to the next part!**

<div class="page"/>

# Part 3: Storing Data in Lists

We need to keep track of snail names. A **list** is perfect for this.

Add this code to `snail_race.py`. **It is test code. You will delete it after you're finished.**:

```python
snailNames = []  # Start with an empty list

# Add names one at a time
for i in range(3):
    name = input("Enter a snail name: ")
    snailNames.append(name)

print(snailNames)
```

## Questions

1. What does `append` do?
   <br><br><br>
2. If you add 3 snails, what is `snailNames[0]`? What is `snailNames[-1]`? If you're not sure, add print statements to check.
   <br><br><br>
3. What does `len(snailNames)` return after adding 5 snails? If you're not sure, add a print statement to check.
   <br><br><br>

**Delete the test code before moving on to the next part!**

<div class="page"/>

# Part 4: Dictionaries for Tracking Progress

We need to track how far each snail has moved. A **dictionary** lets us map each snail's name to its progress.

Add this code to `snail_race.py`. **It is test code. You will delete it after you're finished.**:

```python
snailProgress = {}
snailNames = ["Speedy", "Slowpoke", "Turbo"]

for snailName in snailNames:
    snailProgress[snailName] = 0  # All snails start at position 0

print(snailProgress)
```

## Questions

1. What does `snailProgress["Speedy"]` equal right after this code runs?
   <br><br><br>
2. How would you increase Speedy's progress by 1? Write the code here. Be sure to test it.
   <br><br><br>
3. Write code to increase every snail's progress by 1. Be sure to test your code. Once you have it working, write the code here.
   <br><br><br><br><br><br>

**Delete the test code before moving on to the next part!**

<div class="page"/>

# Part 5: The Random Module

The game uses `random` to decide which snails move.

Add this code to `snail_race.py`. **It is test code. You will delete it after you're finished.**:

```python
import random

snailNames = ["Speedy", "Slowpoke", "Turbo"]

randomSnail = random.choice(snailNames)
moves = random.randint(1, 3)

print(f"{randomSnail} moves {moves} spaces")
```

## Questions

1. What does `random.choice()` do?
   <br><br><br>
2. What does `random.randint(1, 3)` return? Can it return 2? Can it return 3? Can it return 4?
   <br><br><br>

**Delete the test code before moving on to the next part!**

<div class="page"/>

# Part 6: String Operations

To display the race track, we need to create spaces and repeated characters.

You don't need to add this code to your file, but it gives you examples you can use to answer the questions below.

```python
spaces = 5
print(" " * spaces)  # Creates 5 spaces

position = 3
print("@v")
print("." * position)  # Creates 3 dots
```

## Questions

1. What does `" " * 10` produce?
   <br><br><br>
2. What does `"ha" * 3` produce?
   <br><br><br>
3. If `position` is 4, what does `"." * position + "@v"` produce?
   <br><br><br>
4. How could you use string multiplication to create a string that shows a snail at position 7 on the track? Write the code here. (Be sure to test it.)
   <br><br><br>

**Delete the test code before moving on to the next part!**

<div class="page"/>

# Part 7: Time Delays

The `time.sleep()` function pauses the program.

Add this code to `snail_race.py`. **It is test code. You will delete it after you're finished.**:

```python
import time

print("Ready...")
time.sleep(1)
print("Go!")
```

## Questions

1. What happens if you change `time.sleep(1)` to `time.sleep(0.1)`?
   <br><br><br>

**Delete the test code before moving on to the next part!**

<div class="page"/>

# Part 8: Building the Game

Now let's put it all together. Clear out `snail_race.py` to start fresh and add the following:

## Step 1: Constants and Setup

```python
import random, time

MAX_NUM_SNAILS = 8
MAX_NAME_LENGTH = 20
FINISH_LINE = 40

print('''The Great Snail Race

    @v <-- snail

''')
```

## Step 2: Ask for Number of Snails

```python
while True:
    print('How many snails will race? Max:', MAX_NUM_SNAILS)
    response = input('> ')
    if response.isdecimal():
        numSnailsRacing = int(response)
        if 1 < numSnailsRacing <= MAX_NUM_SNAILS:
            break
    print('Enter a number between 2 and', MAX_NUM_SNAILS)
```

<div class="page"/>

## Step 3: Get Snail Names

```python
snailNames = []
for i in range(1, numSnailsRacing + 1):
    while True:
        print('Enter snail #' + str(i) + "'s name:")
        name = input('> ')
        if len(name) == 0:
            print('Please enter a name.')
        elif name in snailNames:
            print('Choose a name that has not already been used.')
        else:
            break
    snailNames.append(name)
```

## Step 4: Initialize and Display

```python
print('\n' * 40)
print('START' + (' ' * (FINISH_LINE - len('START'))) + 'FINISH')
print('|' + (' ' * (FINISH_LINE - len('|'))) + '|')

snailProgress = {}
for snailName in snailNames:
    print(snailName[:MAX_NAME_LENGTH])
    print('@v')
    snailProgress[snailName] = 0

time.sleep(1.5)
```

<div class="page"/>

## Step 5: Main Race Loop

```python
while True:
    winner = None

    for i in range(random.randint(1, numSnailsRacing // 2)):
        randomSnailName = random.choice(snailNames)
        snailProgress[randomSnailName] += 1

        if snailProgress[randomSnailName] == FINISH_LINE:
            print(randomSnailName, 'has won!')
            winner = randomSnailName
            break

    if winner:
        break

    time.sleep(0.2)
    print('\n' * 40)

    print('START' + (' ' * (FINISH_LINE - len('START'))) + 'FINISH')
    print('|' + (' ' * (FINISH_LINE - 1)) + '|')

    for snailName in snailNames:
        spaces = snailProgress[snailName]
        print((' ' * spaces) + snailName[:MAX_NAME_LENGTH])
        print(('.' * snailProgress[snailName]) + '@v')
```

Try playing the game! Run it multiple times to see different outcomes.

<div class="page"/>

# Part 9: Experiments

Now that your game works, try these experiments:

1. **Change the speed:** Modify `time.sleep(0.2)` to make the race faster or slower.

2. **Add a cheat:** Add code that gives an extra boost to a snail with your name:

   ```python
   if "YOUR_NAME" in snailProgress:
       snailProgress["YOUR_NAME"] += 1
   ```

   You'll have to think carefully about where to place this code to make it work correctly!

3. **Longer or shorter race:** Change `FINISH_LINE` to see how it affects the game.

<div class="page"/>

# Part 10: Questions

1. What is the purpose of the `while True` loop at the start of the program?
   <br><br><br>
2. Why do we use `snailNames.append(name)` instead of just setting `snailNames = name`?
   <br><br><br>
3. Explain how the dictionary `snailProgress` tracks each snail's position.
   <br><br><br>
4. What would happen if you replaced `randomSnailName = random.choice(snailNames)` with `randomSnailName = snailNames[0]`?
   <br><br><br>
5. What would happen if you replaced `randomSnailName = random.choice(snailNames)` with `randomSnailName = snailNames[random.randint(0, len(snailNames))]`?
   <br><br><br>
6. How does the game know when to stop?

<div class="page"/>

# Part 11: Challenge

Add a new feature to the game: **Lap Counting**

- Before the race starts, ask how many laps to run
- A snail wins when it completes all laps
- Display the lap number for each snail
- You choose:
  - have the snails go back to the start line after each lap, or
  - have the snails _turn around_ and progress toward the start line for even-numbered laps, then turn around again for odd-numbered laps

Hint: You'll need to track both the lap and the position for each snail!

<div class="page"/>

# Part 12: Web Version

You can play a web version of The Great Snail Race at [https://northridge.dev/snail-race](https://northridge.dev/snail-race).

## Questions

Ask how to look at the source code for the web version. Scan through it. It's in a different programming language (JavaScript), but you should be able to follow most of it.

1. What is the name of the function that moves the snails forward?
   <br><br><br>
2. How does the web version decide which snail moves forward? Write out the line of code that makes the random selection.
