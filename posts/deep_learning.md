# DEEP LEARNING

- [DEEP LEARNING](#deep-learning)
  - [Debug记录](#debug记录)
    - [CUDA版本不对](#cuda版本不对)
    - [网络不收敛](#网络不收敛)
    - [数值计算结果怪异](#数值计算结果怪异)
    - [DCNv2编译不通过](#dcnv2编译不通过)
  - [ToyExperiment](#toyexperiment)
    - [SyncBatchNorm](#syncbatchnorm)

## Debug记录

### CUDA版本不对

表现1：

提示`nvcc fatal`。

解决：

首先用`nvcc -V`查看，发现不是想要的10.1版本。注意，这和`nvidia-smi`查看的可能不一致，前者才是真实的。

编辑变量：`vim ~/.bashrc`，加入以下内容：

```bash
export PATH="/usr/local/cuda-10.1/bin:$PATH"
export LD_LIBRARY_PATH="/usr/lcoal/cuda-10.1/lib64:$LD_LIBRARY_PATH"
```

`source ~/.bashrc`即可。

表现2：

提示`not compiled with GPU support`。

解决：

[[参考]](https://zhuanlan.zhihu.com/p/93278639)

用`conda install pytorch torchvision cudatoolkit=10.1 -c pytorch`来安装。一定要指定`pytorch`频道，否则找不到，或者版本有问题。

（强烈推荐）或者用PT官网提供的pip安装指令安装。注意指定cuda版本号。例如：`pip install torch==1.6.0+cu101 torchvision==0.7.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html`

如果提示nvidia driver太老，安装支持当前CUDA的最新driver即可，不要轻易动CUDA。

### 网络不收敛

表现：

损失值一直非常大。

解决：

- 最后一层不加激活函数。
- 对于深层网路，residual很重要。

### 数值计算结果怪异

表现：

自己写的PSNR计算函数，输入两幅图像后PSNR计算结果异常。

解决：

输入图像数据类型为`np.uint8`。自写程序未将数据类型转换为float，而是直接进行了计算。

例如，在计算`100-200=-100`时，会得到`+156`，显然是不对的。

### DCNv2编译不通过

表现：

不兼容高版本pytorch。

解决：

[[大神的解决方案]](https://github.com/open-mmlab/mmediting/issues/84)

## ToyExperiment

### SyncBatchNorm

环境：

- Ubuntu 20.04
- CUDA 10.1
- PyTorch 1.16

背景：

BN是在每一层CNN处理前对数据的白化处理。BN首先对数据归一化至零均值、1方差，然后进行仿射变换（参数是可学的，保证网络的学习能力不因暴力白化受损）。

BN2D是在每一个C上单独操作的（有多少C，就有多少套仿射变换参数），即归一化用的均值和方差是从`(B H W)`上获取的。

在早期的实现中，BN并未考虑多卡并行问题。即，每张卡上的BN参数是不同的，且统计量也是根据当前卡上的mini-batch统计得到。当bs较大时，这没什么问题。

实验：

```python3
import torch.nn as nn
import torch


class ToyModel(nn.Module):
    def __init__(self):
        super().__init__()
        # BN is applied on each channel separately
        self.bn = nn.BatchNorm2d(num_features=2)

    def forward(self, x):
        return self.bn(x)

toy_model = ToyModel()

loss_fn = nn.MSELoss()
optimizer = torch.optim.Adam(toy_model.parameters(), lr=1e-3)


for i in range(1000):
    toy_model.train()
    input = torch.randn(2, 2, 2, 2)
    raw = input / 2.
    output = toy_model(input)  # BN is applied on this (B C H W) tensor

    print(input)
    print(output * toy_model.bn.running_mean + toy_model.bn.running_var)

    loss = loss_fn(output, raw)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    toy_model.eval()
    with torch.no_grad():
        print(torch.mean(input[:,0,...]), torch.std(input[:,0,...]))
        print(torch.mean(output[:,0,...]), torch.std(output[:,0,...]))
        for name, param in toy_model.named_parameters():
            if param.requires_grad:
                print(name, param.data[0])

    print(f'> {i}: {loss.item()}\n')
```

未完成。
