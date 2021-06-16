# VSCODE

## 基础

- **折叠**：若展开文件列表过长，可使用折叠恢复。
- **打开命令行**：F1，或 `shift + ctrl + p`。
- **打开终端**：`` ctrl + ` ``。
- **打开标签**：双击标签为打开至新窗口；单击为覆盖。
- **JUPYTER**：打开 PYTHON 脚本，在命令行输入 JUPYTER 可见；或在代码前后加上 `#%%`，可进入交互模式，再 `run cell` 即可。

<details>
<summary><b>导出含中文的 JUPYTER NOTEBOOK 为 PDF</b></summary>
<p>

先转换为 TEX 文件：在 IPYNB 文件路径下，运行：`jupyter nbconvert --to latex xxx.ipynb`。

得到 TEX 文件后，用 VSCODE 打开，添加一行 `\usepackage[UTF8]{ctex}`，就可以编译出正常含中文的 PDF 了。

</p>
</details>

## 插件

VSCODE 真正强大之处在于丰富的插件。善用插件，学会编辑各类插件的 setting 文件，达到自己的使用目的。

## 报错

- **MATPLOTLIB 没显示**：用 JUPYTER 交互模式。
- **CONDA 和 POWERSHELL 报错**：参考[博客 1](https://blog.csdn.net/chencaw/article/details/89035571) 和[博客 2](https://blog.csdn.net/cskywit/article/details/99202520)。
