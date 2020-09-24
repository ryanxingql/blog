# DEEP LEARNING

- [DEEP LEARNING](#deep-learning)
  - [Debug记录](#debug记录)
    - [CUDA](#cuda)
    - [网络结构](#网络结构)
    - [数据格式](#数据格式)
    - [DCNv2](#dcnv2)

## Debug记录

### CUDA

**`nvcc fatal`**

用`nvcc -V`查看，发现不是想要的10.1版本。

编辑变量：`vim ~/.bashrc`，加入以下内容：

```bash
export PATH="/usr/local/cuda-10.1/bin:$PATH"
export LD_LIBRARY_PATH="/usr/lcoal/cuda-10.1/lib64:$LD_LIBRARY_PATH"
```

`source ~/.bashrc`即可。

### 网络结构

- 注意最后一层不能激活。
- 网络不收敛：特别是深层网路，加一个residual可能就好了。

### 数据格式

- PSNR异常：检查数据格式和范围。例如，若数据类型为`np.uint8`，在计算`100-200=-100`时，会得到`+156`。因此计算前要先转换成`float`。

### DCNv2

**STDF作者的老版本**

1. 创建conda环境
   - `conda create -n dcnv2 python=3.7`
   - 注意指定python版本，否则默认3.8了。
2. 安装pt
   - `pip install torch==1.6.0+cu101 torchvision==0.7.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html`
   - DCNv2-pytorch编译需要torch。
   - 老老实实安装pt官网指令安装，不要偷懒用conda。
   - 推荐pip安装，更快。
   - CUDA版本是`nvcc --version`查看的；`nvidia smi`不准。
   - 如果速度慢，可以下载后离线安装：`pip install /path/to/whl`即可。
3. 编译时报错`gcc failed`，谷歌后得知是未兼容pt>=1.5。但大神给了[解决方案](https://github.com/open-mmlab/mmediting/issues/84)。
4. 按照STDF作者的README，`simple_check`通过。成功。

**BasicSR**

- 提示`not compiled with GPU support`：[[参考]](https://zhuanlan.zhihu.com/p/93278639)
- `nvcc --version`查看的是真实的CUDA版本，和`nvidia-smi`查看的不一致。根据教程，用`conda install pytorch torchvision cudatoolkit=10.1 -c pytorch`来安装。一定要指定`pytorch`频道，否则找不到，或者版本有问题。
- 如果提示nvidia driver太老，安装支持当前CUDA的最新driver即可，不要动CUDA。CUDA 10.2貌似不兼容DCN。
