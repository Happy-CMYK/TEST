# ./ 当前目录
# 读取的时候没有这个文件就会报错

# r表示去除转义字符"/"!!!!

file = open ( r"C:\Users\ROY\PycharmProjects\pybase\aa\aaa.txt", encoding="utf8" )
print ( file.read () )
# 需要关闭才能保存
file.close ()

# w模式 如果没有这个文件!!!!
file = open ( "aa.txt", "w", encoding="utf8" )
if not file:
 print ("没有此文件")
# print(file.readline())
else:
    file.write ( "艾欧尼亚" )
    print (f"文件指针的位置:{file.tell()}")

f=file
# seek 启动文件指针,寻找第五个字符
n=f.seek(5)
print ( n )

file.close()


# a模式 append 追加模式
file = open ( "aa.txt", "a", encoding="utf8" )
file.write ( "德玛西亚" )
#
#
file.close()



# # print(r"C:\Users\bcc\Desktop\code15\pybase")
#
# # 文件备份
# # 先读取一个文件
# # 把读取文件写入到另外一个文件中
# #
# def file_copy(file_name):
#     # aa.txt 文件  aa-备份.txt
#     # bb.txt 文件  bb-备份.txt
#     file = open(file_name,"rb")
#
#     # content = file.read()
#     name_list = file_name.split(".")  # self.strip.split("-")中strip代表去除字符串两端的空白
#     new_name = name_list[0] + "-备份." + name_list[1]
#     print(file_name)
#     print(new_name)
#     new_file = open(new_name,"wb")
#     #
#     # new_file.write(content)
#     new_file.write(file.read())
#     #
#     file.close() 约等于file.flush
#     new_file.close()
#
# # # file_copy("aa.txt")
# # # "aa.txt" 的分割结果为 "aa","txt"
# # # str_a = "aa.txt"
# # # print(str_a.split("."))
#
# # file_copy("15面向对象.py")

# file_copy("aa/aa.jpg")



import pickle
x, y, z = 1, 2, 3
s = "FishC"
l = ["小甲鱼", 520, 3.14]
d = {"one": 1, "two": 2, "three": 3}
with open ( "data.pkl", "wb" ) as f:
    pickle.dump ( (x, y, z), f )
print((x,y,z),s,l,sep="\n")



import yaml

with open("aa.yml","r",encoding="utf8") as f:
    yaml_obj = yaml.load(f.read(),Loader=yaml.FullLoader)
    print(yaml_obj)    #dict




# 备份文件
from typing import BinaryIO

filename = input ( "请输入要备份的文件的名称：" )
oldFile: BinaryIO = open ( filename, "rb" )
fileFlagNum = filename.rfind ( "." )
fileflag = filename[fileFlagNum:]
print ( fileflag )

newFileName = filename[:fileFlagNum] + "-复件" + fileflag
print ( newFileName )

newfile = open ( newFileName, "wb" )
for linecontent in oldFile.readlines ():
    newfile.write ( linecontent )

oldFile.close ()
newfile.close ()



