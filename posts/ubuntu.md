# UBUNTU

- [UBUNTU](#ubuntu)
  - [文件](#文件)
  - [软件](#软件)
  - [硬盘](#硬盘)
  - [系统](#系统)
    - [查询](#查询)
    - [编辑](#编辑)
    - [安装](#安装)
  - [其他](#其他)

## 文件

创建文件

```bash
echo "hello world!" > README.md
```

## 软件

**zip**

不要用7z，linux不好用。

```bash
# https://serverfault.com/questions/760337/how-to-zip-files-with-a-size-limit/760341

# -r：对子文件递归
# -s 10m：分卷，最大10MB
# archive.zip：目的
# directory：源
$ zip -r -s 10m archive.zip directory/

# 先合成，再解压
$ zip -s 0 split.zip --out unsplit.zip
$ unzip unsplit.zip
```

**窗口置顶**

`alt+space`，选择`always on top`

**更新列表，再更新软件**

```bash
$ sudo apt-get update && apt-get upgrade
```

- 强烈建议更新为国内源：[[参考]](https://mirror.tuna.tsinghua.edu.cn/help/ubuntu/)
- 个人服务器可以执行：`dist-upgrade`。这不仅会升级某些软件，还会卸载一些不需要的软件，比`upgrade`更智能。
- 还可以跟一个`apt-get autoremove`，清理不再需要的依赖。

> 大多数包管理系统是建立在包文件上的集合。包文件包括编译好的二进制文件，软件，安装脚本，依赖列表等。Ubuntu系统的包管理工具格式为`.deb`，常用工具为`apt`、`apt-cache`、`apt-get`等。[[ref]](https://www.sysgeek.cn/linux-package-management/)  
> Ubuntu的母版是Debian。而Debian使用一套名为Advanced Packaging Tool的工具管理包系统。Ubuntu有很多工具可以与APT进行交互，其中`apt`、`apt-cache`、`apt-get`等广受欢迎。`apt`是后者的大一统（虽然没有完全向下兼容），也是趋势。尽量使用`apt`，已经涵盖了`apt-get`的基础功能。[[ref]](https://www.sysgeek.cn/apt-vs-apt-get/)

**拼音**

- [ref](https://blog.csdn.net/wu10188/article/details/86540464)
- 输入法切换：`win+space`
- 中英切换：`shift`

**pip3**

```bash
$ sudo apt install python3-pip
```

**vscode**

在拼音模式下，无法鼠标多选。要win+空格切换到英文。

**anaconda3**

记得`export PATH`

**q2ray**

- 用snap安装：`sudo snap install qv2ray`
- 手动下载v2ray内核，转移到`~/snap/qv2ray/2729/`，按要求解压为`vcore/`。检查核心设置，通过。注意不要sudo！！！
- 在操作界面中将服务器导入。
- Firefox中设为系统proxy即可。
- Chrome要下载[SwitchOmega](https://github.com/FelisCatus/SwitchyOmega/releases)，记得改端口号。
- 系统Network设置貌似不需要动。如果你选择q2ray的系统代理->禁用，network proxy会自动off，反之，会自动manual，甚至端口号都设置好了。

> [[教程]](https://medium.com/@eleveninstrangerthings/%E5%9C%A8ubuntu%E4%B8%8A%E5%AE%89%E8%A3%85%E5%9B%BE%E5%BD%A2%E5%8C%96v2ray%E5%AE%A2%E6%88%B7%E7%AB%AFqv2ray-d0f690b7c519)

**ss（失败）**

- 先买了一个Vultr服务器：https://www.vultrblog.com/vultr-ss.html
- 其中一键ssserver脚本用的是：https://github.com/dlxg/shadowsocks_install
- ubuntu上安装sslocal，写json，命令行即可开启。[教程](http://codetd.com/article/1790848)
- 设置里修改Network协议和端口。
- 注意这是全局的。未考虑分流。
- 常用指令
  - 可能要sudo，否则会报错。
  - `sudo sslocal -c ss.json -d start`
    - 后端启动，无任何信息。
  - `sudo sslocal -c ss.json -d stop`
  - `sudo sslocal -c ss.json`
    - 前端启动，有日志。
  - `sslocal -c xxx.xxx.xxx.xxx -p 2020 -k xxxx -b 127.0.0.1 -l 10808`

## 硬盘

挂载硬盘

```bash
$ sudo fdisk -l # 查看磁盘对应位置，假设是/dev/sdd1
$ sudo mkdir /media/usr/DiskName # 假设磁盘名字为sdcard
$ sudo mount /dev/sdd1 /media/usr/DiskName # 挂载到指定路径
```

记住标识符特别重要，特别是当硬盘较多时。

卸载硬盘

```bash
$ sudo umount /media/usr/DiskName
```

在安装系统一节我们提到，我们保留了两块机械硬盘。我们希望开机自动挂载：
1. 磁盘分区，并格式化、改为ext4格式、作为新硬盘挂载：
   https://blog.csdn.net/zhengchaooo/article/details/79500116
2. 配置开机自动挂载，并改为普通权限：
   https://blog.csdn.net/ls20121006/article/details/78665718

## 系统

### 查询

- 当前目录下的文件信息（包括大小）：`ll`
- 空间占用
  - 当前文件夹占用空间：`du -h --max-depth=1`
  - 各分区占用和剩余空间：`df -hl`
  - 每个用户的home目录占用：`sudo du -sh /home/*`
- 系统信息
  - 内核/操作系统：`uname -a`
  - CPU信息：`cat /proc/cpuinfo`
- 网络
  - ip：`ifconfig`

> [[ref]](https://blog.csdn.net/bluishglc/article/details/41390589)

### 编辑

- 添加用户：`sudo adduser xxx`
- 添加至管理员：`sudo vim /etc/sudoers`
- 改密码：`passwd username`
- 改为短密码：必须先`sudo`

### 安装

以Ubuntu 18.04 LTS为例。

目标

1. 在服务器上配置最新的Ubuntu稳定版本18.04 LTS。18.04比16.04好看很多，非常建议。（2020有20可选择）
2. 有3块硬盘：2块4TB机械硬盘，1块2TB固态硬盘。计划将固态硬盘作为主硬盘，其余两块机械硬盘后期挂载使用。
3. 分区只设定根目录、home目录和swap分区。swap分区和内存大小一样，设为128GB。根据服务器使用经验，大家都会把数据往家目录里堆放，因此我们先分配根目录（不需要太大，我们这里给100GB）和交换分区（和内存一样大，128GB），其他所有空间都给家目录。
4. 设置为中文，这样在安装过程和以后遇到错误时，可以看中文，方便一些。

具体流程

1. 下载`Ubuntu-18.04.3-desktop-amd64.iso`。
2. 下载UltraISO，试用即可。
3. 制作启动盘：
   - 打开UltraISO
   - 文件 -> 打开 -> iso文件
   - 启动 -> 写入硬盘映像 ，选择硬盘驱动器为备用U盘（会被格式化，当心），写入方式UBS-HDD+，最后选择写入。
   - 提示"刻录成功”后，选择返回即可。
4. 将U盘插在服务器上，在BIOS启动项（开机界面狂按F12进入）里选择`UEFI: Generic Flash Disk xxx`，进入Ubuntu引导界面，直接安装（不需要试用）。
5. 选择中文简体、汉语，不连wifi，最小安装。
6. 安装类型选择“其他选项”，自己来定义分区。
   - 其中有3块硬盘：`/dev/sda`，`/dev/sdc`和`/dev/nvme0n1`，以及它们的分区情况。
   - 把存在的分区全部都“-”掉，即删除（不要随便效仿！）。
   - 选择固态硬盘`/dev/nvme0n1`的“空闲”，按“+”添加以下分区。
   - 主分区：102400MB（100GB），主分区，空间起始位置，Ext4日志文件系统，挂载点`/`。
   - 交换分区：131072MB（128GB），逻辑分区，空间起始位置，交换空间。
   - 家目录：剩余所有空间，逻辑分区，空间起始位置，Ext4日志文件系统，挂载点`/home`。
   - 安装启动引导器的设备：因为我们在`/dev/nvme0n1`磁盘上分区的，因此就选择`/dev/nvme0n1`。然后点“现在安装”，点“继续”。
   - 注：后期遇到了没有引导项，无法进入Ubuntu系统的问题。因此添加一个boot分区：分配1024MB，逻辑分区，空间起始位置，Ext4日志文件系统，挂载点`/boot`。然后上一步就选择在该boot分区上安装引导。成功。
7. 选择上海时区。用户名和计算机名字任意，但提醒一点：计算机名字不要太长。因为在terminal中，计算机名会出现在`bash`的每一行命令之前。如果计算机名太长，会导致命令很长。
8. 等待。安装过程有点漫长，可能在20分钟左右。

> [[图片教程]](https://blog.csdn.net/baidu_36602427/article/details/86548203#commentBox)

## 其他

- 停止广播：`mesg n`
- 切换工作区
  - `ctrl+alt+shift+上/下`
  - 按`win`进入工作区视图，鼠标中键滑动可顺滑查看所有工作区。
