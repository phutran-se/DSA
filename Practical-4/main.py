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
    while not Stop:
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
        if choice == "1":
            value = input("Enter value to insert at first: ")
            linked_list.insert_first(value)
        elif choice == "2":
            value = input("Enter value to insert at last: ")
            linked_list.insert_last(value)
            print_info(f"> Inserted: {value}")
        elif choice == "3":
            try:
                rm = linked_list.remove_first()
                print_info(f"> Removed first: {rm}")
            except Exception as e:
                print_error(f"> ERROR on removing first: {e}")
        elif choice == "4":
            try:
                rm = linked_list.remove_last()
                print_info(f"> Removed last: {rm}")
            except Exception as e:
                print_error(f"> ERROR on removing last: {e}")
        elif choice == "5":
            print_info(f"> List = {linked_list.display()}")
        elif choice == "6":
            value = input("Enter value to find: ")
            found = linked_list.find_first(value)
            if found != -1:
                print_info2(f"> Value '{value}' found at index: {found}")
            else:
                print_error(f"> Value '{value}' not found in list")
        elif choice == "7":
            Stop = True
            print_error("Exiting...")
        else:
            print_error("Invalid choice. Please try again.")

if __name__ == "__main__":
    try: 
        main()
    except Exception as e:
        print_error(f"Error: {e}")

    print("Program ended\n")



