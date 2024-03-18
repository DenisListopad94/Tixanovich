"""
1.	Определить класс «Шахматная фигура» с ее координатами на шахматной доске, ее цветом (черный или белый),
виртуальным методом «битья» другой фигуры, и унаследовать от него классы, соответствующие шахматным фигурам
«Ферзь», «Пешка», «Конь». Написать виртуальные методы «битья» другой фигуры, которые принимают координаты другой
фигуры и определяют, может ли данная фигура «бить» фигуру с теми (принятыми) координатами.

from abc import ABC, abstractmethod


class ChessFigure(ABC):

    def __init__(self, x: int, y: int, color: str):
        self.x = x
        self.y = y
        self.color = color

    @abstractmethod
    def attack(self, x_1: int, y_1: int):
        pass


class Queen(ChessFigure):
    def attack(self, x_1: int, y_1: int):
        if self.x + self.y == x_1 + y_1 or ((self.x == x_1) or
        (self.y == y_1)) or (self.x - self.y) == (x_1 - y_1):
            print("The queen threatens the square")
        else:
            print("The queen does not threaten the square")


class Pawn(ChessFigure):
    def attack(self, x_1: int, y_1: int):
        if self.color == "white":
            if (self.x - x_1 == 1 and self.y - y_1 == 1) or (self.x - x_1 == 1 and self.y - y_1 == -1):
                print("The pawn threatens the square")
            else:
                print("The pawn does not threaten the square")
        if self.color == "black":
            if (self.x - x_1 == -1 and self.y - y_1 == 1) or (self.x - x_1 == -1 and self.y - y_1 == -1):
                print("The pawn threatens the square")
            else:
                print("The pawn does not threaten the square")


class Knight(ChessFigure):
    def attack(self, x_1: int, y_1: int):
        dx = abs(self.x - x_1)
        dy = abs(self.y - y_1)
        if dx == 1 and dy == 2 or dx == 2 and dy == 1:
            print("The knight threatens the square")
        else:
            print("The knight does not threaten the square")


queen = Queen(x=5, y=3, color="black")
queen.attack(x_1=3, y_1=2)

pawn = Pawn(x=5, y=5, color="white")
pawn.attack(x_1=6, y_1=4)
pawn_1 = Pawn(x=2, y=4, color="black")
pawn_1.attack(x_1=3, y_1=3)

knight = Knight(x=4, y=5, color="black")
knight.attack(x_1=2, y_1=5)
___________
2.	Создать базовый класс «Грузоперевозчик» и производные классы «Самолет», «Поезд», «Автомобиль».
Определить время и стоимость перевозки для указанных городов и расстояний.


class CargoCarrier:
    def __init__(self, departure_city: str, destination_city: str, distance: int, speed: int):
        self.departure_city = departure_city
        self.destination_city = destination_city
        self.distance = distance
        self.speed = speed

    def transport(self):
        pass


class Airplane(CargoCarrier):
    def transport(self):
       time = self.distance / self.speed
       cost = time * 2000
       print(f"{__class__.__name__}: time - {time}, cost - {cost}")


class Train(CargoCarrier):
    def transport(self):
        time = self.distance / self.speed
        cost = time * 300
        print(f"{__class__.__name__}: time - {time}, cost - {cost}")


class Car(CargoCarrier):
    def transport(self):
        time = self.distance / self.speed
        cost = time * 100
        print(f"{__class__.__name__}: time - {time}, cost - {cost}")

airplane = Airplane("Sity_1", "Sity_2", 700, 1000)
train = Train("Sity_1", "Sity_2", 700, 200)
car = Car("Sity_1", "Sity_2", 700, 100)

airplane.transport()
train.transport()
car.transport()
___________
3.	Создать класс «Живое». Определить наследуемые классы – «лиса», «кролик» и «растение».
Лиса ест кролика. Кролик ест растения. Растение поглощает солнечный свет. Представитель
каждого класса может умереть, если достигнет определенного возраста или для него не будет еды.
Напишите виртуальные методы поедания и определения состояния живого существа (живой или нет,
в зависимости от достижения предельного возраста и наличия еды (входной параметр)).

class Living:
    def __init__(self, age, hungry=False):
        self.age = age
        self.hungry = hungry

    def eat(self, food):
        pass

    def is_alive(self):
        pass


class Fox(Living):
    def eat(self, food):
        if food.__class__ == Rabbit:
            self.hungry = False
            print("The fox ate the rabbit.")
        else:
            self.hungry = True
            print("The fox cannot eat this.")

    def is_alive(self):
        if self.age > 10 or self.hungry:
            return False
        return True

class Rabbit(Living):
    def eat(self, food):
        if food.__class__ == Plant:
            self.hungry = False
            print("The rabbit ate the plant.")
        else:
            self.hungry = True
            print("The rabbit cannot eat this.")

    def is_alive(self):
        if self.age > 5 or self.hungry:
            return False
        return True

class Plant(Living):
    def eat(self, food):
        print("The plant cannot eat.")

    def is_alive(self):
        if self.age > 10:
            return False
        return True


fox = Fox(5, hungry=True)
rabbit = Rabbit(3, hungry=True)
plant = Plant(2)

rabbit.eat(plant)
fox.eat(rabbit)

print(f"Fox is alive: {fox.is_alive()}")
print(f"Rabbit is alive: {rabbit.is_alive()}")
print(f"Plant is alive: {plant.is_alive()}")

fox.eat(None)
rabbit.eat(None)
plant = Plant(11)

print(f"Fox is alive: {fox.is_alive()}")
print(f"Rabbit is alive: {rabbit.is_alive()}")
print(f"Plant is alive: {plant.is_alive()}")
"""
