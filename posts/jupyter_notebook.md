# JUPYTER NOTEBOOK

- [JUPYTER NOTEBOOK](#jupyter-notebook)

<details>
<summary><b>安装</b></summary>

安装ANACONDA会自带，推荐。

修改启动默认路径：

- 打开`C:\Users\XING\.jupyter`的config文件。
- 搜索`c.NotebookApp.notebook_dir`，修改为目标路径。
- 取消注释并修改。

</details>

<details>
<summary><b>使用CONDA环境</b></summary>

要把CONDA环境注册到kernel中。

</details>

<details>
<summary><b>导出PDF</b></summary>

- 直接导出：适用于无中文字符的文档。
- 先导出为MARKDOWN，用VSCODE的`vscode-pandoc`插件存为PDF。
  - 有书签，可生成目录，可为章节加序号。
- 直接在JUPYTER NOTEBOOK界面`ctrl+p`，选择Adobe打印。
  - HTML渲染字体很漂亮。
  - 没有书签，`[toc]`也没有编译。

</details>
