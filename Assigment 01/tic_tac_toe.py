# Tic-Tac-Toe (2 Players)
# No AI, Simple Code

board = [" " for _ in range(9)]

def show_board():
    print("\n---------")
    for i in range(3):
        print(f"| {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} |")
        print("---------")

def check_winner():
    lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]    
    ]
    for line in lines:
        if board[line[0]] == board[line[1]] == board[line[2]] != " ":
            return board[line[0]]
    return None

current_player = "X"
while True:
    show_board()
    position = input(f"Player {current_player}, enter position (1-9): ")
    
    if position.isdigit() and 1 <= int(position) <= 9:
        position = int(position) - 1
        if board[position] == " ":
            board[position] = current_player
            winner = check_winner()
            if winner:
                show_board()
                print(f"Player {winner} wins!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Position already taken!")
    else:
        print("Invalid input! Enter 1-9.")