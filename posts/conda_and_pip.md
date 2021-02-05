# CONDA AND PIP

- [CONDA AND PIP](#conda-and-pip)

强烈推荐用PIP下载包，用CONDA管理虚拟环境。

<details>
<summary><b>PIP添加国内源</b></summary>

[[参考]](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)

（并设为默认）

```bash
pip install pip -U
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

</details>

<details>
<summary><b>PIP离线安装包</b></summary>

- 先试试直接`pip install`，记住名称和大小。
- 在`PyPI`搜索对应版本。
- 下载，直接`pip install /path/to/pkg.whl`

</details>

<details>
<summary><b>PIP timeout error</b></summary>

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

<details>
<summary><b>安装ANACONDA</b></summary>

> 查看最新链接

[[官网]](https://repo.anaconda.com/archive/)

可在服务器`wget`下载。

> 安装

- 空格跳过协议，一切回车默认。
- 若刚刚没选yes激活，手动激活：`conda init bash`，重启terminal。

建议添加国内源。见后。

</details>

<details>
<summary><b>CONDA创建环境</b></summary>

```bash
conda create -n env_name python=3.6  # 最基本操作
conda create -n venv pip python=3.7  # 可同时装好多个包
```

注意！！！！最好指定python，否则默认可能装成python2，后面的安装都是有问题的。

</details>

<details>
<summary><b>CONDA查看已有环境</b></summary>

```bash
conda env list
```

</details>

<details>
<summary><b>CONDA删除环境</b></summary>

```bash
conda env remove -n env_name
```

</details>

<details>
<summary><b>CONDA查看已有包</b></summary>

```bash
conda list
```

</details>

<details>
<summary><b>CONDA安装包</b></summary>

```bash
conda install pkg_name -y  # 默认yes。注意要先进入环境
```

</details>

<details>
<summary><b>CONDA离线下载和安装包</b></summary>

- 在[[官网]](https://anaconda.org/anaconda/repo)搜包。
- 下载。
- 安装：`conda install --use-local path/to/xxx.tar.bz2`

</details>

<details>
<summary><b>CONDA删除包</b></summary>

```bash
conda remove pkg_name
```

</details>

<details>
<summary><b>CONDA添加国内源</b></summary>

```bash
vim ~/.condarc
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
```

</details>

<details>
<summary><b>CONDA查看现有频道（包括其他设置）</b></summary>

```bash
conda config --show
```

</details>

<details>
<summary><b>CONDA修改可用频道</b></summary>

```bash
vim ~/.condarc
```

</details>

<details>
<summary><b>CONDA包安装路径错误</b></summary>

记得`python -m xxx`

</details>

<details>
<summary><b>CONDA一直在solving</b></summary>

删除除`defaults`外所有channels。

</details>

<details>
<summary><b>CONDA超时</b></summary>

- 通常重试即可。
- 重新登陆校园网。
- 添加国内源。
- 删除`defaults`，并把`https`都改为`http`。

</details>

<details>
<summary><b>CondaVerificationError</b></summary>

```bash
conda clean --all
```

</details>

<details>
<summary><b>CONDA不识别ascii码</b></summary>

把PYTHON升级至3.7；不要用3.6。

</details>
