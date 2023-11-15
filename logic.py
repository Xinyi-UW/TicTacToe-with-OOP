# logic.py
import random

class Game:
    def __init__(self):
        symbols = ['X', 'O']
        random.shuffle(symbols)

        num_of_players = None
        while num_of_players not in ['1', '2']:
            num_of_players = input("Enter the number of players (1/2): ")

        if num_of_players == '1':
            self.player1 = Player(symbols[0])
            self.player2 = Bot(symbols[1])
        elif num_of_players == '2':
            self.player1 = Player(symbols[0])
            self.player2 = Player(symbols[1])

        self.board = Board()
        self.current_player = self.player1

    def play(self):
        while not self.board.get_winner() and not self.board.is_draw():
            self.board.print_board()
            print('Next turn: ', self.current_player.symbol)
            x, y = self.current_player.make_move(self.board.board)
            if x == 'q' and y == 'q':
                print("Game exited by the player.")
                break
            self.board.board[x][y] = self.current_player.symbol
            self.current_player = self.player1 if self.current_player == self.player2 else self.player2

        winner = self.board.get_winner()

        self.board.print_board()

        if winner:
            print(winner, ' Won')
        elif self.board.is_draw():
            print("It's a draw.")



class Board:
    def __init__(self):
        self.board = [[None, None, None], [None, None, None], [None, None, None]]

    def print_board(self):
        for row in self.board:
            print(row)

    def get_winner(self):
        for i in range(0, 3):
            if self.board[i][0] is not None and self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return self.board[i][0]
            if self.board[0][i] is not None and self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return self.board[0][i]
        if self.board[1][1] is not None and (self.board[0][0] == self.board[1][1] == self.board[2][2] or self.board[2][0] == self.board[1][1] == self.board[0][2]):
            return self.board[1][1]
        return None

    def is_draw(self):
        for row in self.board:
            if None in row:
                return False
        return True


class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self, board):
        while True:
            move = input("input row and col (0-2) separated by space or 'q' to quit: ")
            if move.lower() == 'q':
                return 'q', 'q'
            try:
                x, y = map(int, move.split())
                if 0 <= x <= 2 and 0 <= y <= 2 and board[x][y] is None:
                    return x, y
                else:
                    print('Invalid input, please try again.')
            except ValueError:
                print('Invalid input, please try again.')


class Bot(Player):
    def make_move(self, board):
        while True:
            x, y = random.randint(0, 2), random.randint(0, 2)
            if board[x][y] is None:
                return x, y
