import torch
# from torchviz import make_dot
# x  = torch.rand(3,requires_grad=True)
# #requires_grad=True means pytorch will automatically create a function for us which is used in backpropagation
# print(x)
# y = x + 2
# print(y)
# z = y * 2 * 2 + 10 - 5
# z = z.mean()
# print(z)
# z.backward()
# print(x.grad) # this will print the gradient of z with respect to x 

x = torch.ones(2,requires_grad=True)
y = x + 2
z = y * 2
z = z.mean()
z.backward()
print(x.grad)