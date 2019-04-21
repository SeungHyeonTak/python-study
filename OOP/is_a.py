# OOP_ is-a 상속
# 상속에서 쓰이는 개념
# 같은 이름의 함수가 있으면 자식의 함수가 우선

class Computer: # 부모클래스 - Super class
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def calculate(self, money):
        self.money = money
        print("컴퓨터 계산중" + self.money)

    def __str__(self): # java로 치면 String() 함수 
        return "나는 컴퓨터 입니다."

class Notebook(Computer): # 자식클래스 Computer를 상속 받음
    def __init__(self, cpu, ram, touch = 'normal', cam = 'small'):
        # 1. 클래스 이름으로 접근
        Computer.__init__(self, cpu, ram)
        self.touch = touch
        self.cam = cam

    def calculate(self, money): # 오버라이딩 - 같은 이름의 함수가 있으면 자식의 함수가 우선
        self.money = money
        print('노트북 계산중')
        print(f"money = {self.money}")

    def __str__(self):
        return super(Notebook, self).__str__() + "그리고 난 노트북이죠!"

class Desktop(Computer):
    def __init__(self, cpu, ram, external_graphic = "Geforce"):
        # 2. super()로 접근
        super(Desktop, self).__init__(cpu, ram)
        
        # super(type, obj) -> bound super object; requires isintance(obj, type)
        self.external_graphic = external_graphic

    def calculate(self, money): # 오버라이딩
        self.money = money
        print("데스크탑 계산중")
        print(f"money = {self.money}")
    
    def __str__(self):
        return super().__str__() + "그리고 난 데스크탑이죠!"

if __name__ == "__main__":
    note = Notebook("i7", 8)
    print(note)
    note.calculate(1000)

    desk = Desktop("i9", 16)
    print(desk)
    desk.calculate(2000)
