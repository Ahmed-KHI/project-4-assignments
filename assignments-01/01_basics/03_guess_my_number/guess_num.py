import random

def main():
    secret_number = random.randint(0, 99)
    
    print("\n🔢 Guess My Number Game 🎮")
    print("I'm thinking of a number between 0 and 99...")
    print("------------------------------------------------")
    
    while True:
        guess = int(input("\nEnter your guess: "))
        
        if guess < secret_number:
            print("❌ Too low! Try again.")
        elif guess > secret_number:
            print("❌ Too high! Try again.")
        else:
            print(f"✅ Congrats! The number was: {secret_number} 🎉")
            break

if __name__ == '__main__':
    main()