# -*-coding:utf-8 -*-
import yaml

file = "yaml_03.yml"

# 方式一
with open(file, encoding='utf-8')as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)
    print(type(data))   # dict 类型。

print("*" * 180)


# 方式二
# with open(file, encoding='utf-8')as f:
#     data2 = f.read()
#     print(data2)
#     print(type(data2))  # str 类型。


