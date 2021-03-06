"""This is a library for linked lists"""


class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node
        else:
            self.head = new_node

    def show(self):
        linked_list = []
        current = self.head
        while current.next_node is not None:
            current = current.next_node
            linked_list.append(current.data)
        print(linked_list)

    def index(self, index):
        i = -1
        current = self.head
        while index != i:
            current = current.next_node
            i += 1
        return current.data

    def deleteFirst(self):
        current = self.head
        self.head = current.next_node
