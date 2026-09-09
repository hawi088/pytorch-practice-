from xml.parsers.expat import model

import torch
import torch.nn as nn
class MyNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.w = nn.Parameter(torch.tensor(3.0))
        self.b = nn.Parameter(torch.tensor(1.0))
    def forward(self,x):
        return self.w * x + self.b
model = MyNetwork()
x = torch.tensor(2.0)
y = model(x)
y.backward()
print(model.w.grad)
# tensor(2.)

print(model.b.grad)
# tensor(1.)