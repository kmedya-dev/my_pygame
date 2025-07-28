import random

number = random.randint(1, 100)

print(f"I'm thinking of a number between 1 and 100. It's {number}")

low = 1
high = 100

while True:
    guess = random.randint(low, high)
    print(f"My guess is {guess}")

    if guess < number:
        print("Too low!")
        low = guess + 1
    elif guess > number:
        print("Too high!")
        high = guess - 1
    else:
        print("I got it!")
        break
