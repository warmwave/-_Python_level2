#
# def coder(s, sym):
#     return "".join([chr(ord(i)+sym-ord('a')) for i in s])
#
#
# print(coder("hello, my name is andrey", 5792))
#

# import subprocess
#
# args = ['ping', 'google.com']
#
# subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
#
# for line in subproc_ping.stdout:
#     line = line.decode('cp866')
#     print(line)



# import chardet
#
# filename = "ansi.txt"
# with open(filename, 'rb') as f:
#     res = chardet.detect(f.read())
# with open(filename, 'r', encoding=res['encoding']) as f:
#     print(f.read().encode('utf-8').decode('utf-8'))
#



# def draw(x1,y1):
#     pass
#
# def move(x1,y1,dx,dy):
#     pass
#
# def get_distance(x1,y1,x2,y2):
#     pass
#
# x1 = 3
# y1 = 5
#
# x2 = 7
# y2 = 1
#
# print(get_distance(x1,x1,x1,x1))
#

class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def _smth(self):
        pass

    def draw(self):
        pass

    def move(self,dx,dy):
        pass

    def get_distance(self, b):
        self._smth()


class Circle(Point):
    pass

# a = Point(2,5)
# b = Point(6,8)
#
# a.get_distance(b)







class Figure:
    def draw(self):
        print("figure")


class Square(Figure):
    def draw(self):
        print("square")

class Rectangle(Figure):
    def draw(self):
        print("rectangle")


mass = [Square(), Rectangle()]

for i in mass:
    i.draw()


None