#####################################
# try exept
#####################################

# try:
#     jkshdfkjshf
#     # print(3/0)
# # except NameError as e:
# #     print(e)
# except ZeroDivisionError:
#     print("делить на ноль нельзя")
# # except Exception:
# #     print('some error')
# else:
#     print('ok')
# finally:
#     print('finish')
# print('sdfs')
#####################################
# generators
#####################################

# l = [i for i in range(50000000)]
# input()

# g = (i for i in range(50000000))
#
# print(next(g))

# l = [1,2,3,4,5]
# g = iter(l)
# #
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
#
# for i in g:
#     print(i)

# def gen(name):
#     for ch in name:
#         yield ch
#         print('hello')
#
#
# g = gen('Max')
# print(type(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# def gen():
#     yield 1
#     yield 2
#     yield 3
#     return 'Finish'
#
# g = gen()
#
# try:
#     print(next(g))
#     print('hhsdkjfhsjh')
#     print(next(g))
#
#     print(next(g))
#     print(next(g))
# except StopIteration as e:
#     print(e)

# def gen1(n):
#     for i in range(1, n + 1):
#         yield f'{i}-worker-team1'
#
#
# def gen2(n):
#     for i in range(1, n + 1):
#         yield f'{i}-worker-team2'
#
#
# teams = [gen1(8), gen2(5)]
#
# while teams:
#     team = teams.pop(0)
#     try:
#         print(next(team))
#         teams.append(team)
#     except StopIteration:
#         pass
import pickle
import uuid


# print(uuid.uuid1())

def gen_jpg_file():
    pattern = '{}.jpg'
    while True:
        yield pattern.format(uuid.uuid1())


file_gen = gen_jpg_file()

#####################################
# files
#####################################
# file_path = '1.txt'
# file = open(file_path, 'a+')
# print(file.read(3))
# # file.seek(0)
# print(file.tell())
# print(file.read(3))
# print(file.readline(),end='')
# print(file.readline(),end='')
# print(file.readline(),end='')
# print([file.readline()])
# print(file.readlines())
# print(file.tell())
# file.writelines(['one strung\n', 'two string\n'])
# print(file.tell())
# file.seek(0)
# print(file.read(), end='')
# file.close()

# with open('1.txt') as file:
#     print(file.read())
#     print(file.closed)
#
# print(file.closed)

# file_path = 'python.jpg'
#
# with open(file_path, 'rb') as file:
#     data = file.read()
#     for i in range(10):
#         with open(next(gen_jpg_file()), 'wb') as file2:
#             file2.write(data)

####################################################################################
import pickle
import json
from typing import Dict, Any

user: Dict[str, Any] = {
    "name": 'Max',
    "age": 15,
    "status": False
}
# #
#
#
# #
# # with open('DB', 'wb') as file:
# #     pickle.dump(user, file)
# with open('DB', 'rb') as file:
#     user = pickle.load(file)
#
# print(user.get('name'))
# with open('db.json', 'w') as file:
#     json.dump(user, file)

with open('db.json', 'r') as file:
    user: dict[str, Any] = json.load(file)

print(user)