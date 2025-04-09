"""
GUI.py - Display a graph on UI

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
"""

import matplotlib.pyplot as plt
import numpy as np
import math

from DSALinkedList import DSALinkedList
from Funct import *

def draw_graph(graph, extra_title=""):
    """
    Draws the given DSAGraph using Matplotlib with a circular layout.
    How:
        - Counts vertices and collects labels from the graph.
        - Assigns positions to vertices in a circle.
        - Collects edges by traversing adjacency lists.
        - Plots nodes and edges using Matplotlib.
    """
    
    # Count vertices
    vertex_count = graph.get_vertex_count()
    if vertex_count == 0:
        print_error("Graph is empty, nothing to draw.")
        return
    
    # Collect labels into a NumPy array
    labels = np.empty(vertex_count, dtype=object)
    curr = graph.vertices.head
    for i in range(vertex_count):
        labels[i] = curr.value.label
        curr = curr.next
    
    # Sort labels manually (bubble sort)
    for i in range(vertex_count):
        for j in range(vertex_count - i - 1):
            if labels[j] > labels[j + 1]:
                labels[j], labels[j + 1] = labels[j + 1], labels[j]
    
    # Assign circular positions to vertices
    radius = 1.0
    positions = {}  # Using a dictionary for positions (not restricted)
    for i in range(vertex_count):
        angle = 2 * math.pi * i / vertex_count
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        positions[labels[i]] = (x, y)
    
    # Collect edges (avoid duplicates since it's undirected)
    edges = DSALinkedList()
    curr = graph.vertices.head
    while curr is not None:
        vertex = curr.value
        adj_curr = vertex.adjacent.head
        while adj_curr is not None:
            edge = (vertex.label, adj_curr.value.label)
            # Check if reverse edge already exists
            edge_exists = False
            edge_curr = edges.head
            while edge_curr is not None:
                if edge_curr.value == (edge[1], edge[0]):
                    edge_exists = True
                    break
                edge_curr = edge_curr.next
            if not edge_exists and edge[0] < edge[1]:  
                edges.insert_last(edge)
            adj_curr = adj_curr.next
        curr = curr.next
    
    # Create the plot
    plt.figure(figsize=(8, 8))
    
    # Draw edges
    edge_curr = edges.head
    while edge_curr is not None:
        edge = edge_curr.value
        x_values = [positions[edge[0]][0], positions[edge[1]][0]]
        y_values = [positions[edge[0]][1], positions[edge[1]][1]]
        plt.plot(x_values, y_values, 'r-', linewidth=1)  # Blue lines for edges
        edge_curr = edge_curr.next
    
    # Draw vertices
    for label in labels:
        x, y = positions[label]
        plt.plot(x, y, 'bo', markersize=30)  # Red circles for nodes
        plt.text(x, y, label, ha='center', va='center', color='white')  # Label in center
    
    # Set plot properties
    plt.title(f"Graph Visualization {extra_title}")
    plt.axis('equal')  # Equal aspect ratio
    plt.axis('off')    # Hide axes
    plt.show()
