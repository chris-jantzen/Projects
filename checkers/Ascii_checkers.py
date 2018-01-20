from random import randint


def printBoard(board):
    print(" _________________________________" + '\n')
    x = 0
    y = 0
    print('| ', end = '')
    for i in game_board:
        print(i + ' | ', end = '')
        x += 1
        if x == 8:
            x = 0
            y += 1
            if y != 8:
                print('\n' + " _________________________________" + '\n' + '| ', end='')
            else:
                print('\n' + " _________________________________" + '\n', end='')


def initializeBoard(p1, p2):
    board = ['_', p2, '_', p2, '_', p2, '_', p2,
             p2, '_', p2, '_', p2, '_', p2, '_',
             '_', p2, '_', p2, '_', p2, '_', p2,
             '_', '_', '_', '_', '_', '_', '_', '_',
             '_', '_', '_', '_', '_', '_', '_', '_',
             p1, '_', p1, '_', p1, '_', p1, '_',
             '_', p1, '_', p1, '_', p1, '_', p1,
             p1, '_', p1, '_', p1, '_', p1, '_']
    return board


def random(min, max):
    return randint(min,max)

p1 = input('Player 1 game piece: ')
p2 = input('Player 2 game piece: ')

win = False
p1turn = True

game_board = initializeBoard(p1,p2)
printBoard(game_board)

firstTurn = input('\nEnter the player that should go first (1 or 2), or 3 for random:')
while True:
    if firstTurn is '1' or firstTurn is '2':
        break
    elif firstTurn is '3':
        firstTurn = random(1,2)
        print(firstTurn)
        break
    else:
        firstTurn = input('Enter the player that should go first (1 or 2), or 3 for random:')
    print(breakout)
    print(firstTurn)
#print(firstTurn)

'''while win == False:
    pass'''
