"""
TowerofHanoi.py - Implement the Towers of Hanoi algorithm

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
"""

from Utils import *

def move_disk(n, src, dest, level):
    """
    Function to move a disk from source to destination with recursion level tracking

    Args:
        n (int): The disk number.
        src (int): The source peg number.
        dest (int): The destination peg number.
        level (int): The recursion level.
    Returns:
        None
    """

    indent = "  " * level  # Indentation based on recursion level
    print_info(f"{indent}Recursion Level={level}")
    print_info(f"{indent}Moving Disk {n} from Source {src} to Destination {dest}")
    print_info(f"{indent}n={n}, src={src}, dest={dest}")
    print()

def towers_of_hanoi(n, src, aux, dest, level=1):
    """
    Function to solve the Towers of Hanoi problem using recursion

    Args:
        n (int): The number of disks.
        src (int): The source peg number.
        aux (int): The auxiliary peg number.
        dest (int): The destination peg number.
        level (int, optional): The recursion level. Defaults to 1.
    Returns:
        None
    """
    if n == 1:
        move_disk(n, src, dest, level)
        return
    
    towers_of_hanoi(n - 1, src, dest, aux, level + 1)
    move_disk(n, src, dest, level)
    towers_of_hanoi(n - 1, aux, src, dest, level + 1)


# Function to test the Towers of Hanoi algorithm
def test_tower_of_hanoi(): 
    Stop = False
    while not Stop:
            sn = input("Enter the number of disks or 'exit' to stop: ").strip()
            if sn == 'exit': 
                print_error("Test stopped")
                Stop = True
            else: 
                try:
                    num_disks = int(sn)
                    if num_disks <= 0:
                        raise ValueError("Number of disks must be a positive integer.")
                    print(f"\nSolving Towers of Hanoi for {num_disks} disks:\n")
                    towers_of_hanoi(num_disks, 1, 2, 3)
                    print_info(f"... # There are {2**num_disks - 1} moves for this case.")
                except Exception as e:
                    print_error(f"Error: {e}")

# Call test function
test_tower_of_hanoi()