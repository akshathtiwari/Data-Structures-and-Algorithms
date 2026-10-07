"""
UCLA Extension - Data Structures and Algorithms - Summer 2025
Assignment #1
Author: Joe Bruin
Purpose: simple template for Python files

Command Line to Run Program:
python3 PythonTemplate.py

"""

# MyNode class which stores some data
class MyNode:
    def __init__(self, data):
        self.data = data

# MyList class which holds a single instance of MyNode
class MyList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        a_node = MyNode(value)
        if self.head is None:
            self.head = a_node

    def print(self):
        if self.head is None:
            print("EMPTY LIST")
            return
        print(self.head.data)

# Sample demo program to test above methods
def main():
    print("Example Python Demo")
    print("===================\n")

    my_list = MyList()
    print("Created New Empty List:")
    my_list.print()

    print("\nInserting Data:")
    my_list.insert(2025)
    my_list.print()

    print("\nDemo Complete")

# call main function
if __name__ == "__main__":
    main()
