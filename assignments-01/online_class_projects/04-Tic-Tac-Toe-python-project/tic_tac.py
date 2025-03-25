import time

# Tic-Tac-Toe Board
board = [" " for _ in range(9)]

# Function to print board
def print_board():
    print("\n")
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-" * 9)
    print("\n")

# Function to check for a win
def check_winner():
    win_conditions = [(0,1,2), (3,4,5), (6,7,8),  # Rows
                      (0,3,6), (1,4,7), (2,5,8),  # Columns
                      (0,4,8), (2,4,6)]           # Diagonals
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return None

# Function to check if board is full (draw)
def is_draw():
    return " " not in board

# Function for player move
def player_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, enter position (1-9): ")) - 1
            if board[move] == " ":
                board[move] = player
                break
            else:
                print("⚠️ Position already taken! Try again.")
        except (ValueError, IndexError):
            print("⚠️ Invalid input! Enter a number between 1 and 9.")

# Main game loop
def tic_tac_toe():
    current_player = "X"
    print_board()
    
    while True:
        player_move(current_player)
        print_board()
        
        # Check winner
        winner = check_winner()
        if winner:
            print(f"🎉 Player {winner} wins!")
            break

        # Check draw
        if is_draw():
            print("😐 It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

        # Short delay for better readability
        time.sleep(1)

# Run the game
if __name__ == "__main__":
    tic_tac_toe()