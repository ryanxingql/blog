# PyTorch

多看手册，少参考博客和书籍。

## `view`, `reshape`, `contiguous`, `clone()` and `detach()`

[[手册]](https://pytorch.org/docs/master/tensor_view.html#tensor-view-doc)

- `view` 会生成一个形状不同、底层数据共享（危险）的 tensor。这么做也是为了节约 copy 的成本。
- `view` 可能使得一个 contiguous 的 tensor 变成 non-coutiguous。
- 还有许多操作基于 `view`，例如 `transpose`、`squeeze`、`expand`。因此也具有上述特性。
- 如果一个数据本身是 contiguous 的，那么 `contiguous` 返回其自身；否则，会返回一个新的 tensor。
- `reshape`，`reshape_as()`，`flatten` 既有可能是 `view`，也有可能是新 tensor；条件比较复杂，不要冒险，应主动规避风险。
- 如果深拷贝一个 `requires_grad=False` 的 tensor，`t.clone()` 即可；否则，需要 `t.detach().clone()`。

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

## 维度

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
