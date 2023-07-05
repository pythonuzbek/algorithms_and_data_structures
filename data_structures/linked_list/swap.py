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

    def swap_data(self, index, key):
        s_index = 1
        cur = self.head
        while cur.next:
            if s_index == index:
                cur.data = key
            cur = cur.next
            s_index += 1

    def swap_node(self, index, key):
        s_index = 2
        cur = self.head
        new_node = Node(key)
        while cur.next:
            if s_index == index:
                new_node.next = cur.next.next
                cur.next = new_node
            cur = cur.next
            s_index += 1
        if s_index == 1:
            self.head = Node(key)
