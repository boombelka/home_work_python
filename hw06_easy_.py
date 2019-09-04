# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
print('Задача 1')
import math
class Treugolnik:
    def __init__(self, x1 , x2, x3, y1, y2, y3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.l1 = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        self.l2 = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
        self.l3 = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)

    def area(self):
        abc = self.l1 + self.l2 + self.l3
        poluperimetr = abc/2
        s = (poluperimetr * (poluperimetr - self.l1) * (poluperimetr - self.l2) * (poluperimetr - self.l3))**-2
        return s

    def perimetr(self):
        p = self.l1 + self.l2 + self.l3
        return(p)

    def higth(self):
        h = 2 * self.area() / self.l1
        return(h)


n = Treugolnik(1, 3, 3, 2, 4, 1).area()
p = Treugolnik(1, 3, 3, 2, 4, 1).perimetr()
h = Treugolnik(1, 3, 3, 2, 4, 1).higth()
print(n)
print(p)
print(h)

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
print('Задание 2')
class Trapeciy:
    def __init__(self, x1 , x2, x3, x4, y1, y2, y3,  y4):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.y4 = y4
        self.l1 = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        self.l2 = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
        self.l3 = math.sqrt((x3 - x4) ** 2 + (y3 - y4) ** 2)
        self.l4 = math.sqrt((x4 - x1) ** 2 + (y4 - y1) ** 2)

    def perinetr(self):
        p = self.l1 + self.l2 + self.l3 + self.l4
        return (p)

    def higth(self):
        h = math.sqrt(self.l1**2 - ((self.l2 - self.l4) / 4))
        return(h)

    def area(self):
        s = self.higth() * (self.l2 + self.l4)
        return(s)

    def proverka(self):
        if self.l1 == self.l3:
            prov = 'Трапеция'
        else:
            prov = 'Не Трапеция'
        return (prov)

p = Trapeciy(1, 2, 3, 4, 2, 5, 5, 2).perinetr()
h = Trapeciy(1, 2, 3, 4, 2, 5, 5, 2).higth()
s = Trapeciy(1, 2, 3, 4, 2, 5, 5, 2).area()
pr = Trapeciy(1, 2, 3, 4, 2, 5, 5, 2).proverka()
print(p)
print(h)
print(s)
print(pr)