# def counter():
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         return count
#     return wrap
#
# count1 = counter()
#
# print(count1())
# print(count1())
# print(count1())
# print(count1())
# print(count1())
# print(count1())
# print(count1())
# print(count1())

# 1)
# создать два класса Prince и Cinderella:
# у золушки должно быть имя возраст и размер ноги
# у принца имя, возраст и размер найденой туфельки, так же должен быть метод который принимает лист золушек и ищет ту самую
#
# 2) максимально в этих двух классах проанотировать типы

# 3) у класса золушки должна быть переменная count которая будет считать сколько экземпляров класса золушка было создано


class Cinderella:
    count = 0
    def __init__(self, name: str, age: int, foot_size: int):
        self.name = name
        self.age = age
        self.foot_size = foot_size
        Cinderella.count += 1

    def __str__(self):
        return f'Cinderella: {self.name} "{self.age}" years old with foot size - "{self.foot_size}"'

    def __repr__(self):
        return self.__str__()

class Prince:
    def __init__(self, name: str, age: int, shoe_found: int):
        self.name = name
        self.age = age
        self.shoe_found = shoe_found

    def find_cinderella(self, x:list):
        for i in x:
           if vars(i).get('foot_size') == self.shoe_found:
                    return i
        return ('not found Cinderella')


prince1 = Prince('Alek', 25, 36)
cinderellas = [Cinderella('Alla', 25, 40), Cinderella('Sasha', 19, 36), Cinderella('Valya', 35, 42), Cinderella('Galya', 20, 38)]
print(f'Prince {prince1.name} found shoe "{prince1.shoe_found}" size which belongs to', prince1.find_cinderella(cinderellas))
print("Numbers of Cinderella's copies is",Cinderella.count)
