import copy
from treelib import Node, Tree
import time

X = "x"
O = "o"
EMPTY = " "
tie = False

nr_vertices = 25
v_label = list(map(str, range(nr_vertices)))
gametree = Tree()

class Tile:
    def __init__(self, x, y):
        self.value = EMPTY
        self.x = x
        self.y = y
    def val(self):
        return self.value
    def place(self, value):
        if self.val() == EMPTY:
            self.value = value
    def can_place(self):
        if self.val() == EMPTY:
            return True
        return False
    def pos(self):
        return (self.x, self.y)

class Set:
    def __init__(self, a, b, c):
        self.lst = [a, b, c]
    def is_full(self):
        if (self.lst[0].val() == self.lst[1].val() ==self.lst[2].val()):
            return self.lst[0].val()
        else:
            return EMPTY
    def val(self, piece):
        c = 0
        for x in self.lst:
            if x.val() == piece:
                c += 1
        return c
    def can_place(self):
        for x in self.lst:
            if x.can_place():
                return True
        return False
    def open_tile(self):
        for x in self.lst:
            if x.val() == EMPTY:
                return x
    def blocked(self, val):
        opp = None
        if val == X:
            opp = O
        elif val == X:
            opp = X
        for x in self.lst:
            if x.val() == opp:
                return True
        return False
    
class Board:
    def __init__(self, lst):
        self.lst = lst
    def getBoard(self):
        return self.lst
    def __str__(self):
        return boardString(self.lst)
    def copy(self):
        return copy.deepcopy(self)

class Game:
    def __init__(self, lst):
        self.lst = lst

class Node:
    def __init__(self, board, lst):
        self.board = board
        self.lst = lst
    def ln(self):
        return len(self.lst)
    def set(self, x):
        self.lst = x
    def copyBoard(self):
        return copy.deepcopy(self.board)
    def __str__(self):
        return boardString(self.board.getBoard())

EMPTY_BOARD = Board([[Tile(1, 1), Tile(1, 2), Tile(1, 3)], 
                     [Tile(2, 1), Tile(2, 2), Tile(2, 3)], 
                     [Tile(3, 1), Tile(3, 2), Tile(3, 3)]])

def solution_set(board): 
    return [Set(board[0][0], board[0][1], board[0][2]), 
            Set(board[1][0], board[1][1], board[1][2]),
            Set(board[2][0], board[2][1], board[2][2]),
            Set(board[0][0], board[1][0], board[2][0]),
            Set(board[0][1], board[1][1], board[2][1]),
            Set(board[0][2], board[1][2], board[2][2]),
            Set(board[0][0], board[1][1], board[2][2]),
            Set(board[0][2], board[1][1], board[2][0])]

def gameSolved(board):
    for x in solution_set(board):
        if (x.is_full() != EMPTY):
            return x.is_full()
    return EMPTY

def printBoard(board):
    #string = "   1  2  3\n"
    for i in range(3):
        for j in range(3):
            string += (f"[{board[i][j].val()}]")
        string += "\n"
    return

def boardString(board):
    string = ""
    for i in range(3):
        for j in range(3):
            if board[i][j].val() == EMPTY:
                string += "#"
            else:
                string += board[i][j].val()
    return string

def place(board, piece, x, y):
    board.lst[x-1][y-1].place(piece)

# simpleGen is used to propagate subtrees by excluding the recursion code of recursiveGen
def simpleGen(node, piece):
    if (gameSolved(node.board.getBoard()) == EMPTY):
        for i in range(1, 4):
            for j in range(1, 4):
                if (node.board.lst[i-1][j-1].can_place()):
                    x = node.copyBoard()
                    place(x, piece, i, j)
                    n = Node(x, [])
                    node.lst.append(n)
                    gametree.create_node(str(n), n, node)

def recursiveGen(node, piece):
    if piece == X:
        other_piece = O
    elif piece == O:
        other_piece = X

    if (gameSolved(node.board.getBoard()) == EMPTY):
        for i in range(1, 4):
            for j in range(1, 4):
                if (node.board.lst[i-1][j-1].can_place()):
                    x = node.copyBoard()
                    place(x, piece, i, j)
                    n = Node(x, [])
                    node.lst.append(n)
                    gametree.create_node(str(n), n, node)
                    #gametree.edge(node, n)
                    
    for n in node.lst:
        recursiveGen(n, other_piece)

print(f"[{time.ctime()}]: program start")
empty_node = Node(EMPTY_BOARD, [])
gametree.create_node(empty_node, empty_node)
print(f"[{time.ctime()}]: base node and tree created")
print(f"[{time.ctime()}]: start recursive search")
recursiveGen(empty_node, X)
print(f"[{time.ctime()}]: recursive search completed")
print(f"[{time.ctime()}]: plot tree")
gametree.save2file('tree.txt')
print(f"[{time.ctime()}]: done")
