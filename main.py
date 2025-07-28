

import time
import random

def introduction():
    print("Welcome to the Text Adventure!")
    time.sleep(1)
    print("You find yourself in a dark room.")
    time.sleep(1)
    print("There is a door to your left and a door to your right.")
    time.sleep(1)

def choose_door():
    choice = random.choice(["left", "right"])
    print(f"The computer chose: {choice}")
    return choice

def left_door():
    print("\nYou chose the left door and find a treasure chest!")
    time.sleep(1)
    print("Congratulations, you win!")

def right_door():
    print("\nYou chose the right door and fell into a pit.")
    time.sleep(1)
    print("Game Over.")

def main():
    introduction()
    door_choice = choose_door()

    if door_choice == "left":
        left_door()
    elif door_choice == "right":
        right_door()

if __name__ == "__main__":
    main()

