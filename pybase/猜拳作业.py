
# 猜拳游戏

# 从控制台输⼊要出的拳 —— 剪刀(1) 石头(2) 布(3) 4 直接胜利
# 电脑 随机 出拳
# ⽐较胜负
#
while True:
    # 1 从控制台输入
    player = input("剪刀(1) 石头(2) 布(3),输入4直接胜利,0退出游戏 请输入:")
    if player == "0":
        print("退出游戏!")
        break

    # 2 电脑随机生成1-3随机数
    import random
    computer = random.randint(1,3)

    # 3 比较胜负 类型转换
    # 判断是否是数字如果是数字 才去转换
    if player.isdigit():

        # 判断输入的数字是否是1234

        player = int(player)
        if player >= 1 and player <= 4:
            print("你出的是:",player)
            print("电脑出的是:",computer)

            # 4 比较胜负
            # 4.1胜利情况 player == 4 直接胜利 player == 1 c==3, p ==2 c==1,p==3,c==2
            # 4.2平局 p==c
            # 4.3输 剩下的就是输
            # if player == 4:
            #     print("你赢了!!")
            # elif player ==1 and computer==3:
            #     print("恭喜你,获得了胜利")
            # elif player ==2 and computer==1:
            #     print("恭喜你,获得了胜利")
            # elif player ==3 and computer==2:
            #     print("恭喜你,获得了胜利")

            if player == 4:
                print("你赢了!!")
            elif (player ==1 and computer==3) or (player ==2 and computer==1 )or (player ==3 and computer==2):
                print("恭喜你,获得了胜利")
            elif player == computer:
                print("平局,还要再战")
            else:
                print("很遗憾,你输了")
        else:
            print("请输入1-4之间的整数")

    else:
        print("请输入1234")

