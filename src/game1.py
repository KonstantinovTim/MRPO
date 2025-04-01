import math
import random


def calculate_lcm(a: int, b: int, c: int) -> int:
    """Calculate the least common multiple of three numbers."""
    lcm_ab = (a * b) // math.gcd(a, b)
    return (lcm_ab * c) // math.gcd(lcm_ab, c)


def generate_numbers() -> tuple[int, int, int]:
    """Generate three random numbers from 1 to 100."""
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    c = random.randint(1, 100)
    return a, b, c


def play_lcm_game() -> None:
    """Play the least common multiple game."""
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the smallest common multiple of given numbers.')

    correct_answers_needed = 3
    correct_answers = 0

    while correct_answers < correct_answers_needed:
        a, b, c = generate_numbers()
        correct_lcm = calculate_lcm(a, b, c)

        print(f'Question: {a} {b} {c}')
        user_answer = input('Your answer: ')

        try:
            user_answer = int(user_answer)
        except ValueError:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_lcm}'.")
            print(f"Let's try again, {name}!")
            return

        if user_answer == correct_lcm:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_lcm}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
