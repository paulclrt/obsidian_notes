
Following this course: https://www.youtube.com/watch?v=Z_ikDlimN6A

(I skipped the first 40 minutes because i already wrote a lot on a blog on machine learning, deeplearning, maths etc)

**Ressource to learn more about recent SOTA models and training papers:** https://huggingface.co/papers/trending


## Tensors

"Tensors are generalizations of vectors and matrices to arbitrary higher dimensions."

Creating a tensor in PyTorch is made using the `torch.Tensor` class (or shortcut functions).

```python
# Scalar (0-dimensional tensor)
scalar = torch.tensor(7)
print(scalar)      # tensor(7)
print(scalar.ndim) # 0
print(scalar.item()) # 7 -> Python int
```

```python
# Vector (1-dimensional tensor)
v = torch.tensor([7, 2])
print(v)           # tensor([7, 2])
print(v.ndim)      # 1
print(v.shape)     # torch.Size([2])
```

```python
# Matrix (2-dimensional tensor)
M = torch.tensor([[7, 8], [9, 10]])
print(M.ndim)  # 2
print(M.shape) # torch.Size([2, 2])
```

```python
# 3D tensor (e.g. a batch of grayscale images: [batch, height, width])
tensor3d = torch.tensor([[1,2], [3,4], [4,5]])
print(tensor3d.ndim) # 3
print(tensor3d.shape) # torch.Size([3, 2, 2])
```

---

### Key tensor attributes

| Attribute | Description |
|---|---|
| `tensor.ndim` | Number of dimensions (rank) |
| `tensor.shape` | Tuple of dimension sizes |
| `tensor.dtype` | Data type (e.g., `torch.float32`, `torch.int64`) |
| `tensor.device` | Device (e.g., `cpu`, `cuda`) |
| `tensor.item()` | Convert 0-d tensor to Python number |
| `tensor.tolist()` | Convert tensor to Python list |

---

### Creating tensors

```python
# From Python scalars/lists
torch.tensor(5)              # 0-d
torch.tensor([1, 2, 3])      # 1-d
torch.tensor([[1,2], [3,4]]) # 2-d

# Explicit dtype and device
torch.tensor([1, 2, 3], dtype=torch.float32, device='cpu')

# Zeros / ones
torch.zeros(3, 4, dtype=torch.float32)
torch.ones(2, 3, dtype=torch.int64)

# Random tensors
torch.rand(2, 3)                # random floats in [0, 1)
torch.randn(2, 3)               # random floats from standard normal
torch.randint(0, 10, (2, 3))    # random ints in [0, 10)

# Like another tensor's shape
x = torch.randn(3, 4)
y = torch.zeros_like(x)  # same shape, all zeros

# Range tensors
torch.arange(start=0, end=10, step=1)    # [0, 1, 2, ..., 9]
torch.linspace(start=0, end=1, steps=5)  # [0, 0.25, 0.5, 0.75, 1]

# Eye (identity matrix)
torch.eye(3)  # 3x3 identity
```

---

### Reshaping and Resizing

```python
x = torch.randn(6)      # 1-d tensor with 6 elements
x_reshaped = x.view(2, 3)   # reshape to 2x3 matrix
# equivalently: x.reshape(2, 3)

# Important: view requires tensor to be contiguous in memory.
# If you need a non-contiguous reshape, use .reshape() instead.

# Flatten (view as 1-d)
flattened = x_reshaped.view(-1)     # -1 infers the dimension
flattened2 = x_reshaped.flatten()   # returns a new tensor (contiguous)

# Permute dimensions (swap axes)
# x shape: (batch, height, width, channels) -> (batch, channels, height, width)
x = torch.randn(2, 224, 224, 3)
x_permuted = x.permute(0, 3, 1, 2)  # now (2, 3, 224, 224)

# squeeze removes dimensions of size 1
x = torch.randn(1, 3, 224, 1)  # (1, 3, 224, 1)
xsqueezed = x.squeeze()       # (3, 224)

# unsqueeze adds a dimension of size 1 at a given dim
x_unsqueezed = x.unsqueeze(0)  # adds dim at index 0

# split tensor into chunks
a, b = torch.chunk(x, 2, dim=0)  # split into 2 chunks along dim 0

# cat tensors (concatenate)
cat = torch.cat([x, y], dim=1)  # concatenate along dim 1
```

---

### Basic tensor operations

```python
x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5, 6])

# Element-wise
print(x + y)      # tensor([5, 7, 9])
print(x - y)      # tensor([-3, -3, -3])
print(x * y)      # tensor([4, 10, 18])
print(x / y)      # tensor([0.2500, 0.4000, 0.5000])

# Matrix multiplication
A = torch.randn(3, 4)
B = torch.randn(4, 5)
C = A @ B           # or A.mm(B) -> shape (3, 5)
torch.matmul(A, B)  # preferred way

# Dot product
d = torch.dot(x, y)  # scalar

# Transpose / T
x = torch.randn(3, 4)
print(x.T)   # transpose (swap rows/cols)
print(x.mT)  # same as .T (newer API)

# In-place operations (modify existing tensor, save memory)
x.add_(1)  # x = x + 1, in-place
x.relu_()  # in-place ReLU

# Clamp values to a range
x_clamped = x.clamp(min=0, max=1)  # values < 0 -> 0, > 1 -> 1

# Sum, mean, min, max
print(x.sum())
print(x.mean())
print(x.max(), x.min())

# Argmin/argmax (indices)
print(x.argmax())  # index of max value

# Stack tensors (new dimension added)
x = torch.tensor([1, 2])
y = torch.tensor([3, 4])
stacked = torch.stack([x, y])  # shape (2, 2) -> new dim at front
```

---

### Models (nn.Module)

```python
torch.manual_seed(42)

# Linear layer: y = xW^T + b
linear = torch.nn.Linear(in_features=2, out_features=6)
x = torch.rand(size=(7, 2))     # batch of 7 samples, 2 features
output = linear(x)              # shape: (7, 6)

# Building a Multi-Layer Perceptron
class MyMLP(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(2, 16)
        self.fc2 = torch.nn.Linear(16, 10)
        self.relu = torch.nn.ReLU()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x

model = MyMLP()
output = model(torch.rand(5, 2))
```

---

### Getting info from tensors

```python
x = torch.arange(0, 100, 10)  # tensor([0, 10, 20, ..., 90])
print(x.shape)      # torch.Size([10])
print(x.min())      # 0
print(x.max())      # 90
print(x.sum())      # 450
print(x.mean())     # 45.0
print(x.type(torch.float32).mean())  # cast then compute mean
```

---

### Positional info

```python
print(x.argmin())  # tensor(0) -> index of minimum value
print(x.argmax())  # tensor(9) -> index of maximum value
```

---

### Data handling with pandas / numpy interop

```python
import pandas as pd
import numpy as np

# Tensor -> numpy (share memory when possible)
t = torch.rand(5)
n = t.numpy()  # t must be contiguous and on CPU

# numpy -> tensor
nt = torch.from_numpy(n)

# pandas <-> tensor via numpy
df = pd.DataFrame(t.numpy(), columns=["value"])
t_from_df = torch.from_numpy(df["value"].values)
```