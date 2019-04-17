# 자료구조
# Stack

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)

        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return None

        res_data = self.top.data
        self.top = self.top.next

        return res_data

    def empty(self):
        if not self.top:
            return True
        else:
            return False

    def peek(self):
        if self.empty():
            return False

        return self.top.data

if __name__ == "__main__":
    s = Stack()

    s.push(1)
    s.push(2)
    s.push(3)
    print(f'pop : {s.pop()}')
    print(f'peek : {s.peek()}')

    while not s.empty():
        print(s.pop(), end=' ')
