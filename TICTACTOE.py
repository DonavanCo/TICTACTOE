import random

def print_board(board):
    
    "Prints Tic Tac Toe board."
    
    for row in board:
        print (" | ".join(row))
        print ("-" * 5)
    return 0

board = [[' ' for _ in range(3)] for _ in range(3)]
players = ['X', '0']

print_board(board)
