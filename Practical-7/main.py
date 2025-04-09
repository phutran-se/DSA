"""
main.py - Entry point for the program

Student 1: Phu Tran (21985654)
Student 2: Minh Quoc Chau Cao (21803620)
"""

from DSAHashTable import DSAHashTable
from Funct import *
import numpy as np

def put_entry(hash_table, key, value):
    print(f"==== Put ({key}, {value}) ====")
    try: 
        hash_table.put(key, value)
        print_info(f"> Done: put")
    except Exception as e: 
        print_error(f"> ERROR: put, error={e}")
    print()

def find_by(hash_table, key): 
    print(f"==== Find key={key} ====")
    try: 
        found = hash_table.get(key)
        print_info(f"> Done: found ({key}, {found})")
    except Exception as e: 
        print_error(f"> ERROR: find: {key}, error={e}")
    print()

def remove_by(hash_table, key): 
    print(f"==== Remove key={key} ====")
    try: 
        hash_table.remove(key)
        print_info(f"> Done: Remove {key}")
    except Exception as e: 
        print_error(f"> ERROR: remove {key}, error={e}")
    print()

def main():
    hash_table = DSAHashTable(10)
    try:
        print("==== Load RandomNames7000.csv from current directory ==== ")
        hash_table.load_from_csv("RandomNames7000.csv")
        print_info("Loaded", hash_table.count, "entries")
        print_info("Load factor:", hash_table.get_load_factor())
        if hash_table.has_key("John"):
            print("Value for 'John':", hash_table.get("John"))
        
        if hash_table.has_key("John"):
            hash_table.remove("John")
            print("Removed 'John'")
        
        # Try to save to output
        print("\n=== Save to output.csv ====")
        hash_table.save_to_csv("output.csv")
        print_info("> Done: Saved to output.csv")
        
    except FileNotFoundError:
        print_error("RandomNames7000.csv not found. Testing with sample data:")
        sample_data = np.array([
            ["1", "Bob"],
            ["2", "Alice"],
            ["3", "Peter"],
            ["4", "Anna"]
        ], dtype=object)
        
        try: 
            for i in range(4):
                hash_table.put(sample_data[i][0], sample_data[i][1])
        except Exception as e: 
            print_error(f"ERROR: {e}")
        
        print_info("Load factor:", hash_table.get_load_factor())
        print_info("Has key=2: 'Alice':", hash_table.has_key("2"))
        print()

        find_by(hash_table, '4')
        find_by(hash_table, '5')
        
        remove_by(hash_table, '4')
        remove_by(hash_table, '4')

        print("==== save to output.csv ====")
        hash_table.save_to_csv("output.csv")
        
    except Exception as e:
        print_error(f"ERROR: {e}")

# Test main
if __name__ == "__main__":
    main()