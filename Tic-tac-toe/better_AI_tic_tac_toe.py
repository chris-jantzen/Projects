from tkinter import *
from tkinter.colorchooser import *
from collections import defaultdict
import functools
import numpy as np
from random import randint

board = np.zeros((3, 3), dtype='int')
color1 = 'red'
color2 = 'gray'
player = 1
gameover = False
tiegame = False
turn_count = 0

def gen_corners():
    global turn_count
    x = 1
    y = 1
    while x == 1:
        x = randint(0, 2)
    while y == 1:
        y = randint(0, 2)
    return (x, y)


def ai_move():
    global board, turn_count
    row = -1
    col = -1
    if turn_count == 0 and board[1, 1] == 0:
        board[1, 1] = 2
        row = 1
        col = 1

    #Horizontal Win Checks
    elif(board[0, 0] == 2 and board[0, 1] == 2 and board[0, 2] == 0):
        board[0, 2] = 2
        row = 0
        col = 2
    elif(board[0, 1] == 2 and board[0, 2] == 2 and board[0, 0] == 0):
        board[0, 0] = 2
        row = 0
        col = 0
    elif(board[0, 0] == 2 and board[0, 2] == 2 and board[0, 2] == 0):
        board[0, 1] = 2
        row = 0
        col = 1
    elif(board[1, 0] == 2 and board[1, 1] == 2 and board[1, 2] == 0):
        board[1, 2] = 2
        row = 1
        col = 2
    elif(board[1, 1] == 2 and board[1, 2] == 2 and board[1, 0] == 0):
        board[1, 0] = 2
        row = 1
        col = 0
    elif(board[1, 0] == 2 and board[1, 2] == 2 and board[1, 1] == 0):
        board[1, 1] = 2
        row = 1
        col = 1
    elif(board[2, 0] == 2 and board[2, 1] == 2 and board[2, 2] == 0):
        board[2, 2] = 2
        row = 2
        col = 2
    elif(board[2, 1] == 2 and board[2, 2] == 2 and board[2, 0] == 0):
        board[2, 0] = 2
        row = 2
        col = 0
    elif(board[2, 0] == 2 and board[2, 2] == 2 and board[2, 1] == 0):
        board[2, 1] = 2
        row = 2
        col = 1
    #Vertical Win Checks
    elif(board[0, 0] == 2 and board[1, 0] == 2 and board[2, 0] == 0):
        board[2, 0] = 2
        row = 2
        col = 0
    elif(board[0, 1] == 2 and board[1, 1] == 2 and board[2, 1] == 0):
        board[2, 1] = 2
        row = 2
        col = 1
    elif(board[0, 2] == 2 and board[1, 2] == 2 and board[2, 2] == 0):
        board[2, 2] = 2
        row = 2
        col = 2
    elif(board[1, 0] == 2 and board[2, 0] == 2 and board[0, 0] == 0):
        board[0, 0] = 2
        row = 0
        col = 0
    elif(board[1, 1] == 2 and board[2, 1] == 2 and board[0, 1] == 0):
        board[0, 1] = 2
        row = 0
        col = 1
    elif(board[1, 2] == 2 and board[2, 2] == 2 and board[0, 2] == 0):
        board[0, 2] = 2
        row = 0
        col = 2
    elif(board[0, 0] == 2 and board[2, 0] == 2 and board[1, 0] == 0):
        board[1, 0] = 2
        row = 1
        col = 0
    elif(board[0, 1] == 2 and board[2, 1] == 2 and board[1, 1] == 0):
        board[1, 1] = 2
        row = 1
        col = 1
    elif(board[0, 2] == 2 and board[2, 2] == 2 and board[1, 2] == 0):
        board[1, 2] = 2
        row = 1
        col = 2
    #Diagonal Win Checks
    elif(board[0, 0] == 2 and board[1, 1] == 2 and board[2, 2] == 0):
        board[2, 2] = 2
        row = 2
        col = 2
    elif(board[0, 0] == 2 and board[2, 2] == 2 and board[1, 1] == 0):
        board[1, 1] = 2
        row = 1
        col = 1
    elif(board[1, 1] == 2 and board[2, 2] == 2 and board[0, 0] == 0):
        board[0, 0] = 2
        row = 0
        col = 0
    elif(board[0, 2] == 2 and board[1, 1] == 2 and board[2, 0] == 0):
        board[2, 0] = 2
        row = 2
        col = 0
    elif(board[0, 2] == 2 and board[2, 0] == 2 and board[1, 1] == 0):
        board[1, 1] = 2
        row = 1
        col = 1
    elif(board[1, 1] == 2 and board[2, 0] == 2 and board[0, 2] == 0):
        board[0, 2] = 2
        row = 0
        col = 2

    #Horizontal Checks
    elif(board[0, 0] == 1 and board[0, 1] == 1 and board[0, 2] == 0):
        board[0, 2] = 2
        row = 0
        col = 2
    elif(board[0, 1] == 1 and board[0, 2] == 1 and board[0, 0] == 0):
        board[0, 0] = 2
        row = 0
        col = 2
    elif(board[0, 0] == 1 and board[0, 2] == 1 and board[0, 1] == 0):
        board[0, 1] = 2
        row = 0
        col = 1
    elif(board[1, 0] == 1 and board[1, 1] == 1 and board[1, 2] == 0):
        board[1, 2] = 2
        row = 1
        col = 2
    elif(board[1, 1] == 1 and board[1, 2] == 1 and board[1, 0] == 0):
        board[1, 0] = 2
        row = 1
        col = 0
    elif(board[1, 0] == 1 and board[1, 2] == 1 and board[1, 1] == 0):
        board[1, 1] = 2
        row = 1
        col = 1
    elif(board[2, 0] == 1 and board[2, 1] == 1 and board[2, 2] == 0):
        board[2, 2] = 2
        row = 2
        col = 2
    elif(board[2, 1] == 1 and board[2, 2] == 1 and board[2, 0] == 0):
        board[2, 0] = 2
        row = 2
        col = 0
    elif(board[2, 0] == 1 and board[2, 2] == 1 and board[2, 1] == 0):
        board[2, 1] = 2
        row = 2
        col = 1
    #Vertical Checks
    elif(board[0, 0] == 1 and board[1, 0] == 1 and board[2, 0] == 0):
        board[2, 0] = 2
        row = 2
        col = 0
    elif(board[0, 1] == 1 and board[1, 1] == 1 and board[2, 1] == 0):
        board[2, 1] = 2
        row = 2
        col = 1
    elif(board[0, 2] == 1 and board[1, 2] == 1 and board[2, 2] == 0):
        board[2, 2] = 2
        row = 2
        col = 2
    elif(board[1, 0] == 1 and board[2, 0] == 1 and board[0, 0] == 0):
        board[0, 0] = 2
        row = 0
        col = 0
    elif(board[1, 1] == 1 and board[2, 1] == 1 and board[0, 1] == 0):
        board[0, 1] = 2
        row = 0
        col = 1
    elif(board[1, 2] == 1 and board[2, 2] == 1 and board[0, 2] == 0):
        board[0, 2] = 2
        row = 0
        col = 2
    elif(board[0, 0] == 1 and board[2, 0] == 1 and board[1, 0] == 0):
        board[1, 0] = 2
        row = 1
        col = 0
    elif(board[0, 1] == 1 and board[2, 1] == 1 and board[1, 1] == 0):
        board[1, 1] = 2
        row = 1
        col = 1
    elif(board[0, 2] == 1 and board[2, 2] == 1 and board[1, 2] == 0):
        board[1, 2] = 2
        row = 1
        col = 2
    #Diagonal Checks
    elif(board[0, 0] == 1 and board[1, 1] == 1 and board[2, 2] == 0):
        board[2, 2] = 2
        row = 2
        col = 2
    elif(board[0, 0] == 1 and board[2, 2] == 1 and board[1, 1] == 0):
        board[1, 1] = 2
        row = 1
        col = 1
    elif(board[1, 1] == 1 and board[2, 2] == 1 and board[0, 0] == 0):
        board[0, 0] = 2
        row = 0
        col = 0
    elif(board[0, 2] == 1 and board[1, 1] == 1 and board[2, 0] == 0):
        board[2, 0] = 2
        row = 2
        col = 0
    elif(board[0, 2] == 1 and board[2, 0] == 1 and board[1, 1] == 0):
        board[1, 1] = 2
        row = 1
        col = 1
    elif(board[1, 1] == 1 and board[2, 0] == 1 and board[0, 2] == 0):
        board[0, 2] = 2
        row = 0
        col = 2

    #Special Checks
        #Edge and side case
    elif board[1, 2] == 1 and board[0, 0] == 1 and board[0, 2] == 0 and board[1, 1] == 2 and \
                        board[2, 0] != 1:
        board[0, 2] = 2
        row = 0
        col = 2
    elif board[1, 2] == 1 and board[2, 0] == 1 and board[2, 2] == 0 and board[1, 1] == 2 and \
                        board[0, 0] != 1:
        board[2, 2] = 2
        row = 2
        col = 0
    elif board[2, 1] == 1 and board[0, 2] == 1 and board[2, 2] == 0 and board[1, 1] == 2 and \
                        board[2, 2] != 1:
        board[2, 2] = 2
        row = 2
        col = 2
    elif board[2, 1] == 1 and board[0, 0] == 1 and board[2, 0] == 0 and board[1, 1] == 2 and \
                        board[2, 0] != 1:
        board[2, 0] = 2
        row = 2
        col = 0
    elif board[1, 0] == 1 and board[0, 2] == 1 and board[0, 0] == 0 and board[1, 1] == 2 and \
                        board[0, 2] != 1:
        board[0, 0] = 2
        row = 0
        col = 0
    elif board[1, 0] == 1 and board[2, 2] == 1 and board[2, 0] == 0 and board[1, 1] == 2 \
                        and board[0, 2] != 1:
        board[2, 0] = 2
        row = 2
        col = 0
    elif board[0, 1] == 1 and board[2, 0] == 1 and board[0, 0] == 0 and board[1, 1] == 2 and \
                        board[2, 2] != 1:
        board[0, 0] = 2
        row = 0
        col = 0
    elif board[0, 1] == 1 and board[2, 2] == 1 and board[0, 2] == 0 and board[1, 1] == 2 and \
                        board[2, 0] != 1:
        board[0, 2] = 2
        row = 0
        col = 2
        #Two edges case
    elif board[0, 1] == 1 and board[1, 2] == 1 and board[1, 1] == 2 and board[0, 2] == 0:
        board[0, 2] = 2
        row = 0
        col = 2
    elif board[0, 1] == 1 and board[1, 0] == 1 and board[1, 1] == 2 and board[0, 0] == 0:
        board[0, 0] = 2
        row = 0
        col = 0
    elif board[1, 0] == 1 and board[0, 1] == 1 and board[1, 1] == 2 and board[0, 0] == 0:
        board[0, 0] = 2
        row = 0
        col = 0
    elif board[1, 0] == 1 and board[2, 1] == 1 and board[1, 1] == 2 and board[2, 0] == 0:
        board[2, 0] = 2
        row = 0
        col = 0
    elif board[2, 1] == 1 and board[1, 0] == 1 and board[1, 1] == 2 and board[2, 0] == 0:
        board[2, 0] = 2
        col = 0
        row = 2
    elif board[2, 1] == 1 and board[1, 2] == 1 and board[1, 1] == 2 and board[2, 2] == 0:
        board[2, 2] = 2
        row = 2
        col = 2
    elif board[1, 2] == 1 and board[0, 1] == 1 and board[1, 1] == 2 and board[0, 2] == 0:
        board[0, 2] = 2
        row = 0
        col = 2
    elif board[1, 2] == 1 and board[2, 1] == 1 and board[1, 1] == 2 and board[2, 2] == 0:
        board[2, 2] = 2
        row = 2
        col = 2

    elif turn_count == 0 or turn_count == 1 and board[1, 1] == 1:
        nums = gen_corners()
        x = nums[0]
        y = nums[1]
        if board[x, y] != 2 and board[x, y] != 1:
            board[x, y] = 2
            row = x
            col = y
        else:
            return ai_move()

    else:
        rand_row = randint(0, 2)
        rand_col = randint(0, 2)
        while True:
            if(board[rand_row, rand_col] == 0):
                board[rand_row, rand_col] = 2
                row = rand_row
                col = rand_col
                break
            else:
                rand_row = randint(0, 2)
                rand_col = randint(0, 2)
    piece(row, col, 2)


