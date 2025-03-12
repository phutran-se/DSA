"""
GCD.py - Function to find the Greatest Common Denominator

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
"""

from Utils import *

def gcd_iterative(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) of two numbers using the iterative method.
    (Euclidean Algorithm)

    Parameters:
        a (int): The first integer.
        b (int): The second integer.
    Returns:
        int: The GCD of the two integers.
    
    Raises: 
        TypeError: If a or b is not an integer type.
        ValueError: If a and b are zeros.
    """
    # Type checking
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Inputs must be integers")
    
    if a == 0 and b == 0: 
        raise ValueError("Invalid input for (0,0)") 

    x = abs(a)
    y = abs(b)

    if x == 0:
        return y
    if y == 0:
        return x
    
    while y: 
        x, y = y, (x % y)

    return x

def gcd_recursive(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) of two numbers using the recursive method.
    (Euclidean Algorithm)

    Parameters:
        a (int): The first integer.
        b (int): The second integer.
    Returns:
        int: The GCD of the two integers.
    
    Raises: 
        TypeError: If a or b is not an integer type.
        ValueError: If a and b are zeros.
    """
    # Type checking
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Inputs must be integers")
    
    if a == 0 and b == 0: 
        raise ValueError("Invalid input for (0,0)") 
    
    x = abs(a)
    y = abs(b)

    if x == 0:
        return y
    if y == 0:
        return x
    
    return gcd_recursive(y, x % y)

# Test GCD
print("*** Simple Test for GCD Functions ***")
for (a,b) in [(10,15), (4,8), (20, 25), (12, 6)]:
    try: 
        print_info(f"> GCD (Iterative) of {a} and {b}: ",  gcd_iterative(a,b))
        print_info(f"> GCD (Recursive) of {a} and {b}: ",  gcd_recursive(a,b))
        print()
    except Exception as e: 
        print(f"ERROR: {e}")

# Function to test from user intput
def test_gcd(): 
    Stop = False
    while not Stop: 
        print("Enter 2 number to find GCD or 'exit' to stop")
        sa = input("Enter first number (a=): ").strip()
        sb = ''
        if sa == 'exit': 
            print_error("Test stopped")
            Stop = True
        else: 
            sb = input("Enter second number (b=): ").strip()
            if sb == 'exit': 
                print_error("Test stopped")
                Stop = True
            else: 
                if not is_an_integer(sa) or not is_an_integer(sb):
                    print_error(f"Expected an interger but input is not an interger type")
                else:
                    try: 
                        a = int(sa)
                        b = int(sb)
                        r1 = gcd_iterative(a, b)
                        r2 = gcd_recursive(a, b)

                        print_info(f"> GCD (Iterative) of {a} and {b}: ",  r1)
                        print_info(f"> GCD (Recursive) of {a} and {b}: ",  r2)
                        print()
                    except Exception as e: 
                        print_error(f"ERROR: {e}")

# Call test
test_gcd()