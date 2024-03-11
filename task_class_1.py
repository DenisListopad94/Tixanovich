'''
1.	Создать класс с двумя переменными. Добавить функцию вывода на экран и функцию изменения этих переменных.
Добавить функцию, которая находит сумму значений этих переменных, и функцию которая находит наибольшее значение
из этих двух переменных.

class Variables:

    def __init__(self, var1: int, var2: int) -> None:
        self.var1 = var1
        self.var2 = var2

    def info_var(self) -> None:
        print(f"Variable 1: {self.var1}, Variable 2: {self.var2}")

    def change_variables(self, new_var1: int, new_var2: int):
        self.var1 = new_var1
        self.var2 = new_var2

    def sum_variables(self):
        return self.var1 + self.var2

    def max_variable(self):
        return max(self.var1, self.var2)



# 2.	Описать класс, реализующий десятичный счетчик, который может увеличивать или уменьшать свое значение на единицу
# в заданном диапазоне. Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.
# Счетчик имеет два метода: увеличения и уменьшения, — и свойство, позволяющее получить его текущее состояние.
# Написать программу, демонстрирующую все возможности класса.

class Decimal_Counter:
    MIN_VALUE = 0
    MAX_VALUE = 10

    def __init__(self, value=MIN_VALUE) -> None:
        self.value = value

    def increment(self):
        if self.value < self.MAX_VALUE:
            self.value += 1
        else:
            print("The counter has reached its maximum value")

    def decrement(self):
        if self.value > self.MIN_VALUE:
            self.value -= 1
        else:
            print("The counter has reached its minimum value")

    @property
    def current_value(self):
        return self.value


3.	Реализуйте класс Shop. Предусмотреть возможность работы с произвольным числом продуктов, поиска
продуктов по названию, добавления их в магазин и удаления продуктов из него.

class Shop:
    def __init__(self):
        self.products = {}

    def add_product(self, name):
        if name not in self.products:
            self.products[name] = {}
            print(f"Product {name} added.")
        else:
            print(f"Product {name} already exists.")

    def remove_product(self, name):
        if name in self.products:
            del self.products[name]
            print(f"Product {name} deleted.")
        else:
            print(f"Product {name} not found.")

    def find_product(self, name: str):
        if name in self.products:
            print(f"Found product {name}")
        return None

    def list_products(self):
        for name in self.products:
            print(f"Name: {name}")


shop = Shop()
shop.add_product("Meat")
shop.add_product("Bread")
shop.add_product("Milk")

shop.list_products()

shop.remove_product("Milk")

shop.find_product("Bread")

4.	Реализуйте класс MoneyBox, для работы с виртуальной копилкой. Каждая копилка имеет ограниченную
вместимость, которая выражается целым числом – количеством монет(capacity -вместимость), которые можно
положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке, предоставлять
возможность добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё какое-то количество
монет, не превышая ее вместимость.
Класс должен иметь следующий вид:
class MoneyBox:
    def__init__(self, capacity) :
    #конструктор с аргументом- вместимость копилки
    def can_add(self,v)
    #True, если можно добавить v монет, False иначе
    def add(self,v)
    #положить v монет в копилку

При создании копилки, число монет в ней равно 0.
Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True.
class MoneyBox:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.coins = 0

    def can_add(self, v: int):
        return self.coins + v <= self.capacity

    def add(self, v: int):
        if self.can_add(v):
            self.coins += v
            print(f"Added {v} coins.")
        else:
            print("Can't add coins because Money Box is full.")

    def get_coins(self):
        print(f"In Money Box {self.coins} coins")

box = MoneyBox(10)
box.add(4)
box.add(3)
box.add(4)
box.get_coins()

'''