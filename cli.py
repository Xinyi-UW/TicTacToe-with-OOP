# cli.py

from logic import Game

def main():
    while True:
        game = Game()
        game.play()

        play_again = input('Do you want to play again? (Y/N): ').upper()
        while play_again not in ('Y', 'N'):
            print("Invalid input. Please enter 'Y' or 'N'.")
            play_again = input('Do you want to play again? (Y/N): ').upper()

        if play_again == 'N':
            exit()

if __name__ == '__main__':
    main()
