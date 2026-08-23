Code is availble: [[4.0_main.py]] and here: [[4.1_main.py]]

| PyTorch module                                                                                     | What does it do?                                                                                                                                                                                                                                                                                                                       |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`torchvision`](https://pytorch.org/vision/stable/index.html)                                      | Contains datasets, model architectures and image transformations often used for computer vision problems.                                                                                                                                                                                                                              |
| [`torchvision.datasets`](https://pytorch.org/vision/stable/datasets.html)                          | Here you'll find many example computer vision datasets for a range of problems from image classification, object detection, image captioning, video classification and more. It also contains [a series of base classes for making custom datasets](https://pytorch.org/vision/stable/datasets.html#base-classes-for-custom-datasets). |
| [`torchvision.models`](https://pytorch.org/vision/stable/models.html)                              | This module contains well-performing and commonly used computer vision model architectures implemented in PyTorch, you can use these with your own problems.                                                                                                                                                                           |
| [`torchvision.transforms`](https://pytorch.org/vision/stable/transforms.html)                      | Often images need to be transformed (turned into numbers/processed/augmented) before being used with a model, common image transformations are found here.                                                                                                                                                                             |
| [`torch.utils.data.Dataset`](https://pytorch.org/docs/stable/data.html#torch.utils.data.Dataset)   | Base dataset class for PyTorch.                                                                                                                                                                                                                                                                                                        |
| [`torch.utils.data.DataLoader`](https://pytorch.org/docs/stable/data.html#module-torch.utils.data) | Creates a Python iterable over a dataset (created with `torch.utils.data.Dataset`).<br>                                                                                                                                                                                                                                                |
|                                                                                                    |                                                                                                                                                                                                                                                                                                                                        |

The dataloader turns a large dataset into smaller chunk for the model to process better.
We call these  chunks **batches** or **mini-batches** and can be set using the **batch_size** argument.


## Writing device agnostic code

This is very simple:
1. Set `device` to 'cpu' or 'cuda' or whatever
2. in all your code/function do `tensor.to(device)`

## What model to use and when

|**Problem type**|**Model to use (generally)**| **Code example**                                                                                                                                                 |
|---|---|---|
|Structured data (Excel spreadsheets, row and column data)|Gradient boosted models, Random Forests, XGBoost| [`sklearn.ensemble`](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.ensemble), [XGBoost library](https://xgboost.readthedocs.io/en/stable/) |
|Unstructured data (images, audio, language)|Convolutional Neural Networks, Transformers| [`torchvision.models`](https://pytorch.org/vision/stable/models.html), [HuggingFace Transformers](https://huggingface.co/docs/transformers/index)<br>            |


There are still elements that could be added froim the original article: https://www.learnpytorch.io/03_pytorch_computer_vision/
Like confusion matrices:
![[confusion_matrix.png]]