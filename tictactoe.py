from tkinter  import *
import random

def next_turn(row, column):
    global player
    # Check if the button is empty and there's no winner yet
    if buttons[row][column]['text'] == "" and check_winner() is False:
        # If it's player 1's turn
        if player == players[0]:
            buttons[row][column]['text'] = player

            # If there's no winner after this move, switch to player 2's turn
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1] + " turn"))

            # If player 1 wins, display the winning message
            elif check_winner() is True:
                label.config(text=(players[0] + " wins"))

            # If it's a tie, display the tie message
            elif check_winner() == "Tie":
                label.config(text=("Tie!"))
        
        # If it's player 2's turn
        else:
            buttons[row][column]['text'] = player

            # If there's no winner after this move, switch to player 1's turn
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + " turn"))

            # If player 2 wins, display the winning message
            elif check_winner() is True:
                label.config(text=(players[1] + " wins"))

            # If it's a tie, display the tie message
            elif check_winner() == "Tie":
                label.config(text=("Tie!"))

# Check if there's a winner after each move
def check_winner():
    # Check rows
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    # Check columns  
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    # Check diagonals
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")        
        return True
        
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    
    # If there's no winner and the board is full, it's a tie
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")               
        return "Tie"
        
    else:
        return False

# Check if there are any empty spaces left on the board
def empty_spaces():
    spaces = 9
    
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    
    if spaces == 0:
        return  False
    else:
        return True
 
 # Start a new game
def new_game():
    global player
    
    player = random.choice(players)
    label.config(text=player + " turn")
    
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")

# Create the main window
window = Tk()
window.title("Tic-Tac-Toe")

# Define the players and randomly choose who starts
players = ["X","O"]
player = random.choice(players)

# Create buttons for the game board
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

# Create a label to display whose turn it is
label = Label(text= player + " turn", font=('Sans Serif', 40))
label.pack(side="top")

reset_button = Button(text="RESTART", font=('Sans Serif', 20), command=new_game)
reset_button.pack(side="top")

# Create a frame for the game board
frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('Sans Serif', 40), width=5, height=2, 
                                      command= lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

# Start the main event loop    
window.mainloop()