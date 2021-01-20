# CONDA AND PIP

- [CONDA AND PIP](#conda-and-pip)
  - [CONDA](#conda)
    - [安装ANACONDA](#安装anaconda)
    - [环境](#环境)
    - [包](#包)
    - [频道](#频道)
    - [DEBUG](#debug)
  - [PIP](#pip)

## CONDA

不推荐用来安装包（下载速度慢，版本可能旧），仅推荐用来管理虚拟环境。

### 安装ANACONDA

<details>
<summary><b>展开详情</b></summary>

> 查看最新链接

[[官网]](https://repo.anaconda.com/archive/)

可在服务器`wget`下载。

> 安装

- 空格跳过协议，一切回车默认。
- 若刚刚没选yes激活，手动激活：`conda init bash`，重启terminal。

建议添加国内源。见后。

</details>

### 环境

<details>
<summary><b>创建环境</b></summary>

```bash
conda create -n env_name python=3.6  # 最基本操作
conda create -n venv pip python=3.7  # 可同时装好多个包
```

注意！！！！最好指定python，否则默认可能装成python2，后面的安装都是有问题的。

</details>

<details>
<summary><b>查看已有环境</b></summary>

```bash
conda env list
```

</details>

<details>
<summary><b>删除包</b></summary>

```bash
conda env remove -n env_name
```

</details>

### 包

<details>
<summary><b>查看已有包</b></summary>

```bash
conda list
```

</details>

<details>
<summary><b>安装包</b></summary>

```bash
conda install pkg_name -y  # 默认yes。注意要先进入环境
```

</details>

<details>
<summary><b>离线下载和安装</b></summary>

- 在[[官网]](https://anaconda.org/anaconda/repo)搜包。
- 下载。
- 安装：`conda install --use-local path/to/xxx.tar.bz2`

</details>

### 频道

<details>
<summary><b>添加国内源</b></summary>

```bash
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
```

</details>

<details>
<summary><b>查看现有频道（包括其他设置）</b></summary>

```bash
conda config --show
```

</details>

<details>
<summary><b>修改可用频道</b></summary>

```bash
vim ~/.condarc
```

</details>

### DEBUG

<details>
<summary><b>包安装路径错误</b></summary>

记得`python -m xxx`

</details>

<details>
<summary><b>一直在solving</b></summary>

删除除`defaults`外所有channels。

</details>

<details>
<summary><b>超时</b></summary>

- 重新登陆校园网。
- 删除`defaults`，并把`https`都改为`http`。

</details>

<details>
<summary><b>CondaVerificationError</b></summary>

```bash
conda clean --all
```

</details>

## PIP

强烈推荐用PIP下载包，添加国内源后速度快。

<details>
<summary><b>添加国内源</b></summary>

[[参考]](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)

（并设为默认）

```bash
pip install pip -U
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

</details>

<details>
<summary><b>离线安装包</b></summary>

- 先试试直接`pip install`，记住名称和大小。
- 在`PyPI`搜索对应版本。
- 下载，直接`pip install /path/to/pkg.whl`

</details>

<details>
<summary><b>timeout error</b></summary>

```bash
pip install --default-timeout=100 xxx -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/
```

另：创建或修改`~/.pip/pip.conf`，内容如下：

```txt
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host=mirrors.aliyun.com
```

</details>
