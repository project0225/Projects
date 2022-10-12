import random


def rolldice(min, max):
    while True:
        print("Rolling Dice...")
        number = random.randint(min, max)
        print(f"You rolled: {number}")
        choice = input("Do you want to roll again? (y/n)")
        if choice == 'n':
            break


rolldice(1,6)