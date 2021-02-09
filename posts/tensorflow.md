# TENSORFLOW

- `tensorflow not found`：在每次 `import tf` 前加入[一段话](https://www.cnblogs.com/yiyezhouming/p/9497697.html)。
- **多卡**：参见[博客](https://blog.csdn.net/minstyrain/article/details/80986397)。

<details>
<summary><b>安装</b></summary>
<p>

首先，NVIDIA 和 CUDA 必须匹配，CUDA 和 TF 版本号也要匹配；关于 CUDA 和  TF 匹配版本参见[此处](https://tensorflow.google.cn/install/source?hl=en#linux)。

官方推荐 [CONDA + PIP 安装](https://www.tensorflow.org/install/pip?hl=zh-cn#conda)；即，新建 CONDA 环境，激活进入，然后 PIP 安装。

注意添加国内源，否则 PIP 也会很慢。

</p>
</details>

<details>
<summary><b><code>insufficient</code></b></summary>
<p>

- 要修改 CUDATOOLKIT 的版本号。例如 NVIDIA driver 是 410.xx，那么 CUDA 只能是 10.0，不能是 10.1。
- 很简单：`conda install cudatoolkit=10.0`，降级；参考[知乎](https://zhuanlan.zhihu.com/p/64376059)。

</p>
</details>
