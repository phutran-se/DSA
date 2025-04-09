"""
Funct.py - Some ultil functions (print)

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
"""


import csv
import numpy as np

# ------------------------------------------------------------------------------
class DSAHashEntry:
    def __init__(self, key="", value=None):
        self.key = key
        self.value = value
        self.state = 0 if key == "" else 1  # 0: never used, 1: used, -1: formerly used

# ------------------------------------------------------------------------------
class DSAHashTable:
    def __init__(self, table_size):
        self.size = self._next_prime(table_size)
        self.hash_array = self._create_array(self.size)
        self.count = 0
        self.MAX_STEP = 7  # Small prime number for double hashing

    def _create_array(self, size):
        # Create NumPy array and initialize with DSAHashEntry objects
        arr = np.empty(size, dtype=object)
        for i in range(size):
            arr[i] = DSAHashEntry()
        return arr

    def _hash(self, key):
        # Primary hash function (using Java's hashCode style)
        hash_idx = 0
        for i in range(self._str_length(key)):
            hash_idx = (31 * hash_idx) + ord(key[i])
        return hash_idx % self.size

    def _step_hash(self, key):
        # Secondary hash function for double hashing (FNV-style)
        hash_idx = 0
        for i in range(self._str_length(key)):
            hash_idx = (hash_idx * 16777619) ^ ord(key[i])
        step = self.MAX_STEP - (hash_idx % self.MAX_STEP)
        return step if step != 0 else 1  # Ensure step is never 0

    def _str_length(self, string):
        # Custom length function
        length = 0
        for _ in string:
            length += 1
        return length

    def _next_prime(self, start_val):
        # Find the next prime number after start_val
        if start_val < 2:
            return 2
        prime_val = start_val + (1 if start_val % 2 == 0 else 0)
        while True:
            prime_val += 2
            is_prime = True
            i = 3
            while i * i <= prime_val:
                if prime_val % i == 0:
                    is_prime = False
                    break
                i += 2
            if is_prime:
                return prime_val

    def _find_slot(self, key, insert=False):
        # Find slot for key using double hashing
        hash_idx = self._hash(key)
        step = self._step_hash(key)
        probes = 0
        
        while True:
            entry = self.hash_array[hash_idx]
            if insert and (entry.state == 0 or entry.state == -1):
                return hash_idx
            elif not insert and entry.state == 0:
                return -1
            elif entry.state == 1 and entry.key == key:
                return hash_idx
            
            hash_idx = (hash_idx + step) % self.size
            probes += 1
            if probes >= self.size:
                return -1 if not insert else hash_idx

    def put(self, key, value):
        # Insert key-value pair
        if self.get_load_factor() >= 0.7:  # Upper threshold
            self._resize(self.size * 2)
        
        idx = self._find_slot(key, True)
        if idx == -1:
            raise Exception("Hash table is full")
        
        entry = self.hash_array[idx]
        if entry.state != 1:  # New entry
            self.count += 1
        entry.key = key
        entry.value = value
        entry.state = 1

    def get(self, key):
        # Retrieve value by key
        idx = self._find_slot(key, False)
        if idx == -1 or self.hash_array[idx].state != 1:
            raise KeyError("Key not found")
        return self.hash_array[idx].value

    def has_key(self, key):
        # Check if key exists
        idx = self._find_slot(key, False)
        return idx != -1 and self.hash_array[idx].state == 1

    def remove(self, key):
        # Remove key-value pair
        idx = self._find_slot(key, False)
        if idx == -1 or self.hash_array[idx].state != 1:
            raise KeyError("Key not found")
        
        self.hash_array[idx].state = -1  # Mark as formerly used
        self.count -= 1
        
        if self.get_load_factor() < 0.3 and self.size > 10:  # Lower threshold
            self._resize(self.size // 2)

    def get_load_factor(self):
        # Calculate current load factor
        return self.count / self.size

    def _resize(self, new_size):
        # Resize the hash table
        old_array = self.hash_array
        old_size = self.size
        self.size = self._next_prime(new_size)
        self.hash_array = self._create_array(self.size)
        self.count = 0
        
        # Rehash all existing entries
        for i in range(old_size):
            entry = old_array[i]
            if entry.state == 1:
                self.put(entry.key, entry.value)

    def save_to_csv(self, filename):
        # Save hash table to CSV file
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for i in range(self.size):
                entry = self.hash_array[i]
                if entry.state == 1:
                    writer.writerow([entry.key, entry.value])

    def load_from_csv(self, filename):
        # Load hash table from CSV file
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            header = True
            for row in reader:
                if header:
                    header = False
                    continue
                if self._str_length(row) >= 2: # check components is 2
                    self.put(row[0], row[1])