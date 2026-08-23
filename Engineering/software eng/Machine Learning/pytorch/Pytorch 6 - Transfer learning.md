
"take a model that is good, take your data, boom"
... basically what this is

_A study into the effects of whether training from scratch or using transfer learning was better from a practitioner's point of view, found transfer learning to be far more beneficial in terms of cost and time. **Source:** [How to train your ViT? Data, Augmentation, and Regularization in Vision Transformers](https://arxiv.org/abs/2106.10270) paper section 6 (conclusion)._

## Where to find pretrained models
|**Location**|**What's there?**|**Link(s)**|
|---|---|---|
|**PyTorch domain libraries**|Each of the PyTorch domain libraries (`torchvision`, `torchtext`) come with pretrained models of some form. The models there work right within PyTorch.|[`torchvision.models`](https://pytorch.org/vision/stable/models.html), [`torchtext.models`](https://pytorch.org/text/main/models.html), [`torchaudio.models`](https://pytorch.org/audio/stable/models.html), [`torchrec.models`](https://pytorch.org/torchrec/torchrec.models.html)|
|**HuggingFace Hub**|A series of pretrained models on many different domains (vision, text, audio and more) from organizations around the world. There's plenty of different datasets too.|[https://huggingface.co/models](https://huggingface.co/models), [https://huggingface.co/datasets](https://huggingface.co/datasets)|
|**`timm` (PyTorch Image Models) library**|Almost all of the latest and greatest computer vision models in PyTorch code as well as plenty of other helpful computer vision features.|[https://github.com/rwightman/pytorch-image-models](https://github.com/rwightman/pytorch-image-models)|
|**Paperswithcode**|A collection of the latest state-of-the-art machine learning papers with code implementations attached. You can also find benchmarks here of model performance on different tasks.|[https://paperswithcode.com/](https://paperswithcode.com/)|


This course section is bascially: internet access to model or on device (edge)

|**Tool/resource**| **Deployment type**           |
|---|---|
|[Google's ML Kit](https://developers.google.com/ml-kit)| On-device (Android and iOS)   |
|[Apple's Core ML](https://developer.apple.com/documentation/coreml) and [`coremltools` Python package](https://coremltools.readme.io/docs)| On-device (all Apple devices) |
|[Amazon Web Service's (AWS) Sagemaker](https://aws.amazon.com/sagemaker/)| Cloud                         |
|[Google Cloud's Vertex AI](https://cloud.google.com/vertex-ai)| Cloud                         |
|[Microsoft's Azure Machine Learning](https://azure.microsoft.com/en-au/services/machine-learning/)| Cloud                         |
|[Hugging Face Spaces](https://huggingface.co/spaces)| Cloud                         |
|API with [FastAPI](https://fastapi.tiangolo.com)| Cloud/self-hosted server      |
|API with [TorchServe](https://pytorch.org/serve/)| Cloud/self-hosted server      |
|[ONNX (Open Neural Network Exchange)](https://onnx.ai/index.html)| Many/general                  |
|Many more...|                               |


Pytorch comes with some pretrained models installed:

|**Architecuture backbone**|**Code**|
|---|---|
|[ResNet](https://arxiv.org/abs/1512.03385)'s|`torchvision.models.resnet18()`, `torchvision.models.resnet50()`...|
|[VGG](https://arxiv.org/abs/1409.1556) (similar to what we used for TinyVGG)|`torchvision.models.vgg16()`|
|[EfficientNet](https://arxiv.org/abs/1905.11946)'s|`torchvision.models.efficientnet_b0()`, `torchvision.models.efficientnet_b1()`...|
|[VisionTransformer](https://arxiv.org/abs/2010.11929) (ViT's)|`torchvision.models.vit_b_16()`, `torchvision.models.vit_b_32()`...|
|[ConvNeXt](https://arxiv.org/abs/2201.03545)|`torchvision.models.convnext_tiny()`, `torchvision.models.convnext_small()`...|
|More available in `torchvision.models`|`torchvision.models...`|

```python
# there is from pytorch v0.13+ a autotransform creation
# basically if the model i already known, pytorch can find the transform required
# you need to specify the weights used though
weights = torchvision.models.EfficientNet_B0_Weights.DEFAULT
auto_transforms = weights.transforms()
print("Auto transforms: ")
print(auto_transforms)

# creating the model (using a prexisting one)
model = torchvision.models.efficientnet_b0(weights=weights).to(device)
```

Our `efficientnet_b0` comes in three main parts:
1. `features` - A collection of convolutional layers and other various activation layers to learn a base representation of vision data (this base representation/collection of layers is often referred to as **features** or **feature extractor**, "the base layers of the model learn the different **features** of images").
2. `avgpool` - Takes the average of the output of the `features` layer(s) and turns it into a **feature vector**.
3. `classifier` - Turns the **feature vector** into a vector with the same dimensionality as the number of required output classes (since `efficientnet_b0` is pretrained on ImageNet and because ImageNet has 1000 classes, `out_features=1000` is the default).