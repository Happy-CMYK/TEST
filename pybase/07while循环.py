
# i = 1
# while i<=10:
#     print(i)
#     print("媳妇,我错了")
#     # i = i+1
#     i+=1

import random

# 只要随到了 10就停止
# i = 0
# while i != 10:
#     i = random.randint(1,10)
#     print(i)
a = 1
while True:
    print("循环次数:",a)
    i = random.randint(1, 10)
    print(i)

    a+=1
    if i == 10:
        break


