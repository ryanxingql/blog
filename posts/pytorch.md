# PYTORCH

- [PYTORCH](#pytorch)
  - [安装](#安装)
  - [多卡](#多卡)
    - [DDP例程](#ddp例程)
    - [原理](#原理)

## 安装

- 根据CUDA教程，安装好系统推荐的NVIDIA驱动时，CUDA就自动安装好了。注意，`nvidia-smi`不准确，`nvcc -V`才是准确的CUDA版本。
- 确定所需PT版本。在官网查看兼容的CUDA版本。若不满足，可重装CUDA及对应的最高版本NVIDIA驱动。
- 按照[官网](https://pytorch.org/get-started/locally/)提供的完整指令，用pip安装。例：
  
  ```bash
  pip install torch==1.6.0+cu101 torchvision==0.7.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html
  ```

  可以指定CUDA版本，推荐。
- 或用CONDA安装（不推荐）：

  ```bash
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
  condo create -n pt python=3.7
  conda activate pt
  ```

## 多卡

### DDP例程

```python3
import torch
import torch.distributed as dist
import torch.multiprocessing as mp
import torch.nn as nn
import torch.optim as optim
from torch.nn.parallel import DistributedDataParallel as DDP


def example(rank, world_size):
    #####
    # 1. 在所有DDP操作前，首先创建default process group
    #####
    dist.init_process_group("gloo", rank=rank, world_size=world_size)
    
    # example local model
    model = nn.Linear(10, 10).to(rank)
    
    #####
    # 2. 输入model，建立DDP model
    # 将rank=0进程上的`state_dict()`广播到其他进程
    # 每个进程都会创建一个local reducer，用以梯度同步
    #####
    ddp_model = DDP(model, device_ids=[rank])
    
    # define loss function and optimizer
    loss_fn = nn.MSELoss()
    optimizer = optim.SGD(ddp_model.parameters(), lr=0.001)

    # forward pass
    outputs = ddp_model(torch.randn(20, 10).to(rank))
    labels = torch.randn(20, 10).to(rank)

    # backward pass
    # 梯度会经过reducer，最后经过allreduce操作得到平均，然后传递给每个进程的所有参数
    loss_fn(outputs, labels).backward()
    
    # update parameters
    # 每个local model各自执行，执行完仍然是相同的
    optimizer.step()

def main():
    # 假设只要两个进程并行
    world_size = 2
    # 开跑
    mp.spawn(example,
        args=(world_size,),
        nprocs=world_size,
        join=True)

if __name__=="__main__":
    main()
```

### 原理

有时，单卡显存不足，我们需要多卡才能跑得动；有时，虽然单卡显存足够，但单卡利用率饱和，多卡可以提高运算速度。

[[知乎教程]](https://zhuanlan.zhihu.com/p/76638962)
[[官方教程]](https://pytorch.org/tutorials/intermediate/ddp_tutorial.html)

有以下几种方式：
1. DataParallel：适用于单机多卡。每次forward都要复制模型，受限于GIL竞争。代码改动最少，效率低。
2. DistributedDataParallel：适用于单机多卡和多机多卡。额外需要`init_process_group`操作。多进程并行，不受GIL影响。在DDP建立时单次广播模型，无须每次forward广播。推荐。
3. 其他，例如model parallel：[[教程]](https://pytorch.org/tutorials/intermediate/model_parallel_tutorial.html)

`torch.distributed`主要有3个组件，见[文档](https://pytorch.org/docs/master/notes/ddp.html)。我们主要用`Distributed Data-Parallel Training (DDP)`。

DDP原理：模型在DDP建立之初分发到各进程。每个进程输入各自的数据进行forward。backward后，计算梯度，分发至各进程。各进程分别进行相同的参数更新，从而保证各模型一致性。

注意：不同进程之间不可共享GPU。即一块卡只能用于一个进程。

