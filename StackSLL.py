from SLL import *


class StackSLL:
    def __init__(self):
        self.stack = None
        self.size = 0

    def push(self, data):
        self.stack = SLinkedList()
        self.stack.start_item(data)
        self.size += 1

    def pop(self):
        self.stack = SLinkedList()
        self.stack.remove_start()
        self.size -= 1

    def is_empty(self):
        if self.stack.head is None:
            return True
        else:
            return False

    def peek(self):
        if self.is_empty():
            return None
        else:
            temp = self.stack.head
            return temp.data

    def size(self):
        return self.size

    def display(self):
        self.stack.display()

    def clean(self):
        self.stack = None
