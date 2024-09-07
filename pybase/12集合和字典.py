''' set
1.创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
2.set是无序且不可重复的,所以就不能利用下标索引也就不能修改值了
3.通常用于多个集合间的操作
'''

m = set ()
print ( type ( m ) )  # set

set = ()
print ( type ( set ) )  # tuple

s1 = {"叫啥", 'asdhkajhdsjak', 12122545}
s2 = {"叫啥", 'ds', 12122545}

s1.add ( 4 )
s1.update ( s2 )

print ( s1 )

s = {'c','i','j','k','l'}
s.update([1,1],'23')
print(s)





"""dict
1.key-value 键 值
2.不能根据下标去获取数据 字典没有下标,根据键值去定位
3.字典的键必须是唯一的
4.字典关键字的值的字典形式嵌套

"""

# 字典的形式
d = {}  # dict
j = {"sjja": ['sad']}  # dict
s = {"sjja": ('sad')}  # dict
p = {"sjja": (1)}  # dict
o = {"sjja": 1, }  # dict

# 字典的使用方法
student_1 = {"name": "小乔", "age": 18, "score": 60, "sex": "female"}
student_2 = {"name": "蒋疼", "age": 20, "score": 80, "sex": "male"}

student_2["name"] = "蒋腾"  # 修改
student_2["nickname"] = "疼疼"
print ( student_2 )

# print(len(student_1))   #4
# print(student_1.keys())  #dict_keys(['name', 'age', 'score', 'sex'])
# print(student_1.values())  #dict_values(['小乔', 18, 60, 'female'])
# print(student_1.items())  #dict_items([('name', '小乔'), ('age', 18), ('score', 60), ('sex', 'female')])

print ( student_1["name"] )
print ( student_1["sex"] )

print ( student_1.get ( "name" ) )
print ( student_1.get ( "sex" ) )

# for k in student_1.keys ():
#     print ( k )
# for v in student_1.values ():
#     print ( v )
# for item in student_1.items():
#     print(item)
# for k, v in student_1.items ():
#     print ( "key:%s,value:%s" % (k, v) )

# 字典的键必须是唯一的
g= {x: y for x in [1, 3, 5] for y in [2, 4, 6]}
print ( g )



# 字典的简单嵌套
json_str = {
    "data": {

        "dep_id": "测试_26", "dep_is": "测试_26", "de": "测试_26"
    }
}

keys = json_str["data"].keys ()

print ( type(keys) )  # dict_keys
# key = keys[1]     # TypeError: 'dict_keys' object is not subscriptable
keys = list ( keys )
print ( type(keys) )  # list
keys = tuple ( keys )
print ( type ( keys ) )  # tuple

key = keys[1]
print ( keys )  # ('dep_id', 'dep_is', 'de')
print ( type ( keys ) )  # tuple

print ( type ( key ) )  # str




# 字典关键字的值的字典形式嵌套
json_str = {
    "data": [
        {
            "dep_id": "测试_26",
            "dep_name": "Test学院",
            "master_name": "Test-Master",
            "slogan": "Here is Slogan"
        }
    ]
}

value = json_str.values ()
print ( value )
print ( type ( json_str ) )  # dict
print ( type ( value ) )  # dict



