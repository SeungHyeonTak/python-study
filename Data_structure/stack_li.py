#자료구조
#stack_list로 구현
#사이즈가 부족? 그러한 이유때문에 연결리스트로 구현하는게 더 효과적이다.

class stack(list):
    push = list.append # push는 간단하게 list의 내장함수인 append를 써줌으로써 뒤에 추가하는 의미를 가지고 있다.

    def empty(self): # list안에 data가 있는지 없는지 bool로 확인하는것
        if not self:
            return True
        else:
            return False

    def peek(self): # 제일위에 어떤 데이터가 있는지 확인 고로 top에 뭐가 있는지(제일 먼저 나가는 녀석이 어떤data인지)
        return self[-1]

if __name__ == "__main__":
    s = stack()

    s.push(1)
    s.push(2)
    s.pop()  #pop은 python list 내장함수이다.
    s.push(3)
    s.push(4)
    print(f"peek data : {s.peek()}")

    while s:
        data = s.pop()
        print(data, end = "\n")
