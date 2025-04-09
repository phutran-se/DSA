"""
TestManualGraph2.py - Test case for Graph 2 using DSAGraph class

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
"""

from DSAGraph import DSAGraph
from GUI import draw_graph  
from Funct import * 


SHOW_GUI = True

def test_graph2():
    # Create a new graph
    graph = DSAGraph()
    
    print("=== Graph 2 Creation ===")
    # Add vertices
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")
    graph.add_vertex("F")
    graph.add_vertex("G")
    graph.add_vertex("H")
    graph.add_vertex("I")
    graph.add_vertex("J")

    print(f"Vertex count after adding A-J: {graph.get_vertex_count()}")  # Expected: 10
    
    # Add edges (undirected)
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("A", "D")
    graph.add_edge("B", "E")
    graph.add_edge("C", "F")
    graph.add_edge("D", "E")
    graph.add_edge("D", "F")
    graph.add_edge("D", "H")
    graph.add_edge("E", "G")
    graph.add_edge("F", "I")
    graph.add_edge("G", "H")
    graph.add_edge("G", "J")
    graph.add_edge("H", "I")
    graph.add_edge("H", "J")
    graph.add_edge("I", "J")
    
    print("\nAdjacency List:")
    s = graph.display_as_list()
    print_info(s)
    # Expected output (insertion order):
    # A: B C D
    # B: A E
    # C: A F
    # D: A E F H
    # E: B D G
    # F: C D I
    # G: E H J
    # H: D G I J
    # I: F H J
    # J: G H I
    
    print("\nMatrix Representation:")
    s = graph.display_as_matrix()
    print_info(s)
    
    if SHOW_GUI:
        draw_graph(graph, "(Graph 2)")
    
    # Test BFS from A
    print("\n=== BFS from A (Graph 2) ===")
    bfs_result = graph.breadth_first_search("A")
    bfs_str = "BFS Traversal: "
    curr = bfs_result.head
    while curr is not None:
        bfs_str += str(curr.value) + " "
        curr = curr.next
    print_info(bfs_str)
    # Expected output (insertion order: B, C, D for A):
    # BFS Traversal: ('A', 'B') ('A', 'C') ('A', 'D') ('B', 'E') ('C', 'F') ('D', 'H') ('E', 'G') ('F', 'I') ('H', 'J')
    
    # Test DFS from A
    print("\n=== DFS from A (Graph 2) ===")
    dfs_result = graph.depth_first_search("A")
    dfs_str = "DFS Traversal: "
    curr = dfs_result.head
    while curr is not None:
        dfs_str += str(curr.value) + " "
        curr = curr.next
    print_info(dfs_str)
    # Expected output (insertion order: B, C, D for A):
    # DFS Traversal: ('A', 'B') ('B', 'E') ('E', 'D') ('D', 'F') ('F', 'C') ('F', 'I') ('I', 'H') ('H', 'G') ('G', 'J')

# Call test
try:
    test_graph2()
except Exception as e:
    print_error(f"[ERROR]: {e}")