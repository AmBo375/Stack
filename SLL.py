class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        tmp = self.head
        while tmp:
            print(tmp.data)
            tmp = tmp.next

    def start_item(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            node.next = self.head
            self.head = node

    def end_item(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            tmp = self.tail
            tmp.next = node
            self.tail = node

    def remove_start(self):
        if self.head is None:
            print("No items on this list")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None

    def remove_end(self):
        if self.head is None:
            print("No items on this list")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            tmp = self.head
            while tmp.next != self.tail:
                tmp = tmp.next
            tmp.next = None
