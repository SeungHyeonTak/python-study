# __init__ -> 생성자란?

#class Member:
#    def setInfo(self, _id, _password):
#        self.id = _id
#        self.passowd = _password
#
#    def getInfo(self):
#        print(f"id = {self.id}, passwod = {self.password}")
#
#if __name__ == "__main__":
#    mem = Member()
#    mem.setInfo("abcd", 1111)
#    mem.getInfo()

## 위의 코드처럼 setInfo를 해준다음 getInfo를 실행해주면 문제는 없다
## 하지만 setInfo를 실행하지 않고 getInfo를 실행한다면
## 인스턴스에 특성이 없다는 Error를 만나고 말것이다.
## 이러한 오류를 줄이기 위해 생성 초기에 변수를 지정해주는것을 도와주는 __init__
## 이라는 함수를 쓸 수 있다.
## 이는 초기화 메서드 / 생성자라고 불린다.

## 쓰이는 방법은 밑에 코드에서 볼 수 있다.

class Member:
    def __init__(self, _id, _password):
        self.id = _id
        self.password = _password

    def getInfo(self):
        print(f"id = {self.id}, pw = {self.password}")

if __name__ == "__main__":
    mem = Member("abcd", 1234) # 함수가 만들어질때 init함수가 호출되는걸 알 수 있다.
    mem.getInfo() # 이로써 setInfo가 없어도 이런식으로 실행될 수 있다.
