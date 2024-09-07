
# name = "李宇宁,蒋疼,陈俊才"

# girl_friends = ["迪丽热巴","古力娜扎","杨幂","周冬雨"]

# print(girl_friends)
# # print(girl_friends[0])
#
# name = girl_friends[0]
# print(name[1])
# print(girl_friends[2])
# 列表定位的形式左闭右开
# print(girl_friends[:2])
#
# print(type(girl_friends))
# 反向取值
# print(girl_friends[::-1])

# print(girl_friends[0])
# print(girl_friends[1])
# print(girl_friends[2])
# print(girl_friends[3])
# i = 0
# while i <len(girl_friends):
#     print(girl_friends[i])
#     i +=1

# girl_friends = ["迪丽热巴","古力娜扎","杨幂","周冬雨"]
# for i in girl_friends:
#     print(i)

# name = "肖战"
#
# tf_boys = ["王俊凯","易烊千玺","王源"]
#
#
# boy_friends = ["吴彦祖","彭于晏","金城武","杨洋",tf_boys]
# print(len(boy_friends))
# print(boy_friends[4][1][2:])
# print(boy_friends)

# 增删改查
# boy_friends = ["吴彦祖","彭于晏","金城武","杨洋"]
# print(boy_friends)
#
# boy_friends.append("蔡徐坤")
# print(boy_friends)
#
# boy_friends. insert(0,"古天乐")
# print(boy_friends)
#
# tf_boys = ["王俊凯","易烊千玺","王源"]
# boy_friends.append(tf_boys)
#
# print(boy_friends)
# #
# boy_friends.extend(tf_boys)
# print(boy_friends)
#
# boy_friends = ["吴彦祖","彭于晏","金城武","杨洋","杨洋"]
#
# print("吴彦祖" in boy_friends)
#
# print(boy_friends.index("杨洋"))
#
# boy_friends[0] = "蔡徐坤"
# print(boy_friends)
#
# print("吴彦祖" not in boy_friends)
#
# print(boy_friends.index("蔡徐坤"))
# print(boy_friends.count("杨洋"))

# del 删除
a =52
print(a)
del a



boy_friends = ["吴彦祖","彭于晏","金城武","杨洋","杨洋样"]
boy_friends.reverse()
print(boy_friends)
del boy_friends[3]
print(boy_friends)

# pop 默认删除最后一个元素
name = boy_friends.pop(0)
print(name)
print(boy_friends)

# remove 删除的成功结果是None
print(boy_friends.remove("金城武"))
print(boy_friends)

# 倒序
a = [1, 4, 2, 3]
a.sort(reverse=True)
print(a)
a.reverse()
print(a)


# set()列表去重
list1 = ['a', 'b', 1, 3, 9, 9, 'a']
list2 = set(list1)
print(list2)




boy_friends = ["吴彦祖","彭于晏","金城武","杨洋","杨洋样"]

print(type(boy_friends))

girl_friends = ["迪丽热巴", "古力娜扎", "杨幂", "赵今麦", "玛玛哈哈"]

print(type(girl_friends))

print(boy_friends)
print(girl_friends)

boy_friends[1] = "王一博"
print(boy_friends)
girl_friends[0] = "曹万江"
print(girl_friends)



