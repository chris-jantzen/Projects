from tkinter import *
from tkinter.colorchooser import *
from collections import defaultdict
import functools
import numpy as np

def redraw_board():
    global board
    for row in range(0, 8):
            for col in range(row%2, 8, 2):
                outlineSquare(row, col, 0)
                if board[row, col] == 0:
                    piece(row, col)
                else:
                    piece(row, col, board[row, col])


def key(event):
    #print('KEY:', repr(event.char))
    global board, player, pick1, root, color1, color2
    if event.char == 'l':
        print('loading game ...')
        board = np.fromfile('checker_board.txt', sep=',', dtype='int').reshape(8, 8)
        redraw_board()
        with open('checker_player.txt', 'r') as f:
            player = int(f.readline())
            print('Player is ', player)
            pick1 = eval(f.readline())
            print('pick1 is ', str(pick1))
    elif event.char == 's':
        print('saving game ....')
        with open('checker_player.txt', 'w') as f:
            f.write(str(player) + '\n')
            f.write(str(pick1) + '\n')
        board.tofile('checker_board.txt', sep=',')
        with open('checker_map.txt', 'w') as f:
            f.write(np.array_str(board))
    elif event.char == 'x':
        root.quit()
    elif event.char == '1':
        color1 = askcolor()[1]
        redraw_board()
    elif event.char == '2':
        color2 = askcolor()[1]
        redraw_board()


root = Tk()
root.geometry('435x445')
root.bind("<Key>", key)

player = 0
pick1 = None
noPick1 = False
moves = []
board = np.zeros((8, 8), dtype='int')
board[[0, 2], ::2] = 1
board[1, 1::2] = 1
board[[5, 7], 1::2] = 2
board[6, ::2] = 2
color1 = '#008080'
color2 = '#002db3'

def checkWin(player):
    global board
    move = []
    for row in range(7):
        for col in range(7):
            if board[row, col] in (player, player+2):
                move.append(validMoves(row, col, player))
            if len(move) != 0:
                return False
    return True


def piece(row, col, piece=None, type=None):
    global color1, color2
    if piece and piece > 2:
        type = 'king'
        piece -= 2
    color = color1 if piece == 1 else color2
    if piece is None:
        square[row][col].create_oval(10/2, 10/2, 90/2, 90/2, fill='black')
    elif type is 'king':
        square[row][col].create_oval(10/2, 10/2, 90/2, 90/2, fill=color)
        square[row][col].create_oval(30/2, 30/2, 70/2, 70/2, width=10/2, outline='black')
    else:
        square[row][col].create_oval(10/2, 10/2, 90/2, 90/2, fill=color)


def outlineSquare(row, col, value=1):
    if value == 1:
        color = 'yellow'
    elif value == 2:
        color = 'green'
    else:
        color = 'black'
    square[row][col].create_rectangle(7/2, 7/2, 96/2, 96/2, width=4, outline=color)


