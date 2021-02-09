# JUPYTER NOTEBOOK

- **安装**：安装 ANACONDA 可自带 JUPYTER；推荐这种方式。
- **使用CONDA环境**：要把 CONDA 环境注册到 kernel 中。

<details>
<summary><b>修改启动默认路径</b></summary>
<p>

- 打开 `C:\Users\XING\.jupyter` 的config文件。
- 搜索 `c.NotebookApp.notebook_dir`，修改为目标路径。
- 取消注释并修改。

</p>
</details>

<details>
<summary><b>导出 PDF</b></summary>
<p>

- 直接导出：适用于无中文字符的文档。
- 先导出为 MARKDOWN，用 VSCODE 的 `vscode-pandoc` 插件存为PDF。
  - 有书签；可生成目录，且自动为章节加序号。
- 直接在 JUPYTER NOTEBOOK 界面 `ctrl + p`，选择 ADOBE 打印。
  - HTML 渲染字体很漂亮。
  - 没有书签；`[toc]` 没有编译。

</p>
</details>
