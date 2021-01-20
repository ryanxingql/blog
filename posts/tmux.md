# TMUX

- [TMUX](#tmux)
  - [设置](#设置)
  - [SESSION](#session)
  - [WINDOW](#window)
  - [PANEL](#panel)
  - [无root安装](#无root安装)

## 设置

- 进入命令行：`ctrl+b -> :`

</details>

<details>
<summary><b>开启鼠标滚轮</b></summary>

- 进入命令行，输入`set -g mouse on`
- 在鼠标模式关闭的情况下，可以右键复制粘贴。在鼠标模式开启时，要同时按住`shift`。

</details>

## SESSION

- 创建：`tmux new -s xxx`
- 离开：`ctrl+b -> d`，detach。
- 进入：`tmux a`，attach；或`tmux a -t xxx`

## WINDOW

- 创建：`ctrl+b -> c`
- 切换：`ctrl+b -> number`
- 改名：`ctrl+b -> , -> new name`
- 关闭：`ctrl+b -> &`；或关掉所有panel。
- 改变窗格序号：`ctrl+b -> : -> swap-window -s 3 -t 1`

## PANEL

- 一分为二，从中割开：`ctrl+b -> "`
- 调整：`ctrl+b -> 空格`
- 关闭：`ctrl+b -> x`
- 粗条显示所在panel：`ctrl+b, m`

## 无root安装

<details>
<summary><b>展开详情</b></summary>

[[ref]](https://gist.github.com/ryin/3106801)：网友在不断更新脚本。

修改环境变量

- `vim ~/.bashrc`
- 在文件末尾添加：`export PATH=$PATH:/home/x/local/bin`
- `source ~/.bashrc`

</details>
