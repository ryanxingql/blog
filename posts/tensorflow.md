# TensorFlow

## 目录

- [TensorFlow](#tensorflow)
  - [目录](#目录)
  - [安装](#安装)
  - [使用](#使用)
    - [多卡](#多卡)
  - [调试](#调试)
    - [`tensorflow not found`](#tensorflow-not-found)
    - [insufficient](#insufficient)

## 安装

首先，NVIDIA 和 CUDA 必须匹配，CUDA 和 TF 版本号也要匹配；关于 CUDA 和  TF 匹配版本参见[此处](https://tensorflow.google.cn/install/source?hl=en#linux)。

官方推荐 [Conda + pip 安装](https://www.tensorflow.org/install/pip?hl=zh-cn#conda)；即，新建 Conda 环境，激活进入，然后 pip 安装。

注意添加国内源，否则 pip 也会很慢。

## 使用

### 多卡

参见[博客](https://blog.csdn.net/minstyrain/article/details/80986397)。

## 调试

### `tensorflow not found`

在每次 `import tf` 前加入[一段话](https://www.cnblogs.com/yiyezhouming/p/9497697.html)。

### insufficient

- 要修改 CUDA Toolkit 的版本号。例如 NVIDIA driver 是 410.x，那么 CUDA 只能是 10.0，不能是 10.1。
- 很简单：`conda install cudatoolkit=10.0`，降级；参考[知乎](https://zhuanlan.zhihu.com/p/64376059)。
