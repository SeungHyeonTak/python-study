class CQueue:
    MAXSIZE = 10  # class member

    def __init__(self):  # 생성자
        self.container = [None for _ in range(CQueue.MAXSIZE)]  # class member 쓰는법
        self.__head = 0
        self.__tail = 0

    def is_empty(self):
        if self.__head == self.__tail:
            return True
        else:
            return False

    def is_full(self):
        next = self.__step_forward(self.__tail)
        if next == self.__head:
            return True
        return False

    def enqueue(self, data):
        if self.is_full():
            raise Exception("The queue is full")
        self.container[self.__tail] = data
        # tail은 마지막 데이터의 다음을 가리킨다.
        self.__tail = self.__step_forward(self.__tail)

    def dequeue(self):
        if self.is_empty():
            raise Exception("The queue is empty")
        ret = self.container[self.__head]
        self.__head = self.__step_forward(self.__head)
        return ret

    def peek(self):
        if self.is_empty():
            raise Exception("The queue is empty")
        return self.container[self.__head]

    # 편의 함수
    def __step_forward(self, x):
        x += 1
        if x >= CQueue.MAXSIZE:
            x = 0
        return x


if __name__ == "__main__":
    cq = CQueue()

    # cq.enqueue(1)
    # cq.enqueue(2)
    # cq.enqueue(3)
    #
    # for i in range(3):
    #     print(cq.dequeue())

    for i in range(8):
        cq.enqueue(i)

    for i in range(5):
        print(cq.dequeue(), end="  ")

    for i in range(8, 14):
        cq.enqueue(i)

    while not cq.is_empty():
        print(cq.dequeue(), end="  ")

    print()
    for i in range(10):
        print(cq.container[i], end="  ")
