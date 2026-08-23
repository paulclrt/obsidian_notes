Experiment tracking is bascially just making your workspace organized. Because training models is nice but when you train 15 different models similar but different and need to save them, compare them and chose the ultimate one. This is a bigmess.

## Different ways to track machine learning experiments

There are as many different ways to track machine learning experiments as there are experiments to run.

|**Method**|**Setup**|**Pros**|**Cons**|**Cost**|
|---|---|---|---|---|
|Python dictionaries, CSV files, print outs|None|Easy to setup, runs in pure Python|Hard to keep track of large numbers of experiments|Free|
|[TensorBoard](https://www.tensorflow.org/tensorboard/get_started)|Minimal, install [`tensorboard`](https://pypi.org/project/tensorboard/)|Extensions built into PyTorch, widely recognized and used, easily scales.|User-experience not as nice as other options.|Free|
|[Weights & Biases Experiment Tracking](https://wandb.ai/site/experiment-tracking)|Minimal, install [`wandb`](https://docs.wandb.ai/quickstart), make an account|Incredible user experience, make experiments public, tracks almost anything.|Requires external resource outside of PyTorch.|Free for personal use|
|[MLFlow](https://mlflow.org/)|Minimal, install `mlflow` and start tracking|Fully open-source MLOps lifecycle management, many integrations.|Little bit harder to setup a remote tracking server than other services.|Free|
![[experiment_tracking.png]]

SummaryWriter from pytorch is very nice: https://docs.pytorch.org/docs/2.13/tensorboard.html
Tensorboard is a nice visuaisation but it seems to be only availble from notebooks. IDK


The `SummaryWriter()` class logs various information to a directory specified by the `log_dir` parameter.
How about we make a helper function to create a custom directory per experiment?
In essence, each experiment gets its own logs directory.


Every hyperparameter stands as a starting point for a different experiment:
- Change the number of **epochs**.
- Change the number of **layers/hidden units**.
- Change the amount of **data**.
- Change the **learning rate**.
- Try different kinds of **data augmentation**.
- Choose a different **model architecture**.

Your first batch of experiments should take no longer than a few seconds to a few minutes to run.
The quicker you can experiment, the faster you can work out what _doesn't_ work, in turn, the faster you can work out what _does_ work.

*Code available here*: [[7.0main.py]]
> Checkout the code line 85-110 to see how to train multiple models on multiple dataset to experiment

This is the output you could have from the code
![[tensor_board_screenshot_exemple.png]]
With all the data in one place, you could easily compare the model adnd choose the best one (the one suiting your needs and constraints the most)