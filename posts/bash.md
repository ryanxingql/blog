# Bash

Bash 做一些快速操作，例如文件复制、文件对比等，特别方便；我们不需要额外写一个 Python 脚本。并且在 Mac 和 Linux 上都能快速方便地执行。

我还没有系统学习 Bash，这里只记录琐碎细节。

双循环，通过共享索引实现：

```bash
list1="001 002 003 004 005 006 007 008 009 010 011 012 013 014 015"
list2="250 300 300 250 600 300 600 600 250 300 600 600 300 300 300"
vidnames=($list1)
vidfrms=($list2)

for ivid in `seq 1 15`
do
echo ${vidnames[$ivid-1]} ${vidfrms[$ivid-1]}
for idx in `seq -f '%03g' 1 ${vidfrms[$ivid-1]}`
do
  diff ../work_dirs/track1/results_final_mkv_unzip/${vidnames[$ivid-1]}/f$idx.png ../work_dirs/track1/results_final/${vidnames[$ivid-1]}/f$idx.png
done
done
```

注意，有些脚本需要解析 array，这个功能 sh 没有，bash 才有。需要这么执行脚本：

```bash
chmod +x <bash-name>.sh
./<bash-name>.sh
```

[[参考]](https://unix.stackexchange.com/a/253900)

索引格式化：

```bash
for idx in `seq -f '%03g' 1 218`
do
diff /dir1/${idx}.png /dir2/${idx}.png
done
```

写一行就行，特别方便：

```bash
for idx in `seq -f '%03g' 1 218`; do diff /dir1/${idx}.png /dir2/${idx}.png; done
```

索引内运算：

```bash
for idx in `seq -f '%03g' 1 300`; do echo 001-960x536-570-30/f00`expr $idx + 11`.png ; done
```
