#coding=gbk


import os
import torch
import numpy  as np
import matplotlib.pyplot as plt
#使用torch函数生成torch数据类型
import torch.nn as nn

from torch.autograd import Variable
predict = Variable(torch.randint(0,4,(2, 3)).type(dtype=torch.float32), requires_grad=True)


a=torch.Tensor([[1,2,2],[1,1,2]])

target = Variable (a)
print(predict)

print(target)
criterion = nn.L1Loss()
loss = criterion(predict, target)
print(loss)

print(predict)
print(target)
criterion = nn.SmoothL1Loss()
loss = criterion(predict, target)
print(loss)

print(predict)
print(target)
criterion = nn.MSELoss()
loss = criterion(predict, target)
print(loss)



print(predict)
print(target)
criterion = nn.CrossEntropyLoss()
loss = criterion(predict, target)
print(loss)



m = nn.LogSoftmax(dim=1) #横向计算
loss = nn.NLLLoss()
torch.manual_seed(2)
# 3行5列的输入，即3个样本各包含5个特征，每个样本通过softmax产生5个输出
input = torch.randn(3, 5, requires_grad=True)
target = torch.tensor([1, 0, 4])
# NLL将取输出矩阵中第0行的第1列、第1行的第0列、第2行的第4列加负号求和
output = loss(m(input), target)
print(output)


