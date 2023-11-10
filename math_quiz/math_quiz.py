import random


def rand_int(min, max):
    """
    Gives a random integer between two numbers 
    Args:
        min (int): the minimum number
        max(int): The maximum number
    Retruns :
        Returns a Random integer.
    """
    min = int(min)
    max = int(max)
    return random.randint(min, max)


def random_operator():
    """
    Gives a random operator
    Args:
    Retruns :
        Returns a Random operator
    """
    return random.choice(['+', '-', '*'])


def operation(num1, num2, operator):
    """
    Gives the result of an operation according to 
    given operator
    Args:
        num1(int): First number to perform the operation 
        num2(int): second number to perform the operation
        operator(char): the operator
    Retruns :
        Returns the result of the operatoion 
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+': ans = num1 + num2
    elif operator == '-': ans = num1 - num2
    else: ans = num1 * num2
    return problem, ans

def math_quiz():
    """
    Driver function which calls all the other functions
    Args:
    Retruns :
        prints the score of the user
    """
    score = 0
    total_ques = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    try:
        for i in range(total_ques):
            num1 = rand_int(1, 10)
            num2 = rand_int(1, 5.5)
            operator = random_operator()

            PROBLEM, ANSWER = operation(num1, num2, operator) # gives the overall answer and the problem statement
            print(f"\nQuestion: {PROBLEM}")
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)

            if useranswer == ANSWER:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {ANSWER}.")

        print(f"\nGame over! Your score is: {score}/{total_ques}")
    except ValueError:
        print("The input must be a integer")

if __name__ == "__main__":
    math_quiz()
