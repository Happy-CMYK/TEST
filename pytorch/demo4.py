#coding=gbk


import os
import torch
import numpy  as np
import matplotlib.pyplot as plt
#ʹ��torch��������torch��������
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



m = nn.LogSoftmax(dim=1) #�������
loss = nn.NLLLoss()
torch.manual_seed(2)
# 3��5�е����룬��3������������5��������ÿ������ͨ��softmax����5�����
input = torch.randn(3, 5, requires_grad=True)
target = torch.tensor([1, 0, 4])
# NLL��ȡ��������е�0�еĵ�1�С���1�еĵ�0�С���2�еĵ�4�мӸ������
output = loss(m(input), target)
print(output)


