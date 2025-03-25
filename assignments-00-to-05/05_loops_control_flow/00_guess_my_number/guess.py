import random

def main():

    secret_number = random.randint(0, 99)
    
    print("I am thinking of a number between 0 and 99...")
    
    attempts = 0  
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 0 or guess > 99:
                print("Please enter a number between 0 and 99.")
            elif guess < secret_number:
                print("🔽 Your guess is too low! Try again.")
            elif guess > secret_number:
                print("🔼 Your guess is too high! Try again.")
            else:
                print(f"🎉 Congrats! You guessed the number {secret_number} in {attempts} attempts.")
                break  
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

if __name__ == '__main__':
    main()