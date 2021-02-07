# CONDA AND PIP

- [CONDA AND PIP](#conda-and-pip)
  - [PIP](#pip)
    - [常规](#常规)
    - [调试](#调试)
  - [CONDA](#conda)
    - [常规](#常规-1)
    - [调试](#调试-1)

强烈推荐用 PIP 下载包，用 CONDA 管理虚拟环境。

## PIP

### 常规

<details>
<summary><b>添加国内源</b></summary>

```bash
pip install pip -U
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

[【TUNA】](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)

</details>

<details>
<summary><b>离线安装包</b></summary>

- 先试试直接 `pip install`，记住名称和大小。
- 在 PYPI 搜索对应版本，下载。
- `pip install /path/to/pkg.whl`

</details>

### 调试

<details>
<summary><b>timeout</b></summary>

```bash
pip install --default-timeout=100 xxx -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/
```

另：创建或修改 `~/.pip/pip.conf`，内容如下：

```txt
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host=mirrors.aliyun.com
```

</details>

<details>
<summary><b>包安装路径错误；已安装的包找不到</b></summary>

```bash
python -m conda install
```

</details>

## CONDA

### 常规

<details>
<summary><b>安装 ANACONDA</b></summary>

- 在[官网](https://repo.anaconda.com/archive/)查看最新链接。
- 可在服务器 `wget` 下载。
- 安装，空格跳过协议，一切回车默认。
- 若没选yes激活，手动激活：`conda init bash`，重启 terminal。

建议立即添加国内源，见后。

</details>

<details>
<summary><b>创建环境</b></summary>

```bash
conda create -n env_name python=3.7  # 最基本操作
conda create -n env_name pip python=3.7  # 可同时装好多个包
```

不要安装 PYTHON 3.6，很可能遇到各种奇怪的问题。

</details>

<details>
<summary><b>查看已有环境</b></summary>

```bash
conda env list
```

</details>

<details>
<summary><b>删除环境</b></summary>

```bash
conda env remove -n env_name
```

</details>

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
<summary><b>离线安装包</b></summary>

- 在[官网](https://anaconda.org/anaconda/repo)搜包。
- 下载。
- `conda install --use-local path/to/xxx.tar.bz2`

</details>

<details>
<summary><b>删除包</b></summary>

```bash
conda remove pkg_name
```

</details>

<details>
<summary><b>添加国内源</b></summary>

```bash
vim ~/.condarc
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

### 调试

<details>
<summary><b>包安装路径错误；已安装的包找不到</b></summary>

```bash
python -m conda install
```

</details>

<details>
<summary><b>一直在 solving</b></summary>

删除除 `defaults` 外所有 channels。

</details>

<details>
<summary><b>timeout</b></summary>

- 通常重试即可。
- 重新登陆校园网。
- 添加国内源。
- 删除 `defaults`，并把 `https` 都改为 `http`。

</details>

<details>
<summary><b>CondaVerificationError</b></summary>

```bash
conda clean --all
```

</details>

<details>
<summary><b>不识别 ASCII 码</b></summary>

把 PYTHON 升级至 3.7；不要用 3.6。

</details>