def validMoves(row, col, player, jumpOnly=False):
    global board
    moves = []
    #Player 1 regular piece
    if player == 1 and board[row, col] == 1:
        #down left
        if col > 0 and board[row+1, col-1] == 0 and not jumpOnly:
            moves.append((row+1, col-1))

        #down right
        if col < 7 and board[row+1, col+1] == 0 and not jumpOnly:
            moves.append((row+1, col+1))

        #jump down left
        if col > 1 and (row + 2) < 8 and board[row+2, col-2] == 0 and \
                                (board[row+1, col-1] == 2 or board[row+1, col-1] == 4):
            moves.append((row+2, col-2))

        #jump down right
        if col < 6 and (row + 2) < 8 and board[row+2, col+2] == 0 and \
                                (board[row+1, col+1] == 2 or board[row+1, col+1] == 4):
            moves.append((row+2, col+2))

    #Player 2 regular piece
    elif player == 2 and board[row, col] == 2:
        #up left
        if col > 0 and board[row-1, col-1] == 0 and not jumpOnly:
            moves.append((row-1, col-1))

        #up right
        if col < 7 and board[row-1, col+1] == 0 and not jumpOnly:
            moves.append((row-1, col+1))

        #jump up left
        if col > 1 and (row - 2) >= 0 and board[row-2, col-2] == 0 and \
                                (board[row-1, col-1] == 1 or board[row-1, col-1] == 3):
            moves.append((row-2, col-2))

        #jump up left
        if col < 6 and (row - 2) >= 0 and board[row-2, col+2] == 0 and \
                                (board[row-1, col+1] == 1 or board[row-1, col+1] == 3):
            moves.append((row-2, col+2))

    #Player 1 King
    elif player == 1 and board[row, col] == 3:
        #down left
        if col > 0 and row + 1 < 8 and board[row+1, col-1] == 0 and not jumpOnly:
            moves.append((row+1, col-1))

        #down right
        if col < 7 and row + 1 < 8 and board[row+1, col+1] == 0 and not jumpOnly:
            moves.append((row+1, col+1))

        #up left
        if col > 0 and row - 1 > 0 and board[row-1, col-1] == 0 and not jumpOnly:
            moves.append((row-1, col-1))

        #up right
        if col < 7 and row - 1 > 0 and board[row-1, col+1] == 0 and not jumpOnly:
            moves.append((row-1, col+1))

        #jump down left
        if col > 1 and (row + 2) < 8 and board[row+2, col-2] == 0 and \
                                (board[row+1, col-1] == 2 or board[row+1, col-1] == 4):
            moves.append((row+2, col-2))

        #jump down right
        if col < 6 and (row + 2) < 8 and board[row+2, col+2] == 0 and \
                                (board[row+1, col+1] == 2 or board[row+1, col+1] == 4):
            moves.append((row+2, col+2))

        #jump up left
        if col > 1 and (row - 2) >= 0 and board[row-2, col-2] == 0 and \
                                (board[row-1, col-1] == 2 or board[row-1, col-1] == 4):
            moves.append((row-2, col-2))

        #jump up right
        if col < 6 and (row - 2) >= 0 and board[row-2, col+2] == 0 and \
                                (board[row-1, col+1] == 2 or board[row-1, col+1] == 4):
            moves.append((row-2, col+2))

    #Player 2 King
    elif player == 2 and board[row, col] == 4:
        #up left
        if col > 0 and row - 1 > 0 and board[row-1, col-1] == 0 and not jumpOnly:
            moves.append((row-1, col-1))

        #up right
        if col < 7 and row - 1 > 0 and board[row-1, col+1] == 0 and not jumpOnly:
            moves.append((row-1, col+1))

        #down left
        if col > 0 and row + 1 < 8 and board[row+1, col-1] == 0 and not jumpOnly:
            moves.append((row+1, col-1))

        #down right
        if col < 6 and row + 1 < 8 and board[row+1, col+1] == 0 and not jumpOnly:
            moves.append((row+1, col+1))

        #jump up left
        if col > 1 and (row - 2) >= 0 and board[row-2, col-2] == 0 and \
                                (board[row-1, col-1] == 1 or board[row-1, col-1] == 3):
            moves.append((row-2, col-2))

        #jump up right
        if col < 6 and (row - 2) >= 0 and board[row-2, col+2] == 0 and \
                                (board[row-1, col+1] == 1 or board[row-1, col+1] == 3):
            moves.append((row-2, col-2))

        #jump down left
        if col > 1 and (row + 2) < 8 and board[row+2, col-2] == 0 and \
                                (board[row+1, col-1] == 1 or board[row+1, col-1] == 3):
            moves.append((row+2, col-2))

        #jump down right
        if col < 6 and (row + 2) < 8 and board[row+2, col+2] == 0 and \
                                (board[row+1, col+1] == 1 or board[row+1, col+1] == 3):
            moves.append((row+2, col+2))

    return moves


