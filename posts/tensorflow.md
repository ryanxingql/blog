# TENSORFLOW

- [TENSORFLOW](#tensorflow)
  - [安装](#安装)
  - [问题解决](#问题解决)
  - [多卡](#多卡)

## 安装

特别麻烦，可能会出现各种问题。

首先，NVIDIA和CUDA必须匹配，CUDA和tf版本号也要匹配。

查看CUDA和tf匹配要求：[[ref]](https://tensorflow.google.cn/install/source?hl=en#linux)

官方推荐conda+pip安装：[[ref]](https://www.tensorflow.org/install/pip?hl=zh-cn#conda)

即，新建conda环境，激活进入，然后pip安装。

注意添加国内源，否则pip也会很慢：`pip install tensorflow==1.2.0 --ignore-installed -i https://mirrors.aliyun.com/pypi/simple/`

## 问题解决

> tensorflow not found

在每次`import tf`前加入一段话：[[ref]](https://www.cnblogs.com/yiyezhouming/p/9497697.html)

> 提示insufficient

- 要修改cudatoolkit的版本号。例如NVIDIA driver是410.xx，那么cuda只能是10.0，不能是10.1。
- 很简单：`conda install cudatoolkit=10.0`，降级。[[ref]](https://zhuanlan.zhihu.com/p/64376059)

## 多卡

[[ref]](https://blog.csdn.net/minstyrain/article/details/80986397)
