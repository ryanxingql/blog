# UBUNTU

- [UBUNTU](#ubuntu)
  - [系统层](#系统层)
  - [软件层](#软件层)

## 系统层

- **查各用户内存占用**：`ps --no-headers -eo user,rss | awk '{arr[$1]+=$2}; END {for (i in arr) {print i,arr[i]}}' | sort -nk2`。
- **限制用户内存**：参见[此处](https://unix.stackexchange.com/questions/34334/how-to-create-a-user-with-limited-ram-usage)。
  - **快速占用 90% 内存测试**：`stress-ng --vm-bytes $(awk '/MemAvailable/{printf "%d\n", $2 * 0.9;}' < /proc/meminfo)k --vm-keep -m 1`。
- **查各用户的 home 目录占用**：`sudo du -sh /home/*`。
- **查当前目录下的文件信息（包括大小）**：`ll`。
- **查当前文件夹占用空间**：`du -h --max-depth=1`。
- **查各分区占用和剩余空间**：`df -hl`。
- **查内核/操作系统**：`uname -a`。
- **查 CPU 信息**：`cat /proc/cpuinfo`。
- **查 IP**：`ifconfig`。
- **关闭广播**：`mesg n`。

- **安装 DEB 文件**：`sudo dpkg -i <xxx.deb>`。
- **命令行创建文件**：`echo "hello world!" > README.md`。
- **查询软件位置**：`whereis matlab`。

- **脚本开机自启动**：参见[博客](https://blog.csdn.net/weixin_42454034/article/details/106564783)。
- **窗口置顶**：`alt + space`，选择 `always on top`。

- **添加用户**：`sudo adduser <...>`。
- **添加管理员**：`sudo vim /etc/sudoers`。
- **改用户密码**：`passwd <user_name>`。
  - **改为短密码**：必须先 `sudo`。

- **安装微软雅黑字体**：参见[博客](https://www.cnblogs.com/feipeng8848/p/9649089.html)。

<details>
<summary><b>安装</b></summary>
<p>

以 UBUNTU 18.04 LTS 为例。

需求：

1. 在服务器上配置最新的 UBUNTU 稳定版本 18.04 LTS。18.04 比 16.04 好看很多，非常建议。（2020 有 20.04 可选择）
2. 有 3 块硬盘：2 块 4 TB 机械硬盘，1 块 2 TB 固态硬盘。计划将固态硬盘作为主硬盘，其余两块机械硬盘后期挂载使用。
3. 分区只设定根目录、home 目录和 swap 分区。swap 分区和内存大小一样，设为 128 GB。根据服务器使用经验，大家都会把数据往家目录里堆放，因此我们先分配根目录（不需要太大，我们这里给 100 GB）和交换分区（和内存一样大，128 GB），其他所有空间都给家目录。
4. 设置为中文，这样在安装过程和以后遇到错误时，可以看中文，方便一些。

具体流程：

1. 下载 `Ubuntu-18.04.3-desktop-amd64.iso`。
2. 下载 UltraISO，试用即可。
3. 制作启动盘：
   - 打开 UltraISO。
   - 文件 -> 打开 -> ISO 文件。
   - 启动 -> 写入硬盘映像 ，选择硬盘驱动器为备用 U 盘（会被格式化，当心），写入方式 `UBS-HDD+`，最后选择写入。
   - 提示"刻录成功”后，选择返回即可。
4. 将 U 盘插在服务器上，在 BIOS 启动项（开机界面狂按 F12 进入）里选择 `UEFI: Generic Flash Disk xxx`，进入 UBUNTU 引导界面，直接安装（不需要试用）。
5. 选择中文简体、汉语，不连 WIFI，最小安装。
6. 安装类型选择“其他选项”，自己来定义分区。
   - 其中有3块硬盘：`/dev/sda`，`/dev/sdc` 和 `/dev/nvme0n1`，以及它们的分区情况。
   - 把存在的分区全部都“-”掉，即删除（不要随便效仿！）。
   - 选择固态硬盘 `/dev/nvme0n1` 的“空闲”，按“+”添加以下分区。
   - 主分区：102400 MB（100 GB），主分区，空间起始位置，Ext4 日志文件系统，挂载点 `/`。
   - 交换分区：131072 MB（128 GB），逻辑分区，空间起始位置，交换空间。
   - 家目录：剩余所有空间，逻辑分区，空间起始位置，Ext4 日志文件系统，挂载点 `/home`。
   - 安装启动引导器的设备：因为我们在 `/dev/nvme0n1` 磁盘上分区的，因此就选择 `/dev/nvme0n1`。然后点“现在安装”，点“继续”。
   - 注：后期遇到了没有引导项，无法进入 UBUNTU 系统的问题。因此添加一个 boot 分区：分配 1024 MB，逻辑分区，空间起始位置，Ext4 日志文件系统，挂载点 `/boot`。然后上一步就选择在该 boot 分区上安装引导。成功。
7. 选择上海时区。用户名和计算机名字任意，但提醒一点：计算机名字不要太长。因为在 terminal 中，计算机名会出现在 BASH 的每一行命令之前。如果计算机名太长，会导致命令很长。
8. 等待。安装过程有点漫长，可能在 20 分钟左右。

参考[图片教程](https://blog.csdn.net/baidu_36602427/article/details/86548203#commentBox)。

</p>
</details>

<details>
<summary><b>挂载/卸载硬盘</b></summary>
<p>

```bash
sudo mkdir </media/usr/path>  # /home/usr/path 也可以

sudo fdisk -l # 查看磁盘对应位置，假设是 /dev/sdd1
sudo mount /dev/sdd1 </media/usr/path/> # 挂载到指定路径

sudo umount </media/usr/path>  # 卸载
```

记住标识符特别重要，特别是当硬盘较多时。

</p>
</details>

<details>
<summary><b>开机自动挂载硬盘</b></summary>
<p>

在安装系统一节我们提到，我们保留了两块机械硬盘；我们希望开机自动挂载。步骤如下：

1. [磁盘分区并格式化；改为 ext4 格式；作为新硬盘挂载](https://blog.csdn.net/zhengchaooo/article/details/79500116)。
2. [配置开机自动挂载，并改为普通权限](https://blog.csdn.net/ls20121006/article/details/78665718)。

</p>
</details>

<details>
<summary><b>切换工作区</b></summary>
<p>

- `ctrl + alt + shift + 上/下`
- 按 `win` 进入工作区视图，鼠标中键滑动可顺滑查看所有工作区。

</p>
</details>

<details>
<summary><b>软件更新</b></summary>
<p>

```bash
sudo apt-get update && apt-get upgrade
```

补充：

- 强烈建议更新为国内源，参见 [TUNA](https://mirror.tuna.tsinghua.edu.cn/help/ubuntu/)。
- 个人服务器可以执行：`dist-upgrade`。这不仅会升级某些软件，还会卸载一些不需要的软件，比 `upgrade` 更智能。
- 还可以跟一个 `apt-get autoremove`，清理不再需要的依赖。

</p>
</details>

<details>
<summary><b>软链接</b></summary>
<p>

```bash
# 创建软链接：在 fake_path 即可访问 real_path
ln -s <real_path> <fake_path>  # 注意 fake_path 末尾不要带 /；real_path 无所谓

# 删除软链接而不删除文件
rm -rf <fake_path>  # 注意末尾不带 /；否则文件夹没删掉，而是删掉了内部文件
```

</p>
</details>

<details>
<summary><b>UNITY + LIGHTDM</b></summary>
<p>

[【安装】](https://www.linuxbabe.com/ubuntu/install-unity-desktop-environment-ubuntu-20-04)

[【定制】](https://www.jianshu.com/p/1c4430d9084e)

</p>
</details>


## 软件层

- **7Z**：UBUNTU 支持不好，不要用。
- **SUNLOGIN**：比 ANYDESK 好用多了，还免费。参见[安装指南](https://www.jianshu.com/p/289001a00cb1)。

<details>
<summary><b>FRP + SUPERVISOR 进程维持 + SUPERVISOR 开机自启</b></summary>
<p>

参见[博客 1](https://cloud.tencent.com/developer/article/1694829) 和[博客 2](https://blog.csdn.net/yuwu00/article/details/108197283)。

配置可以写在 `frpc.ini` 里，此时 command 比较简单：`./ frpc -c xxx/frpc.ini`。

若提示无此命令，`sudo chmod +x frpc`，然后再执行：`./ frpc -c xxx/frpc.ini`。

编辑完配置文件后，应按博客 2 重启 SUPERVISOR。

</p>
</details>

<details>
<summary><b>Q2RAY</b></summary>
<p>

- 用 SNAP 安装：`sudo snap install qv2ray`
- 手动下载 V2RAY 内核，转移到 `~/snap/qv2ray/2729/`，按要求解压为 `vcore/`。检查核心设置，通过。注意不要 `sudo`！
- 在操作界面中将服务器导入。
- FIREFOX 中设为系统 proxy 即可。
- CHROME 要下载 [SWITCHYOMEGA](https://github.com/FelisCatus/SwitchyOmega/releases)，记得改端口号。
- 系统 network 设置貌似不需要动。如果你选择 Q2RAY 的系统代理 -> 禁用，network proxy 会自动 off；反之，会自动 manual，甚至端口号都设置好了。

参考[教程](https://medium.com/@eleveninstrangerthings/%E5%9C%A8ubuntu%E4%B8%8A%E5%AE%89%E8%A3%85%E5%9B%BE%E5%BD%A2%E5%8C%96v2ray%E5%AE%A2%E6%88%B7%E7%AB%AFqv2ray-d0f690b7c519)。

</p>
</details>

<details>
<summary><b>RAR</b></summary>
<p>

```bash
sudo apt install rar unrar
unrar x rar_name.rar
```

</p>
</details>

<details>
<summary><b>SHARDOWSOCKS</b></summary>
<p>

暂时失效。

- 先买了一个 VULTR 服务器：参考[这里](https://www.vultrblog.com/vultr-ss.html)。
- 其中一键 SS-SERVER 的脚本参考[这里](https://github.com/dlxg/shadowsocks_install)。
- UBUNTU 上安装 SSLOCAL，写 JSON，命令行即可开启：参考这篇[教程](http://codetd.com/article/1790848)。
- 设置里修改 network 协议和端口。
- 注意这是全局的，未考虑分流。

常用指令（可能要 `sudo`，否则会报错）：

```bash
sudo sslocal -c ss.json -d start  # 后端启动，无任何信息。
sudo sslocal -c ss.json -d stop
sudo sslocal -c ss.json  # 前端启动，有日志
sslocal -c xxx.xxx.xxx.xxx -p 2020 -k xxxx -b 127.0.0.1 -l 10808
```

</p>
</details>

<details>
<summary><b>TAR.GZ</b></summary>
<p>

LINUX 常用，压缩率比 ZIP 高。

```bash
# 压缩
tar -zcvf archive_name.tar.gz directory_to_compress

# 解压
tar -zxvf archive_name.tar.gz
tar -zxvf archive_name.tar.gz -C /tmp/extract_here/
```

</p>
</details>

<details>
<summary><b>ZIP</b></summary>
<p>

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

分卷压缩和解压：

```bash
# https://serverfault.com/questions/760337/how-to-zip-files-with-a-size-limit/760341
# -r：对子文件递归
# -s 10m：分卷，最大 10 MB
# archive.zip：目的
# directory：源
zip -r -s 10m archive.zip directory/

# 先合成，再解压
zip -s 0 split.zip --out unsplit.zip
unzip unsplit.zip
```

</p>
</details>

<details>
<summary><b>输入法</b></summary>
<p>

推荐搜狗输入法；因为有人维护！

系统输入法（不推荐）参考这篇[博客](https://blog.csdn.net/wu10188/article/details/86540464)。

- 输入法切换：`win + space`。
- 中英切换：`shift`。
- bug：选中文字会删除文字，很痛苦。

</p>
</details>

<details>
<summary><b>视频播放器</b></summary>
<p>

- 一般格式推荐 VLC。
- YUV 格式推荐 VOOYA。
  - 备选方案：GITHUB 下载 YUView.AppImage，赋权限后可以直接使用。

</p>
</details>
