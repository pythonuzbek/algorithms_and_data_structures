class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = Node(0)

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=' ')
            cur = cur.next

    def list_to_linked_list(self, list):
        cur = self.head
        for i in list:
            cur.next = Node(i)
            cur = cur.next
        self.head = self.head.next




    def insert(self, value, position):
        cur = Node(0)
        cur.next = self.head
        self.head = cur
        new_node = Node(value)
        cur = self.head
        for i in range(position):
            cur = cur.next
        new_node.next = cur.next
        cur.next = new_node
        self.head = self.head.next