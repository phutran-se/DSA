"""
main.py - Entry point for the program

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
"""


from Funct import print_error, print_info
from EquationSolver import solve_expression


def test_solve_expr(expression):
    try:
        result = solve_expression(expression)
        print_info("> Result: ", result)
    except Exception as e:
        print_error(f"ERROR on expression: \"{expression}\"\n\tReason: ", e)
    print()

# Example Test
if __name__ == "__main__":
    # Test with simple expression
    test_solve_expr("10 + 5")

    # Test with long expression
    test_solve_expr("12 + (7 * 2)") #( 4 - 10 + 1) - (12 / 4) + 5")

    # Test with invalid expression
    test_solve_expr("12 + 7 * ( 4 -")

    # Test with invalid expression
    test_solve_expr("12 + 7 * 4 / 0")

    exit(0)
    # Loop to test 
    Stop = False
    while not Stop:
        expression = input("Enter the expression or 'exit' to stop: ").strip()
        if expression == 'exit': 
            print_error("Test stopped")
            Stop = True
        else: 
            test_solve_expr(expression)
        print()

