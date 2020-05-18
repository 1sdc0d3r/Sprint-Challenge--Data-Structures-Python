class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)
        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        current = self.head
        while current:
            if current.get_value() == value:
                return True
            current = current.get_next()
        return False

    def reverse_list(self, node, prev=None):
        self.head = None
        while node is not None:
            self.add_to_head(node.value)
            node = node.next


list = LinkedList()
list.add_to_head(1)
list.add_to_head(2)
list.add_to_head(3)
list.add_to_head(4)
list.add_to_head(5)

# print(list.head.value)
list.reverse_list(list.head)
