#!/usr/bin/env python3

class Board():
    def __init__(self, board=int('000000000000000000', 2)):
        self.board = board
        self.signs = {0: ' ', 1: 'X', 2: 'O'}
        self.X = 1
        self.O = 2
        self.o_wins = [
            int('101010000000000000', 2),
            int('000000101010000000', 2),
            int('000000000000101010', 2),
            int('100000100000100000', 2),
            int('001000001000001000', 2),
            int('000010000010000010', 2),
            int('100000001000000010', 2),
            int('000010001000100000', 2),
            ]
        self.x_wins = [
            int('010101000000000000', 2),
            int('000000010101000000', 2),
            int('000000000000010101', 2),
            int('010000010000010000', 2),
            int('000100000100000100', 2),
            int('000001000001000001', 2),
            int('010000000100000001', 2),
            int('000001000100010000', 2),
            ]
        self.x_is_next = True
        print()
        print('New Tic-Tac-Toe Game')
        print()
        print('Type q or quit to exit the game early.')
        print()
        self.draw_board()

    def switch_turn(self):
        self.x_is_next = not self.x_is_next

    def play_x(self):
        print('Player X, next move:')
        if not self.x_is_next:
            # this def needs to be improved...
            raise ValueError
        # player makes move
        row, col = self.get_user_move()
        self.update_board_x(row, col)
        self.switch_turn()
        if self.did_x_win():
            exit(0)

    def play_o(self):
        print('Player O, next move:')
        if self.x_is_next:
            # this def needs to be improved...
            raise ValueError
        # player makes move
        row, col = self.get_user_move()
        self.update_board_o(row, col)
        self.switch_turn()
        if self.did_o_win():
            exit(0)

    def get_user_move(self):
        row, col = None, None
        while not self.is_move_valid(row, col):
            while row is not '0' and row is not '1' and row is not '2':
                row = input('Which row? 0 < row < 2\n')
                if row.lower() == 'quit' or row.lower() == 'q':
                    self.quit_game()
            while col is not '0' and col is not '1' and col is not '2':
                col = input('Which col? 0 < col < 2\n')
                if col.lower() == 'quit' or col.lower() == 'q':
                    self.quit_game()
            row = int(row)
            col = int(col)
        return row, col

    def is_move_valid(self, row, col):
        if not isinstance(row, int) or not isinstance(col, int):
            return False
        position = (3 << self.calculate_shift(row, col))
        if self.board & position:
            print('That space is taken, try again.')
            return False
        else:
            return True

    def calculate_shift(self, row, col):
        return ((3 * row) + col) * 2

    def update_board_x(self, row, col):
        shift = self.calculate_shift(row, col)
        position = self.X << shift
        self.board |= position

    def update_board_o(self, row, col):
        shift = self.calculate_shift(row, col)
        position = self.O << shift
        self.board |= position

    def did_o_win(self):
        for win_board in self.o_wins:
            if win_board == self.board & win_board:
                print()
                print('O Wins!')
                return True
        return False

    def did_x_win(self):
        for win_board in self.x_wins:
            if win_board == self.board & win_board:
                self.draw_board()
                print()
                print('X Wins!')
                return True
        return False

    def draw_board(self):
        output = self.board
        ttt = []
        bar = '  ------------- '
        sep = f' |\n{bar}\n'
        print()
        print('    0   1   2')
        print(bar)
        for row in range(3):
            ttt.append(str(row))
            for col in range(3):
                ttt.append(' | ')
                ttt.append(self.signs[output & 3])
                output >>= 2
            ttt.append(sep)
        print(''.join(ttt))

    def run_game(self):
        moves = 0
        while moves < 9:
            if self.x_is_next:
                self.play_x()
            else:
                self.play_o()
            print()
            print('Next Turn')
            moves += 1
            self.draw_board()
        print('''It's a tie!''')

    def quit_game(self):
        print()
        print('Thank you for playing, now quitting...')
        print()
        exit(0)

def main():
    print('This is the tic-tac-toe board class file. It is imported, not run.')

if __name__ == '__main__':
    main()
    print('End of program.')
