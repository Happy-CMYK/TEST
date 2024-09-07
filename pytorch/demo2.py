#coding=gbk


import os
import torch
import numpy  as np
#ʹ��torch��������torch��������


a=torch.randn(2,3)
print(torch.is_tensor(a))

c=a.storage()

print(torch.is_storage(a))

print(torch.is_storage(c))


a=torch.randn(2,3)
b=torch.randn(7)
print(torch.numel(a))
print(torch.numel(b))


index=torch.tensor([[1,2],[2,1]])
value=torch.tensor([2,3],dtype=torch.float32)

t=torch.sparse_coo_tensor(index,value,(3,4))
print(t)


a=torch.randn(2,3)

b=torch.randn(2,4)

c=torch.randn(4,3)

print(a)
print(b)
print(c)
print(torch.cat((a,b),1))
print(torch.cat((a,c),0))


a=torch.randn(12,3)

print(torch.chunk(a,6,0))


a=torch.randn(3,12)

print(torch.chunk(a,6,1))

a=torch.randn(4,3)
index1=torch.LongTensor([[0,1,2,1]])
index2=torch.LongTensor([[0,1,2]])

print(a)
print(torch.gather(a,1,index1))

print(torch.gather(a,0,index2))



a=torch.randn(4,3)
index1=torch.LongTensor([0,1,2,1])
index2=torch.LongTensor([0,1,2])

print(a)
print(torch.index_select(a,1,index1))

print(torch.index_select(a,0,index2))

a=torch.randint(0,10,(2,3))

print(a)
b=torch.ge(a,5)
print(b)

a=torch.randint(0,10,(2,3))

print(a)
b=torch.ge(a,5)
print(b)
print(torch.masked_select(a,b))


a=torch.randint(0,10,(2,3))
print(a)
print(torch.nonzero(a))



a=torch.randint(0,10,(2,3))
b=a.reshape(3,2)
print(b)
b=a.reshape(6,1)
print(b)
b=a.reshape(1,6)
print(b)
b=a.reshape(6,)
print(b)



a=torch.randn(6,3)

print(a)
print(torch.split(a,3,0))

print(torch.split(a,[1,5],0))
a=torch.randn(3,6)
print(a)
print(torch.split(a,2,1))



a=torch.randint(0,10,(2,3))

print(a)
b=torch.unsqueeze(a,0)
print(b)
b=torch.unsqueeze(a,1)
print(b)



a=torch.randint(0,10,(2,3))

print(a)
b=torch.squeeze(a,0)
print(b)
a=torch.randint(0,10,(6,1))

b=torch.squeeze(a,0)
print(b)


a=torch.randint(0,10,(2,3))

b=torch.randint(0,10,(2,3))
print(a)
print(b)

print(torch.stack((a,b),1))
print(torch.stack((a,b),0))


a=torch.randint(0,10,(2,3))
print(a)
print(torch.t(a))



a=torch.randint(0,10,(2,3))
print(a)
print(torch.transpose(a,0,1))




a=torch.randint(0,10,(2,3))
print(a)
print(torch.unbind(a,0))
print(torch.unbind(a,1))





a=torch.randint(0,10,(2,3))

b=torch.randint(0,10,(2,3))
print(a)
print(b)
print(torch.where(a>5,a,b))

torch.manual_seed(10)
print(torch.initial_seed())


a=torch.tensor([[0.5,0.2],[0.4,0.6]])
print(a)
print(torch.bernoulli(a))


a=torch.tensor([[0.5,0.2],[0.4,0.6]])
print(a)
print(torch.multinomial(a,4, replacement=True))

a=torch.rand(2,3)

print(torch.multinomial(a,4, replacement=True))
a=torch.rand(2,3)
print(a)
print(torch.multinomial(a,4, replacement=True))


print(torch.normal(0,1,(2,3)))

print(torch.normal(0,3,(2,3)))

a=torch.rand(2,3)
torch.save(a,"tensor.pt")


device=torch.device('cpu')
a=torch.load('tensor.pt',map_location=device)

print(a)



a=torch.randn(2,3)
print(a)
#����ֵ����
print(torch.abs(a))
a=torch.rand(2,3)

#�����Ҵ���
print(torch.acos(a))

#�����Ҵ���
print(torch.asin(a))

#���Ҵ���
print(torch.sin(a))

#���д���
print(torch.tan(a))

#˫�����д���
print(torch.tanh(a))

#˫�����Ҵ���
print(torch.sinh(a))
#�����д���
print(torch.atan(a))

#����ȡ��

print(torch.ceil(a))
#exp����
print(torch.exp(a))
#log����
print(torch.log(a))

#ȡ������
print(torch.neg(a))

#��������

print(torch.reciprocal(a))
#�õ���������
print(torch.remainder(a,0.2))
#����Ԫ�طֱ����һ��ֵ��
print(torch.add(a,10))#ÿ��Ԫ�ؼ�10

#�������봦��
print(torch.round(a))

#ƽ��������
print(torch.rsqrt(a))
#sigmoid��������
print(torch.sigmoid(a))

#�õ�Ԫ������boolֵ
print(torch.sign(a))
#��ƽ����
print(torch.sqrt(a))

c=torch.tensor([[0,0,0],[0,0,0]])
a=torch.randn(2,3)
b=torch.rand(2,3)
print(c)
print(a)

print(b)
print(torch.addcdiv(c,0.5,a,b))


