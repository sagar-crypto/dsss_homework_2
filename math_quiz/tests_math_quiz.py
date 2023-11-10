import unittest
from math_quiz import rand_int, random_operator, operation


class TestMathGame(unittest.TestCase):

    def test_rand_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = rand_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_random_operator(self):
        operators = {'+','-','*'}
        result = random_operator()
        self.assertIn(result,operators)

    def test_function_operations(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 3, '-', '5 - 3', 2),
                (6, 4, '*', '6 * 4', 24)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                Problem, Result = operation(num1, num2, operator)
                self.assertEqual(Problem, expected_problem)
                self.assertEqual(Result, expected_answer)

if __name__ == "__main__":
    unittest.main()
