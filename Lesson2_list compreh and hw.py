# def func(a, c, v=4, *args, **kwargs):
#     print(a, v, c)
#     print(args)
#     print(kwargs)
# func(10, 11, 12, 12, 45, 87, name='Max', age=15)

# def decor(func):
#     def wrap(*args, **kwargs):
#         print('*****************************')
#         func(*args, **kwargs)
#         print('*****************************')
#     return wrap
#
# @decor
# @decor
# def greeting(name):
#     print('Hello' + name)
# greeting('Max')

# ***************************************

# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

st = 'as 23 fdfdg544'
s = ''
for i in st:
    if i.isdigit():
        s += i + ', '
print(s[:len(s)-2])
# num = [int(i) for i in st if i.isdigit()]
# print(num)

# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

st = 'as 23 fdfdg544 34 456'
k=''
for i in st:
    if i.isdigit():
        k += i
    else:
        k += ' '
k = ', '.join(k.split())
print(k)

# #################################################################################
#
# list comprehension
#
# 1)есть строка:
# greeting = 'Hello, world'
# записать каждый символ в лист поменяв его на верхний регистр
# пример:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
#
greeting = 'Hello, world'
upperCase = [i.upper() for i in greeting]
print(upperCase)

# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# пример:
# [1, 9, 25, 49, 81, 121, 169, 225, 289, 361, 441, 529, 625, 729, 841, 961, ...]

digitsInSquare = [i**2 for i in range(50) if i%2 != 0]
print(digitsInSquare)

#
# function
#
# - створити функцію яка виводить лист

greeting = ['Hello', 'world']
def listOutput(x):
    print(x)
listOutput(greeting)

# - створити функцію яка приймає три числа та виводить та повертає найменьше.

def minOf(x, y, z):
    print(min(x, y, z))
    return min(x, y, z)
minOf(5, 8, 1)

# - створити функцію яка приймає три числа та виводить та повертає найбільше.

def maxOf(x, y, z):
    print(max(x, y, z))
    return max(x, y, z)
maxOf(5, 8, 1)

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

def maxMin(*args):
    print(max(args))
    return min(args)
x=maxMin(5,6,8,10,34)
print(x)
# - створити функцію, яка виводить list

greeting = ['Hello', 'Alex']
def listOut(x):
    print(x)
listOut(greeting)

# - створити функцію, яка повертає найбільше число з list
numberList = [123, 45, 0, 984, 47, 3, 75, 9458]
def maxListValue(listX):
    return(max(listX))
print(maxListValue(numberList))

# - створити функцію, яка повертає найменьше число з list
numberList = [123, 45, 0, 984, 47, 3, 75, 9458]
def minListValue(listX):
    return(min(listX))
print(minListValue(numberList))

# - створити функцію, яка приймає list чисел та складає значення елементів list та повертає його.
numberList = [123, 45, 0, 984, 47, 3, 75, 9458]
def sumListValue(listX):
    return sum(listX)
print(sumListValue(numberList))

# - створити функцію, яка приймає list чисел та повертає середнє арифметичне його значень.
numberList = [123, 45, 0, 984, 47, 3, 75, 9458]
def avgListValue(listX):
    return(sum(listX)/len(listX))
print(avgListValue(numberList))


# decorators
# - є функція:
# def pr():
#     return 'Hello_boss_!!!'
#  написати декоратор до цієї функції, який замінює нижні підчеркування на пробіли і повертає це значення

def change_(func):
    def inner():
        return func().replace('_', ' ')
    return inner

@change_
def pr():
    return 'Hello_boss_!!!'

print(pr())