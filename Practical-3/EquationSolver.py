from DSAStack import DSAStack
from DSAQueue import ShufflingQueue
from Funct import *

def precedence(op):
    """
    Determine the precedence of a given operator.

    Parameters:
        : A string representing an operator ('+', '-', '*', '/').
    Returns:
        int: An integer representing the precedence level of the operator.
             Returns 1 for '+' and '-', 2 for '*' and '/', and 0 for any other operator.
    """

    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):  
        return 2
    return 0

def is_number(token):
    """
    Check if the given token can be converted to a float.

    Args:
        token (str): The token to check.
    Returns:
        bool: True if the token can be converted to a float, False otherwise.
    """

    try:
        float(token)
        return True
    except ValueError:
        return False

def preprocess_expression(expression):
    """
    Preprocesses a mathematical expression by ensuring spaces around operators and parentheses.

    Args:
        expression (str): The mathematical expression to preprocess.
    Returns:
        str: The preprocessed expression with spaces around operators and parentheses, 
             and extra spaces removed.
    """

    # Ensure spaces around operators and parentheses
    operators = set("+-*/()")
    new_expr = ""
    for char in expression:
        if char in operators:
            new_expr += f" {char} "     # Add space around operator or parenthesis
        else:
            new_expr += char
    return ' '.join(new_expr.split())   # Remove extra spaces

def infix_to_postfix(expression, preprocess_exp):
    """
    Converts an infix expression to a postfix expression.
    Args:
        expression (str): The infix expression to be converted.
        preprocess_exp (bool): If True, preprocess the expression to ensure spaces around operators and parentheses.
    Returns:
        ShufflingQueue: A queue containing the tokens of the postfix expression in order.
    Raises:
        Exception: If there are unmatched parentheses in the expression.
    """

    if preprocess_exp:
        expression = preprocess_expression(expression) # Ensure spaces around operators and parentheses

    tokens = expression.strip().split() # Split the expression into tokens
    stack = DSAStack(len(tokens))       # Create a stack to store operators
    queue = ShufflingQueue(len(tokens)) # Create a queue to store the postfix expression
    
    # Process each token in the expression
    for token in tokens:
        if is_number(token):
            queue.enqueue(float(token))     # Add numbers directly to the queue
        elif token in "+-*/":
            # Pop operators with higher or equal precedence from the stack
            while (not stack.is_empty() and precedence(stack.peek()) >= precedence(token)):
                queue.enqueue(stack.pop())  # Add the operator to the queue
            stack.push(token)               # Push the current operator to the stack
        elif token == "(":                  # Push opening parenthesis to the stack
            stack.push(token)
        elif token == ")":                  # Pop operators from the stack until an opening parenthesis is found
            while not stack.is_empty() and stack.peek() != "(": 
                queue.enqueue(stack.pop())  # Add operators to the queue
            if stack.is_empty():
                raise Exception("Error: Unmatched closing parenthesis.")
            stack.pop()  # Remove '('
    
    # Pop any remaining operators from the stack
    while not stack.is_empty():
        if stack.peek() == "(":
            raise Exception("Error: Unmatched opening parenthesis.")
        queue.enqueue(stack.pop())
    
    return queue

def evaluate_postfix(queue):
    """
    Evaluates a postfix expression provided as a queue of tokens.

    Args:
        queue (DSAQueue): A queue containing the postfix expression tokens. 
                          Tokens can be floats or operators ('+', '-', '*', '/').
    Returns:
        float: The result of evaluating the postfix expression.
    Raises:
        Exception: If there are not enough operands before an operator.
        Exception: If division by zero is attempted.
        Exception: If no result is found in the stack after evaluation.
    """
    
    stack = DSAStack(queue.count)   # Create a stack to store operands
    while not queue.is_empty():     # Process each token in the queue
        token = queue.dequeue() 
        if isinstance(token, float):
            stack.push(token)
        elif token in "+-*/": # Perform the operation on the top two operands
            if stack.is_empty():
                raise Exception("Error: Not enough operands before operator '{}'.".format(token))
            op2 = stack.pop()
            if stack.is_empty():
                raise Exception("Error: Not enough operands before operator '{}'.".format(token))
            op1 = stack.pop()
            if token == '+': 
                stack.push(op1 + op2)
            elif token == '-':
                stack.push(op1 - op2)
            elif token == '*':
                stack.push(op1 * op2)
            elif token == '/':
                if op2 == 0: # Check for division by zero
                    raise Exception("Error: Division by zero.")
                stack.push(op1 / op2)
    
    if stack.is_empty():
        raise Exception("Error: No result found in stack.")
    
    return stack.pop()

def solve_expression(expression, preprocess_exp):
    """
    Solves a given mathematical expression.

    Args:
        expression (str): The infix expression to be solved.
        preprocess_exp (bool): Whether to preprocess the expression.
    Returns:
        float: The result of evaluating the postfix expression.
    """

    print_info("> Infix expression:", expression)
    queue = infix_to_postfix(expression, preprocess_exp)    # Convert infix to postfix
    print_info("> Postfix expression:", queue)  
    return evaluate_postfix(queue)                          # Evaluate postfix expression
