"""
Factorial.py - Functions for Factorial Calculation

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
"""

from Utils import *

def factorical_iterative(n): 
    """
    Calculate factorial of a number using iteration.
    
    Parameters:
        n (int): The non-negative integer to calculate factorial for.
        
    Returns:
        int: The factorial of n (n!).
        
    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.
    """

    # Type checking
    if not isinstance(n, int):
        raise TypeError(f"Expected an interger but '{n}' is not an interger type") 
    
    # Support ?
    if n < 0: 
        raise ValueError("Factorical does not support for negative numbers")
    
    accum = 1 # store the result
    for i in range(1, n + 1):
        accum *= i
    return accum

def factorical_recursive(n):
    """
    Calculate factorial of a number using recursion.
    
    Parameters:
        n (int): The non-negative integer to calculate factorial for.
        
    Returns:
        int: The factorial of n (n!).
        
    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.
    """
    
    # Type checking
    if not isinstance(n, int):
        raise TypeError(f"Expected an interger but '{n}' is not an interger type") 
    
    # Support ?
    if n < 0: 
        raise ValueError("Factorical does not support for negative numbers")
    
    # Condition for stop the function
    if n == 0 or n == 1: 
        return 1
    # Return the last multply with previous value
    return n * factorical_recursive(n - 1)
    
# Test for Factorial Function
print("*** Simple Test for Factorial Functions ***")

for val in [5, "6"]:
    try:
        print_info(f"> Factorial (Iterative) {val}! =",  factorical_iterative(val))
        print_info(f"> Factorial (Recursive) {val}! =",  factorical_recursive(val))
        print()
    except Exception as e: 
        print_error(f"ERROR: {e}")

# Function to test from user input
def test_factorial(): 
    Stop = False
    while not Stop: 
        s = input("Enter a number to calculate factorial or 'exit' to stop: ")
        s = s.strip()
        if s == 'exit': 
            print_error("Test stopped")
            Stop = True
        else: 
            if not is_an_integer(s):
                print_error(f"Expected an interger but '{s}' is not an interger type")
            else:
                try: 
                    n = int(s)
                    r1 = factorical_iterative(n)
                    r2 = factorical_recursive(n)
                    print_info(f"> Factorial (Iterative) {n}! =",  r1)
                    print_info(f"> Factorial (Recursive) {n}! =",  r2)
                    print()
                except Exception as e: 
                    print_error(f"ERROR: {e}")

# Call test
test_factorial()