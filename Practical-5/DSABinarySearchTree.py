"""
DSABinarySearchTree.py - A binary search tree implementation 

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
"""

from DSAQueue import DSAQueue

# Node class for the binary search tree
class DSATreeNode:
    def __init__(self, key, value):
        self._key   = key
        self._value = value
        self._left  = None
        self._right = None

    def get_key(self):
        """Get key of the node"""
        return self._key
    def set_key(self, new_key):
        "Set key of the node"
        self._key = new_key

    def get_value(self):
        """Get value of the node"""
        return self._value
    
    def set_value(self, new_value):
        """Set value of the node"""
        self._value = new_value

    def get_left(self):
        """Get left child of the node"""
        return self._left
    
    def set_left(self, new_left):
        """Set left child of the node"""
        self._left = new_left
    
    def get_right(self):
        """Get right child of the node"""
        return self._right
    
    def set_right(self, new_right):
        """Set right child of the node"""
        self._right = new_right

    def __str__(self):
        return f"Key: {self._key} Value: {self._value}"

# Binary Search Tree class
class DSABinarySearchTree:
    def __init__(self):
        self._root = None

    # ----------------- Insert Methods -----------------
    def insert(self, key, value):
        """Insert a new node into the tree"""
        self._root = self._insert_recursive(key, value, self._root)

    def _insert_recursive(self, key, value, cur_node):
        """Recursively insert a new node into the tree"""
        if cur_node is None:
            return DSATreeNode(key, value)
        if key == cur_node.get_key():
            raise ValueError("Duplicate key not allowed")
        elif key < cur_node.get_key():
            n = self._insert_recursive(key, value, cur_node.get_left())
            cur_node.set_left(n)
        elif key > cur_node.get_key():
            n = self._insert_recursive(key, value, cur_node.get_right())
            cur_node.set_right(n)
        return cur_node

    # ----------------- Delete Methods -----------------
    def delete(self, key):
        """Delete a node from the tree"""
        self._root = self._delete_recursive(key, self._root)

    def _delete_recursive(self, key, cur_node):
        """Recursively delete a node from the tree"""
        if cur_node is None:
            raise ValueError("Key not found")
        if key < cur_node.get_key():
            cur_node.set_left(self._delete_recursive(key, cur_node.get_left()))
        elif key > cur_node.get_key():
            cur_node.set_right(self._delete_recursive(key, cur_node.get_right()))
        else:
            if cur_node.get_left() is None:
                return cur_node.get_right()
            elif cur_node.get_right() is None:
                return cur_node.get_left()
            else:
                successor = self._promote_successor(cur_node.get_right())
                if successor != cur_node.get_right():
                    successor.set_right(cur_node.get_right())
                successor.set_left(cur_node.get_left())
                return successor
        return cur_node
    
    def _promote_successor(self, cur_node):
        """Recursively promote the successor node"""
        if cur_node.get_left() is None:
            return cur_node
        successor = self._promote_successor(cur_node.get_left())
        if successor == cur_node.get_left():
            cur_node.set_left(successor.get_right())
        return successor
    
    # ----------------- Find Methods -----------------
    def find(self, key):
        """Find a node in the tree"""
        return self._find_recursive(key, self._root)
    
    def _find_recursive(self, key, cur_node):
        """Recursively find a node in the tree"""
        if cur_node is None:
            raise ValueError("Key not found")
        if key == cur_node.get_key():
            return cur_node.get_value()
        elif key < cur_node.get_key():
            return self._find_recursive(key, cur_node.get_left())
        else:
            return self._find_recursive(key, cur_node.get_right())
        
    # ----------------- Min/Max Methods -----------------
    def min(self):
        """Find the minimum node in the tree"""
        if self._root is None:
            raise ValueError("Tree is empty")
        return self._min_recursive(self._root)

    def _min_recursive(self, cur_node):
        """Recursively find the minimum node in the tree"""
        if cur_node.get_left() is None:
            return cur_node
        return self._min_recursive(cur_node.get_left())

    def max(self):
        """Find the maximum node in the tree"""
        if self._root is None:
            raise ValueError("Tree is empty")
        return self._max_recursive(self._root)

    def _max_recursive(self, cur_node):
        """Recursively find the maximum node in the tree"""
        if cur_node.get_right() is None:
            return cur_node
        return self._max_recursive(cur_node.get_right())
    
    # ----------------- Height Methods -----------------
    def height(self):
        """Find the height of the tree"""
        return self._height_recursive(self._root)

    def _height_recursive(self, cur_node):
        """Recursively find the height of the tree"""
        if cur_node is None:
            return -1
        left_height = self._height_recursive(cur_node.get_left())
        right_height = self._height_recursive(cur_node.get_right())
        #print(f"Node: {cur_node.get_key()}, left={left_height}, right={right_height}")
        return 1 + max(left_height, right_height)

    # ----------------- Balance Methods -----------------
    def balance(self):
        """Check the balance of the tree"""
        if self._root is None:
            return 100.0
        left_height = self._height_recursive(self._root.get_left())
        right_height = self._height_recursive(self._root.get_right())
        total_height = max(left_height, right_height) + 1
        diff = abs(left_height - right_height)
        #print(f"total height: {total_height}")
        #print(f"diff: {diff}")
        return (1 - diff / total_height) * 100 if total_height > 0 else 100.0

    # ----------------- Traversal Methods -----------------
    def in_order(self):
        """In-order traversal of the tree"""
        queue = DSAQueue()
        self._in_order_recursive(self._root, queue)
        return queue.get_items()

    def _in_order_recursive(self, cur_node, queue):
        """Recursively perform in-order traversal of the tree"""
        if cur_node:
            self._in_order_recursive(cur_node.get_left(), queue)
            queue.enqueue(cur_node.get_key())
            self._in_order_recursive(cur_node.get_right(), queue)

    def pre_order(self):
        """Pre-order traversal of the tree"""
        queue = DSAQueue()
        self._pre_order_recursive(self._root, queue)
        return queue.get_items()

    def _pre_order_recursive(self, cur_node, queue):
        """Recursively perform pre-order traversal of the tree"""
        if cur_node:
            queue.enqueue(cur_node.get_key())
            self._pre_order_recursive(cur_node.get_left(), queue)
            self._pre_order_recursive(cur_node.get_right(), queue)

    def post_order(self):
        """Post-order traversal of the tree"""
        queue = DSAQueue()
        self._post_order_recursive(self._root, queue)
        return queue.get_items()

    def _post_order_recursive(self, cur_node, queue):
        """Recursively perform post-order traversal of the tree"""
        if cur_node:
            self._post_order_recursive(cur_node.get_left(), queue)
            self._post_order_recursive(cur_node.get_right(), queue)
            queue.enqueue(cur_node.get_key())

    # Display
    def display(self):
        """Display the tree using in-order, pre-order and post-order traversal"""
        print("......Inorder Traversal:", self.in_order())
        print(".....Preorder Traversal:", self.pre_order())
        print("....Postorder Traversal:", self.post_order())