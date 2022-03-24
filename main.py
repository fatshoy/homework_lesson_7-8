from abc import ABC, abstractmethod


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line:                                  # composition
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def length(self):                        # расстояние между точками по теореме пифагора
        return ((self.point_1.x - self.point_2.x)**2 + (self.point_1.y - self.point_2.y)**2)**0.5


class Shape(ABC):                            # абстрактный класс

    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimetr(self):                     # абстрактные геттеры (property)
        pass


class Square(Shape, Line):

    def __init__(self, side):
        #super(Line).__init__()
        self.side = side.length()

    @property
    def area(self):
        return self.side ** 2

    @property
    def perimetr(self):
        return self.side * 4


class Rect(Shape):

    def __init__(self, a, b, c, d):
        self.side1 = Line(a,b)
        self.side2 = Line(c,d)

    @property
    def area(self):
        return self.side1.length() * self.side2.length()

    @property
    def perimetr(self):
        return 2 * self.side1.length() + 2 * self.side2.length()


class Cube(Square):

    def __init__(self, side):
        self.side = side.length()

    def volume(self):
        return self.side ** 3
