# CONDA AND PIP

强烈推荐用 PIP 下载包，用 CONDA 管理虚拟环境。

## PIP

### 常规

<details>
<summary><b>添加国内源</b></summary>
<p>

```bash
pip install pip -U
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

参考 [TUNA](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)。

</p>
</details>

<details>
<summary><b>离线安装包</b></summary>
<p>

- 在 PYPI 搜索合适版本，下载。
- `pip install </path/to/pkg.whl>`

</p>
</details>

### 调试

- **包安装路径错误；已安装的包找不到**：`python -m conda install <pkg_name>`。

<details>
<summary><b><code>timeout</code></b></summary>
<p>

```bash
pip install --default-timeout=100 <pkg_name> -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/
```

另：创建或修改 `~/.pip/pip.conf`，内容如下：

```txt
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host=mirrors.aliyun.com
```

</p>
</details>

## CONDA

### 常规

- **查看已有环境**：`conda env list`。
- **删除环境**：`conda env remove -n <env_name>`。
- **查看已有包**：`conda list`。
- **安装包**：`conda install <pkg_name> -y`；默认yes；注意要先进入环境。
- **删除包**：`conda remove <pkg_name>`。
- **查看现有频道（包括其他设置）**：`conda config --show`。
- **修改可用频道**：`vim ~/.condarc`。

<details>
<summary><b>新建或克隆环境</b></summary>
<p>

```bash
conda create -n <env_name> python=3.7 <other_pkg_names>  # 可以同时安装多个包；不要用 PYTHON 3.6，和 CONDA 不友好。

conda create -n <env_name> --clone <src_name>  # 复制环境
```

</p>
</details>

<details>
<summary><b>安装 ANACONDA</b></summary>
<p>

- 在[官网](https://repo.anaconda.com/archive/)查看最新链接。
- 可在服务器 `wget` 下载。
- 安装，空格跳过协议，一切回车默认。
- 若没选 yes 激活，手动激活：`conda init bash`，重启 terminal。

建议立即添加国内源，见后。

</p>
</details>

<details>
<summary><b>离线安装包</b></summary>
<p>

- 在[官网](https://anaconda.org/anaconda/repo)搜包。
- 下载。
- `conda install --use-local <path/to/xxx.tar.bz2>`

</p>
</details>

<details>
<summary><b>添加国内源</b></summary>
<p>

```bash
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
```

</p>
</details>

### 调试

- **包安装路径错误；已安装的包找不到**：`python -m conda install <pkg_name>`。
- `solving`：删除除 `defaults` 外所有 channels。
- `CondaVerificationError`：`conda clean --all`。
- **不识别 ASCII 码**：把 PYTHON 升级至 3.7；不要用 3.6。

<details>
<summary><code>timeout</code></summary>
<p>

- 通常重试即可。
- 重新登陆校园网。
- 添加国内源。
- 删除 `defaults`，并把 `https` 都改为 `http`。

</p>
</details>
