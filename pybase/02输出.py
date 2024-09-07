# # print("hello world")
goods_a = 998

goods_name = "笔记本电脑"

goods_num = 1.2345
#
print("商品a的名字是%s,价格为%d元,库存为%.4f万台" % (goods_name,goods_a,goods_num))
# %s 字符串占位符无敌
print("商品a的名字是%s,价格为%s元,库存为%s万台" % (goods_name,goods_a,goods_num))

print("商品a的名字是{},价格为{}元,库存为{}万台".format(goods_name,goods_a,goods_num))
# f
print(f"商品a的名字是{goods_name},价格为{goods_a}元,库存为{goods_num}万台")



n = int(input())
dic = {}

# idea: 动态建构字典
for i in range(n):
    line = input().split( )
    key = int(line[0])
    value = int(line[1])
    dic[key] = dic.get(key, 0) + value  # 累积key所对应的value

for each in sorted(dic):  # 最后的键值对按照升值排序
    print(each, dic[each])











