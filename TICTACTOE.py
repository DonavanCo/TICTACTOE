#v2 of tictactoe uses GUI to play game
import tkinter as tk
import random #for computer opponent

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

def disable_buttons():
    for row_buttons in buttons:
        for button in row_buttons:
            button.config(state=tk.DISABLED)

def reset_game():
    global current_player, board, button_texts
    
    for row in range(3):
        for col in range(3):
            board[row][col] = ' '
            button_texts[row][col].set(' ')
            buttons[row][col].config(state=tk.NORMAL)
    
    current_player = 'X'
    label.config(text="Player X's turn")

# Create NEW Board for v2      
board = [[' ' for _ in range(3)] for _ in range(3)]

# Create Tkinter
root = tk.Tk()
root.title("Tic Tac Toe")


# Create label
current_player = 'X'
label = tk.Label(root, text="Player X's turn", font=('Arial', 14))
label.grid(row=3, columnspan=3, pady=10)

# Create reset button
reset_button = tk.Button(root, text="Reset", font=('Arial', 14), command=reset_game)
reset_button.grid(row=4, columnspan=3, pady=10)

root.mainloop()
