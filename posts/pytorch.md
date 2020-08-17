# PYTORCH

- [PYTORCH](#pytorch)
  - [安装](#安装)

## 安装

> 比TensorFlow简单太多了。

- 首先要考虑CUDA和NVIDIA的支持，确定版本。cudnn无需操心。
- 然后用`conda`安装：

  ```bash
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
  condo create -n pt python=3.6
  conda activate pt
  conda install albumentations
  ```
