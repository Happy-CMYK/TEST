# coding=gbk
import os
import torch
import numpy  as np
import matplotlib.pyplot as plt
# 使用torch函数生成torch数据类型

from torch.autograd import Variable

x = Variable ( torch.randint ( 0, 4, (2, 3) ).type ( dtype=torch.float32 ), requires_grad=True )

print ( x )
# 进行x运算
y = x * x
out = y.mean ()
print ( y )

print ( out )

out.backward ()
print ( x.grad.data )

learning_rating = 0.000001
y_list = []


def grad_update(x):
    print ( "||" )
    print ( x )

    for i in range ( 1000 ):
        y = x * x
        out = torch.abs ( y.sum () )
        print ( out )
        out.backward ()
        x.data = x.data - (learning_rating * x.grad.data)
        # print(x.data)
        y_list.append ( out.data )
        print ( x.data )
        print ( x.grad.data )


grad_update ( x )
plt.plot ( list ( range ( len ( y_list ) ) ), y_list )
plt.show ()

