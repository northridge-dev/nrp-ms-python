# Guessing Game

Let's make a guessing game. Read the code below to find out how it works. **Describe the game's behavior in your own words.**

<br>
<br>
<br>
<br>

## Code

```python
import random # we will use the random module to generate a random number

target = random.randint(1, 100) # generate a random number between 1 and 100
guesses_left = 10

#
while guesses_left > 0:
    print(f"You have {guesses_left} guesses left.")
    print("")

    guess = input("Guess a number between 1 and 100: ")
    guess = int(guess) #
    guesses_left -= 1 #

    #
    if guess < target:
        print("Too low! Try again.")
        print("")
    elif guess > target:
        print("Too high! Try again.")
        print("")
    else: #
        break #

#
if guess == target:
    print("Congratulations! You guessed the number!")
else:
    print(f"Sorry, you're out of guesses. The number was {target}.")
```

## Questions

1. There are 7 lines of code marked with `#`. In the code, write a comment for each explaining what it does.
2. What would happen if we removed the line `guesses_left -= 1`?
3. What would happen if we removed the line `guess = int(guess)`?
4. What would happen if we removed the line `break`?
5. Why do we need the line `if guess == target:` at the end of the program?
