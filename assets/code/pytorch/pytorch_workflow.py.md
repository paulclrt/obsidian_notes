import torch
from torch import nn
import matplotlib.pyplot as plt

print(f"Torch version: {torch.__version__}")


# --- 1. DATA PREPARATION ---

# Create a simple line (y = x)
x = torch.arange(0, 100, 10, dtype=torch.float32)
y = torch.arange(0, 100, 10, dtype=torch.float32)

# Split into training and validation sets (80/20)
training_split = int(len(x) * 0.8)
x_train, y_train = x[:training_split], y[:training_split]
x_validation, y_validation = x[training_split:], y[training_split:]

print(f"Train: {len(x_train)} | Validation: {len(x_validation)}")


# --- 2. PLOT DATA ---

def plot_predictions(train_data=x_train,
                     train_labels=y_train,
                     test_data=x_validation,
                     test_labels=y_validation,
                     predictions=None):
    plt.figure(figsize=(10, 7))
    plt.scatter(train_data, train_labels, c="b", s=4, label="Training data")
    plt.scatter(test_data, test_labels, c="g", s=4, label="Validation data")

    if predictions is not None:
        plt.scatter(test_data, predictions, c="r", s=4, label="Model output")

    plt.legend(prop={"size": 14})

plot_predictions()


# --- 3. BUILD MODEL ---

class LinearRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.weights = nn.Parameter(torch.randn(1, dtype=torch.float32), requires_grad=True)
        self.bias = nn.Parameter(torch.randn(1, dtype=torch.float32), requires_grad=True)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.weights * x + self.bias

torch.manual_seed(42)

model_0 = LinearRegressionModel()
print(f"Parameters: {list(model_0.parameters())}")
print(f"State dict: {model_0.state_dict()}")


# --- 4. INFERENCE (PREDICTION WITHOUT TRAINING) ---

with torch.inference_mode():
    y_preds = model_0(x_validation)

print(f"Original input: {x_validation}")
print(f"Predictions: {y_preds}")
plot_predictions(predictions=y_preds)


# --- 5. TRAINING LOOP ---

loss_fn = nn.L1Loss()
optimizer = torch.optim.SGD(params=model_0.parameters(), lr=0.01)

epochs = 100

for epoch in range(epochs):
    model_0.train()

    y_pred = model_0(x_train)
    loss = loss_fn(y_pred, y_train)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 10 == 0:
        model_0.eval()
        with torch.inference_mode():
            preds = model_0(x_validation)
            test_loss = loss_fn(preds, y_validation)
            print(f"Epoch {epoch}/{epochs} | Train loss: {loss} | Test loss: {test_loss}")

print("After training:")
preds = model_0(x_validation)
print(f"Predictions: {preds}")
print(f"Error: {y_validation - preds}")


# --- 6. SAVE & LOAD MODEL ---

from pathlib import Path

modelpath = Path("model")
modelpath.mkdir(parents=True, exist_ok=True)

modelname = "01_pytorch_workflow_model0.pth"
model_save_path = modelpath / modelname

torch.save(obj=model_0.state_dict(), f=model_save_path)

loaded_model_0 = LinearRegressionModel()
loaded_model_0.load_state_dict(torch.load(f=model_save_path))

loaded_model_0.eval()
p = loaded_model_0(x_validation)
print(f"Loaded model results: {p}")


# --- 7. GPU SUPPORT (optional) ---

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Current device: {next(model_0.parameters()).device}")
model_0.to(device)