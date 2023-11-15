# logic.py
import random

class Game:
    def __init__(self):
        self.setup_game()

    def setup_game(self):
        symbols = ['X', 'O']
        random.shuffle(symbols)

        while True:
            num_of_players = input("Enter the number of players (1/2): ")
            if num_of_players in ['1', '2']:
                break
            else:
                print("Invalid input. Please enter '1' or '2'.")

        if num_of_players == '1':
            self.player1, self.player2 = Player(symbols[0]), Bot(symbols[1])
        else:
            self.player1, self.player2 = Player(symbols[0]), Player(symbols[1])

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

        self.show_result()

    def show_result(self):
        self.board.print_board()
        winner = self.board.get_winner()

        if winner:
            print(winner, 'Won')
        elif self.board.is_draw():
            print("It's a draw.")
