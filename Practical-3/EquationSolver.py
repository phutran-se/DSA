"""
EquationSolver.py - Implement the Equation Solver functions

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
"""

from DSAStack import DSAStack
from DSAQueue import ShufflingQueue, CircularQueue

def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

def infix_to_postfix(expression):
    stack = DSAStack()
    queue = ShufflingQueue(len(expression.split()))
    tokens = expression.split()
    
    for token in tokens:
        if token.isdigit():
            queue.enqueue(float(token))
        elif token in "+-*/":
            while (not stack.is_empty() and precedence(stack.peek()) >= precedence(token)):
                queue.enqueue(stack.pop())
            stack.push(token)
        elif token == "(":
            stack.push(token)
        elif token == ")":
            while not stack.is_empty() and stack.peek() != "(":
                queue.enqueue(stack.pop())
            if not stack.is_empty():
                stack.pop()
    
    while not stack.is_empty():
        queue.enqueue(stack.pop())
    
    return queue

def evaluate_postfix(queue):
    stack = DSAStack(queue.count)
    
    while not queue.is_empty():
        token = queue.dequeue()
        if isinstance(token, float):
            stack.push(token)
        else:
            if stack.is_empty():
                raise Exception("Error: Stack is empty when trying to pop operands.")
            op2 = stack.pop()
            if stack.is_empty():
                raise Exception("Error: Stack is empty when trying to pop operands.")
            op1 = stack.pop()
            if token == '+':
                stack.push(op1 + op2)
            elif token == '-':
                stack.push(op1 - op2)
            elif token == '*':
                stack.push(op1 * op2)
            elif token == '/':
                if op2 == 0:
                    raise Exception("Error: Division by zero.")
                stack.push(op1 / op2)
    
    if stack.is_empty():
        raise Exception("Error: No result found in stack.")
    
    return stack.pop()

def solve_expression(expression):
    queue = infix_to_postfix(expression)
    return evaluate_postfix(queue)
