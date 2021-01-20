# VSCODE

- [VSCODE](#vscode)

<details>
<summary><b>快捷键</b></summary>

- 打开命令行：F1，或`shift + ctrl + p`
- 打开终端：`` ctrl + ` ``
- 双击标签为打开至新窗口；单击为覆盖。

</details>

<details>
<summary><b>REMOTE-SSH</b></summary>

[[ref]](https://zhuanlan.zhihu.com/p/64849549)

</details>

<details>
<summary><b>JUPYTER</b></summary>

打开PYTHON脚本，打开命令行，输入JUPYTER可见。

或在代码前后加上`#%%`，可进入交互模式，再run cell。

</details>

<details>
<summary><b>CONDA和POWERSHELL报错</b></summary>

- [[ref1]](https://blog.csdn.net/chencaw/article/details/89035571)
- [[ref2]](https://blog.csdn.net/cskywit/article/details/99202520)

</details>

<details>
<summary><b>MATPLOTLIB没有显示</b></summary>

用交互模式。在代码前后加上`#%%`，可run cell。

</details>

<details>
<summary><b>导出含中文的JUPYTER NOTEBOOK为PDF</b></summary>

先转换为TEX文件：在IPYNB文件路径下，运行：`jupyter nbconvert --to latex xxx.ipynb`。

得到TEX文件后，用VSCODE打开，添加一行`\usepackage[UTF8]{ctex}`，就可以编译出正常含中文的PDF了。

</details>
