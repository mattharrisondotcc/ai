# tic-tac-toe

This is a simple CLI tic-tac-toe game I implemented one afternoon in Python3.

Currently it is just a Player X vs Player O game between two users, but I plan
on implementing AI strategies so it can be both a human-vs-human and
human-vs-bot game.

For a creative constraint, I imagined the game "board" as a vector and loosely
speaking stored it as a "bit array" in an integer. Two-bit fields correspond 
to each board space, where values 00 = unused, 01 = X, and 10 = O.

As an example, this board configuration:

XO_
__X
\_O_

would be a vector <1, 2, 0, 0, 0, 1, 0, 2, 0> stored as: 0b'011000000001001000'.

Each move tests user input with bitwise operations to validate the move, and 
then again used bitwise operators to test the board against winning 
configurations after each move. The users can quit by entering 'q' or 'quit' 
any time.
