# 正侧表达式
content = """绿油油,红彤彤,金灿灿,黑乎乎,绿油油油"""
import re

# 最好加上"r",,,指定本次需要操作的正则表达式
p = re.compile ( r".油." )
# 利用当前的这个正则表达式在content这个文本中,查找所有的匹配项,结果是一个列表
message = p.findall ( content )
print ( message )

# 表示油出现2次,或者3次
p = re.compile ( "油{2,3}" )
message = p.findall ( content )
print ( message )

p = re.compile ( ",.*" )
message = p.findall ( content )
print ( message )

content = """<html>,<head,<title>Title</title>"""
import re

# ?表示单独取出每个标签
p = re.compile ( r"<.*?>" )
message = p.findall ( content )
print ( message )

content = """苹果.是绿色的
橙子.是黄色的
香蕉.是黄色的
"""
import re

# .和正则表达式有冲突需要用到转义字符\,这里的'r'就不需要了
p = re.compile ( ".*\." )
message = p.findall ( content )
print ( message )

content = """苹果.是5的_橙子.是6的_香蕉.是7的
不好吃"""
import re

# .和正则表达式有冲突需要用到转义字符\,这里的'r'就不需要了
p = re.compile ( "\D" )  # 匹配任意一个不是"0-9"的数字字符
message = p.findall ( content )
print ( message )

p = re.compile ( "\s" )  # 匹配任意一个空白字符
message = p.findall ( content )
print ( message )

p = re.compile ( "\S" )  # 匹配任意一个非空白字符
message = p.findall ( content )
print ( message )

p = re.compile ( "\w" )  # 匹配任意一个文字字符
message = p.findall ( content )
print ( message )

p = re.compile ( "\W" )  # 匹配任意一个非文字字符
message = p.findall ( content )
print ( message )

content = """001-苹果-60
002-香蕉-50
003-橘子-40"""
# 默认单行模式,需要开启多行模式需要添加're.MULTILINE'

# ^表示开头
p = re.compile ( "^\d+-", re.MULTILINE )
message = p.findall ( content )
print ( message )

# $表示结尾,多行模式
p = re.compile ( "-\d*$", re.MULTILINE )
message = p.findall ( content )
print ( message )

# 单行模式
p = re.compile ( "-\d*$" )
message = p.findall ( content )
print ( message )

p = re.compile ( "苹|橘子|5" )
message = p.findall ( content )
print ( message )

p = re.compile ( "(.*)-" )
message = p.findall ( content )
print ( message )

content = """
张三,手机号码为1523222356
李四,手机号码为51626646
王五,手机号码为5245226663"""

p = re.compile ( "(.*),手机号码为(\d*)" )
message = p.findall ( content )
print ( message )

# \D 里一个D表示不是"0-9"的数字字符字符,D*表示多个不是"0-9"的数字字符
p = re.compile ( "(.*),\D*(\d*)" )
message = p.findall ( content )
print ( message )

content = """
2万/月
2.5万/每月"""

# - "([\d\.]*)"：表示匹配任意数字或小数点，使用括号将其分组，方便后续提取。
# - "万/每{0,1}月"：表示匹配“万/月”或“万/每月”，其中“每”字可有可无，使用花括号表示可选项
p = re.compile ( "([\d\.]*)万/每{0,1}月" )
message = p.findall ( content )
for i in message:
    print ( i )
print(message)
