# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return str(self.__dict__)
#
#     def __len__(self):
#         return len(self.name)
#
#     def __add__(self, other):
#         return f'{self.name}-{other.name}'
#
#     def __sub__(self, other):
#         return self.age + other.age
#
#     def __lt__(self, other):
#         return self.age < other.age
#
#
# user = User('Max', 20)
# user2 = User('Karina', 16)
# print(user)
# print(len(user))
#
# print(user+user2)
# print(user-user2)
# print(user<user2)
# print(user>user2)

#####################################

# class User:
#     __count = 0
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         User.__count += 1
#
#     def get_name(self):
#         return self.name
#
#     @staticmethod
#     def greeting():
#         print('Hello')
#
#     @classmethod
#     def get_count(cls):
#         return cls.__count
#
#
# user = User('Max', 33)
# user2 = User('Max', 33)
# user3 = User('Max', 33)
#
# print(User.get_count())

#####################################
# ДЗ

# Создать класс Rectangle:
# -конструктор принимает две стороны x,y
# -описать арифметические методы:
#   + сума площадей двух экземпляров класса
#   - разница площадей
#   == или площади равны
#   != не равны
#   >, < меньше или больше
#   при вызове метода len() подсчитывать сумму сторон


class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return f'Sum of squares =  {self.x * self.y + other.x * other.y}'

    def __sub__(self, other):
        return f'Squares difference =  {self.x * self.y - other.x * other.y}'

    def __eq__(self, other):
        return f'Squares are equal: {self.x * self.y == other.x * other.y}'

    def __ne__(self, other):
        return f'Squares are not equal: {self.x * self.y != other.x * other.y}'

    def __lt__(self, other):
        return f'Square 1 < square 2: {self.x * self.y < other.x * other.y}'
    def __gt__(self, other):
        return f'Square 1 > square 2: {self.x * self.y > other.x * other.y}'

    def __len__(self):
        return self.x * 2 + self.y * 2

rect1 = Rectangle(3, 6)
rect2 = Rectangle(2, 9)
rect3 = Rectangle(2, 3)
print(rect1 + rect3)
print(rect1 - rect2)
print(rect1 == rect2)
print(rect1 != rect2)
print(rect1 < rect3)
print(rect1 > rect3)
print(len(rect1))
print('####################################################')
###############################################################################
# 1) написати програму для запису відомостей про пасажирські перевезення
# 2) перевезення відбувається трьома способами, літаком, машиною, поїздом,
# 3) дані які треба буде зберігати:
#   - кількість пасажирів(машина)
#   - км(машина)
#   - вартість пального(машина)
#   - вартість квитка(літак, поїзд)
#   - клас:перший,другий(літак)
#   - час реєстрації(літак)
#   - місце: купе,св(поїзд)
#   - час в дорозі(всі)
# 4) методи:
#   + - розрахунок вартості доїзду(машина)
#   +- загальний час перельоту(літак)
#   + - порівняти час в дорозі між двома будь якими транспортними засобами(двома об'єктами) - наприклад"літак на 5 годин швидше за поїзд"
#   - вивести всі дані про перевезення(поїзд)
#
class Vehicle:
    def __init__(self, name: str, time: int):
        self.name = name
        self.time = time
    def __sub__(self, other):
        if self.time < other.time:
            return f'{self.name.capitalize()} is on {other.time - self.time} hours quicker than {other.name}'
        elif self.time > other.time:
            return f'{other.name.capitalize()} is on {self.time - other.time} hours quicker than {self.name}'
        else:
            return f'The road of by {self.name.capitalize()} takes same {self.time} hours as by {other.name}'
        
class Car(Vehicle):
    def __init__(self, name: str, time: int, passengers: int, distance: float, fuel_cost: float):
        Vehicle.__init__(self, name, time)
        self.passengers = passengers
        self.distance = distance
        self.fuel_cost = fuel_cost
    @property
    def trip_cost(self):
        return f'Cost for a trip by {self.name} = {round(self.distance * self.fuel_cost, 2)} uah'

class Airplane(Vehicle):
    def __init__(self, name: str, time: int, ticket_cost: float, seating_type: int, reg_time: str):
        Vehicle.__init__(self, name, time)
        self.ticket_cost = ticket_cost
        self.seating_type = seating_type
        self.reg_time = reg_time

    @property
    def trip_time(self):
        return f'Total trip time by {self.name}: {self.time} hours'

class Train(Vehicle):
    def __init__(self, name: str, time: int, ticket_cost: float, seat_class: str):
        Vehicle.__init__(self, name, time)
        self.ticket_cost = ticket_cost
        self.seat_class = seat_class

    @property
    def data_returner(self):
        return f'Total trip time by {self.name} is {self.time} hours. ' \
               f'Ticket costs for {self.seat_class} is {self.ticket_cost} uah'

air1 = Airplane('airplane', 12, 125.5, 1, '12:05')
car1 = Car('car', 24, 5, 134.5, 2.8)
train1 = Train('train', 13, 345.6, 'SV')
print(car1-air1)
print(train1-car1)
print(car1.trip_cost)
print(air1.trip_time)
print(train1.data_returner)
print('####################################################')

#   ######################################################################
#
# 1)Створити пустий list
# 2)Створити клас Letter
# 3) створити змінну класу __count.
# 4) - при створенні об'єкта має створюватись змінна об'єкта(пропертя) __text, для цієї змінної мають бути гетер і сетер
# 5) при створені об'єкта __count має збільшуватися на 1
# 6) має бути метод(метод класу) для виводу __сount
# 7) має бути метод який записує в наш ліст текст з нашої змінної __text

textList = []
class Letter:
    __count = 0

    def __init__(self, text: str):
        self.__text = text
        Letter.__count += 1

    def get_text(self):
        return self.__text

    def set_text(self, new_text):
        self.__text = new_text

    @classmethod
    def get_count(cls):
        return cls.__count

    def text_to_list(self):
        textList.append(self.__text)

letter1 = Letter('Dear Karina!')
letter2 = Letter('How are you doing?')
letter1.text_to_list()
letter2.text_to_list()
print(textList)
print(Letter.get_count())
print(letter2.get_text())
letter2.set_text('Have not seen long time')
print(letter2.get_text())

