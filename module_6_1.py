class Animal:
    fed = False
    alive = True

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

    def __str__(self):
        if self.alive == False:
            return f'{self.name} умер'
        elif self.alive == True and self.fed == True:
            return f'{self.name} живой и сытый'
        elif self.alive == True and self.fed == False:
            return f'{self.name} живой, но голодный'

class Plant:
    edible = False
    def __init__(self, name):
        self.name = name
    pass

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True

#Основная программа
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
print(a1)
print(a2)
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
print(a1)
print(a2)