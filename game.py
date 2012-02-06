import os
import random
from time import sleep

SIZE = 50

def display_char(x):
    if x == 0:
        return " "
    elif x == 1:
        return "X"
    else:
        raise ValueError
    
def display(board):
    os.system('clear')
    for line in board:
        print " ".join([display_char(d) for d in line])

def neighbours(x, y):
    neighbours = [(x-1, y-1),
                  (x-1, y),
                  (x-1, y+1),
                  (x, y-1),
                  (x, y+1),
                  (x+1, y-1),
                  (x+1, y),
                  (x+1, y+1)]
    neighbours = [(x1, y1) for (x1, y1) in neighbours if x1 >= 0 and x1 < SIZE
                                                     and y1 >= 0 and y1 < SIZE]
    return neighbours

def alive_neighbours(x, y, board):
    return sum(board[y1][x1] for x1, y1 in neighbours(x, y))

def next_value(x, y, board):
    friends = alive_neighbours(x, y, board)
    if board[y][x] == 1:
        if friends < 2:
            return 0
        if friends in [2,3]:
            return 1
        if friends > 3:
            return 0
    else:
        if friends == 3:
            return 1
        else:
            return 0

def next_board(board):
    return [[next_value(x, y, board) for x in range(SIZE)] for y in range(SIZE)]


def loop(board):
    while True:
        display(board)
        sleep(0.1)
        board = next_board(board)
        
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        board = [[random.choice([0, 1]) for x in range(SIZE)] for y in
                range(SIZE)]
    else:
        f = open(sys.argv[1])
        board = [[int(s) for s in line.strip()] for line in f.readlines()]
        f.close()

    SIZE = len(board)

    try:
        loop(board)
    except KeyboardInterrupt:
        os.system('clear')
