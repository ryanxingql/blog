# Tmux

## 无管理员权限安装

参考[脚本](https://gist.github.com/ryin/3106801)。

## 使用

### 命令

- 进入命令行：`ctrl + b` &#8594; `:`。
- 开启鼠标模式：`set mouse on`。
  - 光标停留在底部绿条，滚轮即可切换窗口。

### Session

- 查看：`tmux ls`。
- 创建：`tmux new -s xxx`。
- 离开：`ctrl + b` &#8594; `d`（detach）。
- 进入：`tmux a`（attach）；或 `tmux a -t xxx`。

### Window

- 创建：`ctrl + b` &#8594; `c`。
- 切换：`ctrl + b` &#8594; `number`。
- 改名：`ctrl + b` &#8594; `,` &#8594; `new name`。
- 关闭：`ctrl + b` &#8594; `&`；或关掉所有 panel。
- 改变窗格序号：`ctrl + b` &#8594; `:` &#8594; `swap-window -s 3 -t 1`。

### Panel

- 一分为二，从中割开：`ctrl + b` &#8594; `"`。
- 自动调整：`ctrl + b` &#8594; `空格`。
- 关闭：`ctrl + b` &#8594; `x`。
- 粗条显示所在 panel：`ctrl + b` &#8594; `m`。
