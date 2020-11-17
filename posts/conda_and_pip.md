# CONDA AND PIP

- [CONDA AND PIP](#conda-and-pip)
  - [Conda](#conda)
    - [安装Anaconda](#安装anaconda)
    - [环境](#环境)
    - [包](#包)
    - [频道](#频道)
    - [DEBUG记录](#debug记录)
  - [Pip](#pip)
    - [频道](#频道-1)
    - [包](#包-1)
    - [DEBUG记录](#debug记录-1)

## Conda

不推荐用来安装包（下载速度慢，版本可能旧），仅推荐用来管理虚拟环境。

### 安装Anaconda

$\clubsuit$ 查看最新链接：

[[官网]](https://repo.anaconda.com/archive/)

可在服务器`wget`下载。

$\clubsuit$ 安装：

- 空格跳过协议，一切回车默认。
- 若刚刚没选yes激活，手动激活：`conda init bash`，重启terminal。

建议添加国内源。

### 环境

$\clubsuit$ 创建环境：

```bash
conda create -n env_name python=3.6  # 最基本操作
conda create -n venv pip python=3.7  # 可同时装好多个包
```

$\clubsuit$ 查看已有环境：

```bash
conda env list
```

$\clubsuit$ 删除包：

```bash
conda env remove -n env_name
```

注意！！！！最好指定python，否则默认可能装成python2，后面的安装都是有问题的。

### 包

$\clubsuit$ 查看已有包：

```bash
conda list
```

$\clubsuit$ 安装包：

```bash
conda install pkg_name -y  # 默认yes。注意要先进入环境
```

$\clubsuit$ 离线下载和安装：

- 在[[官网]](https://anaconda.org/anaconda/repo)搜包。
- 下载。
- 安装：`conda install --use-local path/to/xxx.tar.bz2`

### 频道

$\clubsuit$ 添加国内源：

```bash
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
```

$\clubsuit$ 查看现有频道（包括其他设置）：

```bash
conda config --show
```

$\clubsuit$ 修改可用频道：

```bash
vim ~/.condarc
```

### DEBUG记录

$\clubsuit$ 包安装路径错误：

记得`python -m xxx`

$\clubsuit$ 一直在solving：

删除除`defaults`外所有channels。

$\clubsuit$ 超时：

- 重新登陆校园网。
- 删除`defaults`，并把`https`都改为`http`。

$\clubsuit$ `CondaVerificationError`

```bash
conda clean --all
```

## Pip

强烈推荐用以下载包，添加国内源后速度快。

### 频道

$\clubsuit$ 添加国内源：

[[参考]](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)

（并设为默认）

```bash
pip install pip -U
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

### 包

$\clubsuit$ 离线安装：

- 先试试直接`pip install`，记住名称和大小。
- 在`PyPI`搜索对应版本。
- 下载，直接`pip install /path/to/pkg.whl`

### DEBUG记录

$\clubsuit$ timeout：

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
