import threading
import time
from multiprocessing import Process, Queue


# def f(duration, s, queue):
#     i = 0
#     while True:
#         queue.put(i)
#         i += 1
#         time.sleep(duration)
#
#
# if __name__ == '__main__':
#     q = Queue()
#     t = Process(target=f, args=(3, "first", q))
#     t.daemon = True
#
#     t.start()
#
#     while True:
#         print("Get from queue")
#         print(q.get())
#
#
# # GIL
# # Global Interpretator Lock
#
#
# class MyThread(threading.Thread):
#
#     def __init__(self, duration):
#         super().__init__()
#         self.duration = duration
#
#     def run(self):
#         for i in range(10):
#             time.sleep(self.duration)
#             print("Inside thread")
#
#
# a = MyThread(0.5)
#
# a.start()
#
# def f(duration, s):
#     while True:
#         print(f"Hello from {s} thread")
#         #t = threading.Thread()
#         time.sleep(duration)
#
# def g():
#     for i in range(10):
#         time.sleep(0.3)
#         print("Inside thread")
#
#
# # t = threading.Thread(target=f, args=(3,"first"), daemon=True)
# t2 = threading.Thread(target=g, daemon=True)
#
# # t.start()
# t2.start()
# #
# # print(t2.name)
# # print(t2.is_alive())
# # print(t2.isDaemon())
# # print(t2.ident)
# #
# # t2.setName("MyThread")
# # print(t2.name)
# #
# # t2.join()
# #
# # t2.setDaemon(False)
# #
# # print(t2.is_alive())
# # a = input("Input data: ")
