# Pip and Conda

创建和管理虚拟环境，只推荐 Conda。

至于安装包的区别，参见[知乎](https://www.zhihu.com/question/395145313/answer/1230725052)。总的而言，Conda 可安装范围更广，对兼容性更严格；Pip 更快。

## Pip

### Pip 添加国内源

```bash
pip install pip -U
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

参考 [TUNA](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)。

### Pip 离线安装包

- 在 PyPI 搜索合适版本，下载。
- `pip install </path/to/pkg.whl>`

### Pip 调试

#### Pip 找不到安装包

```bash
python -m conda install <pkg_name>
```

#### Pip `timeout`

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

## Conda

### 安装 Anaconda

- 在[官网](https://repo.anaconda.com/archive/)查看最新链接。
- 可在服务器 `wget` 下载。
- `sh` 安装（不需要权限），空格跳过协议，一切回车默认。
- 若没选 yes 激活，手动激活：`conda init bash`，重启 terminal。

建议立即添加国内源，见后。

### Conda 简单指令

- **查看已有环境**：`conda env list`。
- **删除环境**：`conda env remove -n <env_name>`。
- **查看已有包**：`conda list`。
- **安装包**：`conda install <pkg_name> -y`；默认yes；注意要先进入环境。
- **删除包**：`conda remove <pkg_name>`。
- **查看现有频道（包括其他设置）**：`conda config --show`。
- **修改可用频道**：`vim ~/.condarc`。

### Conda 新建或克隆环境

```bash
# 可以同时安装多个包；不要用 Python 3.6，和 Conda 不友好
conda create -n <env_name> python=3.7 <other_pkg_names>

# 克隆
conda create -n <env_name> --clone <src_name>
```

### Conda 环境迁移

当同一环境需要配置在多个服务器上时，Conda 提供了快速的环境克隆方案。

多种方案参见[知乎](https://zhuanlan.zhihu.com/p/87344422)。具体而言，用 YML 转移是一种很好的方案，可以兼顾 Pip 和 Conda 安装的包，且不要求系统平台相同；但需要联网重新下载所有包。

```bash
# 备份环境
conda env export > <yml-name>.yml

# 克隆已备份环境
conda env create -f <yml-name>.yml
```

### Conda 离线安装包

- 在[官网](https://anaconda.org/anaconda/repo)搜包。
- 下载。
- `conda install --use-local <path/to/xxx.tar.bz2>`

### Conda 添加国内源

```bash
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
```

### Conda 调试

#### Conda 找不到安装包

```bash
python -m conda install <pkg_name>
```

#### Conda `solving`

删除除 `defaults` 外所有 channels。

#### `CondaVerificationError`

```bash
conda clean --all
```

#### Conda 不识别 ASCII 码

把 Python 升级至 3.7；不要用 3.6。

#### Conda `timeout`

- 通常重试即可。
- 重新登陆校园网。
- 添加国内源。
- 删除 `defaults`，并把 `https` 都改为 `http`。
