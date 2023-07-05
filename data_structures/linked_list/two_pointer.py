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

    def two_pointer(self):
        odd = self.head
        even = self.head.next
        if odd.next == None:
            return
        t1 = odd
        t2 = even
        while t1.next and t2.next:
            t1.next = t1.next.next
            t1 = t1.next
            t2.next = t2.next.next
            t2 = t2.next
        t1.next = even
