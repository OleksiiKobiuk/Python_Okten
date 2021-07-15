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
# import pickle
from typing import Dict, List, Any
class PurchaseBook:

    def __init__(self, purchase_list):
        self.purchase_list = purchase_list

    def __setitem__(self, new_dict):
        self.new_dict = new_dict
        self.purchase_list.append(new_dict)

    def __getitem__(self):
        for i in self.purchase_list:
            print(i)

    def sum_of_purchases(self):
        self.sum_purchases = 0
        for i in self.purchase_list:
            self.sum_purchases += i.get('cost')
        return print('Общая сумма всех покупок =', self.sum_purchases)

    def max_purchase(self):
        self.new_l = [i.get('cost') for i in self.purchase_list]
        self.max_val = max(self.new_l)
        for i in self.purchase_list:
            if i.get('cost') == self.max_val:
                print(f'Most expensive purchase is {i}')
                break

    def find_item(self, item):
        self.item = item
        self.q = None
        for i in self.purchase_list:
            if item in i.values():
                self.q = i.get('cost')
                break
        if self.q != None:
            print(item, ':', self.q)
        else:
            print(f'{item} is absent in purchase list')

    def average_check(self):
        self.new_l = [i.get('cost') for i in self.purchase_list]
        print('Average check =', int(sum(self.new_l) / len(self.new_l)))






purchase_book = [{'item': 'apple', 'cost': 45},
    {'item': 'beer', 'cost': 30},
     {'item': 'mango', 'cost': 60},
      {'item': 'fish', 'cost': 120},
       {'item': 'bicycle', 'cost': 2300},
        {'item': 'notebook', 'cost': 26000},
         {'item': 'rice', 'cost': 86}]
# with open('PB', 'wb') as file:
#     pickle.dump(purchase_book, file)
# with open('PB', 'w') as file:
#     json.dump(purchase_book, file)
pl1 = PurchaseBook(purchase_book)
with open('PB', 'w') as file:
    json.dump(pl1.purchase_list, file)
with open('PB', 'r') as file:
    purchase_book: List[Dict[str, Any]] = json.load(file)
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
        new_item = input('Введите название покупки:')
        new_value = int(input('Ведите стоимость покупки:'))
        new_dict1 = {'item': new_item, 'cost': new_value}
        pl1.__setitem__(new_dict1)
        with open('PB', 'w') as file:
            json.dump(pl1.purchase_list, file)
        with open('PB', 'r') as file:
            purchase_book: List[Dict[str, Any]] = json.load(file)
        print(f'You added: {purchase_book[len(purchase_book)-1]}')
    elif a == 2:
        print('Список покупок:')
        pl1.__getitem__()
        # for i in purchase_book:
        #     print (i)
    elif a == 3:
        pl1.sum_of_purchases()
        # sum_purchases = 0
        # for i in purchase_book:
        #     sum_purchases += i.get('cost')
        # print('Общая сумма всех покупок =', sum_purchases)
    elif a == 4:
        pl1.max_purchase()
        # new_l = [i.get('cost') for i in purchase_book]
        # max_val = max(new_l)
        # for i in purchase_book:
        #     if i.get('cost') == max_val:
        #         print(f'Most expensive purchase is {i}')
        #         break
    elif a == 5:
        itemName = input('Введите название покупки:')
        pl1.find_item(itemName)
        # q = None
        # for i in purchase_book:
        #     if itemName in i.values():
        #         q = i.get('cost')
        #         break
        # if q != None:
        #     print(itemName,':',q)
        # else:
        #     print(f'{itemName} is absent in purchase list')
    elif a == 6:
        pl1.average_check()
        # new_l = [i.get('cost') for i in purchase_book]
        # print('Average check =', int(sum(new_l) / len(new_l)))

