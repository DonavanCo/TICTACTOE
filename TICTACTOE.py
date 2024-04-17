import random #for computer opponent

def print_board(board):
    
    #Prints Tic Tac Toe board.
    
    for row in board:
        print (" | ".join(row))
        print ("-" * 5)
    return 0

def check_winner(board):
    
    #Checks if there's a winner
    
    #Horizontal win
    for row in board:
        if len(set(row)) ==1 and row[0] != ' ':
            return row[0]
    
    #Vertical win
    for col in range(3):
        if len(set([board[row][col] for row in range(3)])) == 1 and board[0][col] != ' ':
            return board[0][col]
    
    #Diagonal win
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def is_board_full(board):
    
    #Checks if the board is full
    
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def computer(board): #Computer opponent
    
    empty_cell = [(i,j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(empty_cell) if empty_cell else None
    
def game():
    #Start of Game
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', '0']
    turn = 0
    
    while True:
        print_board(board)
        #players turn
        if players[turn] == 'X':
            row = int(input("Enter row number (0, 1, or 2): "))
            col = int(input("Enter column number (0, 1, or 2): "))

            if board[row][col] != ' ':
                print("Cell already occupied. Try again.")
                continue
                
            board[row][col] = players[turn]
        #computer turn
        else:
            print("Computer's turn")
            move = computer(board)
            if move:
                row, col = move
                board[row][col] = players[turn]

        winner = check_winner(board)
        #check for winner
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        turn = (turn + 1) % 2

if __name__ == "__main__":
    game()
