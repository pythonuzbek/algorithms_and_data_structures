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

    def get_node(self, index):
        current = self.head
        for i in range(index):
            current = current.next
            if current is None:
                return None
        return current

    def find_total(self):
        cur = self.head
        total = 0
        while cur:
            cur = cur.next
            total += 1
        return total

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data


    def has_cycle(llist):
        slow = llist.head
        fast = llist.head
        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


