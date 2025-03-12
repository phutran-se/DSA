"""
Fibonacci.py - Functions for Fibonacci

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
"""

from Utils import *

def fibonacci_iterative(n): 
    """
    Calculate the nth Fibonacci number using iteration.
    
    Args:
        n (int): The position in the Fibonacci sequence
        
    Returns:
        int: The nth Fibonacci number.
        
    Raises:
        ValueError: If n is non-positive.
    """
    if n <= 0: 
        raise ValueError("Fibonacci does not support for non-positive numbers")

    if n == 1 or n == 2: 
       return 1
   
    n1 = 1 # 1st 
    n2 = 1 # 2nd
    for _ in range(3, n + 1): 
        n1, n2 = n2, n1 + n2
    return n2

def fibonacci_iterative_list(n): 
    """
    Calculate the nth Fibonacci number using iteration.
    
    Args:
        n (int): The position in the Fibonacci sequence
        
    Returns:
        list: The list of Fibonacci numbers.
        
    Raises:
        ValueError: If n is non-positive.
    """
    if n <= 0: 
        raise ValueError("Fibonacci does not support for non-positive numbers")

    list = []
   
    n1 = 1 # 1st 
    n2 = 1 # 2nd
    for i in range(1, n + 1): 
        list.append(n1)
        n1, n2 = n2, n1 + n2
        
    return list

def fibonacci_recursive(n): 
    """
    Calculate the nth Fibonacci number using recursive.
    
    Args:
        n (int): The position in the Fibonacci sequence
        
    Returns:
        int: The nth Fibonacci number.
        
    Raises:
        ValueError: If n is non-positive.
    """
    if n <= 0: 
        raise ValueError("Fibonacci does not support for non-positive numbers")
    
    if n == 1 or n == 2: 
       return 1
    
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    
def fibonacci_recursive_list(n): 
    """
    Calculate the nth Fibonacci number using iteration.
    
    Args:
        n (int): The position in the Fibonacci sequence
        
    Returns:
        list: The list of Fibonacci numbers.
        
    Raises:
        ValueError: If n is non-positive.
    """
    if n <= 0: 
        raise ValueError("Fibonacci does not support for non-positive numbers")
   
    if n <= 0: 
        raise ValueError("Fibonacci does not support for non-positive numbers")
    if n == 1: 
        return [1]
    if n == 2: 
        return [1, 1]
    
    list = fibonacci_recursive_list(n-1)
    list.append(list[-1] + list[-2])
    return list

# Test for Factorial Function
print("*** Simple Test for Fibonacci Functions ***")
val = 5
print_info(f"> Fibonacci (Iterative) of {val}: ", fibonacci_iterative(val))
print_info(f"> Fibonacci (Recursive) of {val}: ", fibonacci_recursive(val))

print_info(f"> Fibonacci (Iterative) numbers of {val}: ", fibonacci_iterative_list(val))
print_info(f"> Fibonacci (Recursive) numbers of {val}: ", fibonacci_recursive_list(val))


def test_fibonacci(list_all=False): 
    Stop = False
    while not Stop: 
        s = input("Enter a number to calculate fibonacci or 'exit' to stop: ")
        s = s.strip()
        if s == 'exit': 
            print("Test stopped")
            Stop = True
        else: 
            if not is_an_integer(s):
                print_error(f"Expected an interger but '{s}' is not an interger")
            else:
                try: 
                    n = int(s)
                    if not list_all:
                        r1 = fibonacci_iterative(n)
                        r2 = fibonacci_recursive(n)
                        print_info(f"> Fibonacci (Iterative) of {n}: ", r1)
                        print_info(f"> Fibonacci (Recursive) of {n}: ", r2)
                    else: 
                        l1 = fibonacci_iterative_list(n)
                        l2 = fibonacci_recursive_list(n)
                        print_info(f"> Fibonacci (Iterative) numbers of {n}: ", l1)
                        print_info(f"> Fibonacci (Recursive) numbers of {n}: ", l2)
                    
                except Exception as e: 
                    print_error(f"ERROR: {e}")

# Call test
#test_fibonacci()
test_fibonacci(True)