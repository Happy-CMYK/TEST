
#coding=gbk

import os
import torch
import numpy  as np
#ʹ��torch��������torch��������


a=torch.randn(2,3)
print(a.type())
a = a.type(torch.int64)

print(a.type())

a=torch.randn(2,3)
print(a.size())

a=torch.randn(2,)
print(a.size())
a=torch.randn(6)
print(a.size())

os.system("pause")
