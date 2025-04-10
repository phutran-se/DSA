"""
TestGraph.py - Test for DSAGraph

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
"""

from DSAGraph import DSAGraph
from GUI import draw_graph 
from Funct import *  

SHOW_GUI = False

def test_graph():
    # Create a new graph
    graph = DSAGraph()
    
    print("=== Initial Graph Creation ===")
    # Test 1: Adding vertices
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")
    graph.add_vertex("G")

    print(f"Vertex count after adding A, B, C, D, E: {graph.get_vertex_count()}")  # Expected: 5
    print(f"Has vertex 'A': {graph.has_vertex('A')}")  # Expected: True
    print(f"Has vertex 'F': {graph.has_vertex('F')}")  # Expected: False
    
    # Test 2: Adding edges
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "D")
    graph.add_edge("A", "E")
    graph.add_edge("D", "E")
    graph.add_edge("D", "G")
    #graph.add_edge("C", "F", False) # Check with not existed vertex F


    print("\nAfter adding edges (A-B, A-C, B-D, C-D, A-E, D-E):")
    s = graph.display_as_list()
    print_info(s)
    # Expected output:
    # A: B C E
    # B: A D
    # C: A D
    # D: B C E
    # E: A D
    
    print("\nMatrix representation:")
    s = graph.display_as_matrix()
    print_info(s)
    # Expected output:
    #   A B C D E
    # A 0 1 1 0 1
    # B 1 0 0 1 0
    # C 1 0 0 1 0
    # D 0 1 1 0 1
    # E 1 0 0 1 0
    
    if SHOW_GUI:
        draw_graph(graph, "(created)")

    # Test 3: BFS from A
    print("\n=== BFS from A (Initial Graph) ===")
    bfs_result = graph.breadth_first_search("A")
    bfs_str = "BFS Traversal: "
    curr = bfs_result.head
    while curr is not None:
        bfs_str += str(curr.value) + " "
        curr = curr.next
    print_info2(bfs_str)
    # Expected output (assuming adjacency order B, C, E):
    # BFS Traversal: ('A', 'B') ('A', 'C') ('A', 'E') ('B', 'D')

    # Test 4: DFS from A
    print("\n=== DFS from A (Initial Graph) ===")
    dfs_result = graph.depth_first_search("A")
    dfs_str = "DFS Traversal: "
    curr = dfs_result.head
    while curr is not None:
        dfs_str += str(curr.value) + " "
        curr = curr.next
    print_info2(dfs_str)
    # Expected output (assuming adjacency order B, C, E):
    # DFS Traversal: ('A', 'B') ('B', 'D') ('D', 'E') ('E', 'C')

    if SHOW_GUI:
        draw_graph(graph, "(created)")
        
    # Test 5: Delete an edge (A-B)
    print("\n=== Deleting Edge A-B ===")
    graph.delete_edge("A", "B")
    s = graph.display_as_list()
    print_error(s)
    # Expected output:
    # A: C E
    # B: D
    # C: A D
    # D: B C E
    # E: A D
    
    print("\nMatrix representation:")
    s = graph.display_as_matrix()
    print_error(s) 
    # Expected output:
    #   A B C D E
    # A 0 0 1 0 1
    # B 0 0 0 1 0
    # C 1 0 0 1 0
    # D 0 1 1 0 1
    # E 1 0 0 1 0
    
    if SHOW_GUI:
        draw_graph(graph, "(deleted edge: A-B)")

    # Test 6: BFS from A after edge deletion
    print("\n=== BFS from A (After Deleting A-B) ===")
    bfs_result = graph.breadth_first_search("A")
    bfs_str = "BFS Traversal: "
    curr = bfs_result.head
    while curr is not None:
        bfs_str += str(curr.value) + " "
        curr = curr.next
    print_info2(bfs_str)
    # Expected output (assuming adjacency order C, E):
    # BFS Traversal: ('A', 'C') ('A', 'E') ('C', 'D') ('D', 'B')

    # Test 7: DFS from A after edge deletion
    print("\n=== DFS from A (After Deleting A-B) ===")
    dfs_result = graph.depth_first_search("A")
    dfs_str = "DFS Traversal: "
    curr = dfs_result.head
    while curr is not None:
        dfs_str += str(curr.value) + " "
        curr = curr.next
    print_info2(dfs_str)
    # Expected output (assuming adjacency order C, E):
    # DFS Traversal: ('A', 'C') ('C', 'D') ('D', 'B') ('D', 'E')

    # Test 8: Delete a vertex (C)
    print("\n=== Deleting Vertex C ===")
    graph.delete_vertex("C")
    print(f"Vertex count after deleting C: {graph.get_vertex_count()}")  # Expected: 4
    s = graph.display_as_list()
    print_info(s)
    # Expected output:
    # A: E
    # B: D
    # D: B E
    # E: A D
    
    print("\nMatrix representation:")
    s = graph.display_as_matrix()
    print_info(s)
    # Expected output:
    #   A B D E
    # A 0 0 0 1
    # B 0 0 1 0
    # D 0 1 0 1
    # E 1 0 1 0 

    if SHOW_GUI:
        draw_graph(graph, "(deleted vertex: C)")

    # Test 9: BFS from A after vertex deletion
    print("\n=== BFS from A (After Deleting C) ===")
    bfs_result = graph.breadth_first_search("A")
    bfs_str = "BFS Traversal: "
    curr = bfs_result.head
    while curr is not None:
        bfs_str += str(curr.value) + " "
        curr = curr.next
    print_info2(bfs_str)
    # Expected output (assuming adjacency order E):
    # BFS Traversal: ('A', 'E') ('E', 'D') ('D', 'B')

    # Test 10: DFS from A after vertex deletion
    print("\n=== DFS from A (After Deleting C) ===")
    dfs_result = graph.depth_first_search("A")
    dfs_str = "DFS Traversal: "
    curr = dfs_result.head
    while curr is not None:
        dfs_str += str(curr.value) + " "
        curr = curr.next
    print_info2(dfs_str)
    # Expected output (assuming adjacency order E):
    # DFS Traversal: ('A', 'E') ('E', 'D') ('D', 'B')

    # Test 11: Add duplicate vertex and new edges
    print("\n=== Adding Duplicate Vertex A ===")
    graph.add_vertex("A")
    print(f"Vertex count after adding duplicate A: {graph.get_vertex_count()}")  # Expected: 4
    
    print("\n=== Adding Edge B-E, E-F ===")
    graph.add_edge("B", "E")
    graph.add_edge("E", "F")
    print(f"Vertex count after adding B-E, E-F: {graph.get_vertex_count()}")  # Expected: 5
    s = graph.display_as_list()
    print_info(s)
    # Expected output:
    # A: E
    # B: D E
    # D: B E
    # E: A B D F
    # F: E
    
    print("\nMatrix representation:")
    s = graph.display_as_matrix()
    print_info(s)
    # Expected output:
    #   A B D E F
    # A 0 0 0 1 0
    # B 0 0 1 1 0
    # D 0 1 0 1 0
    # E 1 1 1 0 1
    # F 0 0 0 1 0

    if SHOW_GUI:
        draw_graph(graph, "(added edge: B-E, E-F)")

    # Test 12: BFS from A after adding edges
    print("\n=== BFS from A (Final Graph) ===")
    bfs_result = graph.breadth_first_search("A")
    bfs_str = "BFS Traversal: "
    curr = bfs_result.head
    while curr is not None:
        bfs_str += str(curr.value) + " "
        curr = curr.next
    print_info2(bfs_str)
    # Expected output (assuming adjacency order E):
    # BFS Traversal: ('A', 'E') ('E', 'B') ('E', 'D') ('E', 'F')

    # Test 13: DFS from A after adding edges
    print("\n=== DFS from A (Final Graph) ===")
    dfs_result = graph.depth_first_search("A")
    dfs_str = "DFS Traversal: "
    curr = dfs_result.head
    while curr is not None:
        dfs_str += str(curr.value) + " "
        curr = curr.next
    print_info2(dfs_str)
    # Expected output (assuming adjacency order E):
    # DFS Traversal: ('A', 'E') ('E', 'B') ('B', 'D') ('E', 'F')

    # Exception
    print(graph.get_vertex('X'))
    graph.delete_edge('C', 'E')
    graph.delete_edge('C', 'K')
    graph.delete_vertex('H')

# Call test
try: 
    test_graph()
except Exception as e: 
    print_error(f"[ERROR]: {e}")
