# UNEX Data Structures and Algorithms 2025
# SinglyLinkedList.py
# Singly Linked List in Python

# Class Node represents a single node with its data and next pointer
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Class LinkedList represents the entire list using a head as the first node
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insertAtPosition(self, data, index):
        if index == 1:
            self.insertAtBeginning(data)
            return
        position = 1
        current_node = self.head
        while current_node is not None and position + 1 != index:
            position += 1
            current_node = current_node.next
        if current_node is not None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")

    def deleteAtBeginning(self):
        if self.head is None:
            return
        self.head = self.head.next

    def deleteAtEnd(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current_node = self.head
        while current_node.next and current_node.next.next:
            current_node = current_node.next
        current_node.next = None

    def deleteAtPosition(self, position):
        temp = self.head
        prev = None
        if temp is None:
            return
        if position == 1:
            self.head = temp.next
            return
        for i in range(1, position):
            prev = temp
            temp = temp.next
            if temp is None:
                print("Data not present")
        if temp is not None:
            prev.next = temp.next

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def length(self):
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size

    def get(self, index):
        if self.head is None:
            return -1
        if index < 1:
            return -1
        if index == 1:
            return self.head.data
        current_node = self.head
        position = 1
        while current_node is not None and current_node.next is not None and position != index:
            position += 1
            current_node = current_node.next
        if current_node is None:
            return -1
        return current_node.data
    
    def find(self, data):
        if self.head is None:
            return False
        if self.head.data == data:
            return True
        current_node = self.head
        while current_node is not None and current_node.next is not None:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False
    
if __name__ == "__main__":
    llist = LinkedList()
    
    print("Inserting 5 at Beginning of empty list")
    llist.insertAtBeginning(5)
    llist.traverse()

    print("Inserting 3 at Beginning")
    llist.insertAtBeginning(3)
    llist.traverse()

    print("Inserting 4 at Beginning")
    llist.insertAtBeginning(4)
    llist.traverse()

    print("Inserting 2 at End")
    llist.insertAtEnd(2)
    llist.traverse()

    print("Inserting 6 at End")
    llist.insertAtEnd(6)
    llist.traverse()

    print("Inserting 1 at position 2")
    llist.insertAtPosition(1, 2)
    llist.traverse()

    print("Length of linked list = ", llist.length())    

    print("Deleting at Beginning")
    llist.deleteAtBeginning()
    llist.traverse()

    print("Deleting at End")
    llist.deleteAtEnd()
    llist.traverse()

    print("Deleting at Position 2")
    llist.deleteAtPosition(2)
    llist.traverse()

    print("Length of linked list = ", llist.length())    

    print("Getting Data at Postion 1 = ", llist.get(1))
    print("Getting Data at Postion 2 = ", llist.get(2))
    print("Getting Data at Postion 5 = ", llist.get(5)) 

    print("Finding 5 = ", llist.find(5))
    print("Finding 3 = ", llist.find(3))
