# has-a 객체합성
# 현실상황을 객체합성이라는 기법을 사용하여 해결한다.

class Gun:
    def __init__(self, kind):
        self.kind = kind

    def bang(self):
        print("빵야빵야")


# 객체합성
class Police():
    def __init__(self, gun_kind = ''):
        if gun_kind:
            self.gun = Gun(gun_kind)
            # Gun 클래스의 인스턴스객체를 생성하여 Police의 인스턴스 멤버로 할당함
        else:
            self.gun = None 
            # gun이라는 인스턴스 멤버는 있지만 값은 없는 상태

    def get_gun(self, gun_kind):
        self.gun = Gun(gun_kind)

    def shoot(self):
        if self.gun:
            self.gun.bang()
        else:
            print("당신에게는 총이 없습니다.")

if __name__ == "__main__":
    p1 = Police('리볼버')
    print(p1.gun.kind)
    p1.shoot()

    p2 = Police()
    p2.shoot()
    p2.get_gun('기관총')
    p2.shoot()