def tie():
    global board
    for row in range(3):
        for col in range(3):
            if board[row, col] == 0:
                return False
    return True


def checkWin(player):
    global board
    win = False
    if(board[0, 0] != 0 and (board[0, 0] == board[0, 1] and board[0, 0] == board[0, 2])):
        win = True
    elif(board[1, 0] != 0 and (board[1, 0] == board[1, 1] and board[1, 0] == board[1, 2])):
        win = True
    elif(board[2, 0] != 0 and (board[2, 0] == board[2, 1] and board[2, 0] == board[2, 2])):
        win = True
    elif(board[0, 0] != 0 and (board[0, 0] == board[1, 0] and board[0, 0] == board[2, 0])):
        win = True
    elif(board[0, 1] != 0 and (board[0, 1] == board[1, 1] and board[0, 1] == board[2, 1])):
        win = True
    elif(board[0, 2] != 0 and (board[0, 2] == board[1, 2] and board[0, 2] == board[2, 2])):
        win = True
    elif(board[0, 0] != 0 and (board[0, 0] == board[1, 1] and board[0, 0] == board[2, 2])):
        win = True
    elif(board[0, 2] != 0 and (board[0, 2] == board[1, 1] and board[0, 2] == board[2, 0])):
        win = True
    return win


def resetboard():
    global board, gameover, tiegame, player, turn_count
    gameover = False
    tiegame = False
    turn_count = 0
    player = 1
    for row in range(3):
        for col in range(3):
            square[row][col].create_rectangle(0, 0, 200, 200, fill='black')
    board = np.zeros((3, 3), dtype='int')
    chatter.config(text='Player ' + str(1) + '\'s turn')


