"""
main.py - Entry point for the program

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
"""

import sys
from Funct import print_error, print_info
from EquationSolver import solve_expression

def test_solve_expr(expression, preprocess_exp=False):
    """
    Test the solve_expression function with the given expression

    Args:
        expression (str): The expression to be solved
        preprocess_exp (bool, optional): Whether to preprocess the expression. Defaults to False.
    """
    
    try:
        result = solve_expression(expression, preprocess_exp)
        print_info(f"> Result: {result}\n")
    except Exception as e:
        print_error(f"> ERROR on expression: \"{expression}\"\n\tReason: {e}\n")

# Example Test
if __name__ == "__main__":

    # Check if the -p flag is present for preprocessing
    preprocess_exp = '-p' in sys.argv

    # Test with simple expression
    test_solve_expr("10 + 5", preprocess_exp)

    # Test with simple expression
    test_solve_expr("10 + 5 * 2", preprocess_exp)

    # Test with simple expression with brackets without spaces
    test_solve_expr("10 + (5*2)", preprocess_exp)

    # Test with long expression with brackets
    test_solve_expr("12 + ( 7 * 2 + 4 - 10 + 1 ) - ( 12 / 4 ) + 5", preprocess_exp)

    # Test with invalid expression (division by zero)
    test_solve_expr("12 + 7 * 4 / 0", preprocess_exp)

    # Test with invalid expression (missing closing bracket)
    test_solve_expr("12 + 7 * ( 4 -")

    # Loop to test 
    Stop = False
    while not Stop:
        expression = input("Enter the expression or 'exit' to stop: ").strip()
        if expression == 'exit': 
            print_error("Test stopped")
            Stop = True
        else: 
            test_solve_expr(expression, preprocess_exp)
        print()

