# property (getter / setter)
# 클래스변수는 생성자 오버로딩시 유용하게 사용됨

# 내생각인데 그냥 일반적인 getter / setter 인데 더 간단하게 구현할 수 있는 방법인것같다

# @property를 사용하는 목적
# 1. 변수를 변경 할 때 어떠한 제한을 두고 싶어서
# 2. get, set 함수를 만들지 않고 더 간단하게 접근하게 하기 위해서
# 3. 하위호환성에 도움이 됨

class Person:
    def __init__(self, name, mon):
        self.name = name
        self.money = mon # property메소드 money에 mon 할당

    @property # 값을 가져오는 메서드 
    def money(self):
        print("getter 실행!")
        return self._money # 클래스의 ._money 변수값 리턴

    # setter 함수 - 멤버변수 _money 설정 및 변경
    @money.setter # 값을 저장하는 메서드
    def money(self, how_much):
        print("setter 실행!")
        if how_much < 0:
            self._money = 0 #클래스의 ._money 변수값 할당
        else:
            self._money = how_much # 클래스의 ._money 변수값 할당

    def __str__(self):
        return "name : {}, money : {}".format(self.name, self._money)

if __name__ == "__main__":
    p1 = Person("monkey", -500)
    
    p1.money
    print(p1._money)

    p1.money = 50 # 인스턴스.속성 형식으로 접근하여 값 저장
    
    p1.money
    print(p1._money) # 인스턴스.속성 형식으로 값을 가져옴
