"""
TestManualGraph1.py - Test case for Graph 1 using DSAGraph class

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
"""

from DSAGraph import DSAGraph
from GUI import draw_graph  
from Funct import *  

SHOW_GUI = True

def test_graph1():
    # Create a new graph
    graph = DSAGraph()
    
    print("=== Graph 1 Creation ===")
    # Add vertices
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")
    graph.add_vertex("F")
    graph.add_vertex("G")

    print(f"Vertex count after adding A-G: {graph.get_vertex_count()}")  # Expected: 7
    
    # Add edges (undirected)
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("A", "D")
    graph.add_edge("B", "E")
    graph.add_edge("C", "D")
    graph.add_edge("D", "F")
    graph.add_edge("E", "F")
    graph.add_edge("E", "G")
    graph.add_edge("F", "G")
    
    print("\nAdjacency List:")
    s = graph.display_as_list()
    print_info(s)
    # Expected output (insertion order):
    # A: B C D
    # B: A E
    # C: A D
    # D: A C F
    # E: B F G
    # F: D E G
    # G: E F
    
    print("\nMatrix Representation:")
    s = graph.display_as_matrix()
    print_info(s)
    
    if SHOW_GUI:
        draw_graph(graph, "(Graph 1)")
    
    # Test BFS from A
    print("\n=== BFS from A (Graph 1) ===")
    bfs_result = graph.breadth_first_search("A")
    bfs_str = "BFS Traversal: "
    curr = bfs_result.head
    while curr is not None:
        bfs_str += str(curr.value) + " "
        curr = curr.next
    print_info(bfs_str)
    # Expected output (insertion order: B, C, D for A):
    # BFS Traversal: ('A', 'B') ('A', 'C') ('A', 'D') ('B', 'E') ('D', 'F') ('E', 'G')
    
    # Test DFS from A
    print("\n=== DFS from A (Graph 1) ===")
    dfs_result = graph.depth_first_search("A")
    dfs_str = "DFS Traversal: "
    curr = dfs_result.head
    while curr is not None:
        dfs_str += str(curr.value) + " "
        curr = curr.next
    print_info(dfs_str)
    # Expected output (insertion order: B, C, D for A):
    # DFS Traversal: ('A', 'B') ('B', 'E') ('E', 'F') ('F', 'D') ('D', 'C') ('F', 'G')

# Call test
try:
    test_graph1()
except Exception as e:
    print_error(f"[ERROR]: {e}")