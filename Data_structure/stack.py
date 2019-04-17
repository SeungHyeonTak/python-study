# 자료구조
# stack _연결리스트 구현
class Node:
    def __init__(self, data):
        self.data = data #new_node로 선언해주고 push에서 값을 받아오는 역할
        self.next = None #다음 데이터가 어떤것인지 모르기 때문에 일단 None으로 둔다

class Stack:
    def __init__(self): # 생성자
        self.top = None #제일 처음 top은 값을 가지고 있지 않는다.

    def push(self, data): #data 추가
        new_node = Node(data) #위의 Node에서 받은 data를 new_node에 선언한다.
        new_node.next = self.top # new_node의 다음으로 받을 데이터를 top을 통해 None으로 남겨둔다.
        self.top = new_node #push하고 제일 처음에 data를 받은 new_node를 top으로 지정해준다.
    
    def pop(self): # data 삭제
        ret = self.top.data # 기존의 top의 값을 알기 위해 다른 변수로 저장해둔다.
        self.top = self.top.next #pop()은 제일 마지막의 값을 먼저 내보내기 때문에 
        # 그러므로 top의 전값을 top으로 두고 기존 top의 값은 삭제시킨다.
        return ret # 값의 출력을 위해 리턴으로 남겨준다.

    def peek(self): # 현재 최상단 top의 값 나타내기
        if self.top != None: # top이 None값이 아니고 data값이 있을때 나타내기
            return self.top.data
        else:
            return None

    def empty(self): #노드안에 값이 있는지 없는지 bool로 나타내준다.
        if not self.top:
            return True
        return False

if __name__ == "__main__":
    st = Stack()

    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)
    st.pop()
    print("peek data : {}".format(st.peek()))

    while not st.empty(): # 출력을 위해 empty를 통해 값이 존재하는지 안하는지 True/False로 확인
        print(st.pop(), end = " ") # True일경우 들어와서 pop부분에 마지막 data를 통해서 알려준다.
    print('\n')
