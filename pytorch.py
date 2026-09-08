import torch
import numpy as np
# x = torch.rand(3,2)
# y = torch.rand(3,2)
# z = x + y
# a = x-y
# b = x * y
# c = x / y
# print(z)
# print(a)
# print(b)
# print(c )
# d = torch.rand(4,4)
# print(d)
# e = d.view(16)
# print(e)

# x = torch.ones(5)
# print(x)
# print(x.dtype)
# print("=====")
# z = x.numpy()
# print(z)
# print(type(z))
# print("=====")
# x.add_(1)
# print(x)
# print(z)

# a = np.ones(5)
# print(a)
# b = torch.from_numpy(a)
# print(b)


x = torch.ones(5 , 3)
print(x)
print(x.shape)
print(x.size())

y = x.view(-1,5)
print(y)
A = torch.tensor([
    [1,3],
    [2,4],
    [7,3]
])
B = torch.tensor([
    [5,6],
    [7,8]   
])

# C = torch.matmul(B,A)
# print(C)

print("======")
d = A @ B
print(d)