# PYTORCH

- [PYTORCH](#pytorch)
  - [安装](#安装)
  - [多卡](#多卡)

## 安装

> 比TensorFlow简单太多了。

- 首先要考虑CUDA和NVIDIA的支持，确定版本。cudnn无需操心。
- 然后用`conda`安装（不推荐）：

  ```bash
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
  condo create -n pt python=3.6
  conda activate pt
  conda install albumentations
  ```
- 推荐严格按照[官网](https://pytorch.org/get-started/locally/)要求，并用pip安装：
  
  ```bash
  pip install torch==1.6.0+cu101 torchvision==0.7.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html
  ```

## 多卡

[[教程]](https://zhuanlan.zhihu.com/p/76638962)




