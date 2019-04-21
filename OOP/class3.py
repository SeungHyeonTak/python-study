# class / static method의 차이

# class method와 static method의 차이는 상속에서 두드러지게 차이가 난다.

# 상속 예제 구현

class Language: # 부모클래스
    default_language = "English"

    def __init__(self):
        self.show = "나의 언어는" + self.default_language

    @classmethod
    def class_my_language(cls):
        return cls() # class에서는 cls인자를 활용하여 클래스속성을 가져오는것을 알 수 있음
        # @classmethod로 바꾸어서 cls를 전달해서 그것으로 객체를 생성하면 Language객체를 대신해서 KoreanLanguage 객체를 돌려 받게 된다

    @staticmethod
    def static_my_language():
        return Language() # Language의 객체가 생성됨

    def print_language(self):
        print(self.show)


class KoreanLanguage(Language): # 자식클래스(부모클래스)
    default_language = "한국어"

if __name__ == "__main__":
    a = KoreanLanguage.static_my_language()
    b = KoreanLanguage.class_my_language()
    a.print_language() # English
    b.print_language() # 한국어
