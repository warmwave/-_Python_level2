# import os
#
#
# files = [text_file for text_file in os.listdir(".") if text_file.startswith("info") and text_file.endswith(".txt")]
#
# os_prod_list = []
# os_name_list = []
# os_code_list = []
# os_type_list = []
#
# templates = ["Изготовитель системы","Название ОС", "Код продукта", "Тип системы"]
#
# for file in files:
#     with open(file) as f:
#         data = []
#         lines = f.readlines()
#
#         for line in lines:
#             if any([line for temp in templates if line.startswith(temp)]):
#                 buf = line.strip().split(":")
#                 data.append({buf[0]: buf[1].strip()})
#
#         print(data)
#
#
#         # pass
#         #
#         data = [line.strip().split(":") for line in f.readlines() if any([line.startswith(temp) for temp in templates])]
#         # print(data)
        # print(f.readlines())






























# import json
#
# def get_dict_order(item, quantity, price, buyer, date):
#     return {"item":item, "quantity":quantity, "price":price, "buyer":buyer, "date":date}
#
# with open("orders.json") as f:
#     data = json.loads(f.read())
#
#     if "orders" in data:
#         data["orders"].append(get_dict_order("Laptop","2","50000","Pak","2018-09-10"))
#
#
# with open("orders.json", "w") as f:
#     f.write(json.dumps(data))


