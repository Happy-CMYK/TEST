#coding=gbk


import os
import torch
import numpy  as np
import matplotlib.pyplot as plt

from torch.utils import data
from numpy import random
#使用torch函数生成torch数据类型
import torch.nn as nn

from torch.autograd import Variable
torch.manual_seed(1)

X = np.linspace(-1, 1, 200)
Y = 0.5 * X + 0.2* np.random.normal(0, 0.5, (200, ))
#plt.scatter(X,Y)
#plt.show()
#将X，Y转成200 batch大小，1维度的数据
X=Variable(torch.Tensor(X.reshape(200,1)))
Y=Variable(torch.Tensor(Y.reshape(200,1)))

model = torch.nn.Sequential(torch.nn.Linear(1, 1),)

optimizer = torch.optim.SGD(model.parameters(), lr=0.5)
loss_function = torch.nn.MSELoss()
for i in range(300):
     prediction = model(X)
     loss = loss_function(prediction, Y)
     optimizer.zero_grad()
     loss.backward()
     optimizer.step()

#plt.figure(1, figsize=(5, 5))

#plt.title('model')
#plt.scatter(X.data.numpy(), Y.data.numpy())
#plt.plot(X.data.numpy(), prediction.data.numpy(), 'r-', lw=5)
#plt.show()


X =torch.randn(100,4)
w=torch.tensor([1,2,3,4])

Y =torch.matmul(X, w.type(dtype=torch.float))  + torch.normal(0, 0.1, (100, ))+6.5
Y=Y.reshape((-1, 1))
print(Y.type())
print(w.type())
print(X.type())
#将X，Y转成200 batch大小，1维度的数据
X=Variable(X)
Y=Variable(Y)
def load_array(data_arrays, batch_size, is_train=True):
    dataset = data.TensorDataset(*data_arrays)
    return data.DataLoader(dataset, batch_size, shuffle=is_train)

data_iter = load_array((X, Y), 32)


model = torch.nn.Sequential(torch.nn.Linear(4, 1))

optimizer = torch.optim.SGD(model.parameters(), lr=0.03)
loss_function = torch.nn.MSELoss()
num_epochs = 20
for epoch in range(num_epochs):
    for x, y in data_iter:
        l = loss_function(model(x), y)
        optimizer.zero_grad()
        l.backward()
        optimizer.step()
    l = loss_function(model(X), Y)
    print(f'epoch {epoch + 1}, loss {l:f}')

for para in model.parameters():
        print(para)
