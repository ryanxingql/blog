# JUPYTER NOTEBOOK

- [JUPYTER NOTEBOOK](#jupyter-notebook)
  - [安装](#安装)
  - [修改启动默认路径](#修改启动默认路径)
  - [使用conda环境](#使用conda环境)
  - [导出PDF](#导出pdf)

## 安装

安装Anaconda会自带，推荐。

## 修改启动默认路径

- 打开`C:\Users\XING\.jupyter`的config文件。
- 搜索`c.NotebookApp.notebook_dir`，修改为目标路径。
- 取消注释并修改。

## 使用conda环境

要把conda环境注册到kernel中。

## 导出PDF

- 直接导出：适用于无中文字符的文档。
- 先导出为markdown，用VSCode的`vscode-pandoc`插件存为PDF。
  - 有书签，可生成目录，可为章节加序号。
- 直接在jupyter notebook界面`ctrl+p`，选择Adobe打印。
  - HTML渲染字体很漂亮。
  - 没有书签，`[toc]`也没有编译。
