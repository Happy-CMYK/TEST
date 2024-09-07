import pymysql

# connon 连接数据库
conn = pymysql.connect (
    host="127.0.0.1",
    port=3306,
    user="root",
    passwd="root",
    database="mysql",
    charset="utf8"
)

# 游标对象
cursor = conn.cursor ()

cursor.execute('show databases;')


# sql_1 = "update students set name ='李云飞'where id=3"
i = 1
while i < 5:
    i = i + 1
    # 需要格式化"f"
    sql_1 = f"insert into students value (0,'lisions{i}',18{18 + i},1.88,'男',1,0)"
    num = cursor.execute ( sql_1 )
    conn.commit ()

    print ( i )

# cursor.close ()
# conn.close ()

# sql注入
# 登录
# 用户名 和密码存放在数据库
try:
    sql_1 = "update students set name ='钢蛋' where id = 5"
    # 在python中所有sql语句的执行  自动开启事务 但是不会自动提交
    cursor.execute(sql_1)
    conn.commit()
except Exception as e:
    conn.rollback()

sql ='select * from students '
num = cursor.execute(sql)
print(num)
# 拿到所有数据
print (cursor.fetchall())
# 拿到第一条数据
print (cursor.fetchone())
# 拿到其中几条数据
print ( cursor.fetchmany ( 5 ) )

def login(username,pwd):
    sql = f'select * from users where username="{username}" and pwd = %s'
    print(sql)

    row_conut = cursor.execute(sql,pwd)
    print(row_conut)
    if row_conut>0:
        print("登录成功")
    else:
        print("登录失败")

login("abc","12345\" or \"1 =1")
for i in range(row_conut):
    print(cursor.fetchone())

print(cursor.fetchmany(5))
print(cursor.fetchall())

cursor.close ()
# conn.close()





