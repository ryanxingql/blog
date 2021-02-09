# TMUX

- [TMUX](#tmux)
  - [配置](#配置)
  - [Session](#session)
  - [WINDOW](#window)
  - [PANEL](#panel)

## 配置

- **进入命令行**：`ctrl + b` -> `:`。

<details>
<summary><b>鼠标模式</b></summary>
<p>

进入命令行，输入 `set -g mouse on`，即可开启鼠标模式。

在鼠标模式关闭的情况下，可以右键复制粘贴。在鼠标模式开启时，要同时按住 `shift`。

</p>
</details>

<details>
<summary><b>无管理员权限安装</b></summary>
<p>

参见[脚本](https://gist.github.com/ryin/3106801)；网友在不断更新。

修改环境变量：

- `vim ~/.bashrc`
- 在文件末尾添加：`export PATH=$PATH:/home/x/local/bin`。
- `source ~/.bashrc`

</p>
</details>

## Session

- **查看**：`tmux ls`。
- **创建**：`tmux new -s xxx`。
- **离开**：`ctrl + b` -> `d`（detach）。
- **进入**：`tmux a`（attach）；或 `tmux a -t xxx`。

## WINDOW

- **创建**：`ctrl + b` -> `c`。
- **切换**：`ctrl + b` -> `number`。
- **改名**：`ctrl + b` -> `,` -> `new name`。
- **关闭**：`ctrl + b` -> `&`；或关掉所有 panel。
- **改变窗格序号**：`ctrl + b` -> `:` -> `swap-window -s 3 -t 1`。

## PANEL

- **一分为二，从中割开**：`ctrl + b` -> `"`。
- **自动调整**：`ctrl + b` -> `空格`。
- **关闭**：`ctrl + b` -> `x`。
- **粗条显示所在 panel**：`ctrl + b` -> `m`。
