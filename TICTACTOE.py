import random

def print_board(board):
    
    #Prints Tic Tac Toe board.
    
    for row in board:
        print (" | ".join(row))
        print ("-" * 5)
    return 0

def check_winner(board):
    
    #Checks if there's a winner
    
    for row in board:
        if len(set(row)) ==1 and row[0] != ' ':
            return row[0]
        
    for col in range(3):
        if len(set([board[row][col] for row in range(3)])) == 1 and board[0][col] != ' ':
            return board[0][col]

board = [[' ' for _ in range(3)] for _ in range(3)]
players = ['X', '0']

print_board(board)
