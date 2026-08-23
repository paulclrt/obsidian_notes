Code is available: [[3.0_main.py]]

|**Hyperparameter**|**Binary Classification**|**Multiclass classification**|
|---|---|---|
|**Input layer shape** (`in_features`)|Same as number of features (e.g. 5 for age, sex, height, weight, smoking status in heart disease prediction)|Same as binary classification|
|**Hidden layer(s)**|Problem specific, minimum = 1, maximum = unlimited|Same as binary classification|
|**Neurons per hidden layer**|Problem specific, generally 10 to 512|Same as binary classification|
|**Output layer shape** (`out_features`)|1 (one class or the other)|1 per class (e.g. 3 for food, person or dog photo)|
|**Hidden layer activation**|Usually [ReLU](https://pytorch.org/docs/stable/generated/torch.nn.ReLU.html#torch.nn.ReLU) (rectified linear unit) but [can be many others](https://en.wikipedia.org/wiki/Activation_function#Table_of_activation_functions)|Same as binary classification|
|**Output activation**|[Sigmoid](https://en.wikipedia.org/wiki/Sigmoid_function) ([`torch.sigmoid`](https://pytorch.org/docs/stable/generated/torch.sigmoid.html) in PyTorch)|[Softmax](https://en.wikipedia.org/wiki/Softmax_function) ([`torch.softmax`](https://pytorch.org/docs/stable/generated/torch.nn.Softmax.html) in PyTorch)|
|**Loss function**|[Binary crossentropy](https://en.wikipedia.org/wiki/Cross_entropy#Cross-entropy_loss_function_and_logistic_regression) ([`torch.nn.BCELoss`](https://pytorch.org/docs/stable/generated/torch.nn.BCELoss.html) in PyTorch)|Cross entropy ([`torch.nn.CrossEntropyLoss`](https://pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html) in PyTorch)|
|**Optimizer**|[SGD](https://pytorch.org/docs/stable/generated/torch.optim.SGD.html) (stochastic gradient descent), [Adam](https://pytorch.org/docs/stable/generated/torch.optim.Adam.html) (see [`torch.optim`](https://pytorch.org/docs/stable/optim.html) for more options)|Same as binary classification|


|Loss function/Optimizer|Problem type|PyTorch Code|
|---|---|---|
|Stochastic Gradient Descent (SGD) optimizer|Classification, regression, many others.|[`torch.optim.SGD()`](https://pytorch.org/docs/stable/generated/torch.optim.SGD.html)|
|Adam Optimizer|Classification, regression, many others.|[`torch.optim.Adam()`](https://pytorch.org/docs/stable/generated/torch.optim.Adam.html)|
|Binary cross entropy loss|Binary classification|[`torch.nn.BCELossWithLogits`](https://pytorch.org/docs/stable/generated/torch.nn.BCEWithLogitsLoss.html) or [`torch.nn.BCELoss`](https://pytorch.org/docs/stable/generated/torch.nn.BCELoss.html)|
|Cross entropy loss|Multi-class classification|[`torch.nn.CrossEntropyLoss`](https://pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html)|
|Mean absolute error (MAE) or L1 Loss|Regression|[`torch.nn.L1Loss`](https://pytorch.org/docs/stable/generated/torch.nn.L1Loss.html)|
|Mean squared error (MSE) or L2 Loss|Regression|[`torch.nn.MSELoss`](https://pytorch.org/docs/stable/generated/torch.nn.MSELoss.html#torch.nn.MSELoss)|


If the model is doing stuff that is "random", the plot helpher function can help
```python
import requests
from pathlib import Path 

# Download helper functions from Learn PyTorch repo (if not already downloaded)
if Path("helper_functions.py").is_file():
  print("helper_functions.py already exists, skipping download")
else:
  print("Downloading helper_functions.py")
  request = requests.get("https://raw.githubusercontent.com/mrdbourke/pytorch-deep-learning/main/helper_functions.py")
  with open("helper_functions.py", "wb") as f:
    f.write(request.content)

from helper_functions import plot_predictions, plot_decision_boundary

# Plot decision boundaries for training and test sets
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title("Train")
plot_decision_boundary(model_0, X_train, y_train)
plt.subplot(1, 2, 2)
plt.title("Test")
plot_decision_boundary(model_0, X_test, y_test)
```

![[pytorch_decision_boundary.png]]



|Model improvement technique*|What does it do?|
|---|---|
|**Add more layers**|Each layer _potentially_ increases the learning capabilities of the model with each layer being able to learn some kind of new pattern in the data. More layers are often referred to as making your neural network _deeper_.|
|**Add more hidden units**|Similar to the above, more hidden units per layer means a _potential_ increase in learning capabilities of the model. More hidden units are often referred to as making your neural network _wider_.|
|**Fitting for longer (more epochs)**|Your model might learn more if it had more opportunities to look at the data.|
|**Changing the activation functions**|Some data just can't be fit with only straight lines (like what we've seen), using non-linear activation functions can help with this (hint, hint).|
|**Change the learning rate**|Less model specific, but still related, the learning rate of the optimizer decides how much a model should change its parameters each step, too much and the model overcorrects, too little and it doesn't learn enough.|
|**Change the loss function**|Again, less model specific but still important, different problems require different loss functions. For example, a binary cross entropy loss function won't work with a multi-class classification problem.|
|**Use transfer learning**|Take a pretrained model from a problem domain similar to yours and adjust it to your own problem. We cover transfer learning in [notebook 06](https://www.learnpytorch.io/06_pytorch_transfer_learning/).|


## Classification evaluation metrics

|**Metric name/Evaluation method**|**Defintion**|**Code**|
|---|---|---|
|Accuracy|Out of 100 predictions, how many does your model get correct? E.g. 95% accuracy means it gets 95/100 predictions correct.|[`torchmetrics.Accuracy()`](https://torchmetrics.readthedocs.io/en/stable/classification/accuracy.html#id3) or [`sklearn.metrics.accuracy_score()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html)|
|Precision|Proportion of true positives over total number of samples. Higher precision leads to less false positives (model predicts 1 when it should've been 0).|[`torchmetrics.Precision()`](https://torchmetrics.readthedocs.io/en/stable/classification/precision.html#id4) or [`sklearn.metrics.precision_score()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html)|
|Recall|Proportion of true positives over total number of true positives and false negatives (model predicts 0 when it should've been 1). Higher recall leads to less false negatives.|[`torchmetrics.Recall()`](https://torchmetrics.readthedocs.io/en/stable/classification/recall.html#id5) or [`sklearn.metrics.recall_score()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html)|
|F1-score|Combines precision and recall into one metric. 1 is best, 0 is worst.|[`torchmetrics.F1Score()`](https://torchmetrics.readthedocs.io/en/stable/classification/f1_score.html#f1score) or [`sklearn.metrics.f1_score()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html)|
|[Confusion matrix](https://www.dataschool.io/simple-guide-to-confusion-matrix-terminology/)|Compares the predicted values with the true values in a tabular way, if 100% correct, all values in the matrix will be top left to bottom right (diagnol line).|[`torchmetrics.ConfusionMatrix`](https://torchmetrics.readthedocs.io/en/stable/classification/confusion_matrix.html#confusionmatrix) or [`sklearn.metrics.plot_confusion_matrix()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay.from_predictions)|
|Classification report|Collection of some of the main classification metrics such as precision, recall and f1-score.|[`sklearn.metrics.classification_report()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html)|
