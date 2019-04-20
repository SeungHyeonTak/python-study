# 클래스에서 self란

class Car:
    honk = "빵빵"

    def set_info(self, color, year):
        self.color = color
        self.year = year
        # self는 객체내의 정보를 저장하거나 불러올수 있음.

    def get_info(self):
        print(f"color : {self.color}, year : {self.year}")

if __name__ == "__main__":
    my_car = Car()
    my_car.set_info("Red", 2019) # color / year 값 저장
    my_car.get_info() # get_info를 호출함으로써 값이 출력되는걸 알 수 있음
