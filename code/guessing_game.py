import random

target = random.randint(1, 100)
guesses_left = 4

while guesses_left > 0:
    print(f"You have {guesses_left} guesses left.")
    print("")

    guess = input("Guess a number between 1 and 100: ")
    guess = int(guess)
    guesses_left -= 1

    if guess < target:
        print("Too low! Try again.")
        print("")
    elif guess > target:
        print("Too high! Try again.")
        print("")
    else:
        break

if guess == target:
    print("Congratulations! You guessed the number!")
else:
    print(f"Sorry, you're out of guesses. The number was {target}.")