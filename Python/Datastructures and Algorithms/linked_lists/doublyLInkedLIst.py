from collections import deque



class Node:
    def _init_(self, data):
        self.data = data
        self.next = None
        self.pre = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        # 1 & 2: Allocate the Node & Put in the data
        new_node = Node(data=new_data)

        # 3. Make next of new node as head and previous as NULL
        new_node.next = self.head
        new_node.prev = None

        # 4. change prev of head node to new node
        if self.head is not None:
            self.head.prev = new_node

        # 5. move the head to point to the new node
        self.head = new_node

    def print_list(self):
        node = self.head
        while node:
            print(node.data, end=" ")
            node = node.next
        print()

# Create a new DoublyLinkedList
dll = DoublyLinkedList()

# Add nodes to the list
dll.push(10)
dll.push(20)
dll.push(30)

dll.print_list()
