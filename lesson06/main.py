# # def f():
# #     print("Hello")
# #
# #     def aa():
# #         print("AA")
# #
# #     return aa
# #
# #
# # def d():
# #     f()
# #     print("World!")
# #
# #
# # a = f
# #
# # d = a()
# # d()
#
#
#
#
#
# def f():
#     print("Hello")
#
# def decorator(func):
#     def wrapper():
#         print("Before")
#         func()
#         print("After")
#
#     return wrapper
#
# f()
# f = decorator(f)
# f()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# import time
#
# def my_sum(a, b):
#     time.sleep(1)
#     return a + b
#
#
# cargo = dict()
#
#
# def caching(func):
#     def wrapper(a, b):
#         if (a, b) in cargo:
#             return cargo[(a, b)]
#
#         ret = func(a, b)
#
#         cargo[(a, b)] = ret
#
#         return ret
#
#     return wrapper
#
#
# my_sum = caching(my_sum)
#
#
# for i in range(5):
#     print(".")
#     my_sum(1,2)

#
# import time
#
#
# def my_sum(a, b):
#     time.sleep(1)
#     return a + b
#
#
# def my_sum_v2(a, b, c):
#     time.sleep(1)
#     return a + b + c
#
#
# cargo = dict()
#
#
# def caching(func):
#     def wrapper(a, b):
#         if (a, b) in cargo:
#             return cargo[(a, b)]
#
#         ret = func(a, b)
#
#         cargo[(a, b)] = ret
#
#         return ret
#
#     return wrapper
#
#
# def caching_v2(func):
#     def wrapper(a, b, c):
#         if (a, b, c) in cargo:
#             return cargo[(a, b, c)]
#
#         ret = func(a, b, c)
#
#         cargo[(a, b, c)] = ret
#
#         return ret
#
#     return wrapper
#
#
# my_sum = caching(my_sum)
# my_sum = caching_v2(my_sum_v2)
#
# for i in range(5):
#     print(".")
#     my_sum(1, 2)


# import time
#
#
# def my_sum(a, b):
#     time.sleep(1)
#     return a + b
#
#
# def my_sum_v2(a, b, c):
#     time.sleep(1)
#     return a + b + c
#
#
# cargo = dict()
#
#
# def caching(func):
#     def wrapper(*args):
#
#         if args in cargo:
#             return cargo[args]
#
#         ret = func(*args)
#
#         cargo[args] = ret
#
#         return ret
#
#     return wrapper
#
#
# my_sum = caching(my_sum)
# my_sum_v2 = caching(my_sum_v2)
#
# for i in range(5):
#     print(".")
#     my_sum(1, 2)


# import time
#
# cargo = dict()
#
#
# def caching(func):
#     def wrapper(*args):
#         if args in cargo:
#             return cargo[args]
#
#         ret = func(*args)
#
#         cargo[args] = ret
#
#         return ret
#
#     return wrapper
#
#
# @caching
# def my_sum(a, b):
#     time.sleep(1)
#     return a + b
#
#
# @caching
# def my_sum_v2(a, b, c):
#     time.sleep(1)
#     return a + b + c
#
#
# for i in range(5):
#     print(".")
#     my_sum(1, 2)


# def log_param(msg):
#     def log(func):
#         def wrapper(*args):
#             func(*args)
#             print(msg)
#
#         return wrapper
#
#     return log
#
#
# @log_param("My sum log")
# def my_sum(a, b):
#     return a + b
#
# # my_sum = log_param("My sum log")(my_sum)
#
#
# @log_param("My sumv2 log")
# def my_sum_v2(a, b, c):
#     return a + b + c
#
#
# my_sum(1, 2)
# my_sum_v2(1, 2, 4)

#
# def set_bold(func):
#     def wrapper(*args):
#         return f"<b>{func(*args)}</b>"
#
#     return wrapper
#
#
# def set_italic(func):
#     def wrapper(*args):
#         return f"<i>{func(*args)}</i>"
#
#     return wrapper
#
#
# def add_br(func):
#     def wrapper(*args):
#         return f"{func(*args)}<br/>"
#
#     return wrapper
#
#
# #
# # @set_italic
# # @set_bold
# # @add_br
# # def get_name(name):
# #     return f"{name}"
#
# def get_name(name):
#     return f"{name}"
#
#
# get_name = set_italic(set_bold(add_br(get_name)))
#
# print(get_name("Andrey"))


#
# def set_bold(func):
#     def wrapper(*args):
#         return f"<b>{func(*args)}</b>"
#
#     return wrapper
#
#
# def set_italic(func):
#     def wrapper(*args):
#         func(*args)
#
#     return wrapper
#
#
# def add_br(func):
#     def wrapper(*args):
#         return f"{func(*args)}<br/>"
#
#     return wrapper
#
#
# #
# @set_bold
# @set_italic
# @add_br
# def get_name(name):
#     return f"{name}"
#
# # def get_name(name):
# #     return f"{name}"
# #
# #
# # get_name = set_italic(set_bold(add_br(get_name)))
#
# print(get_name("Andrey"))
#
#


# import when_deco_is_called
#
# @when_deco_is_called.register
# def ff():
#     pass


# class Log:
#     def __init__(self, msg):
#         self.msg = msg
#
#     def __call__(self, func):
#         def wrapper(*args):
#             func(*args)
#             print(self.msg)
#
#         return wrapper
#
#
# @Log("Andrey")
# @Log("World!")
# def f():
#     print("Hello")
#
#
# f()


# import sys
# s = dict()
#
# print(sys.getsizeof(s))


# -------------------- SOCKETS ------------------------------------


# import socket
# import threading
#
# s = socket.socket()
#
# s.bind(("", 9090))
# s.listen(5)


# def read_data(client):
#     while True:
#         print("recv ", end=" ")
#         data = client.recv(1024)
#         print(data)
#
#
# while True:
#     print("Pre accept")
#     client, addr = s.accept()
#
#     threading.Thread(target=read_data, args=(client,)).start()


import select
import socket

s = socket.socket()

s.bind(("", 9090))
s.listen(5)
s.settimeout(0)

clients = []

while True:
    print("Pre accept")

    try:
        client, addr = s.accept()

        clients.append(client)

    except:
        pass

    if len(clients) > 0:
        r, w, e = select.select(clients, clients, clients)

        for i in r:
            data = i.recv(1024)
            print(data)

        for i in w:
            i.send(b"Hello")
