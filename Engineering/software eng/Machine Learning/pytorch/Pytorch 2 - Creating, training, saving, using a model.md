Source: https://www.learnpytorch.io/02_pytorch_classification/

6 parts process:

| **Topic**                                                    | **Contents**                                                                                               |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| **1. Getting data ready**                                    | Create/prepare data, split into train/validation, visualize                                               |
| **2. Building a model**                                      | Create model class, choose loss function, optimizer                                                       |
| **3. Fitting the model to data (training)**                  | Training loop with epochs, forward pass, loss, backward pass, optimizer step                              |
| **4. Making predictions and evaluating a model (inference)** | Model evaluation on test data                                                                             |
| **5. Saving and loading a model**                            | Save/load model state_dict                                                                                |
| **6. Putting it all together**                               | Combine all steps                                                                                         |

---

## Step 1: Data Preparation

```python
# Create data (simple line y = x)
x = torch.arange(0, 100, 10, dtype=torch.float32)
y = torch.arange(0, 100, 10, dtype=torch.float32)

# Split into training (80%) and validation (20%)
training_split = int(len(x) * 0.8)
x_train, y_train = x[:training_split], y[:training_split]
x_validation, y_validation = x[training_split:], y[training_split:]

# Plot for visual check
def plot_predictions(train_data, train_labels, test_data, test_labels, predictions=None):
    plt.figure(figsize=(10, 7))
    plt.scatter(train_data, train_labels, c="b", s=4, label="Training")
    plt.scatter(test_data, test_labels, c="g", s=4, label="Validation")
    if predictions is not None:
        plt.scatter(test_data, predictions, c="r", s=4, label="Predictions")
    plt.legend(prop={"size": 14})
```

---

## Step 2: Build Model

```python
# Subclass nn.Module
class LinearRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.weights = nn.Parameter(torch.randn(1), requires_grad=True)
        self.bias = nn.Parameter(torch.randn(1), requires_grad=True)

    def forward(self, x):
        return self.weights * x + self.bias

# Instantiate
torch.manual_seed(42)
model = LinearRegressionModel()

# Loss & optimizer
loss_fn = nn.L1Loss()
optimizer = torch.optim.SGD(params=model.parameters(), lr=0.01)
```

---

## Step 3: Training Loop

```python
epochs = 100

for epoch in range(epochs):
    model.train()           # Set training mode

    # Forward pass
    y_pred = model(x_train)
    loss = loss_fn(y_pred, y_train)

    # Backward pass
    optimizer.zero_grad()   # Reset gradients
    loss.backward()         # Compute gradients
    optimizer.step()        # Update parameters

    # Print progress every 10 epochs
    if epoch % 10 == 0:
        model.eval()        # Set evaluation mode
        with torch.inference_mode():
            preds = model(x_validation)
            test_loss = loss_fn(preds, y_validation)
            print(f"Epoch {epoch}/{epochs} | Train: {loss:.4f} | Test: {test_loss:.4f}")
```

---

## Step 4: Inference & Evaluation

```python
# Make predictions
model.eval()
with torch.inference_mode():
    y_preds = model(x_validation)

print(f"Predictions: {y_preds}")
print(f"Error: {y_validation - y_preds}")
```

---

## Step 5: Save & Load Model

```python
from pathlib import Path

# Save
modelpath = Path("model")
modelpath.mkdir(parents=True, exist_ok=True)
torch.save(obj=model.state_dict(), f=modelpath / "model.pth")

# Load
loaded_model = LinearRegressionModel()
loaded_model.load_state_dict(torch.load(modelpath / "model.pth"))

loaded_model.eval()
preds = loaded_model(x_validation)
print(f"Loaded model results: {preds}")
```

---

## Step 6: GPU Support (optional)

```python
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Current device: {next(model.parameters()).device}")
model.to(device)
```

---

## Key PyTorch Modules

| Module | What does it do? |
|---|---|
| [`torch.nn`](https://pytorch.org/docs/stable/nn.html) | Building blocks for computational graphs |
| [`torch.nn.Parameter`](https://pytorch.org/docs/stable/generated/torch.nn.parameter.Parameter.html) | Stores tensors with `requires_grad=True` for autograd |
| [`torch.nn.Module`](https://pytorch.org/docs/stable/generated/torch.nn.Module.html) | Base class for all neural networks; requires `forward()` method |
| [`torch.optim`](https://pytorch.org/docs/stable/optim.html) | Optimization algorithms (SGD, Adam, etc.) |
| `forward()` | Defines the computation on input data |

---

## Loss & Optimizer Reference

| Function | What does it do? | Where does it live? | Common values |
|---|---|---|---|
| **Loss function** | Measures how wrong predictions are vs truth labels | [`torch.nn`](https://pytorch.org/docs/stable/nn.html#loss-functions) | `nn.L1Loss()` (regression), `nn.BCELoss()` (binary classification) |
| **Optimizer** | Tells model how to update parameters to minimize loss | [`torch.optim`](https://pytorch.org/docs/stable/optim.html) | `torch.optim.SGD()`, `torch.optim.Adam()` |

---

## Save/Load Reference

| Method | What does it do? |
|---|---|
| [`torch.save`](https://pytorch.org/docs/stable/torch.html?highlight=save#torch.save) | Saves serialized object to disk using `pickle` |
| [`torch.load`](https://pytorch.org/docs/stable/torch.html?highlight=torch%20load#torch.load) | Loads pickled object from disk |
| [`torch.nn.Module.load_state_dict`](https://pytorch.org/docs/stable/generated/torch.nn.Module.html?highlight=load_state_dict#torch.nn.Module.load_state_dict) | Loads model's parameter dictionary |