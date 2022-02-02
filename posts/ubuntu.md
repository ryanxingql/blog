# Ubuntu

- [Ubuntu](#ubuntu)
  - [系统](#系统)
    - [特殊需求](#特殊需求)
    - [安装](#安装)
    - [开机自动挂载硬盘](#开机自动挂载硬盘)
    - [挂载/卸载硬盘](#挂载卸载硬盘)
    - [切换工作区](#切换工作区)
    - [软件更新](#软件更新)
    - [软链接](#软链接)
    - [Unity plus LightDM](#unity-plus-lightdm)
  - [软件](#软件)
    - [TAR](#tar)
    - [压缩](#压缩)
      - [TAR.GZ](#targz)
      - [ZIP](#zip)
      - [PIGZ](#pigz)
      - [RAR](#rar)
      - [7Z](#7z)
    - [Sunlogin](#sunlogin)
    - [FRP plus supervisor 进程维持 plus supervisor 开机自启](#frp-plus-supervisor-进程维持-plus-supervisor-开机自启)
    - [输入法](#输入法)
    - [视频播放器](#视频播放器)
    - [科学上网](#科学上网)

## 系统

### 特殊需求

- **查各用户内存占用**：`ps --no-headers -eo user,rss | awk '{arr[$1]+=$2}; END {for (i in arr) {print i,arr[i]}}' | sort -nk2`。
- **限制用户内存**：参见[此处](https://unix.stackexchange.com/questions/34334/how-to-create-a-user-with-limited-ram-usage)。
  - **快速占用 90% 内存测试**：`stress-ng --vm-bytes $(awk '/MemAvailable/{printf "%d\n", $2 * 0.9;}' < /proc/meminfo)k --vm-keep -m 1`。
- **查内核/操作系统**：`uname -a`。
- **查 CPU 信息**：`cat /proc/cpuinfo`。
- **关闭广播**：`mesg n`。
- **脚本开机自启动**：参见[博客](https://blog.csdn.net/weixin_42454034/article/details/106564783)。
- **窗口置顶**：`alt + space`，选择 `always on top`。
- **安装微软雅黑字体**：参见[博客](https://www.cnblogs.com/feipeng8848/p/9649089.html)。

### 安装

以 Ubuntu 18.04 LTS 为例。

需求：

1. 在服务器上配置最新的 Ubuntu 稳定版本 18.04 LTS。18.04 比 16.04 好看很多，非常建议。（2020 有 20.04 可选择）
2. 有 3 块硬盘：2 块 4 TB 机械硬盘，1 块 2 TB 固态硬盘。计划将固态硬盘作为主硬盘，其余两块机械硬盘后期挂载使用。
3. 分区只设定根目录、home 目录和 swap 分区。swap 分区和内存大小一样，设为 128 GB。根据服务器使用经验，大家都会把数据往家目录里堆放，因此我们先分配根目录（不需要太大，我们这里给 100 GB）和交换分区（和内存一样大，128 GB），其他所有空间都给家目录。
4. 如果是新手，设置为中文方便调试；如果是老手，设置为英文，路径美观。

具体流程：

1. 下载 `Ubuntu-18.04.3-desktop-amd64.iso`。
2. 下载 UltraISO，试用即可。
3. 制作启动盘：
   - 打开 UltraISO。
   - 文件 -&#8594;> 打开 &#8594; ISO 文件。
   - 启动 &#8594; 写入硬盘映像（注意不是软盘映像），选择硬盘驱动器为备用 U 盘（会被格式化，当心），写入方式 `USB-HDD+`，写入。
   - 提示"刻录成功”后，选择返回即可。
4. 将 U 盘插在服务器上，在 BIOS 启动项（开机界面狂按 F12 进入）里选择 `UEFI: Generic Flash Disk xxx`，进入 Ubuntu 引导界面，直接安装（不需要试用）。
5. 最小安装，不装游戏等。
6. 安装类型选择“其他选项”（不要随便擦除硬盘和 Windows 系统，除非真的需要），自定义分区。
   - 其中有3块硬盘：`/dev/sda`，`/dev/sdc` 和 `/dev/nvme0n1`，以及它们的分区情况。
   - 把不需要的分区全部都“-”掉，即删除，成为 free space。
   - 我们下面只操作固态硬盘，机械硬盘在后续章节再介绍自动挂载。选择固态硬盘 `/dev/nvme0n1` 的“空闲”，按“+”添加以下分区。
   - 主分区：102400 MB（100 GB），主分区，空间起始位置，Ext4 日志文件系统，挂载点 `/`。
   - 交换分区：131072 MB（128 GB），逻辑分区，空间起始位置，交换空间。
   - boot 分区：分配 1024 MB，逻辑分区，空间起始位置，Ext4 日志文件系统，挂载点 `/boot`。
   - 家目录：剩余所有空间，逻辑分区，空间起始位置，Ext4 日志文件系统，挂载点 `/home`。
   - 选择在 boot 分区上安装引导。
   - 安装。
7. 选择上海时区。用户名和计算机名字任意，但提醒一点：计算机名字不要太长。因为在 terminal 中，计算机名会出现在 BASH 的每一行命令之前。如果计算机名太长，会导致命令很长。
8. 安装。

参考[图片教程](https://blog.csdn.net/baidu_36602427/article/details/86548203)。

在没有离开本机前，建议开机执行以下基本操作：

1. `sudo apt update`：否则很多基础工具找不到安装仓库，如 `net-tools`。
2. `sudo apt install net-tools`：`ifconfig` 必需。
3. `sudo apt install ssh`：否则无法用 SSH 连接。
4. 顺便一波升级：`sudo apt upgrade`。

后续操作都可以远程执行。

### 开机自动挂载硬盘

在安装系统一节我们提到，我们保留了两块机械硬盘；我们希望开机自动挂载。步骤如下：

1. [磁盘分区并格式化；改为 ext4 格式；作为新硬盘挂载](https://blog.csdn.net/zhengchaooo/article/details/79500116)。
2. [配置开机自动挂载，并改为普通权限](https://blog.csdn.net/ls20121006/article/details/78665718)。

### 挂载/卸载硬盘

```bash
sudo mkdir </media/usr/path>  # /home/usr/path 也可以

#sudo fdisk -l # 查看磁盘对应位置，假设是 /dev/sdd1
lsblk -f  # 通过硬盘标识符或名字，查看对应位置，如 /dev/sdd1
sudo mount /dev/sdd1 </media/usr/path/> # 挂载到指定路径

sudo umount </media/usr/path>  # 卸载
```

记住标识符特别重要，特别是当硬盘较多时。

### 切换工作区

- `ctrl + alt + shift + 上/下`
- 按 `win` 进入工作区视图，鼠标中键滑动可顺滑查看所有工作区。

### 软件更新

```bash
sudo apt-get update && apt-get upgrade
```

补充：

- 强烈建议更新为国内源，参见 [TUNA](https://mirror.tuna.tsinghua.edu.cn/help/ubuntu/)。
- 个人服务器可以执行：`dist-upgrade`。这不仅会升级某些软件，还会卸载一些不需要的软件，比 `upgrade` 更智能。
- 还可以跟一个 `apt-get autoremove`，清理不再需要的依赖。

### 软链接

```bash
# 创建软链接：在 fake_path 即可访问 real_path
ln -s <real_path> <fake_path>  # 注意 fake_path 末尾不要带 /；real_path 无所谓

# 删除软链接而不删除文件
rm -rf <fake_path>  # 注意末尾不带 /；否则文件夹没删掉，而是删掉了内部文件
```

### Unity plus LightDM

[[安装]](https://www.linuxbabe.com/ubuntu/install-unity-desktop-environment-ubuntu-20-04)

[[定制]](https://www.jianshu.com/p/1c4430d9084e)

## 软件

### TAR

[[博客]](https://zhuanlan.zhihu.com/p/407720976)

```bash
# 将testfile1、2打包到archive.tar
tar -cvf archive.tar testfile1 testfile2

# 查看archive.tar内容
tar -tvf archive.tar

# 提取archive.tar中的文件到当前路径
tar -xvf archive.tar

# 只提取testfile1
tar -xvf archive.tar testfile1

# 保留testfile1所在的目录结构
tar -xvf archive.tar dir1/testfile1

# 提取archive.tar中文件至指定路径testpath下（必须存在）
tar -xvf archive.tar -C testpath
```

- `-c`：create，创建打包文件。
- `-v`：verbose，显示进度。
- `-f`：file，指定存档文件，名称为其后第一个参数。因此，不要随意调换参数顺序。例如 `-cfv` 会创建一个名为 `v` 的存档文件。
- `-t`：list，列举。
- `-x`：extract，提取打包文件。
- `-C`：directory，指定路径。

### 压缩

#### TAR.GZ

实际上是先用 TAR 打包，然后用 GZIP 压缩。由于 TAR 和 GZIP 组合太常用了，因此 TAR 直接加入 GZIP 压缩参数。

```bash
# 压缩testfolder至archive.tar.gz
tar -zcvf archive.tar.gz testfolder

# 解压archive.tar.gz
tar -zxvf archive.tar.gz

# 解压archive.tar.gz至指定路径testpath下（必须存在）
tar -zxvf archive.tar.gz -C testpath
```

打包文件的后缀可以是 `tar.gz` 或 `tgz`。

#### ZIP

各平台兼容，但压缩率不高。

压缩某文件夹，最外层为该文件夹：

```bash
zip -r <zip_name>.zip <folder_path>/  # 注意要加 /
```

不包含外部文件夹压缩：

```bash
cd <folder_path>
zip -r ../<zip_name>.zip *
```

仅查看内部信息，不解压：

```bash
unzip -l <zip_path> | less  # 如果不加 | less，所有 content 会递归涌至屏幕
```

解压至指定路径：

```bash
unzip a_zip.zip -d a_folder  # 不需要事先创建路径；如果 zip 最外层是一个文件夹 a_dir，那么最终路径是 a_folder/a_dir/
unzip -j a_zip.zip -d a_folder  # a_zip 所有文件都会被放在 a_folder，不含任何子文件夹
```

分卷压缩（方便大文件传输，推荐）和解压：

```bash
# https://serverfault.com/questions/760337/how-to-zip-files-with-a-size-limit/760341
# -r：对子文件递归
# -s：分卷最大尺寸，例如10m，4g
# archive.zip：输出主压缩包，还会有子压缩包archive.z01/z02/...等
# directory：源文件夹；要加/
zip -r -s 10m archive.zip directory/

# 先合成，再解压
zip -s 0 archive.zip --out unsplit.zip && unzip unsplit.zip
```

#### [PIGZ](https://zlib.net/pigz/pigz.pdf)

有时候文件太多太大，GZ 和 ZIP 单线程太慢了。PIGZ 可以多线程。

压缩文件夹：

```bash
tar --use-compress-program="pigz -k [-p 20] " -cvf out.tar.gz dir1 dir2
```

- 先用 TAR 将若干文件夹打包为一个 TAR 文件，然后用 PIGZ 压缩为 GZ。这是因为 PIGZ 只能打包文件，不能打包文件夹，因此要用 TAR 先打包成文件。
- `-k`：保留源文件。
- `-p`：指定进程数。默认使用所有进程。

解压和 TAR.GZ 格式解压一样：

```bash
tar -zxvf output.tar.gz
```

#### RAR

```bash
sudo apt install rar unrar
unrar x rar_name.rar
```

#### 7Z

Ubuntu 支持不好，不建议用。

### Sunlogin

比 AnyDesk 好用多了，还免费。参见[安装指南](https://www.jianshu.com/p/289001a00cb1)。

### FRP plus supervisor 进程维持 plus supervisor 开机自启

参见博客：[[1]](https://cloud.tencent.com/developer/article/1694829) 和 [[2]](https://blog.csdn.net/yuwu00/article/details/108197283)。

配置可以写在 `frpc.ini` 里，此时 command 比较简单：`./ frpc -c xxx/frpc.ini`。

若提示无此命令，`sudo chmod +x frpc`，然后再执行：`./ frpc -c xxx/frpc.ini`。

编辑完配置文件后，应按博客 2 重启 supervisor。

### 输入法

推荐搜狗输入法；因为有人维护！

系统输入法（不推荐）参考这篇[博客](https://blog.csdn.net/wu10188/article/details/86540464)。

- 输入法切换：`win + space`。
- 中英切换：`shift`。
- bug：选中文字会删除文字，很痛苦。

### 视频播放器

- 一般格式推荐 VLC。
- YUV 格式推荐 Vooya。
  - 备选方案：GitHub 下载 YUView.AppImage，赋权限后可以直接使用。

### 科学上网

找个靠谱的机场，会有资源和教程供参考。

Ubuntu 上推荐使用 q2ray 软件。

在使用过程中搞清楚代理、端口、规则等概念，就会用了。
