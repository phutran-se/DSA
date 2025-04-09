"""
main.py - Entry point for the program

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
"""

from DSAGraph import DSAGraph
from Funct import *
from GUI import draw_graph

def main():
    graph = DSAGraph()
    while True:
        print("\n* Graph Menu:")
        print("(a) Add node")
        print("(b) Delete node")
        print("(c) Add edge")
        print("(d) Delete edge")
        print("(e) Display as list")
        print("(f) Display as matrix")
        print("(g) Breadth First Search")
        print("(h) Depth First Search")
        print("(i) Draw graph")
        print("(q) Quit")
        print()
        choice = input("Enter your choice: ").lower()
        
        if choice == 'a':
            label = input("Enter node label: ").strip()
            if(len(label) > 0):
                graph.add_vertex(label)
                print_info2(f"> DONE: Node {label} added")
            else: 
                 print_error("> ERROR: Label is empty")
            print()
            
        elif choice == 'b':
            label = input("Enter node label to delete: ").strip()
            if graph.has_vertex(label):
                graph.delete_vertex(label)
                print_info2(f"> DONE: Node {label} deleted")
            else:
                print_error(f"> ERROR: Node {label} not found")
            print()
                
        elif choice == 'c':
            label1 = input("Enter first node label: ").strip()
            label2 = input("Enter second node label: ").strip()
            if(len(label1) > 0 and len(label2) > 0):
                try: 
                    graph.add_edge(label1, label2, False)
                    print_info2(f"> DONE: Edge added between {label1} and {label2}")
                except Exception as e: 
                    print_error(f'> ERROR: Add failed: {e}')
            else: 
                print_error(f"> ERROR: One or both lables is empty: label1={label1}, label2={label2}")
            print()
            
        elif choice == 'd':
            label1 = input("Enter first node label: ").strip()
            label2 = input("Enter second node label: ").strip()
            if(len(label1) > 0 and len(label2) > 0):
                try: 
                    graph.delete_edge(label1, label2)
                    print_info2(f"> DONE: Edge deleted between {label1} and {label2}")
                except Exception as e: 
                    print_error(f'> ERROR: Delete edge failed: {e}')
            else: 
                print_error(f"> ERROR: One or both lables is empty: label1={label1}, label2={label2}")
            print()

        elif choice == 'e':
            s = graph.display_as_list()
            print_info2("> Graph is displayed as list: ")
            print_info2(s)
            print()
            
        elif choice == 'f':
            s = graph.display_as_matrix()
            print_info2("> Graph is displayed as matrix: ")
            print_info2(s)
            print()

        elif choice == 'g':
            start = input("Enter starting node label: ").strip()
            result = graph.breadth_first_search(start)
            print_info2("> BFS traversal: ", end="")
            curr = result.head
            bfs_str = ""
            while curr is not None:
                bfs_str += str(curr.value) + " "
                curr = curr.next
            print_info2(bfs_str)
            print()
            
        elif choice == 'h':
            start = input("Enter starting node label: ").strip()
            result = graph.depth_first_search(start)
            print_info2("> DFS traversal: ", end="")
            curr = result.head
            dfs_str = ""
            while curr is not None:
                dfs_str += str(curr.value) + " "
                curr = curr.next
            print_info2(dfs_str)
            print()

        elif choice == 'i': 
            draw_graph(graph)

        elif choice == 'q':
            print("Exiting...")
            break
            
        else:
            print_error("ERROR: Invalid choice, please try again")


if __name__ == "__main__":
    # Run the main function
    try: 
        main()
    except Exception as e: 
        print_error(f"[ERROR] Exception: {e}")