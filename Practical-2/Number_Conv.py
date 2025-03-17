"""
Number_Conv.py - Function for number converstions

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
"""

from Utils import *

def decimal_to_baseX_iterative(n, base):
    """
    Convert a decimal number to a base-X (2-16) number using the iterative method.

    Parameters:
        n (int): The decimal number to convert.
        base (int): The base to convert to (2-16).

    Returns:
        str: The base-X number as a string.

    Raises:
        TypeError: If inputs are not integers.
        ValueError: If base is not between 2 and 16, or if n is negative.
    """

    if not (isinstance(n, int) and isinstance(base, int)):
        raise TypeError("Expected an integer but input is not an integer")
    if base < 2 or base > 16:
        raise ValueError(f"Base must be between 2 and 16, base {base} is invalid")
    if n < 0:
        raise ValueError(f"Number must be positive, number {n} is invalid")

    if n == 0:
        return "0" # Return 0 if n is 0
    
    digits = "0123456789ABCDEF" # Digits for base 16

    result = ""
    while n:
        r = n // base
        m = n % base
        result = digits[m] + result # Add the remainder to the result
        n = r # Update the number to the quotient

    return result

def decimal_to_baseX_recursive(n, base):
    """
    Convert a decimal number to a base-X (2-6) number using the recursive method.

    Parameters:
        n (int): The decimal number to convert.
        base (int): The base to convert to.

    Returns:
        str: The base-X number as a string.
    Raises:
        TypeError: If inputs are not integers.
        ValueError: If base is not between 2 and 16, or if n is negative.
    """

    if not (isinstance(n, int) and isinstance(base, int)):
        raise TypeError(f"Expected an integer but input is not an integer")
    if base < 2 or base > 16:
        raise ValueError(f"Base must be between 2 and 16, base {base} is invalid")
    if n < 0:
         raise ValueError(f"Number must be positive, number {n} is invalid")

    if n == 0: 
        return ""
    digits = "0123456789ABCDEF"

    if n < base: 
        return digits[n] # Return the digit if n is less than the base

    r = n // base
    m = n % base
    return decimal_to_baseX_recursive(r, base) + digits[m] #  Recursively call the function with the quotient and add the remainder to the result

# Test for decimal_to_baseX Functions
print("*** Simple Test for Number Conversion Functions ***")
# Base 2
vals =  [6, 16, 33, 192, 255, -50]
bases = [2, 8, 10, 16, 20, 0]

for n in vals:
    for base in bases:
        # Try catch block to handle exceptions
        try :
            print(f"> Convert {n} to base-{base} (Iterative) = ", decimal_to_baseX_iterative(n, base))
            print(f"> Convert {n} to base-{base} (Recursive) = ", decimal_to_baseX_recursive(n, base))
        except Exception as e:
            print_error(f"ERROR: {e}")
    print("----")


# Function to test from user input
def test_convert_num():
    Stop = False
    while not Stop: 
        print("Enter a number and a base to convert or 'exit' to stop")
        sn = input("Enter a number (n=): ").strip()
        if sn == 'exit': 
            print_error("Test stopped")
            Stop = True
        else: 
            sb = input("Enter a base value (b=): ").strip()
            if sb == 'exit': 
                print_error("Test stopped")
                Stop = True
            else: 
                if not is_an_integer(sn) or not is_an_integer(sb):
                    print_error(f"Expected an interger but inputs (n={sn}, base={sb}) are not an interger")
                else:
                    try: 
                        n = int(sn)
                        base = int(sb)
                        r1 = decimal_to_baseX_iterative(n, base)
                        r2 = decimal_to_baseX_recursive(n, base)

                        print_info(f"> Convert (Iterative) {n} to base-{base}: ",  r1)
                        print_info(f"> Convert (Recursive) {n} to base-{base}: ",  r2)

                    except Exception as e: 
                        print_error(f"ERROR: {e}")


# Call test
test_convert_num()