c=torch.tensor([[0,0,0],[0,0,0]])
a=torch.randn(2,3)
b=torch.rand(2,3)
print(c)
print(a)
print(b)
print(torch.addcmul(c,0.5,a,b))

a=torch.randn(2,3)
b=torch.rand(2,3)
print(a)
print(b)

print(torch.mul(a,b))

a=torch.randint(1,4,(3,3))
print(a)
print(torch.cumprod(a,0))
print(torch.cumprod(a,1))



a=torch.randint(1,4,(3,3))
print(a)
print(torch.cumsum(a,0))
print(torch.cumsum(a,1))


a=torch.randint(1,5,(6,))

b=torch.randint(1,5,(6,))
a=a.type(dtype=torch.float32)
b=b.type(dtype=torch.float32)
print(a)
print(b)
print(torch.dist(a,b,2))


print(torch.dist(a,b,4))


a=torch.randint(1,5,(2,3))

b=torch.randint(1,5,(2,3))
a=a.type(dtype=torch.float32)
b=b.type(dtype=torch.float32)
print(a)
print(b)
print(torch.dist(a,b,2))


print(torch.dist(a,b,4))



a=torch.randint(1,4,(3,3))
print(a)

#���ֵ���ڶ�������������ķ��򣬰��л��ǰ���
print(torch.mean(a.type(dtype=torch.float32),0))
print(torch.mean(a.type(dtype=torch.float32),1))



#����λ�����ڶ�������������ķ��򣬰��л��ǰ���
print(torch.median(a,0))
print(torch.median(a,1))



#������
print(torch.mode(a,0))
print(torch.mode(a,1))
#�����P������⣬�ڶ���Ϊ��������������������Ϊ���ѡ��
print(torch.norm(a.type(dtype=torch.float32),2,0))
print(torch.norm(a.type(dtype=torch.float32),2,1))


#���۳˽�����ڶ����˲���������
print(torch.prod(a.type(dtype=torch.float32),0))
print(torch.prod(a.type(dtype=torch.float32),1))
#���׼��
print(torch.std(a.type(dtype=torch.float32),0))
print(torch.std(a.type(dtype=torch.float32),1))
#���
print(torch.sum(a,0))
print(torch.sum(a,1))
#�󷽲�
print(torch.var(a.type(dtype=torch.float32),0))
print(torch.var(a.type(dtype=torch.float32),1))
#�����ֵ
print(torch.max(a,0))
print(torch.max(a,1))
#����Сֵ
print(torch.min(a,0))
print(torch.min(a,1))
#��������
print(torch.sort(a,0))
print(torch.sort(a,1))



a=torch.randint(1,4,(3,3))

b=torch.randint(1,4,(3,3))
print(torch.eq(a,1))
print(torch.eq(a,b))



a=torch.randint(1,4,(3,3))

b=torch.randint(1,4,(3,3))
print(torch.equal(a,b))
a=torch.tensor([[1,2,3]])

b=torch.tensor([[1,2,3]])
print(torch.equal(a,b))

b=b.type(dtype=torch.float32)
print(a.type())
print(b.type())
print(torch.equal(a,b))



a=torch.randint(1,4,(3,3))

b=torch.randint(1,4,(3,3))
print(a)
print(b)
print(torch.ge(a,b))



a=torch.randint(1,4,(4,4))

print(a)

print(torch.kthvalue(a,2,0))

print(torch.kthvalue(a,2,1))


a=torch.randint(1,4,(4,4))

print(a)

print(torch.topk(a,2,0))

print(torch.topk(a,2,1))


a=torch.randint(1,4,(2,3))
b=torch.randint(1,4,(2,3))
print(a)
print(b)


print(torch.cross(a,b))



a=torch.randint(1,4,(2,3))
print(a)

print(torch.diag(a))
print(torch.diag(torch.tensor([1,2,3])))


a=torch.randint(1,10,(2,3))
print(a)

print(torch.histc(a.type(dtype=torch.float32),5))
a=torch.randint(1,10,(10,))
print(a)

print(torch.histc(a.type(dtype=torch.float32),5))
print(torch.histc(a.type(dtype=torch.float32),5,5,10))


a=torch.randint(1,10,(2,3))
print(a)

print(torch.renorm(a.type(dtype=torch.float32),2,0,10))

print(torch.renorm(a.type(dtype=torch.float32),2,1,10))


a=torch.randint(1,10,(2,3))
print(a)

print(torch.trace(a.type(dtype=torch.float32)))



a=torch.randint(1,10,(3,3))
print(a)

print(torch.tril(a.type(dtype=torch.float32)))


a=torch.randint(1,10,(3,3))
print(a)

print(torch.triu(a.type(dtype=torch.float32)))

a=torch.randint(1,10,(3,))
b=torch.randint(1,10,(3,))
print(a)
print(b)
print(torch.dot(a,b))



a=torch.randint(1,10,(3,3))
print(a)

print(torch.linalg.eig(a.type(dtype=torch.float32)))



a=torch.randint(1,10,(3,3))
print(a)

print(torch.inverse(a.type(dtype=torch.float32)))


a=torch.randint(1,5,(2,3))

b=torch.randint(1,5,(3,2))
print(a)
print(b)
print(torch.mm(a.type(dtype=torch.float32),b.type(dtype=torch.float32)))



a=torch.randint(1,5,(2,3))

b=torch.randint(1,5,(3,))
print(a)
print(b)
print(torch.mv(a.type(dtype=torch.float32),b.type(dtype=torch.float32)))
os.system("pause")

