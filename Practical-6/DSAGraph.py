"""
DSAGraph.py - Define class DSAGraphVertex and DSAGraph

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
"""

import numpy as np
from DSALinkedList import DSALinkedList, DSAListNode
from DSAQueue import DSAQueue
from DSAStack import DSAStack

# ------------------------------------------------------------------------------
class DSAGraphNode:
    def __init__(self, label, value=None):
        self.label = label
        self.value = value
        self.adjacent = DSALinkedList() # Using your DSALinkedList for adjacency
        self.visited = False
    
    def add_edge(self, vertex):
        # Check if vertex already exists in adjacent list
        curr = self.adjacent.head
        while curr is not None:
            if curr.value == vertex:
                return
            curr = curr.next
        self.adjacent.insert_last(vertex)
    
    def get_adjacent(self):
        return self.adjacent
    
    def set_visited(self):
        self.visited = True
    
    def clear_visited(self):
        self.visited = False
    
    def get_visited(self):
        return self.visited
    
    def __str__(self):
        return str(self.label)


# ------------------------------------------------------------------------------
class DSAGraph:
    def __init__(self):
        self.vertices = DSALinkedList()  # Using your DSALinkedList for vertices
    
    def add_vertex(self, label, value=None):
        """
        Adds a new vertex with the given label and optional value to the graph.
        How:
            - Traverses self.vertices to check if a vertex with the given label already exists.
            - If not found, creates a new DSAGraphNode with the label and value.
            - Inserts the new node at the end of self.vertices using insert_last().
        """

        # Check if vertex already exists
        curr = self.vertices.head
        while curr is not None:
            if curr.value.label == label:
                return
            curr = curr.next
        new_vertex = DSAGraphNode(label, value)
        self.vertices.insert_last(new_vertex)
    
    def add_edge(self, label1, label2, auto_create_vertex = True):
        """
        Adds an undirected edge between two vertices identified by label1 and label2.
        How:
            - Traverses self.vertices to find or create vertices with label1 and label2.
            - If either vertex doesn’t exist, creates it using DSAGraphNode and adds it to self.vertices.
            - Adds the second vertex to the first vertex’s adjacency list using add_edge().
            - Adds the first vertex to the second vertex’s adjacency list (undirected graph).
        """
        vertex1 = None
        vertex2 = None
        curr = self.vertices.head
        
        # Find vertices
        while curr is not None:
            if curr.value.label == label1:
                vertex1 = curr.value
            if curr.value.label == label2:
                vertex2 = curr.value
            curr = curr.next
        
        if (vertex1 is None or vertex2 is None) and not auto_create_vertex:
            raise ValueError(f"Cannot add edge: One or both vertices ({label1}, {label2}) do not exist.")

        # Add vertices if they don't exist
        if vertex1 is None:
            vertex1 = DSAGraphNode(label1)
            self.vertices.insert_last(vertex1)
        if vertex2 is None:
            vertex2 = DSAGraphNode(label2)
            self.vertices.insert_last(vertex2)
        
        # Add edges (undirected)
        vertex1.add_edge(vertex2)
        vertex2.add_edge(vertex1)
    
    def delete_vertex(self, label):
        """
        Removes a vertex and all its associated edges from the graph.
        How:
            - Traverses self.vertices to find the node with the given label.
            - Updates the linked list pointers (prev and next) to remove the node from self.vertices.
            - Traverses all other vertices’ adjacency lists to remove references to the deleted vertex.
            - Adjusts head and tail pointers of self.vertices and adjacency lists as needed.
        """

        curr = self.vertices.head
        prev = None
        
        # Find and remove vertex
        while curr is not None:
            if curr.value.label == label:
                if prev is None:
                    self.vertices.head = curr.next
                else:
                    prev.next = curr.next
                if curr.next is not None:
                    curr.next.prev = prev
                if curr == self.vertices.tail:
                    self.vertices.tail = prev
                
                # Remove edges to this vertex
                curr_adj = self.vertices.head
                while curr_adj is not None:
                    adj_curr = curr_adj.value.adjacent.head
                    adj_prev = None
                    while adj_curr is not None:
                        if adj_curr.value == curr.value:
                            if adj_prev is None:
                                curr_adj.value.adjacent.head = adj_curr.next
                            else:
                                adj_prev.next = adj_curr.next
                            if adj_curr.next is not None:
                                adj_curr.next.prev = adj_prev
                            if adj_curr == curr_adj.value.adjacent.tail:
                                curr_adj.value.adjacent.tail = adj_prev
                            break
                        adj_prev = adj_curr
                        adj_curr = adj_curr.next
                    curr_adj = curr_adj.next
                break
            prev = curr
            curr = curr.next
    
    def delete_edge(self, label1, label2, raise_exception = True):
        """
        Removes an undirected edge between two vertices.
        How:
            - Traverses self.vertices to find vertices with label1 and label2.
            - If both exist, traverses the adjacency list of the first vertex to remove the second vertex.
            - Traverses the adjacency list of the second vertex to remove the first vertex.
            - Updates prev and next pointers in both adjacency lists, adjusting head and tail if necessary.
        """        
        vertex1 = None
        vertex2 = None
        curr = self.vertices.head
        
        # Find vertices
        while curr is not None:
            if curr.value.label == label1:
                vertex1 = curr.value
            if curr.value.label == label2:
                vertex2 = curr.value
            curr = curr.next
        
        if vertex1 is None or vertex2 is None:
            if raise_exception:
                raise ValueError("One or both labels not found")
            else: 
                return
        
        # Remove vertex2 from vertex1's adjacent list
        curr = vertex1.adjacent.head
        prev = None
        while curr is not None:
            if curr.value == vertex2:
                if prev is None:
                    vertex1.adjacent.head = curr.next
                else:
                    prev.next = curr.next
                if curr.next is not None:
                    curr.next.prev = prev
                if curr == vertex1.adjacent.tail:
                    vertex1.adjacent.tail = prev
                break
            prev = curr
            curr = curr.next
        
        # Remove vertex1 from vertex2's adjacent list
        curr = vertex2.adjacent.head
        prev = None
        while curr is not None:
            if curr.value == vertex1:
                if prev is None:
                    vertex2.adjacent.head = curr.next
                else:
                    prev.next = curr.next
                if curr.next is not None:
                    curr.next.prev = prev
                if curr == vertex2.adjacent.tail:
                    vertex2.adjacent.tail = prev
                break
            prev = curr
            curr = curr.next
    
    def has_vertex(self, label):
        """
        Checks if a vertex with the given label exists in the graph.
        How:
            - Traverses self.vertices from head to tail.
            - Returns True if a node with the matching label is found, False otherwise.
        """
        curr = self.vertices.head
        while curr is not None:
            if curr.value.label == label:
                return True
            curr = curr.next
        return False
    
    def get_vertex_count(self):
        """
        Returns the number of vertices in the graph.
        How:
            - Init a counter to 0.
            - Traverses self.vertices from head to tail, incrementing the counter for each node.
            - Returns the final count.
        """
        count = 0
        curr = self.vertices.head
        while curr is not None:
            count += 1
            curr = curr.next
        return count
    
    def get_vertex(self, label):
        """
        Retrieves the vertex object with the given label.
        How:
            - Traverses self.vertices from head to tail.
            - Returns the DSAGraphNode object if found, None if not found.
        """
        curr = self.vertices.head
        while curr is not None:
            if curr.value.label == label:
                return curr.value
            curr = curr.next
        return None
    
    def display_as_list(self):
        """
        Displays the graph as an adjacency list.
        How:
            - Traverses self.vertices from head to tail.
            - For each vertex, prints its label followed by the labels of all adjacent vertices.
            - Traverses each vertex’s adjacency list (adjacent) to print adjacent vertex labels.
        """

        str_list = ""
        curr = self.vertices.head
        while curr is not None:
            vertex = curr.value
            str_list += str(vertex.label) + ": "
            adj_curr = vertex.adjacent.head
            while adj_curr is not None:
                str_list += str(adj_curr.value.label) + " "
                adj_curr = adj_curr.next
            str_list += "\n"
            curr = curr.next
            
        return str_list
    
    def display_as_matrix(self):
        """
        Displays the graph as an adjacency matrix.
        How:
            - Counts vertices using get_vertex_count().
            - Creates a list of labels by traversing self.vertices.
            - Manually sorts labels using bubble sort (since sort() is restricted).
            - Prints a header row with sorted labels.
            - For each vertex, prints its label and a row of 0s and 1s:
                + Traverses its adjacency list to check for each label in the sorted list.
                + Prints "1" if an edge exists, "0" otherwise.
        """

        str_list = ""
        # Count vertices
        vertex_count = self.get_vertex_count()
        if vertex_count == 0:
            return str_list
        
        # Create list of labels
        labels = np.empty(vertex_count, dtype=object)
        curr = self.vertices.head
        for i in range(vertex_count):
            labels[i] = curr.value.label  # Populate with labels from nodes
            curr = curr.next
        
        # Sort labels manually (bubble sort since sort() is restricted)
        for i in range(vertex_count):
            for j in range(vertex_count - i - 1):
                if labels[j] > labels[j + 1]:
                    labels[j], labels[j + 1] = labels[j + 1], labels[j]
        
        # Print header
        str_list += "  "
        for label in labels:
            str_list += str(label) + " "
        str_list += "\n"
        
        # Print matrix
        curr = self.vertices.head
        while curr is not None:
            vertex = curr.value
            str_list += str(vertex.label) + " "
            for label in labels:
                found = False
                adj_curr = vertex.adjacent.head
                while adj_curr is not None:
                    if adj_curr.value.label == label:
                        found = True
                        break
                    adj_curr = adj_curr.next
                str_list += "1 " if found else "0 "
            str_list += "\n"
            curr = curr.next

        return str_list
    
    def breadth_first_search(self, start_label):
        """
        Performs a breadth-first search starting from the given label, returning a list of edges.
        How:
            - Retrieves the starting vertex using get_vertex().
            - Clears all visited flags by traversing self.vertices.
            - Creates a DSALinkedList (T) for the result and a DSAQueue (Q).
            - Marks the start vertex as visited and enqueues it.
            - While the queue is not empty:
                + Dequeues a vertex (v).
                + Traverses its adjacency list, adding unvisited neighbors to T and Q.
                + Marks each neighbor as visited.
            
            - Returns T containing edge list.
        """

        T = DSALinkedList()  # Result path
        Q = DSAQueue()

        start_vertex = self.get_vertex(start_label)
        if start_vertex is None:
            return T
        
        # Clear visited flags
        curr = self.vertices.head
        while curr is not None:
            curr.value.clear_visited()
            curr = curr.next
    
        
        start_vertex.set_visited() # Set A as visited
        Q.enqueue(start_vertex)
        
        while not Q.is_empty():
            v = Q.dequeue()
            adj_curr = v.adjacent.head
            while adj_curr is not None:
                w = adj_curr.value
                if not w.get_visited():
                    T.insert_last((v.label, w.label))
                    w.set_visited()
                    Q.enqueue(w)
                adj_curr = adj_curr.next
        
        return T
    
    def depth_first_search(self, start_label):
        """
        Performs a depth-first search starting from the given label, returning a list of edges.
        How:
            - Retrieves the starting vertex using get_vertex().
            - Clears all visited flags by traversing self.vertices.
            - Creates a DSALinkedList (T) for the result and a DSAStack (S).
            - Marks the start vertex as visited and pushes it onto the stack.
            - While the stack is not empty:
                + Peeks at the top vertex (v).
                + Traverses its adjacency list to find the first unvisited neighbor (w).
                + If found, adds the edge to T, marks w as visited, and pushes w onto the stack.
                + If no unvisited neighbors, pops the top vertex.
            
            - Returns T containing edge list.
        """

        T = DSALinkedList()  # Result path
        S = DSAStack()

        start_vertex = self.get_vertex(start_label)
        if start_vertex is None:
            return T
        
        # Clear visited flags
        curr = self.vertices.head
        while curr is not None:
            curr.value.clear_visited()
            curr = curr.next
        
        start_vertex.set_visited() # Set A as visited
        S.push(start_vertex)
        
        while not S.is_empty():
            v = S.peek()
            unvisited_found = False
            adj_curr = v.adjacent.head
            
            while adj_curr is not None:
                w = adj_curr.value
                if not w.get_visited():
                    T.insert_last((v.label, w.label))
                    w.set_visited()
                    S.push(w)
                    unvisited_found = True
                    break
                adj_curr = adj_curr.next
            
            if not unvisited_found:
                S.pop()
        
        return T