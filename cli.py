# cli.py
import random

from logic import Board, Player, Bot, Game

if __name__ == '__main__':
    while True:
        game = Game()
        game.play()
        while True:
            play_again = input('Do you want to play again? (Y/N): ')
            if play_again.upper() == 'Y':
                break
            elif play_again.upper() == 'N':
                exit()
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")
