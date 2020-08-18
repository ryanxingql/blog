# CONDA AND PIP

- [CONDA AND PIP](#conda-and-pip)
  - [Conda](#conda)
    - [安装Anaconda](#安装anaconda)
    - [环境操作](#环境操作)
    - [包操作](#包操作)
    - [频道操作](#频道操作)
    - [问题解决](#问题解决)
  - [Pip](#pip)
    - [添加国内源](#添加国内源)
    - [离线安装](#离线安装)
    - [问题解决](#问题解决-1)
      - [timeout](#timeout)

## Conda

### 安装Anaconda

- 查看最新链接：[[官网]](https://repo.anaconda.com/archive/)
- `wget`下载。
- 安装：空格跳过协议，一切回车默认。
- 若刚刚没选yes激活，手动激活：`conda init bash`，重启terminal。
- 添加国内源：
  
  ```bash
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
  ```

### 环境操作

```bash
conda create -n env_name python=3.6  # 最基本操作
conda create -n venv pip python=3.7  # 同时装好两个包
conda env list
conda env remove -n env_name
```

注意！！！！最好指定python，否则默认可能装成python2，后面的安装都是有问题的。

### 包操作

```bash
conda install pkg_name -y  # 默认yes。注意要先进入环境
```

离线下载和安装

- 在[[官网]](https://anaconda.org/anaconda/repo)搜包。
- 下载。
- 安装：`conda install --use-local path/to/xxx.tar.bz2`

### 频道操作

查看现有频道（包括其他设置）：`conda config --show`

用vim修改：`vim ~/.condarc`

### 问题解决

- 一直在solving：删除除`defaults`外所有channels。
- 超时：删除`defaults`，并把`https`都改为`http`。
- `CondaVerificationError`：`conda clean --all`

## Pip

### 添加国内源

并设为默认：

```bash
pip install pip -U
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

### 离线安装

- 先试试直接`pip install`，记住名称和大小。
- 在`PyPI`搜索对应版本。
- 下载，直接`pip install /path/to/pkg.whl`

### 问题解决

#### timeout

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