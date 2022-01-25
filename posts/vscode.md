# VSCode

- [VSCode](#vscode)
  - [基础](#基础)
  - [导出含中文的 Jupyter Notebook 为 PDF](#导出含中文的-jupyter-notebook-为-pdf)
  - [插件](#插件)
  - [调试](#调试)

## 基础

- **折叠**：若展开文件列表过长，可使用折叠恢复。
- **打开标签**：双击标签为打开至新窗口；单击为覆盖。
- **Jupyter**：打开 Python 脚本，在命令行输入 Jupyter 可见；或在代码前后加上 `#%%`，可进入交互模式，再 `run cell` 即可。

## 导出含中文的 Jupyter Notebook 为 PDF

先转换为 TeX 文件：在 `.ipynb` 文件路径下，运行：`jupyter nbconvert --to latex xxx.ipynb`。

得到 TeX 文件后，用 VSCode 打开，添加一行 `\usepackage[UTF8]{ctex}`，就可以编译出正常含中文的 PDF 了。

## 插件

VSCode 真正强大之处在于丰富的插件。善用插件，学会编辑各类插件的 setting 文件，达到自己的使用目的。

## 调试

- **Matplotlib 没显示**：用 Jupyter 交互模式。
- **Conda 和 PowerShell 报错**：参考[博客 #1](https://blog.csdn.net/chencaw/article/details/89035571) 和[博客 #2](https://blog.csdn.net/cskywit/article/details/99202520)。