def redraw_board2():
    global board
    for row in range(3):
        for col in range(3):
            square[row][col].create_rectangle(0, 0, 200, 200, fill='black')
    for row in range(3):
        for col in range(3):
            if board[row, col] in (1, 2):
                piece(row, col, board[row, col])


def redraw_board():
    global board
    for row in range(3):
        for col in range(3):
            if board[row, col] in (1, 2):
                piece(row, col, board[row, col])


def key(event):
    global board, player, root, color1, color2, gameover, tiegame
    if event.char == 'l':
        resetboard()
        print('loading game ...')
        board = np.fromfile('/google/tinker/Tic-tac-toe/tictactoe_board.txt', \
                                sep=',', dtype='int').reshape(3, 3)
        redraw_board()
        with open('/google/tinker/Tic-tac-toe/tictactoe_player.txt', 'r') as f:
            player = int(f.readline())
            print('Player is ', player)
            '''pick1 = eval(f.readline())
            print('pick1 is ', str(pick1))'''
    elif event.char == 's':
        print('saving game ....')
        with open('/google/tinker/Tic-tac-toe/tictactoe_player.txt', 'w') as f:
            f.write(str(player) + '\n')
            #f.write(str(pick1) + '\n')
        board.tofile('/google/tinker/Tic-tac-toe/tictactoe_board.txt', sep=',')
        with open('/google/tinker/Tic-tac-toe/tictactoe_map.txt', 'w') as f:
            f.write(np.array_str(board))
    elif event.char == 1:
        root.quit()
    elif event.char == '1':
        color1 = askcolor()[1]
        redraw_board()
    elif event.char == '2':
        color2 = askcolor()[1]
        redraw_board()
    elif event.char == 'r':
        resetboard()
        # print('reset')
    elif event.char == 'x':
        root.quit()


