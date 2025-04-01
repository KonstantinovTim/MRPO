from src.game1 import play_lcm_game
from src.game2 import play_progression_game


def main() -> None:
    print('Welcome to Brain Games!')
    print('Available games:')
    print('1. Least Common Multiple (LCM)')
    print('2. Geometric Progression')

    choice = input('Choose a game (1 or 2): ')

    if choice == '1':
        play_lcm_game()
    elif choice == '2':
        play_progression_game()
    else:
        print('Invalid choice. Please select 1 or 2.')

if __name__ == '__main__':
    main()
