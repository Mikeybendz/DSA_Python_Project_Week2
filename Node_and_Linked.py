'''This code defines a Node class and a LinkedList class to implement a simple linked list data structure. The Node class has a value
and a reference to the next node, while the LinkedList class provides methods to append new nodes,
remove nodes by value, search for values, count the number of nodes, and get a list of all values in the linked list. 
The code also includes instantiation of nodes and a linked list, as well as demonstration of the LinkedList methods.

Student Name: Michael Bender
Student ID: 2514766
'''

# Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
    # method to append a new node to the end of the list
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    # method to remove a node with the specified value from the list
    def remove(self, value):
        if self.head and self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current and current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next
    # method to search for a value in the list and return True if found, otherwise False
    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            print(f"Comparing {current.value} with target value {value}")
            current = current.next
        print(f"No match found for value {value}")
        return False
    # method to count the number of nodes in the list and return the count
    def count(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    # method to get a list of all values in the linked list and return it
    def get_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result
# Error fix. Didnt require the explicit node instantiation for the linked list!
# Instantiate linked lists
linked_list = LinkedList()
linked_list.append(10)
print(linked_list.get_list()) # Print for verification, should print [10]
linked_list.append(20)
print(linked_list.get_list())  # Should print [10, 20]

# Use LinkedList methods
print(linked_list.get_list())  # [10, 20]
print(linked_list.search(20))  # Should print True
print(linked_list.count())  # Should print 2