def piece(row, col, player, reset=False):
    global color1, color2
    if player == 1:
        color = color1
    elif player == 2:
        color = color2
    else:
        color = 'black'
    if player == 1 and reset:
        square[row][col].create_line(10, 10, 190, 190, fill=color, width=20)
        square[row][col].create_line(10, 190, 190, 10, fill=color, width=20)
    elif player == 2 and reset:
        square[row][col].create_oval(10, 10, 190, 190, fill=color)
        square[row][col].create_oval(40, 40, 160, 160, fill='black')
    elif player == 1:
        square[row][col].create_line(10, 10, 190, 190, fill=color, width=20)
        square[row][col].create_line(10, 190, 190, 10, fill=color, width=20)
    elif player == 2:
        square[row][col].create_oval(10, 10, 190, 190, fill=color)
        square[row][col].create_oval(40, 40, 160, 160, fill='black')


#player 1 is x, player 2 is o
def picksquare(row, col, event):
    global board, player, pick, gameover, tiegame, turn_count
    if gameover or tiegame:
        return
    if board[row, col] == 0:
        board[row, col] = player
        piece(row, col, player)
        if checkWin(player):
            gameover = True
            chatter.config(text='Player ' + str(player) + ' Wins!')
        if not gameover and tie():
            tiegame = True
            chatter.config(text='It\'s a tie.')
            return
        if player == 1 and not gameover:
            player = 2
            ai_move()
            # print(board)
            turn_count += 1
            redraw_board2()
            if checkWin(player):
                gameover = True
                chatter.config(text='Player ' + str(player) + ' wins!')
                return
            if tie():
                tiegame = True
                chatter.config(text="It's a tie.")
                return
            player = 1
    else:
        return

root = Tk()
root.geometry('612x650')
root.bind("<Key>", key)

square = defaultdict(list)
frame = Frame(root)
frame2 = Frame(frame)
frame2.grid()

for row in range(3):
    for col in range(3):
        square[row].append(Canvas(frame2, height=200, width=200, bg='black'))
        square[row][col].grid(row=row, column=col)
        square[row][col].bind('<Button-1>', functools.partial(picksquare, row, col))
frame2.pack(fill=X)

chatter = Label(frame, text='Chatter ...')
chatter.pack(fill=X)
frame.pack(fill=X)

chatter.config(text='Player ' + str(player) + '\'s turn.')
mainloop()
