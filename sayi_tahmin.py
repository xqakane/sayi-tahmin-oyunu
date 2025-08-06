import random

print("I have picked a number between 1 and 100. Try to guess it!")

number = random.randint(1, 100)
guess = 0
attempts = 0

while guess != number:
    guess = int(input("your guess: "))
    attempts += 1

    if guess < number:
         print("Try a higher number.")
    elif guess > number:
         print("Try a lower number.")
    else:
         print(f"Congratulations, Ezgi! You guessed it in {attempts} tries")
         
