"""
Utils.py - Some ultil functions (print, check integer)

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
"""

BLUE = "\033[34m"
RED = "\033[91m"
RESET = "\033[0m"

def print_error(*args, sep=' ', end='\n'):
    msg = sep.join(str(arg) for arg in args)
    print(f"{RED}{msg}{RESET}", end=end)

def print_info(*args, sep=' ', end='\n'):
    msg = sep.join(str(arg) for arg in args)
    print(f"{BLUE}{msg}{RESET}", end=end)

def is_an_integer(s): 
    return s.lstrip('-').isdigit()