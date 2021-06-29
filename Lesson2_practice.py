# прога, що виводить кількість кожного символа з введеної строки,
# наприклад:
# st = 'as 23 fdfdg544' #введена строка
#
# 'a' -> 1  #вивело в консолі
# 's' -> 1
# ' ' -> 2
# '2' -> 1
# '3' -> 1
# 'f' -> 2
# 'd' -> 2
# 'g' -> 1
# '5' -> 1
# '4' -> 2
# """

st = 'as 23 fdfdg544'
new_st = []
for i in st:
    if i in new_st:
        continue
    else:
        new_st.append(i)
        x = st.count(i)
        print (i,'->',x)

#
# list comprehension
#
# 1)  есть лист:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# создать новый лист и записать в него 'GT' если элемент в numbers больше 4 и 'LT' если элемент меньше или равен 4
# пример:
# ['LT', 'LT', 'LT', 'LT', 'GT', 'GT', 'GT', 'GT']

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
numbersNew = ['GT'if x>4 else 'LT' for x in numbers]
print(numbersNew)



# 2) есть два листа:
# list1 = [1, 2, 3, 4, 5]
# list2 = [-1, 7, 10, -5, -2]
#
# записать в лист тюплы (x,y) если x+y == 0
# пример:
# [(1, -1), (2, -2), (5, -5)]

list1 = [1, 2, 3, 4, 5]
list2 = [-1, 7, 10, -5, -2]
listTuple = [(x,y) for x in list1 for y in list2 if x+y == 0]
print(listTuple)