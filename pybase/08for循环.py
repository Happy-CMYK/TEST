# a_str = "100"
# # 遍历
# for char_a in a_str:
#     print ( char_a )


# # 迭代
# for each in "Fishic":
#     print ( each )
#
# i = 0
# while i < 10:
#     i = i + 1
#     if i == 4:
#         continue
#     print ( "现在是循环了第%d次" % i )
#
# if i == 5:
#     break

# 寻找质数:
# for i in range(2,1000):
#     for x in range(2,i):
#         if i % x == 0:
#             # print(i,"=",x,"*",i//x,end='\t')
#             break
#     else:
#         print(i,"是质数",end='\t')


# 计数,计算某个字符串的个数
man = 'dasj5245a'
print ( man.count ( 'a', 1, 9 ) )


# 一万元给20位员工按绩效随机发工资,,,,还是缩进问题!!!    yue =余额
money = 10000
for i in range ( 1, 21 ):
    import random

    score = random.randint ( 1, 10 )
    if score < 5:
        print ( f"员工{i}的绩效为{score},不满足,不发工资,下一位" )
        continue
    if money >= 1000:
        money -= 1000
        print ( f'员工{i}的绩效为{score}满足条件,发放工资1000元,公司账户余额:{money}' )
    else:
        print ( f"余额不足,当前余额为{money},不足以发放工资,下个月再来" )

money = 4000
for i in range ( 1, 11 ):
    import random

    score = random.randint ( 1, 10 )
    if score < 5:
        print ( f'员工{i}的绩效为{score},不满足,不发工资,下一位' )
        continue
    if money >= 1000:
        money -= 1000
        print ( f'员工{i}的绩效为{score},满足条件发放工资1000元,公司账户余额为{money}' )
    else:
        print ( f"余额不足,当前余额为{money},不足以发放工资,下个月再来" )
