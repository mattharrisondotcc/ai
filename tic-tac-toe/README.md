# tic-tac-toe

This is a simple CLI tic-tac-toe game I implemented one afternoon in Python3.

Currently it is just a Player X vs Player O game between two users, but I plan
on implementing AI strategies so it can be both a human-vs-human and
human-vs-bot game.

For a creative constraint, I imagined the game "board" as a vector and stored 
as a "bit array" in an integer. Two digit fields correspond to each board 
space, where values 00 = unused, 01 = X, and 10 = O.

Each move tests user input with bitwise operations to validate the move, and 
then again used bitwise operators to test the board against winning 
configurations after each move. The users can quit by entering 'q' or 'quit' 
any time.
