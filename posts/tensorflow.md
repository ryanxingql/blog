# TENSORFLOW

- [TENSORFLOW](#tensorflow)

<details>
<summary><b>安装</b></summary>

- 首先，NVIDIA和CUDA必须匹配，CUDA和TF版本号也要匹配。

查看CUDA和TF匹配要求：[[ref]](https://tensorflow.google.cn/install/source?hl=en#linux)

- 官方推荐CONDA+PIP安装：[[ref]](https://www.tensorflow.org/install/pip?hl=zh-cn#conda)

即，新建CONDA环境，激活进入，然后PIP安装。

- 注意添加国内源，否则PIP也会很慢：`pip install tensorflow==1.2.0 --ignore-installed -i https://mirrors.aliyun.com/pypi/simple/`

</details>

<details>
<summary><b>提示：tensorflow not found</b></summary>

在每次`import tf`前加入一段话：[[ref]](https://www.cnblogs.com/yiyezhouming/p/9497697.html)

</details>

<details>
<summary><b>提示：insufficient</b></summary>

- 要修改CUDATOOLKIT的版本号。例如NVIDIA driver是410.xx，那么CUDA只能是10.0，不能是10.1。
- 很简单：`conda install cudatoolkit=10.0`，降级。[[ref]](https://zhuanlan.zhihu.com/p/64376059)

</details>

<details>
<summary><b>多卡</b></summary>

[[ref]](https://blog.csdn.net/minstyrain/article/details/80986397)

</details>
