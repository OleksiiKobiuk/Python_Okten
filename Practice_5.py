# Переделываем практическую:
#
# -Должен быть класс записной книжки
# -А каждая манипуляция над ней должна быть методом класса
# -Все данные сохраняем в файл
#
#
# реализовать записную книжку покупок:
# - каждая запись должна содержать название покупки и ее цену
# -сделать менюшку для работы с записной книжкой:
#     '1) Создать запись'
#     '2) Список всех записей'
#     '3) Общая сумма всех покупок'
#     '4) Самая дорогая покупка'
#     '5) Поиск по названию покупки'
#     '9) Выход'
# - можете придумать свои пункты
import json
import pickle
from typing import Dict, Any
class PurchaseBook:

    def __init__(self, purchase_dict):
        self.purchase_dict = {}
        self.__dict__.update(purchase_dict)

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, key):
        return self.purchase_dict[key]

    def get_key_value(self):
        return self.__getitem__()


purchase_book = {
        'apple': 45,
        'beer': 30,
        'mango': 60,
        'fish': 120,
        'bicycle': 2300,
        'notebook': 26000,
        'rice': 86
    }
# with open('PB', 'wb') as file:
#     pickle.dump(purchase_book, file)
# with open('PB', 'w') as file:
#     json.dump(purchase_book, file)
pl1 = PurchaseBook(purchase_book)

a=0
while a != 7:
    print('1.Создать запись в книге покупок\n'
      '2.Вывести список всех покупок\n'
      '3.Общая сумма всех покупок\n'
      '4.Самая дорогая покупка\n'
      '5.Поиск по названию покупки\n'
      '6.Средний чек\n'
      '7.Выход')
    a = int(input('Сделайте выбор: '))
    if a == 1:
        new_key = input('Введите название покупки:')
        new_value = int(input('Ведите стоимость покупки:'))
        pl1[new_key] = new_value
        # with open('PB', 'wb') as file:
        #     pickle.dump(pl1.purchase_dict, file)
        # with open('PB', 'rb') as file:
        #     purchase_book = pickle.load(file)
        with open('PB', 'w') as file:
            json.dump(pl1.purchase_dict, file)
        with open('PB', 'r') as file:
            purchase_book:Dict[str:Any] = json.load(file)
        for k, v in purchase_book.items():
            print(k)
            print(v)


        # print(pl1.__getitem__({'mango'}))
        # for i in pl1.purchase_dict:
            # print(pl1.__getitem__('mango'))
        # for k, v in pl1.purchase_dict:
        #     print(f'{pl1.purchase_dict[k]}: {v}')

# print(pl1.__getattribute__('banana'))