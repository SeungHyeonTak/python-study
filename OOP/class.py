# class member / instance member / symbol table 
class Point:
    # class member
    a = 10
    def __init__(self, _x, _y):
        # instance member
        self.x = _x
        self.y = _y
        # self 란 이 함수를 부르는 객체가 해당 클래스의 인스턴스인지 확인해 주기위한 장치
        # 단순히 확인한는것에서 나아가 self를 이용하여 객체내의 정보를 저장하거나 불러올 수 있음

    @classmethod
    def class_method(cls): # class method
        print("클래스 메소드 호출", cls.a)

    def instance_func(self): # instance method
        print("인스턴스 메소드 호출")

    def __str__(self):
        return f"({self.x}, {self.y})"

if __name__ == "__main__":
    #Point.instance_func() # 인스턴스 메소드는 인스턴스가 있어야 실행가능함
    Point.class_method()

    p1 = Point(1, 2)
    # __dict__ 를 통해서 객체의 심볼 테이블을 확인 가능하다.
    print(f"instance symbol table : {p1.__dict__}") # 인스턴스의 심볼 테이블 확인

    # 변수의 이름과 데이터주소를 저장하는 테이블을 심볼 테이블이라고 한다.
    print(f"class symbol table : {Point.__dict__}") # 클래스의 심볼 테이블 확인

    # 참고할만한 사항
    # >> 인스턴스가 클래스 변수에 접근하여 수정할 수 없다.
    print(Point.a)
    print(p1.a)
    #p1.a = 5 # 인스턴스 멤버 생성
    Point.a = 20 # 하지만 class member의 변경은 가능함
    print(Point.a) # 클래스 멤버 a는 수정되지 않음
    print(p1.a)
    print(p1.__dict__)

    # instance member 끼리는 변경가능
    print(f"x : {p1.x}, y : {p1.y}")
    p1.x = 3
    p1.y = 4
    print(f"x : {p1.x}, y : {p1.y}")

    print(p1.__dict__)

