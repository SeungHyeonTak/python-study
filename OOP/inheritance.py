# 상속
# 클래스에서 상속이란 물려주는 클래스(Parent class, Super class)의 내용을 물려받는 클래스(Child class, sub class)가 가지게 되는 내용
# 자식클래스를 선언할때 소괄호 부모클래스를 포함시킨다.

class Country: # 부모클래스
    """ Super class """

    name = "국가명"
    population = "인구"
    capital = "수도"

    def show(self):
        print("국가 클래스의 메소드입니다.")

class Korea(Country): # 자식 클래스 (부모클래스)
    """ Sub class """

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("국가의 이름은 : ", self.name)

if __name__ == "__main__":
    a = Korea("대한민국")
    a.show()
    a.show_name()

    print(a.capital)
    print(a.name)