def picksquare(row, col, event):
    global pick1
    global board
    global player
    global chatter
    global moves
    global noPick1
    gameover = False

    if player == 0:
        if (board[row, col] in (1,2)):
            player = board[row, col]
        else:
            chatter.config(text='Player 0 again ...')
            return
    
    #print('User selected:', row, col)
    if (row % 2 + col) % 2:
        chatter.config(text='Invalid Move')
        return
    if pick1 is None:
        if board[row, col] in (player, player + 2):
            outlineSquare(row, col, 1)
            pick1 = (row, col)
            if checkWin(player) != True:
                chatter.config(text='Player ' + str(player) + ' : Select square to move to')
            moves = validMoves(row, col, player)
            for move in moves:
                outlineSquare(move[0], move[1], 2)
    else:
        #print('pick2 : selected', row, col)
        if board[row, col] in (player, player + 2):
            if noPick1:
                return
            #print('player picked another piece')
            for move in moves:
                outlineSquare(move[0], move[1], 0)
            outlineSquare(pick1[0], pick1[1], 0)
            pick1 = None
            return picksquare(row, col, None)
        else:
            #Check if (row, col) is in moves
            if (row, col) in moves:
                for move in moves:
                    outlineSquare(move[0], move[1], 0)
                outlineSquare(pick1[0], pick1[1], 0)
                piece(pick1[0], pick1[1])
                if row == 0 and player == 2:
                    piece(row, col, player, 'king')
                    board[row, col] = 4
                    board[pick1[0], pick1[1]] = 0
                elif row == 7 and player == 1:
                    piece(row, col, player, 'king')
                    board[row, col] = 3
                    board[pick1[0], pick1[1]] = 0
                else:
                    if board[pick1[0], pick1[1]] == 3:
                        piece(row, col, player, 'king')
                        board[pick1[0], pick1[1]] = 0
                        board[row, col] = 3
                    elif board[pick1[0], pick1[1]] == 4:
                        piece(row, col, player, 'king')
                        board[pick1[0], pick1[1]] = 0
                        board[row, col] = 4
                    else:
                        piece(row, col, player)
                        board[pick1[0], pick1[1]] = 0
                        board[row, col] = player

                #print('is jump', row, col, pick1[0], pick1[1])
                #if jump
                if abs(col - pick1[1]) == 2:
                    kill = ((row+pick1[0])//2, (col+pick1[1])//2)
                    board[kill[0], kill[1]] = 0
                    piece(kill[0], kill[1])
                    for move in moves:
                        outlineSquare(move[0], move[1], 0)
                    moves = validMoves(row, col, player, jumpOnly=True)
                    if len(moves) > 0:
                        for move in moves:
                            outlineSquare(move[0], move[1], 2)
                        pick1 = (row, col)
                        noPick1 = True
                        return picksquare(row, col, None)
                    else:
                        noPick1 = False
                player = 2 if player == 1 else 1
                gameover = checkWin(player)
                if gameover and player == 2:
                    chatter.config(text='Game Over! Player ' + str(1) + ' wins!')
                    return
                elif gameover and player == 1:
                    chatter.config(text='Game over! Player ' + str(2) + ' wins!')
                pick1 = None
                chatter.config(text='Player ' + str(player) + ' : Select square to move to')

square = defaultdict(list)
frame = Frame(root)
frame2 = Frame(frame)
frame2.grid()
for row in range(8):
    for col in range(8):
        square[row].append(Canvas(frame2, height=100/2, width=100/2, \
                                  bg='red' if (row % 2 + col) % 2 else 'black'))
        square[row][col].grid(row=row, column=col)
        square[row][col].bind('<Button-1>',
                              functools.partial(picksquare, row, col))
frame2.pack(fill=X)

chatter = Label(frame, text='Chatter ...')
chatter.pack(fill=X)
frame.pack(fill=X)

chatter.config(text='Player 1 : Select checker to move')
piece(0, 0, 1)
piece(0, 2, 1)
piece(0, 4, 1)
piece(0, 6, 1)
piece(1, 1, 1)
piece(1, 3, 1)
piece(1, 5, 1)
piece(1, 7, 1)
piece(2, 0, 1)
#piece(2, 2, 1, 'king')
piece(2, 2, 1)
piece(2, 4, 1)
piece(2, 6, 1)

piece(5, 1, 2)
piece(5, 3, 2)
piece(5, 5, 2)
piece(5, 7, 2)
piece(6, 0, 2)
piece(6, 2, 2)
piece(6, 4, 2)
piece(6, 6, 2)
piece(7, 1, 2)
piece(7, 3, 2)
piece(7, 5, 2)
piece(7, 7, 2)

#piece(3, 1, 1, 'king')
#piece(4, 2, 2, 'king')

mainloop()
