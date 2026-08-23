Code is available: [[5.0_main.py]]
When you have your own data:
subclass `torch.utils.data.Dataset`

For each image:
- Turn it into tensors.
- Turn it into a `torch.utils.data.Dataset` and subsequently a `torch.utils.data.DataLoader`, we'll call these `Dataset` and `DataLoader` for short.

There are several different kinds of pre-built datasets and dataset loaders for PyTorch, depending on the problem you're working on.

|**Problem space**|**Pre-built Datasets and Functions**|
|---|---|
|**Vision**|[`torchvision.datasets`](https://pytorch.org/vision/stable/datasets.html)|
|**Audio**|[`torchaudio.datasets`](https://pytorch.org/audio/stable/datasets.html)|
|**Text**|[`torchtext.datasets`](https://pytorch.org/text/stable/datasets.html)|
|**Recommendation system**|[`torchrec.datasets`](https://pytorch.org/torchrec/torchrec.datasets.html)|

Checkout [[Data augmentation]] for creating data/noisy data out of thin air to improve model predictions and robustness
https://docs.pytorch.org/vision/main/auto_examples/transforms/plot_transforms_illustrations.html

> **Note:** One of the ways to speed up deep learning models computing on a GPU is to leverage **operator fusion**.
> 
> This means in the `forward()` method in our model above, instead of calling a layer block and reassigning `x` every time, we call each block in succession

**This is not optimized:**
```python
    def forward(self, x: torch.Tensor):
        x = self.conv_block_1(x)
        x = self.conv_block_2(x)
        x = self.classifier(x)
        return x
```

**This is:**
```python
    def forward(self, x: torch.Tensor):
        return self.classifier(self.conv_block_2(self.conv_block_1(x))) # <- leverage the benefits of operator fusion
```

See [_Making Deep Learning Go Brrrr From First Principles_](https://horace.io/brrr_intro.html) by Horace He for more ways on how to speed up machine learning models.

### Training curves (over/under-fitting)

![[overfitting_underfitting_curves.png]]
This is how your learning curves should look like.

#### Overfitting (solutions)
Since the main problem with overfitting is that your model is fitting the training data _too well_, you'll want to use techniques to "reign it in".
A common technique of preventing overfitting is known as [**regularization**](https://ml-cheatsheet.readthedocs.io/en/latest/regularization.html).
I like to think of this as "making our models more regular", as in, capable of fitting _more_ kinds of data.
Let's discuss a few methods to prevent overfitting.

| **Method to prevent overfitting** | **What is it?**                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Get more data**                 | Having more data gives the model more opportunities to learn patterns, patterns which may be more generalizable to new examples.                                                                                                                                                                                                                                                                      |
| **Simplify your model**           | If the current model is already overfitting the training data, it may be too complicated of a model. This means it's learning the patterns of the data too well and isn't able to generalize well to unseen data. One way to simplify a model is to reduce the number of layers it uses or to reduce the number of hidden units in each layer.                                                        |
| **Use data augmentation**         | [**Data augmentation**](https://developers.google.com/machine-learning/glossary#data-augmentation) manipulates the training data in a way so that's harder for the model to learn as it artificially adds more variety to the data. If a model is able to learn patterns in augmented data, the model may be able to generalize better to unseen data.                                                |
| **Use transfer learning**         | [**Transfer learning**](https://developers.google.com/machine-learning/glossary#transfer-learning) involves leveraging the patterns (also called pretrained weights) one model has learned to use as the foundation for your own task. In our case, we could use one computer vision model pretrained on a large variety of images and then tweak it slightly to be more specialized for food images. |
| **Use dropout layers**            | Dropout layers randomly remove connections between hidden layers in neural networks, effectively simplifying a model but also making the remaining connections better. See [`torch.nn.Dropout()`](https://pytorch.org/docs/stable/generated/torch.nn.Dropout.html) for more.                                                                                                                          |
| **Use learning rate decay**       | The idea here is to slowly decrease the learning rate as a model trains. This is akin to reaching for a coin at the back of a couch. The closer you get, the smaller your steps. The same with the learning rate, the closer you get to [**convergence**](https://developers.google.com/machine-learning/glossary#convergence), the smaller you'll want your weight updates to be.                    |
| **Use early stopping**            | [**Early stopping**](https://developers.google.com/machine-learning/glossary#early_stopping) stops model training _before_ it begins to overfit. As in, say the model's loss has stopped decreasing for the past 10 epochs (this number is arbitrary), you may want to stop the model training here and go with the model weights that had the lowest loss (10 epochs prior).                         |

#### How to deal with underfitting
When a model is [**underfitting**](https://developers.google.com/machine-learning/glossary#underfitting) it is considered to have poor predictive power on the training and test sets.
In essence, an underfitting model will fail to reduce the loss values to a desired level.
Right now, looking at our current loss curves, I'd considered our `TinyVGG` model, `model_0`, to be underfitting the data.
The main idea behind dealing with underfitting is to _increase_ your model's predictive power.
There are several ways to do this.

| **Method to prevent underfitting**      | **What is it?**                                                                                                                                                                                                                                                                  |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Add more layers/units to your model** | If your model is underfitting, it may not have enough capability to _learn_ the required patterns/weights/representations of the data to be predictive. One way to add more predictive power to your model is to increase the number of hidden layers/units within those layers. |
| **Tweak the learning rate**             | Perhaps your model's learning rate is too high to begin with. And it's trying to update its weights each epoch too much, in turn not learning anything. In this case, you might lower the learning rate and see what happens.                                                    |
| **Use transfer learning**               | Transfer learning is capable of preventing overfitting and underfitting. It involves using the patterns from a previously working model and adjusting them to your own problem.                                                                                                  |
| **Train for longer**                    | Sometimes a model just needs more time to learn representations of data. If you find in your smaller experiments your model isn't learning anything, perhaps leaving it train for a more epochs may result in better performance.                                                |
| **Use less regularization**             | Perhaps your model is underfitting because you're trying to prevent overfitting too much. Holding back on regularization techniques can help your model fit the data better.                                                                                                     |
|                                         |                                                                                                                                                                                                                                                                                  |

*Note: This section where he augments data to try to have better fitting is also interesting to read: https://www.learnpytorch.io/04_pytorch_custom_datasets/#9-model-1-tinyvgg-with-data-augmentation*
Same for this section on making the data (from outside the training) to fit inside the model: https://www.learnpytorch.io/04_pytorch_custom_datasets/#113-putting-custom-image-prediction-together-building-a-function