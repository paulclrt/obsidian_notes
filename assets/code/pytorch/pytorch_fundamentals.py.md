import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


print(torch.__version__)


# --- Creating tensors ---

# Scalar (0-dimensional)
scalar = torch.tensor(7)
print(scalar)

# Tensor (multi-dimensional)
tensor = torch.tensor([[1,2], [3,4], [4,5]])
print(tensor)
print(tensor.ndim)
print(tensor.shape)

# Random tensors
zeros = torch.zeros([2, 4], dtype=torch.int32)
ones = torch.ones([9, 5], dtype=torch.float64)
print(zeros)
print(ones)

r = torch.rand(10, 10, dtype=torch.float64)
print(r)
print(r.shape)
print(r.ndim)

# Create a random tensor similar shape to an image tensor
img = torch.rand(size=(224, 224, 3))  # height, width, color channels
print(img.shape, img.ndim)


# --- Ranges ---

print("Specific torch range:")
r = torch.arange(start=10, end=100, step=3, dtype=torch.float32)
print(r)


# --- Tensor operations ---

# Element-wise operations
x = torch.tensor([1, 2, 3], dtype=torch.float32)
y = torch.tensor([4, 5, 6], dtype=torch.float32)
print("x + y:", x + y)
print("x * y:", x * y)

# Matrix multiplication
a = torch.rand(size=(2, 3))
b = torch.rand(size=(3, 2))
c = a @ b
print("Matrix multiplication:", c)


# --- Models ---

# Seed for reproducibility
torch.manual_seed(42)

# Linear layer: y = xW^T + b
linear = torch.nn.Linear(in_features=2, out_features=6)
x = torch.rand(size=(7, 2))
output = linear(x)
print(output)


# --- Getting info from tensors ---

x = torch.arange(0, 100, 10)
print(x)
print(x.shape)
print(x.min())
print(x.max())
print(x.sum())
print(x.type(torch.float32).mean())

# Positional info
print(x.argmin())
print(x.argmax())