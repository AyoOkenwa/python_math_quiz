import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    if operator == "+":
        answer = left + right
    elif operator == "-":
        answer = left - right
    else:
        answer = left * right

    expression = f"{left} {operator} {right}"
    return expression, answer


def run_quiz():
    incorrect = 0

    input("Press Enter to start!")
    print("----------------------")

    start_time = time.time()

    for question_number in range(1, TOTAL_PROBLEMS + 1):
        expression, answer = generate_problem()

        while True:
            guess = input(f"Problem #{question_number}: {expression} = ")

            if guess == str(answer):
                break

            incorrect += 1
            print("Incorrect, try again.")

    end_time = time.time()
    total_time = round(end_time - start_time, 2)
    correct = TOTAL_PROBLEMS

    print("----------------------")
    print("Quiz complete!")
    print(f"Score: {correct}/{TOTAL_PROBLEMS}")
    print(f"Incorrect attempts: {incorrect}")
    print(f"Time: {total_time} seconds")
    print("Nice work!")


if __name__ == "__main__":
    run_quiz()