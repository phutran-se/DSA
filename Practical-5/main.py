"""
main.py - Entry point for the program

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
"""

from DSABinarySearchTree import DSABinarySearchTree
from Funct import *

def main():
    tree = DSABinarySearchTree()
    while True:
        print("\n1. Add Node")
        print("2. Delete Node")
        print("3. Display Tree")
        print("4. Find Minimum")
        print("5. Find Maximum")
        print("6. Find Height")
        print("7. Check Balance")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        # Insert 
        if choice == '1':
            is_valid = False
            key = 0
            while not is_valid:
                try: 
                    key = int(input("Enter key to insert: ").strip())
                    is_valid = True
                except Exception as e: 
                    print_error(f"You enter an invalid value ({e})")
            value = input("Enter value for the node: ").strip()
            tree.insert(key, value)
        # Delete
        elif choice == '2':
            key = int(input("Enter key to delete: "))
            try:
                tree.delete(key)
                print(f"...........Delete key={key}: done")
            except ValueError as e:
                print_error(f"...........Delete key={key}: failed (reason: {e})")
        # Traversal
        elif choice == '3':
            print("\nSelect A Traversal Method to Display Tree[1-3]:")
            print("1. In-order")
            print("2. Pre-order")
            print("3. Post-order")
            traversal_choice = input("Enter your choice: ")
            # In order
            if traversal_choice == '1':
                print("......In-order Traversal:", tree.in_order())
            # Pre order
            elif traversal_choice == '2':
                print(".....Pre-order Traversal:", tree.pre_order())
            # Post order
            elif traversal_choice == '3':
                print("....Post-order Traversal:", tree.post_order())
            # Invalid
            else:
                print_error("Invalid traversal method, returning to main menu.")
        # Min 
        elif choice == '4':
            try:
                min_node = tree.min()
                print(f"...........Minimum key: {min_node.get_key()}\n")
            except Exception as e: 
                print_error(f"...........Minimum key: error (reason: {e})\n")
        # Max
        elif choice == '5':
            try:
                max_node = tree.max()
                print(f"...........Maximum key: {max_node.get_key()}\n")
            except Exception as e: 
                print_error(f"...........Maximum key: error (reason: {e})\n")
        # Height
        elif choice == '6':
            print("Tree Height:", tree.height())
        # Balance
        elif choice == '7':
            print("Tree Balance:", tree.balance())
        elif choice == '8':
            break
        else:
            print_error("Invalid choice, please try again.\n")

def test_tree():
    # Tree
    tree = DSABinarySearchTree()

    # Add
    print_info("> Adding nodes to the tree:")
    tree.insert(5, "Five")
    tree.insert(3, "Three")
    tree.insert(8, "Eight")
    tree.insert(2, "Two")
    tree.insert(4, "Four")
    tree.insert(10, "Ten")
    tree.insert(7, "Seven")
    tree.insert(9, "Nine")
    #tree.insert(1, "One")
    tree.insert(11, "Eleven")
    tree.insert(6, "Six")
    print("...........Add done\n")
    
    # Display
    print_info("> Displaying the tree:")
    tree.display()
    print()

    # Find key 
    print_info("> Find key:")
    for kk in [8, 20]:
        try: 
            print(f"...........Found: key={kk}, value={tree.find(kk)}")
        except Exception as e: 
            print_error(f"...........Error: key={kk}, error = {e}")
    print()

    # Find min
    print_info("> Finding the minimum key:")
    try:
        min_node = tree.min()
        print(f"...........Minimum key: {min_node.get_key()}\n")
    except Exception as e: 
        print_error(f"...........Minimum key: error (reason: {e})\n")
    
    # Find max
    print_info("> Finding the maximum key:")
    try:
        max_node = tree.max()
        print(f"...........Maximum key: {max_node.get_key()}\n")
    except Exception as e: 
        print_error(f"...........Maximum key: error (reason: {e})\n")

    # Find height
    print_info("> Finding the height of the tree:")
    print(f"...........Tree height: {tree.height()}\n")

    # Check balance
    print_info("> Checking the balance of the tree:")
    print(f"...........Tree balance: {tree.balance()}\n")

    # Delete
    print_info("> Deleting nodes from the tree:")
    list_to_delete = [1, 3, 5, 7, 20, 9, 10]
    for k in list_to_delete: 
        try:
            tree.delete(k)
            print(f"...........Delete key={k}: done")
        except Exception as e: 
            print_error(f"...........Delete key={k}: failed (reason: {e})")
    
    # Display
    print()
    print_info("> Displaying the tree:")
    tree.display()
    print()

if __name__ == "__main__":
    # Create some testcases for the tree
    test_tree()

    # Run the main function
    main()