import random

num = random.randint(1, 100)
tries = 0

print("Guess a number between 1 and 100")

while True:
    guess = int(input("Enter guess: "))
    tries += 1

    if guess < num:
        print("Too low!")
    elif guess > num:
        print("Too high!")
    else:
        print(f"Correct! You guessed in {tries} tries.")
        break
