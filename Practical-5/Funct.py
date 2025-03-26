"""
Funct.py - Some ultil functions (print)

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
"""

RED = "\033[91m"
BLUE = "\033[34m"
GREEN = "\033[32m"
RESET = "\033[0m"

# Print with red color
def print_error(*args, sep=' ', end='\n'):
    msg = sep.join(str(arg) for arg in args)
    print(f"{RED}{msg}{RESET}", end=end)

# Print with blue color
def print_info(*args, sep=' ', end='\n'):
    msg = sep.join(str(arg) for arg in args)
    print(f"{BLUE}{msg}{RESET}", end=end)

# Print with green color
def print_info2(*args, sep=' ', end='\n'):
    msg = sep.join(str(arg) for arg in args)
    print(f"{GREEN}{msg}{RESET}", end=end)