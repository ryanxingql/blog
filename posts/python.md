# PYTHON

- [PYTHON](#python)
  - [文件读写](#文件读写)
  - [`os`](#os)
  - [`shutil`](#shutil)
  - [`numpy`](#numpy)
  - [`tqdm`](#tqdm)
  - [`time`](#time)

## 文件读写

```Python
fp = open("xxx.txt", 'w')
fp.write("haha\nhaha")
fp.close()
```

读一行：`a = fp.readline()`

## `os`

路径:

```Python
os.path.join("/home", "usrname")

os.path.basename("/home/usrname/xxx.yuv").split(".")[0]

if not os.exists(ADir):
    os.makedirs(ADir)

os.removedirs(ADir)  # 只能删除空路径
```

## `shutil`

```Python
shutil.rmtree(APath)  # 递归删除文件夹及文件
```

## `numpy`

`resize`没有返回值，`reshape`有。

## `tqdm`

基础用法

```Python
from tqdm import tqdm

for i in tqdm(range(1e3)):
    pass
```

简化

```Python
from tqdm import trange

for i in trange(1e3):
    pass
```

手动控制更新

```Python
from tqdm import tqdm

with tqdm(total=1e3) as pbar:
    for i in range(1e2):
        pbar.update(10)  # 每次更新，进度+10
```

设置文字描述

```Python
from tqdm import tqdm

pbar = tqdm([name1, name2, name3])
for name in pbar:
    pbar.set_description("processing %s" % name)
```

设置`pbar`属性，如宽度

```Python
tqdm(alist, ncols=80)
```

可以避免太宽换行显示。

如果有多个pbar，一定要在每个pbar完成使命后`pbar.close()`，否则不换行。

## `time`

- `time.time()`：返回时间戳
