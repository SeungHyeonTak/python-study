# 정적메소드 class method / static method
# 정적 메소드란? 클래스에서 직접 접근할 수 있는 method이다.
# python에서는 class에서 직접 접근할 수 있는 method가 두가지 있다 (class method와 static method)
# 하지만! 다른언어와 다르게 정적 메소드임에도 불구하고 인스턴스에서도 접근이 가능함 (※주의)

class CustomClass:
    # instance method 
    def add_instance_method(self, a, b): # instance method는 첫번째로 자신을 입력함
        return print(f"instance : {a + b}")
    
    # class method
    @classmethod
    def add_class_method(cls, a, b): # class method 는 첫번째 인자로 클래스를 입력
        return print(f"class : {a + b}")

    # static method
    @staticmethod
    def add_static_method(a, b): # static method는 특별히 추가되는 인자가 없음
        return print(f"static : {a + b}")

if __name__ == "__main__":
    CustomClass.add_instance_method(None, 3, 5) # self 자리에 None을 넣어둔것은 아직 객체내의 정보를 저장하지 않았기때문에
    
    # 밑의 method들은 객체에서 접근이 되는걸 보여주고 있음
    CustomClass.add_class_method(3,5)
    CustomClass.add_static_method(3,5)




