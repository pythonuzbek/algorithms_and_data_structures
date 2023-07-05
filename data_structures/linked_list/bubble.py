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

    def bubble(self):
        cur = self.head
        total = 0
        while cur.next:
            total += 1
            cur = cur.next

        i = 0
        while i < total:
            j = 0
            cur = self.head
            while j < total - i:
                if cur.data > cur.next.data:
                    cur.data, cur.next.data = cur.next.data, cur.data
                cur = cur.next
                j += 1
            i += 1
        a = self.head.data

        i = 0
        while i < total:
            j = 0
            cur = self.head
            while j < total - i:
                if cur.data < cur.next.data:
                    cur.data, cur.next.data = cur.next.data, cur.data
                cur = cur.next
                j += 1
            i += 1
        return self.head.data + a