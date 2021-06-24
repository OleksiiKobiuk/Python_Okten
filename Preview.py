# name = 'Bob'
# age = 30
# print('name = %(name)s \nage = %(age)s' %{'age':age, 'name':name})
# print('name = {n} \nage = {a}'.format(a= age, n = name))
# print(f'name = {name} \nage = {age}')
# print(f'name = {name.center(6, "*" )} \nage = {age-3}')
#
# list1 = [5,6]
# list2 = list1[:]

# list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
# # найти min число в листе
# print(min(list), 'is a min value')
#
# # удалить все одинаковые значения
# new_list = []
# for i in list:
#     if i in new_list:
#         print(i,'is a duplication')
#     else: new_list.append(i)
# list = new_list.copy()
# print(list)
#
# #  заменить каждое четвертое значение на "Х"
# list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
# i = 3
# while i<=len(list):
#     list.pop(i)
#     list.insert(i,'X')
#     i+=4
# print(list)
#
# # 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:
# i = int(input('Enter a number: '))
# x=1
# print('*'*i)
# while x<=i-2:
#     print('*',' '*(i-2),'*')
#     x+=1
# print('*'*i)
# # ЯКІ СИМВОЛИ ВИКОРИСТАТИ, ЩОБ ВИВОДИВСЯ СИМЕТРИЧНИЙ ПРЯМОКУТНИК?
#
# # 3) вывести табличку умножения с помощью цикла while
# x=1
# while x<=10:
#     y = 1
#     while y<=10:
#         print(x,'*',y, '= ', x*y)
#         y+=1
#     x+=1
# 4) переделать первое задание под меню с помощью цикла
a=0
while a != 6:
    print('1.Найти min число в листе\n'
      '2.Удалить все дубликаты в листе\n'
      '3.Заменить каждое четвертое значение на "Х"\n'
      '4.Вывести на экран пустой квадрат из "*" сторона которого указана в переменой\n'
      '5.Вывести табличку умножения с помощью цикла while\n'
      '6.Выход')
    a = int(input('Сделайте выбор: '))
    list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
    if a == 1:
        print(list)
        print('Min value of a list: ', min(list))
    elif a == 2:
        print(list)
        new_list = []
        for i in list:
            if i not in new_list:
                new_list.append(i)
        list = new_list.copy()
        print(list)
    elif a == 3:
        i = 3
        while i<=len(list):
            list.pop(i)
            list.insert(i,'X')
            i+=4
        print(list)
    elif a == 4:
        i = int(input('Введіть сторону квадрата: '))
        x=1
        print('*'*i)
        while x<=i-2:
            print('*',' '*(i-2),'*')
            x+=1
        print('*'*i)
        # # ЯКІ СИМВОЛИ ВИКОРИСТАТИ, ЩОБ ВИВОДИВСЯ СИМЕТРИЧНИЙ ПРЯМОКУТНИК?
    elif a == 5:
        x = 1
        while x<=10:
            y = 1
            while y<=10:
                print(x,'*',y, '= ', x*y)
                y+=1
            x+=1

# ***  - вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа
# пример:
# [1, 2, 3, 4, 5, 6, 7, 8, 9] => 5
# [-1, -2, 3, 4, 555] => 4
# [5, 5, 5, 5] => 5
# [-10, 5, 5] => 5

list1 = input('Введіть числові значення списку через кому: ').split(',')
print(list1)
new_list = []
sumList = 0
for i in list1[0:]:
    sumList += int(i)
avgValue= int(sumList/len(list1))
    # int(sum(list1)/len(list1)) - якщо список буде одразу даний
print('Середнє значення списку =',avgValue)
for i in range(len(list1)):
    value = abs(avgValue-int(list1[i]))
    new_list.append(value)
print('Найближче значення до середнього арифметичного списку:',list1[new_list.index(min(new_list))])
