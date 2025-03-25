import random

NUM_SIDES = 6

def roll_dice():

    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    print(f"Dice rolled: {die1} and {die2} | Total: {die1 + die2}")

def main():
    print("Rolling the dice three time...\n")
    for _ in range(3):
        roll_dice()

if __name__ == "__main__":
    main()