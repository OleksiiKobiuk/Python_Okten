# Pеализовать записную книжку покупок:
# - каждая запись должна содержать название покупки и ее цену
# -сделать менюшку для работы с записной книжкой:
#     '1) Создать запись'
#     '2) Список всех записей'
#     '3) Общая сумма всех покупок'
#     '4) Самая дорогая покупка'
#     '5) Поиск по названию покупки'
#     '6) Средний чек'
#     '7) Выход'

purchase_book = {
    'apple': 45,
    'beer': 30,
    'mango': 60,
    'fish': 120,
    'bicycle': 2300,
    'notebook': 26000,
    'rice': 86
}
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
        key = input('Введите название покупки:')
        value = int(input('Ведите стоимость покупки:'))
        purchase_book.setdefault(key, value)
        print(purchase_book)
    elif a == 2:
        print('Список покупок:')
        for k, v in purchase_book.items():
            print(k,':', v)
    elif a == 3:
        print('Общая сумма всех покупок =',sum(purchase_book.values()))
    elif a == 4:
        val = max(purchase_book.values())
        for k, v in purchase_book.items():
            if v == val:
                print('Самая дорогая покупка -',k,':', v)
                break
    elif a == 5:
        itemName = input('Введите название покупки:')
        if itemName in purchase_book.keys():
            print(itemName,':',purchase_book.get(itemName))
            break
        else:
            print('Данного товара нет в книге покупок')
    elif a == 6:
        print('Средний чек =', int(sum(purchase_book.values())/len(purchase_book.values())))
