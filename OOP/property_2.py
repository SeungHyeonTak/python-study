# property 두번째 예시

class rainbow:
    def __init__(self):
        self.COLORS = ['빨', '주', '노', '초', '파', '남', '보']
        self._colors = self.COLORS

    @property
    def colors(self):
        print("getter 실행!")
        return self._colors

    @colors.setter
    def colors(self, color_set_list):
        print("setter 실행")
        self._colors = [color for color in color_set_list if color in self.COLORS]

if __name__ == "__main__":
    my_rainbow = rainbow()

    my_rainbow._colors
    print(my_rainbow.colors)

    my_rainbow.colors = ['흰', '검', '빨', '주', '노','보']

    my_rainbow._colors
    print(my_rainbow.colors)
