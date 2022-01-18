# 常用指令

按应用平台分类。

## macOS

| 对象 | 功能 | 步骤1 | 步骤2 | 步骤3 |
|:-|:-|:-|:-|:-|
| macOS | 搜索 | `cmd + space` |  |  |
|  | 锁屏 | 按指纹键 |  |  |
|  | 移动对象 | 三指滑动；可在短时间内接力，不需要连续 |  |  |
|  | 查看所有打开应用 | 四指上滑 |  |  |
|  | 预览文件（如视频） | 选中文件后，空格即可，不用双击打开 |  |  |
|  | 移动文件路径 | 要么同时打开源路径和目标路径的 finder，然后移动文件；要么在命令行操作。没有剪切 |  |  |
|  | 打开终端/截屏 | 搜索 | 输入 terminal/screenshot |  |
|  | 自由拖动截屏 | `cmd + shift + 4` |  |  |
|  | 自动排列图标 | `ctrl + cmd + 1` |||
|  | 获取文件路径到终端（文件夹不行） | 把文件直接拖入终端 |||
|  | 显示文件夹下隐藏文件 | `cmd + shift + .` |||
|  | 输入法中英文切换 | `ctrl + space` 或 `caps`（不灵敏） |||
|  | 英文输入大写 | 长按 `caps` 持续输入，或按住 `shift` 输入少量大写字符 |||
|  | 光标跳至行首/行尾 | `cmd + left/right` |||
|  | 光标跳过一个字符串 | `opt + left/right` |||
|  | 选中字符 | `shift + left/right` |||
|  | 选中字符串 | 持续执行上述操作；或在初始位置单指按压后滑动选取；或 `opt + shift + left/right` |||
|  | 选中字符串到行首/行尾 | `shift + cmd + left/right` |||
|  | 选中字符串到上一行/下一行同一位置 | `shift + up/down` |||
|  | 翻页 | `fn + up/down` |||
|  | 撤销 | `cmd + z` |||
|  | 复制/粘贴 | `cmd + c/v` |||
|  | 保存 | `cmd + s` |||
|  | 搜索 | `cmd + f` |||
|  | 删除文件或文件夹 | `cmd + delete` |||
|  | 关闭窗口 | `cmd + w` |||
|  | 关闭软件（finder 不能关） | `cmd + q` |||
|  | 改某格式默认打开应用 | 选择文件的更多信息 |修改默认打开应用||
|  | 安装软件 | 下载 dmg |移动到 application|eject，删除 dmg|
| PyCharm | 复制当前行到下一行 | `cmd + d` |||
|  | 注释/取消注释当前行 | `cmd + /` |||
| VSCode | 展示所有命令 | `shift + cmd + p` |||
| VSCode LaTeX | 正向搜索 | `opt + cmd + j` |||
|  | 注释/取消注释当前行 | `cmd + /` |||
| XMind | 添加笔记 | `shift + cmd + n` |||
|  | 添加链接 | `cmd + k` |||
|  | 添加同级词条 | `enter` |||
|  | 添加下一级词条 | `tab` |||

## 全平台

| 对象 | 功能 | 步骤1 | 步骤2 | 步骤3 |
| :- | :- | :- | :- | :- |
| Hexo | 清空公开仓库 | `hexo clean` |||
|  | 生成公开仓库 | `hexo g` |||
|  | 部署公开仓库 | `hexo d` |||
|  | 生成后部署 | `hexo g -d` |||
| Markdown | 输入右箭头 | 输入 `&#8594;` |||
| VSCode LaTeX | 反向搜索 | 鼠标双击 |||

## Linux

| 对象 | 功能 | 步骤1 | 步骤2 | 步骤3 |
| :- | :- | :- | :- | :- |
| Tmux | 查看所有 session | `tmux ls` |||
|  | 交换 window | `ctrl + b` | `:` | `swap-window -s 0 -t 1` |
|  | 翻页 | `ctrl + b` | 翻页键 |  |
|  | 自动调整 panel 大小 | `ctrl + b` | `space` |  |
|  | 高亮/取消高亮当前 panel | `ctrl + b` | `m` |  |
|  | 进入命令行模式 | `ctrl + b` |  |  |
|  | 开启鼠标操作模式 | `ctrl + b` | `set mouse on` |  |
| Ubuntu | 打开 terminal | `ctrl + alt + t` |||
|  | 查各用户的 home 目录占用       | `sudo du -sh /home/*` |||
|  | 改用户密码                     | `passwd <usrname>`（改短密码要权限） |||
|  | 添加用户                       | `sudo adducer <usrname>` |||
|  | 添加管理员权限                 | `sudo vim /etc/sudoers/` |编辑||
|  | 快速创建文档                   | `echo haha > readme.txt` |||
|  | 查看路径列表信息               | `ll` |||
|  | 查看路径列表信息，包括隐藏文件 | `ll -ah` |||
|  | 查看分区占用和剩余空间         | `df -hl` |||
|  | 查看路径占用空间               | `du -h --max-depth=1` |||
|  | 查 ip                          | `ifconfig` |||
|  | 查软件位置                     | `whereis <softwareName>` |||
|  | 安装 deb 文件                  | `sudo dpkg -i <debName>` |||

![tmux](../imgs/command-tmux.png)

## Windows

| 对象 | 功能 | 步骤1 | 步骤2 | 步骤3 |
|:-|:-|:-|:-|:-|
| 罗技 MX Master 3 | 左右滑动 Edge 或 VSCode 页面 | 用滚轮即可，需在设置里设置 |||
| Batch | 批量重命名文件 | `ren *_a.png *_b.png` |||
| PyCharm | 复制当前行到下一行 | `ctrl + d` |||
|  | 注释/取消注释当前行 | `ctrl + /` |||
| Termius | 切换 terminal | `alt + left/right` |||
|  | 开/关 snippets | `ctrl + s` |||
| VSCode | 复制当前行到下一行 | `shift + alt + down` |||
|  | 展示所有命令 | `shift + ctrl + p` |||
| VSCode LaTeX | 正向搜索 | `ctrl + alt + j` |||
|  | 注释/取消注释当前行 | `ctrl + /` |||
| Windows | 多选字母 | `shift + left/right/up/down` |||
|  | 多选单词 | `shift + ctrl + left/right/up/down` |||
|  | 锁屏 | `win + l` |||
|  | 关闭页面 | `ctrl + w` |||

## watchOS

| 对象    | 功能           | 步骤1                    | 步骤2 | 步骤3 |
| :------ | :------------- | :----------------------- | :---- | :---- |
| watchOS | 回到表盘主界面 | 用手盖住表盘，再放开即可 |       |       |
