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

    def merge_list(self, l1, l2):
        cur = self.head
        for i in l1:
            cur.next = Node(i)
            cur = cur.next
        self.head = self.head.next
        for j in l2:
            cur.next = Node(j)
            cur = cur.next

    def mergeTwoLists(self, list1, list2):
        head = Node()
        tmp = head
        while list1 and list2:
            if list1.val < list2.val:
                tmp.next = Node(list1.val)
                list1 = list1.next
            else:
                tmp.next = Node(list2.val)
                list2 = list2.next
            tmp = tmp.next
        if list1:
            tmp.next = list1
        if list2:
            tmp.next = list2

        return head.next
