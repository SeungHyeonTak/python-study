#자료구조
##queue __node로 구현

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        res = self.front.data
        self.front = self.front.next
        return res

    def peek(self):
        if self.front != None:
            return self.front.data
        else:
            return None

    def is_empty(self):
        if not self.front:
            return True
        return False

if __name__ == "__main__":
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.dequeue()
    print(f"peek data : {q.peek()}")

    while not q.is_empty():
        print(q.dequeue(), end = " ")
    print("\n")
