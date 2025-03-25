import random

NUM_ROUNDS = 5

def play_game():
    print("Welcome to the High-Low Game!")
    print('-' * 40)
    
    player_score = 0  # Keeping track of the player's score
    
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num} starts!")
        
        computer_number = random.randint(1, 100)
        player_number = random.randint(1, 100)
        print(f"Your generated number is: {player_number}")
        
        user_choice = input("Do you think your number is higher or lower than the computer's? (higher/lower): ")
        
        while user_choice not in ["higher", "lower"]:
            user_choice = input("Invalid input! Please enter 'higher' or 'lower': ")
        
        is_higher_correct = user_choice == "higher" and player_number > computer_number
        is_lower_correct = user_choice == "lower" and player_number < computer_number
        
        if is_higher_correct or is_lower_correct:
            print(f"Correct guess! The computer's number was {computer_number}.")
            player_score += 1
        else:
            print(f"Oops! Wrong guess. The computer's number was {computer_number}.")
        
        print(f"Current Score: {player_score}")
        print("-" * 40)
    
    print(f"Final Score: {player_score} out of {NUM_ROUNDS}")
    if player_score == NUM_ROUNDS:
        print("Excellent! You played perfectly!")
    elif player_score > NUM_ROUNDS // 2:
        print("Great job! You did well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    play_game()