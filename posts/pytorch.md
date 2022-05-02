# PyTorch

## 目录

- [PyTorch](#pytorch)
  - [目录](#目录)
  - [安装](#安装)
  - [view 方法 vs. reshape 方法](#view-方法-vs-reshape-方法)
  - [理解维度](#理解维度)
  - [多卡](#多卡)
  - [Dataloader](#dataloader)
    - [Pre-fetcher](#pre-fetcher)
  - [Reproducibility](#reproducibility)
    - [如何控制](#如何控制)
      - [种子](#种子)
      - [cuDNN](#cudnn)
      - [PyTorch 随机算法](#pytorch-随机算法)
      - [CUDA 算子](#cuda-算子)
      - [CUDA RNN 和 LSTM](#cuda-rnn-和-lstm)
      - [Dataloader](#dataloader-1)

## 安装

首先安装 CUDA。根据 CUDA 教程，安装好系统推荐的 NVIDIA 驱动时，CUDA 就自动安装好了。注意，`nvidia-smi` 不准确，`nvcc -V` 才是准确的 CUDA 版本。

确定所需 PT 版本。在官网查看兼容的 CUDA 版本。若不满足，可重装 CUDA 及对应的最高版本 NVIDIA 驱动。

按照[官网](https://pytorch.org/get-started/locally/)提供的完整指令，用 pip 安装，可以指定 CUDA 版本。例：

```bash
pip install torch==1.6.0+cu101 torchvision==0.7.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html
```

或用 Conda 安装（不推荐）：

```bash
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
condo create -n pt python=3.7
conda activate pt
```

## [view 方法 vs. reshape 方法](https://pytorch.org/docs/master/tensor_view.html#tensor-view-doc)

- `view` 会生成一个形状不同、底层数据共享（危险）的 tensor。这么做也是为了节约 copy 的成本。
- `view` 可能使得一个 contiguous 的 tensor 变成 non-coutiguous。
- 还有许多操作基于 `view`，例如 `transpose`、`squeeze`、`expand`。因此也具有上述特性。
- 如果一个数据本身是 contiguous 的，那么 `contiguous` 返回其自身；否则，会返回一个新的 tensor。
- `reshape`，`reshape_as()`，`flatten` 既有可能是 `view`，也有可能是新 tensor；条件比较复杂，不要冒险，应主动规避风险。
- 如果深拷贝一个 `requires_grad=False` 的 tensor，`t.clone()` 即可；否则，需要 `t.detach().clone()`。

## 理解维度

以 `torch.mean(input, dim, keepdim=False)` 函数为例。

```python
>>> a = torch.randn(4, 4)
>>> a
tensor([[-0.3841,  0.6320,  0.4254, -0.7384],
        [-0.9644,  1.0131, -0.6549, -1.4279],
        [-0.2951, -1.3350, -0.7694,  0.5600],
        [ 1.0842, -0.9580,  0.3623,  0.2343]])

>>> torch.mean(a, 1)
tensor([-0.0163, -0.5085, -0.4599,  0.1807])

>>> torch.mean(a, 1, True)
tensor([[-0.0163],
        [-0.5085],
        [-0.4599],
        [ 0.1807]])
```

例中 `dim=1`，字面意思是沿着 `dim=1` 维度操作 `mean`，即让该维度消失或为 1（由 `keepdim` 决定）。

为了达到这一目的，就需要获取所有 `(h=0, w=*)` 取平均，再获取所有 `(h=1, w=*)` 取平均，依此类推。这样，`h` 维度就不会改变，而 `w` 维度会消失。

在二维矩阵中，效果为横向取平均；在三维矩阵中，效果为在每个 `c` 中横向取平均。

再以 `torch.nn.functional.normalize(input, p=2, dim=1, eps=1e-12, out=None)` 为例。如果输入张量为 `(b c h w)`，那么 `(b=0 c=* h=0 w=0)` 的所有元素内部执行正则化，`(b=0 c=* h=0 w=1)` 的所有元素内部执行正则化，依此类推。

## 多卡

- [官方分布式文档](https://pytorch.org/docs/stable/distributed.html)
- [官方 DDP 教程](https://pytorch.org/tutorials/intermediate/ddp_tutorial.html)
- [知乎](https://zhuanlan.zhihu.com/p/178402798)
- [知乎](https://zhuanlan.zhihu.com/p/76638962)

## Dataloader

### Pre-fetcher

根据[讨论](https://discuss.pytorch.org/t/how-to-prefetch-data-when-processing-with-gpu/548/45)，当 worker 数目大于 0 时，不需要 prefetch；因为默认的机制是，会有多个 dataloder 副本。

根据[讨论](https://discuss.pytorch.org/t/how-to-prefetch-data-when-processing-with-gpu/548/19)，当 CPU 空闲时，不建议使用 CUDA。

## [Reproducibility](https://pytorch.org/docs/stable/notes/randomness.html)

由于系统、平台、软件版本等不同，PyTorch 无法保证每一次运算结果都相同。即便是随机种子一致，也不一定。

我们可以控制随机源，从而保证 PyTorch 的可复现性。注意，这样做会影响模型速度。

### 如何控制

#### 种子

控制 PyTorch RNG（random number generator）的种子：

```python
import torch
torch.manual_seed(0)
```

程序中一些自定义的算子，需要自己去设置种子。如：

```python
import random
import numpy as np
random.seed(0)
np.random.seed(0)  # c1
```

`np.random.seed(0)` 控制的是 global NumPy RNG。有一些应用也用到了 NumPy RNG，但不受该全局发生器控制，需要单独设置种子。

#### cuDNN

CUDA 卷积算子会用到 cuDNN 库。当使用一组新的 size 参数调用 cuDNN 卷积时，cuDNN 会先跑一个 benchmark，找出最快的卷积算法，然后使用它。测试速度和平台、噪声都有关系，由此导致了随机性。

关闭 benchmark：

```python
import torch
torch.backends.cudnn.benchmark = False
```

该操作会让 cuDNN 选择固定一种算法，因此速度一般会变慢。

这还不够，这种固定的算法可能是一个随机算法。我们还需要额外指定使用确定性算法，看下一节。

#### PyTorch 随机算法

让 PyTorch 使用确定性算法（如果有），代替已知的随机算法：

```python
import torch
torch.use_deterministic_algorithms(True)
```

如果使用了没有确定性算法的随机算法，会报错。

上一节提到，我们让 cuDNN 固定选择了一种算法。但该算法可能是随机算法。因此我们要指定使用确定性算法。指定方式有两种，一种是上面的指令，另一种是：

```python
import torch
torch.backends.cudnn.deterministic = True
```

我个人理解后一种算法覆盖范围更小。

#### [CUDA 算子](https://docs.nvidia.com/cuda/cublas/index.html#cublasApi_reproducibility)

CUDA 提供的 CUBLAS 库的不同版本的运算结果可能不同。

#### CUDA RNN 和 LSTM

一些 CUDA 版本上，RNN 和 LSTM 表现随机。需要进一步看 `torch.nn.RNN()` 和 `torch.nn.LSTM()`。

#### Dataloader

默认情况下，多进程的 dataloader 会给每个进程分配种子。我们可以指定分配方式，即指定 `worker_init_fn` 函数：

```python
def seed_worker(worker_id):
    worker_seed = torch.initial_seed() % 2**32
    numpy.random.seed(worker_seed)
    random.seed(worker_seed)

g = torch.Generator()
g.manual_seed(0)

DataLoader(
    train_dataset,
    batch_size=batch_size,
    num_workers=num_workers,
    worker_init_fn=seed_worker,
    generator=g,
)
```
