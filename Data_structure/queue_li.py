#자료구조
##queue __list로 구현
class Queue(list): # list로 구현
    enqueue = list.append #queue를 쌓는다. stack에 push처럼

    def dequeue(self): #삭제 큐 - stack과 마찬가지로 pop으로 지운다
        de = self.pop(0) # 실수로 list.pop을 하는경우가 있는데 기본적인건 지키기
        return de

    def peek(self):
        return self[0] # queue는 처음에 들어간 data가 제일먼저 빠지므로 보여지는것이 제일 앞쪽이어야 한다

    def empty(self):#queue안에 data가 있는지 없는지 확인
        if not self:
            return True
        else:
            return False

if __name__ == "__main__":
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.dequeue() #여기서 dequeue를 하더라도 제일 처음 data가 나간다 잊지말기
    q.enqueue(3)
    print(f'peek data : {q.peek()}')

    while not q.empty():
        print(q.dequeue(), end = " ")
