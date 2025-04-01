import random


def generate_geometric_progression() -> tuple[str, int]:
    """Generate a geometric progression with a hidden element."""
    start = random.randint(1, 5)
    step = random.randint(2, 5)
    length = random.randint(5, 10)

    progression: list[int] = [start * (step**i) for i in range(length)]
    hidden_pos = random.randint(0, length - 1)
    correct_answer = progression[hidden_pos]

    question_parts = []
    for i, num in enumerate(progression):
        question_parts.append('..' if i == hidden_pos else str(num))

    question = ' '.join(question_parts)
    return question, correct_answer


def play_progression_game() -> None:
    """Play the geometric progression game."""
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')

    correct_answers_needed = 3
    correct_answers = 0

    while correct_answers < correct_answers_needed:
        question, correct_answer = generate_geometric_progression()

        print(f'Question: {question}')
        user_answer = input('Your answer: ')

        try:
            user_answer = int(user_answer)
        except ValueError:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
