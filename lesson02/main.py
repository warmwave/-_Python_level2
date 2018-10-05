#Comma Separated Values
#
# with open("data.csv") as f:
#     for data in f.read().split('\n'):
#         print(data.split(','))
# import csv
#
# with open("data.csv") as f:
#     data = csv.reader(f)
#     for i in data:
#         print(i)
#
# data = [ ["Name","LastName","Age"],["5","4","7"],["1","2","3"] ]
#
# with open("new.csv", 'w', newline='') as f:
#     wr = csv.writer(f, delimiter=';')
#
#     for line in data:
#         wr.writerow(line)


# JSON
# JavaScript Object Notation

import json

# with open("test.json") as f:
#
#     obj = json.loads(f.read())
#
#     print(obj)

#
# d = {
#
#     ("key", "second_key", "third_key"):"value",
#     ("key", "second_key", "third_key"):"value2"
#
# }
#
# print("After creation dictionary")
# print(d[("key", "second_key")])


# d = {
#
#     ["key", "second_key"]:[123,321,123]
#
# }
#
# print("After creation dictionary")
# print(d.keys()[0].append("awd"))


# d = {
#
#     True:False,
#     False: True,
#     None: None
#
# }
#
# print("After creation dictionary")
# print(d[True])


# d = {
#
#     123:"fsef",
#     123.1232: 5434
#
# }


# import json
#
# f = json.dumps(d)
# print(f)


# print(d)

# import json

# json.dump

# json.load

# import json
# from pprint import pprint
#
# with open('test.json') as f:
#     data = json.load(f)
#
# pprint(data)

# import json
# from pprint import pprint
#
# with open('test.json') as f:
#     data = json.loads(f.read())
#
# pprint(data)

# sample = {
#
#     "key":"value",
#     "key2":"value2"
#
# }
#
# import json
# with open('result.json', 'w') as fp:
#     json.dump(sample, fp)
#


# import yaml
# from pprint import pprint
#
# with open("test.yaml") as f:
#     pprint(yaml.load(f))
#
#
# import yaml
# from pprint import pprint
#
# with open("test.yaml") as f:
#     data = yaml.load(f)
#     data['invoice'] = "Hello, world!!!"
#
#
#     with open("output.yaml", 'w') as fw:
#         yaml.dump(data, fw)

# import yaml
# from pprint import pprint
#
# with open("test.yaml") as f:
#     data = yaml.load(f)
#     data['invoice'] = "Hello, world!!!"
#
#
#     with open("output2.yaml", 'w') as fw:
#         yaml.dump(data, fw, default_flow_style=False)







# XML
#
# eXtensible Markup Language

# FB2 Fiction Book 2

















# from bs4 import BeautifulSoup
#
# with open("test.xml") as f:
#     soup = BeautifulSoup(f.read(), 'lxml')
#
#     c = soup.findAll('companyname', {"class":"my_class"})
#
#     for i in c:
#         print(i.text)
#     # print(c.attrs)


from bs4 import BeautifulSoup

with open("test.xml") as f:
    soup = BeautifulSoup(f.read(), 'lxml')

    c = soup.find('fulladdress', {"id": "123"})\

    if c is not None:
        c = c.find('city')

    print(c)


