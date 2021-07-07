# Jupyter Notebook

## 安装

安装 Anaconda 可自带 Jupyter；推荐这种方式。

## 使用 Conda 环境

要把 Conda 环境注册到 kernel 中。

## 修改启动默认路径

- 打开 `C:\Users\XING\.jupyter` 的config文件。
- 搜索 `c.NotebookApp.notebook_dir`，修改为目标路径。
- 取消注释并修改。

## 导出 PDF

- 直接导出：适用于无中文字符的文档。
- 先导出为 Markdown，用 VSCode 的 `vscode-pandoc` 插件存为 PDF。
  - 有书签；可生成目录，且自动为章节加序号。
- 直接在 Jupyter Notebook 界面 `ctrl + p`，选择 Adobe 打印。
  - HTML 渲染字体很漂亮。
  - 没有书签；`[toc]` 没有编译。
