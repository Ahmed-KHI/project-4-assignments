import random 

def roll_die():
    return random.randint(1, 6)

def roll_two_die():
    die1 = roll_die()
    die2 = roll_die()

    return die1, die2, die1 + die2

def main():
    die1, die2, total = roll_two_die()
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice: {total}")

if __name__ == "__main__":
    main()