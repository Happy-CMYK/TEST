# import os
# os.rename("dd.txt","dd-终极版.txt")
# os.remove("dd-备份.txt")
# os.mkdir("bbb")
# print(os.getcwd()) # 获得当前目录
# os.chdir("dd") # 尽量不要使用  容易乱
# print(os.listdir("./")) # 当前目录的所有文件
# os.rmdir("bbb")


# 文件作业
# 创建一个文件夹 dd  文件夹里面创建10个文件
# 把所有的文件 比如dd. txt
# 输入1 改成 dd-胖达出品.txt
# 输入2 dd-胖达出品.txt 改回 dd.txt

def creatfile():

    import os
    # 创建文件夹dd
    if not os.path.exists('dd'):
        os.mkdir('dd')
    # 在dd文件夹内创建10个文件
    for i in range(1, 11):
        filename = f"dd/dd{i}.txt"
        with open(filename, 'w') as file:
            file.write("This is file " + str(i))
# def work():
#     worker=input("'1'表示替换成胖达出品,'2'表示替换回原名称,请按提示输入数字:")
#     if worker == "1":
# # 将所有文件名中的"dd"替换为"dd-胖达出品"
#         for i in range(1, 11):
#             old_filename = f"dd/dd{i}.txt"
#             new_filename = f"dd/dd{i}-胖达出品.txt"
#             os.rename(old_filename, new_filename)
#     if worker =="2":
# # 将所有文件名中的"dd-胖达出品"替换回"dd"
#         for i in range(1, 11):
#             old_filename = f"dd/dd{i}-胖达出品.txt"
#             new_filename = f"dd/dd{i}.txt"
#             os.rename(old_filename, new_filename)
#     else:
#         print ('请按提示输入数字:1或2'  )
# if __name__ == '__main__':
#     creatfile ()
#     work()


# 单独创建一个txt文件
filename = f"aa/csdsd.txt"
with open(filename, 'w') as file:
            file.write("This is file " + str(1))


with open( 'tsts.txt','w+',encoding='utf-8') as f1, open('tsasts.txt','w+',encoding='utf-8')as f2:
    f1.write ( "This is file " )
    f2.write ( "This is file " )
