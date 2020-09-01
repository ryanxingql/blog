# PYTHON

- [PYTHON](#python)
  - [argparse](#argparse)
  - [File IO](#file-io)
  - [numpy](#numpy)
  - [os](#os)
  - [shutil](#shutil)
  - [time](#time)
  - [tqdm](#tqdm)

## argparse

常规用法：

- 设置长+短命名，注意引用时为长命名。
- 设置默认值，使用时可缺省，方便。
- 写一段话，描述参数的含义，方便理解。

```python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-io_v', '--io_val', type=str, \
    default="disk", \
    help="IO backend for validation: (lmdb | disk*)."
    )

opts = parser.parse_args()
print(opts.io_val)

opts_dict = vars(opts)  # 转换成字典，方便log逐行打印
log_fp.write(opts_dict['io_val'] + '\n')
```

有时可以对参数分组（例如训练集和测试集都有相同含义的参数）：

```python3
group1 = parser.add_argument_group("group 1")
group2 = parser.add_argument_group("group 2")

group1.add_argument("--option1")
group2.add_argument("--option2")
```

## File IO

```python3
fp = open("xxx.txt", 'w')
fp.write("haha\nhaha")
fp.close()
```

读一行：`a = fp.readline()`

numpy提供了更快的二进制读写方式：`np.fromfile(fp, dtype=np.uint8, count=block_size)`

## numpy

`resize`没有返回值，`reshape`有。

## os

路径:

```python3
os.path.join("/home", "usrname")

os.path.basename("/home/usrname/xxx.yuv").split(".")[0]

if not os.exists(ADir):
    os.makedirs(ADir)

os.removedirs(ADir)  # 只能删除空路径
```

## shutil

```python3
shutil.rmtree(APath)  # 递归删除文件夹及文件
```

## time

- `time.time()`：返回时间戳


## tqdm

**基础用法**

```python3
from tqdm import tqdm

for i in tqdm(range(1e3)):
    pass
```

**简化**

```python3
from tqdm import trange

for i in trange(1e3):
    pass
```

**手动控制更新**

```python3
from tqdm import tqdm

with tqdm(total=1e3) as pbar:
    for i in range(1e2):
        pbar.update(10)  # 每次更新，进度+10
```

**设置文字描述**

```python3
from tqdm import tqdm

pbar = tqdm([name1, name2, name3])
for name in pbar:
    pbar.set_description("processing %s" % name)
```

**进一步设置属性（如宽度和描述）**

```python3
# 可以避免太宽换行显示
tqdm(alist, ncols=80)

# 可以把eta等去掉，只保留描述，百分比和bar
with tqdm(
    total=60*24, 
    ncols=40, 
    bar_format='{desc}{percentage:.1f}% |{bar}|'
    ) as pbar:
    pbar.update(accum_minute)
```

**关闭对象**

如果有多个pbar，一定要在每个pbar完成使命后`pbar.close()`，否则不换行。
