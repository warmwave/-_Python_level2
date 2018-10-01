# coding: UTF-8

import subprocess
import chardet

# задание 1
# list = ['разработака', 'сокет', 'декоратор']

# for l in list:
# 	# Эти слова и так в "строке"
# 	print(l)
# 	print(type(l))
# 	# Это уже 
# 	print(l.encode())
# 	print(type(l.encode()))
# 	print()


# задание 2
# list = ['class', 'function', 'method']

# for l in list:
# 	print(bytes(l, encoding = 'utf-8'), len(l.encode()), type(l.encode()))


# задание 3
# list = ['attribute', 'класс»', 'функция', 'type', 'Testování']

# for l in list:
# 	try:
# 		print(l.encode())
# 		print(type(l.encode()))
# 	except UnicodeError as e:
# 		print(l, 'невозможно записать в байтовом типе')


# # задание 4
# list = ['разработака', 'администрирование', 'protocol', 'standart']

# for l in list:
# 	# Эти слова и так в "строке"
# 	print(l)
# 	print(type(l))
# 	# Это уже 
# 	print(l.encode())
# 	print(type(l.encode()))
# 	print()


# задание 5
# http://take.ms/nXdOJ - кириллицe мне взять неоткуда)
args = ['ping', 'google.com', '-c 3']
process = subprocess.Popen(args, stdout=subprocess.PIPE)
# stdout = str(process.communicate())

for line in process.stdout:
    print(i, line)