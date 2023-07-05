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

    def first_remove(self):
        self.head = self.head.next
        cur = self.head
        while cur.next:
            cur = cur.next

    def last_remove(self):
        cur = None
        while self.head:
            cur = Node(self.head.data, cur)
            self.head = self.head.next
        self.head = cur
        self.head = self.head.next
        tmp = None
        while self.head:
            tmp = Node(self.head.data, tmp)
            self.head = self.head.next
        self.head = tmp

    def remove_data(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                cur.next = cur.next.next
            cur = cur.next

    def remove_position(self, position):
        index = 2
        cur = self.head
        if position == 1:
            self.head = self.head.next
        while cur.next:
            cur = cur.next
            if index == position:
                cur.next = cur.next.next
            index += 1


