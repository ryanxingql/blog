# TMUX

- [TMUX](#tmux)
  - [Session](#session)
  - [Window](#window)
  - [Panel](#panel)
  - [无root安装](#无root安装)
  - [其他](#其他)

## Session

- 创建：`tmux new -s xxx`
- 离开：`ctrl+b -> d`，detach。
- 进入：`tmux a`，attach；或`tmux a -t xxx`

## Window

- 创建：`ctrl+b -> c`
- 切换：`ctrl+b -> number`
- 改名：`ctrl+b -> , -> new name`
- 关闭：`ctrl+b -> &`；或关掉所有panel。
- 改变窗格序号：`ctrl+b -> : -> swap-windows -s 3 -t 1`

## Panel

- 一分为二，从中割开：`ctrl+b -> "`
- 调整：`ctrl+b -> 空格`
- 关闭：`ctrl+b -> x`

## 无root安装

- [[ref]](https://gist.github.com/ryin/3106801)：网友在不断更新脚本。
- 修改环境变量
  - `vim ~/.bashrc`
  - 在文件末尾添加：`export PATH=$PATH:/home/x/local/bin`
  - `source ~/.bashrc`

## 其他

- 和系统互动：貌似是`shift + 鼠标右键`，可以选择paste之类。不同终端（例如VSCode和Moba的终端）不一样。
