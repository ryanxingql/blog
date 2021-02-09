# DEEP LEARNING

<details>
<summary><b><code>nvcc fatal</code></b></summary>
<p>

首先用 `nvcc -V` 查看，发现不是想要的 10.1 版本。注意，这和 `nvidia-smi` 查看的可能不一致，前者才是真实的。

编辑变量：`vim ~/.bashrc` ，加入以下内容：

```bash
export PATH="/usr/local/cuda-10.1/bin:$PATH"
export LD_LIBRARY_PATH="/usr/lcoal/cuda-10.1/lib64:$LD_LIBRARY_PATH"
```

最后 `source ~/.bashrc` 即可。

</p>
</details>

<details>
<summary><b><code>not compiled with GPU support</code></b></summary>
<p>

可以用 PT 官网提供的 PIP 安装指令安装。注意指定 CUDA 版本号。例如：

```bash
pip install torch==1.6.0+cu101 torchvision==0.7.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html
```

或用 `conda install pytorch torchvision cudatoolkit=10.1 -c pytorch` 来安装。

如果提示 NVIDIA driver 太老，安装支持当前 CUDA 的最新 driver 即可（参见 NVIDIA 博文），不要轻易动 CUDA。

参考[知乎](https://zhuanlan.zhihu.com/p/93278639)。

</p>
</details>

<details>
<summary><b>损失值一直非常大</b></summary>
<p>

- 最后一层不加激活函数。
- 对于深层网路，residual 很重要。

</p>
</details>

<details>
<summary><b>PSNR 等函数计算结果怪异</b></summary>
<p>

输入图像数据类型为 `np.uint8`。自写程序未将数据类型转换为 FLOAT，而是直接进行了计算。

例如，在计算 $100-200=-100$ 时，会得到 `+156`，显然是不对的。

</p>
</details>

<details>
<summary><b>DCNv2 编译不通过</b></summary>
<p>

不兼容高版本 PT。解决方法参见 [issue](https://github.com/open-mmlab/mmediting/issues/84)。

</p>
</details>
