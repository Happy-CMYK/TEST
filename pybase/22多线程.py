from threading import Thread, Lock
from time import sleep

zhifubao = {
    'zhangsan': 10000,
    'lisi': 5000,
    'wangwu': 3000,
    'zhaolei': 5000
}

# 注意必须是Lock()
zhifu_lock = Lock ()


def thread1_didi_pay(account, amount):

    print ( '*t1:即将开始操作' )
    # 上锁
    zhifu_lock.acquire ()
    balance = zhifubao[account]

    print ( ('*t1:完成交易需要两秒钟') )
    sleep ( 2 )
    print ( ('*t1:deduct') )

    zhifubao[account] = balance - amount
    # 释放锁
    zhifu_lock.release ()


def thread2_yue_pay(account, amount):
    print ( '*t2:即将开始操作' )

    zhifu_lock.acquire ()
    balance = zhifubao[account]

    print ( ('*t2:完成交易需要两秒钟') )
    sleep ( 2 )
    print ( ('*t2:deduct') )
    zhifubao[account] = balance + amount
    zhifu_lock.release ()


t1 = Thread ( target=thread1_didi_pay, args=("zhangsan", 2000) )
t2 = Thread ( target=thread2_yue_pay, args=("zhangsan", 3000) )

t1.start ()
t2.start ()

t1.join ()
t2.join ()

print("---------------")
print(zhifubao['zhangsan'])