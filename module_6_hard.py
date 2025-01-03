from functools import reduce
from math import sqrt

class Figure():
    sides_count = 0

    def __init__(self, __color, *__sides, filled=True):
        self.__sides = self.__is_valid_sides(__sides)
        self.__color = list(__color)
        self.filled = filled

    def __is_valid_sides(self, __sides, retry=False):
        sides_int = True
        for i in __sides:
            if not isinstance(i, int) or i<0:
                sides_int = False
        if sides_int:
            if len(__sides) == 1 and isinstance(self, Cube):
                return [__sides[0] for x in range(0, 12)]
            elif len(__sides) == self.sides_count:
                return [x for x in __sides]
            elif len(__sides) != self.sides_count and retry==False:
                return [1 for x in range(1,self.sides_count+1)]
            else:
                False
        else:
            False

    def get_color(self):
        return self.__color

    def __is_valid_color(self,list_rgb):
        valid_color = [x for x in list_rgb if isinstance(x, int) and x >= 0 and x < 256]
        if len(valid_color) == 3:
            return True

    def set_color(self, r, g, b):
        list_rgb = [r,g,b]
        if self.__is_valid_color(list_rgb):
            self.__color = list_rgb

    def get_sides(self):
        return self.__sides

    def __len__(self):
        if isinstance(self, Circle):
            return self.__sides[0]
        else:
            perimeter = reduce(lambda a, x: a+x, self.__sides)
            return perimeter

    def set_sides(self, *new_sides):
        old_sides = self.__sides
        self.__sides = self.__is_valid_sides(new_sides, retry=True)
        if not self.__sides:
            self.__sides = old_sides

class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, *__sides, filled=True):
        super().__init__(__color, *__sides)
        self.__radius = __sides[0] / ( 2 * 3.14)

    def get_square(self):
        return f'Площадь круга: {round(3.14 * self.__radius ** 2, 2)}'

class Triangle(Figure):
    sides_count = 3
    def __init__(self, __color, *__sides, filled=True):
        super().__init__(__color, *__sides)
        self.__sides = __sides

    def get_square(self):
        p = super().__len__() / 2
        return f'Площадь треугольника: {round(sqrt(p*(p-self.__sides[0])*(p-self.__sides[1])*(p-self.__sides[2])),2)}'

class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, *__sides, filled=True):
        super().__init__(__color, *__sides)
        self.__sides = __sides

    def get_volume(self):
        return f'Объем куба: {round(self.__sides[0] ** 3, 2)}'

#Основная программа
circle1 = Circle((200, 200, 100), 10)
c2 = Circle((200, 200, 100), 10, 15, 6)
t1 = Triangle((200, 200, 100), 10, 6)
cu1 = Cube((200, 200, 100), 9)
cu2 = Cube((200, 200, 100), 9, 12)
cube1 = Cube((222, 35, 130), 6)
print(cu2.get_sides())
print(t1.get_sides())

circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())
cu1.set_sides(5) # Изменится
print(cu1.get_sides())


print(f'Периметр круга, это длина окружности:: {len(circle1)}') # Проверка периметра (круга), это и есть длина
print(f'Периметр куба: {len(cube1)}') # Периметр куба
triangle1 = Triangle((213,222,170), 40,20,35)
triangle1.set_sides(10,15,20)
print(f'Периметр треугольника: {len(triangle1)}') # Периметр треугольника
print(triangle1.get_square()) # Площадь треугольника
print(cube1.get_volume()) # Проверка объёма (куба)
