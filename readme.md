'tictactoe-tree' about page
@IvanoMaker

This program is designed to brute-force find all possible moves and games in 'tic-tac-toe'.

Tic-tac-toe is an MNK game played on a 3x3 grid. It requires two players, which alternate turns throughout the game. Each player places a mark on 
the board, typically an X or an O, claiming that space.
Players can not place on already occupied squares. A player wins when they have 3 of their marks in a row, horizontal, vertical, or diagonal. 
A game can end in a tie if neither player has 3 of their marks in a row and the gameboard is full.

This game uses a linked-list data structure to find all the moves. Each board state (called a node in the code) has two fields, 
a 'board' instance with all the board data, and a list (initially empty) which
is populated with the possible moves which can be placed on that board situation.

All of the game states are represented in a simple Unix text based tree, where each row contains a unique gamestate. 
The gamestate is represented as a 9 length string with each element being either an x, o, or #. The string should be read
from left to right, with each 3 bits being their respective row and the elements there. a # means that position is empty.

i.e. o#xxx#oxo is the stored state of
[O][ ][X]  ->  o#x
[X][X][ ]  ->  xx#
[O][X][O]  ->  oxo

Example of the tree structure:

├── o#x#x##xo
│   ├── o#x#x#oxo
│   │   ├── o#x#xxoxo
│   │   │   ├── o#xoxxoxo
│   │   │   └── oox#xxoxo
│   │   │       └── ooxxxxoxo
│   │   ├── o#xxx#oxo
│   │   │   ├── o#xxxooxo
│   │   │   │   └── oxxxxooxo
│   │   │   └── ooxxx#oxo
│   │   │       └── ooxxxxoxo

According to this program, there are 549,945 possible board situations in tic-tac-toe
(Length of file) - (1 from the starting state) = 549,946 - 1 = 549,945

The output file is provided on the repository page, however, it has been split into two files (tree_1 and tree_2) 
with each respective half of the tree file in each one. The original output file is ~30.8 megabytes, which is too much to upload to Git Hub.
