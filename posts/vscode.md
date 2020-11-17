# VSCODE

- [VSCODE](#vscode)
  - [基础](#基础)
  - [问题解决](#问题解决)
  - [特殊](#特殊)
    - [导出markdown为PDF](#导出markdown为pdf)

## 基础

> 打开命令行

- F1，或`shift + ctrl + p`

> 新建页

- 双击打开。单击会覆盖。

> Remote设置

- [[ref]](https://zhuanlan.zhihu.com/p/64849549)

## 问题解决

> Conda和PowerShell报错

- [[ref1]](https://blog.csdn.net/chencaw/article/details/89035571)
- [[ref2]](https://blog.csdn.net/cskywit/article/details/99202520)

> matplotlib没有显示

用交互模式。在代码前后加上`#%%`，可run cell。

## 特殊

### 导出markdown为PDF

> Pandoc

- 下载[Pandoc](https://github.com/jgm/pandoc/releases)。
- 打开VSCode的`setting -> Extensions -> Pandoc Option Configuration -> Pdf Opt String`
- 填：`-N -s --toc --pdf-engine=xelatex -V CJKmainfont="Microsoft YaHei" --highlight-style zenburn -V geometry:margin=2.5cm`
  - 具体含义参见：[[ref]](https://jdhao.github.io/2017/12/10/pandoc-markdown-with-chinese/)
- 命令行输入`pandoc`，选择`pdf`，等待自动弹出PDF。
- 由于Pandoc自身的问题，对markdown有许多特殊要求，否则会出现格式错误。
  - 每个list、block quote、table前必须空一行。
  - 多行内容，必须在行末增加`line break`，即两个空格。
  - 如果内容较少，图片会被挤到最后一页。

> Markdown Preview Enhanced插件

右键预览，chrome打开，直接打印。
