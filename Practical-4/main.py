"""
main.py - Entry point for the program

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
"""

from DSALinkedList import DSALinkedList
from Funct import *

def main():
    """
    Main function to interact with a linked list through a menu-driven interface.
    The function provides the following options:
        1. Insert First: Insert a value at the beginning of the linked list.
        2. Insert Last: Insert a value at the end of the linked list.
        3. Remove First: Remove the first value from the linked list.
        4. Remove Last: Remove the last value from the linked list.
        5. Display List: Display all values in the linked list.
        6. Exit: Exit the menu.
    
    The function continuously prompts the user for a choice until the user chooses to exit.
    """

    linked_list = DSALinkedList() # Create a new linked list
    Stop = False
    while not Stop: # Loop until the user chooses to exit
        # Create menu options
        print("\nLinked List Menu:")
        print("1. Insert First")
        print("2. Insert Last")
        print("3. Remove First")
        print("4. Remove Last")
        print("5. Display List")
        print("6. Find First Occurrence of a Value")
        print("7. Exit")
        print()
        
        choice = input("Enter your choice [1-7]: ")
        if choice == "1": # Insert First
            value = input("Enter value to insert at first: ")
            linked_list.insert_first(value)
        elif choice == "2": # Insert Last
            value = input("Enter value to insert at last: ")
            linked_list.insert_last(value)
            print_info(f"> Inserted: {value}")
        elif choice == "3": # Remove First
            # Try to remove the first value and catch any exceptions
            try:
                rm = linked_list.remove_first()
                print_info(f"> Removed first: {rm}")
            except Exception as e:
                print_error(f"> ERROR on removing first: {e}")
        elif choice == "4": # Remove Last
            # Try to remove the last value and catch any exceptions
            try:
                rm = linked_list.remove_last()
                print_info(f"> Removed last: {rm}")
            except Exception as e:
                print_error(f"> ERROR on removing last: {e}")
        elif choice == "5": # Display the content of linked list 
            print_info(f"> List = {linked_list.display()}")
        elif choice == "6": # Find the first occurrence of a value
            val = input("Enter value to find: ")
            found = linked_list.find_first(val)
            if found != -1: # If the value is found
                print_info2(f"> Value '{val}' found at index: {found}")
            else: # If the value is not found
                print_error(f"> Value '{val}' not found in list")
        elif choice == "7": # Exit
            Stop = True # Set the stop flag to True
            print_error("Exiting...")
        else:
            print_error("Your choice is invalid. Please try again!!!")

if __name__ == "__main__":
    # Run the main function and try to catch any exceptions to avoid the program from crashing
    try: 
        main()
    except Exception as e:
        print_error(f"Error: {e}")

    print("Program ended\n")



