# PYTHON

- [PYTHON](#python)
  - [数据结构](#数据结构)
  - [输入输出](#输入输出)
  - [画图](#画图)
  - [函数和包](#函数和包)

## 数据结构

<details>
<summary><b>多行字符串</b></summary>

```python3
print("""Hello!
Welcome!
Goodbye!"""
)
```

```bash
Hello!
Welcome!
Goodbye!
```

尽量不要缩进，否则输出也有缩进。

</details>

<details>
<summary><b>字符串format简单方法</b></summary>

应该是3.8的新特性。

```python3
name = 'Ryan'
print(f'My name is {name}.')
```

```bash
My name is Ryan.
```

</details>

<details>
<summary><b>字符串拼接</b></summary>

```python3
a = 'Hello ' + 'World!'
print(a)

b = (
    'Hello '
    'World!'
    )
print(b)
```

```bash
Hello World!
Hello World!
```

注意，第二种写法没有逗号，否则就变成tuple了。

</details>

## 输入输出

<details>
<summary><b>一般文件</b></summary>

```python3
fp = open("xxx.txt", 'w')
fp.write("haha\nhaha")
fp.close()
```

读一行：`a = fp.readline()`

numpy提供了更快的二进制读写方式：
`np.fromfile(fp, dtype=np.uint8, count=block_size)`

</details>

<details>
<summary><b>CSV</b></summary>

一般文件读取方法：

```python3
import csv

csv_path = 'demo.csv'

# read
csv_fp = open(csv_path, 'r', newline='')
reader = csv.reader(csv_fp)
for line_list in reader:
    print(line_list)

# write
csv_fp = open(csv_path, 'w', newline='')
writer = csv.writer(csv_fp)
writer.writerow(['index_vid','psnr_ori','psnr_enh','dpsnr','name_vid'])

csv_fp.close()
```

更智能：

```python3
import pandas as pd

df = pd.read_csv(csv_file)
saved_column = df.column_name  # you can also use df['column_name']
```

</details>

## 画图

[[official]](https://matplotlib.org/tutorials/introductory/pyplot.html)

[[3D plot]](https://blog.csdn.net/u014636245/article/details/82799573)

<details>
<summary><b>基础操作</b></summary>

```python3
import matplotlib.pyplot as plt
plt.plot(result)
plt.title(f'dMSE, QP={qp}')
plt.xlabel('TV')
plt.ylabel('dMSE')
plt.show()
```

</details>

<details>
<summary><b>堆积柱状图</b></summary>

每次`bar`都建立在底层bar之上。

```python3
plt.bar(index_lst, new_y_lst, width=3, bottom=old_y_acc_lst)
```

默认hold，直至`plt.show()`

</details>

## 函数和包

<details>
<summary><b>NUMPY</b></summary>

> random

```python3
np.random.choice(a_list)
```

从列表或迭代器中随机选一个。

> reshape

`resize`没有返回值，`reshape`有。

</details>

<details>
<summary><b>ARGPARSE</b></summary>

> 常规用法

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

> 输入列表

```python3
parser = argparse.ArgumentParser()
parser.add_argument('gpu', metavar='N', type=int, nargs='+')
args = parser.parse_args()
print(args.gpu)

python test.py 0 1 2 3
```

有时可以对参数分组（例如训练集和测试集都有相同含义的参数）：

```python3
group1 = parser.add_argument_group("group 1")
group2 = parser.add_argument_group("group 2")

group1.add_argument("--option1")
group2.add_argument("--option2")
```

</details>

<details>
<summary><b>ASSERT</b></summary>

```python3
assert not op.exists(a_path), "ALREADY EXISTS!"

a = "haha"
b = "hahha"
assert a in b, (f"{a} is not in "
    f"{b}!")
```

</details>

<details>
<summary><b>MULTIPROCESSING</b></summary>

> Pool of Workers

- `apply_async`：支持异步，非阻塞，返回结果后回调。
- `map`：阻塞，直至结果返回。
- `close`：关闭进程池，不再接受新任务。
- `join`：主进程阻塞，等待子进程退出。要在`close`后使用。

```python3
import multiprocessing as mp
import time


def func_demo(proc_id):
    print(f"start {proc_id}")
    time.sleep(3)
    print(f"end {proc_id}")


if __name__ == '__main__':  # windows下要写在里面
    pool = mp.Pool(processes=2)  # 最多2个进程并行
    proc_id_list = list(range(4)) # 0 -> 3
    for proc_id in proc_id_list:
        pool.apply_async(func=func_demo, args=(proc_id, ))
    pool.close()  # 禁止新进程加入
    pool.join()  # 阻塞，等所有子进程结束（再完成后面代码）
```

```bash
start 0
start 1
end 0
end 1
start 2
start 3
end 2
end 3
```

可以看到，同时只有2个进程并行。即当0和1执行后，循环阻塞，直至0结束后，2或3才开始执行。

> 代码记录

曾经在`pool.apply_asygn(func)`外面写`pbar.update()`。

后果就是，pbar速度飞快，然而`func()`却没有执行完。

通过查看htop可知，`apply_sygn(func)`是创建了众多进程，并且不受外部代码影响（不堵塞），直到`pool.close()`。

因此，`pbar.update()`最好放到`callback()`内部。否则进度是虚假的。

```python3
...
callback=lambda x :pbar.update(1)
```

注意得有一个形参x。因为callback必须接收参数，哪怕是无用的。
能放到`func()`里吗？貌似可以，但冲突很严重，速度慢。

> 背景知识

[[进程 vs. 线程]](https://zhuanlan.zhihu.com/p/76343641)

当我们启动程序时，系统中至少启动了一个对应进程。而一个进程可以包含多个线程。
这些线程可以共享进程空间中的内存空间。如果不加以管理，程序容易发生逻辑错误。
因此常用锁或信号量等机制来限制公共资源的使用。

作者开启了python中的多线程，发现单线程和多线程在速度上几乎没有区别。
原因：在python中，同一时刻只有一个线程运行，约束方式即GIL锁。
因此，python的多线程不是并行，而是并发。

![python-1](../imgs/python-1.jpg)

如图，python在工作一段时间（check interval）后，会主动释放GIL，让其他线程也参与工作。
在python3中，该间隔为15ms。

为了sidestep GIL问题，我们可以使用多进程而不是多线程。
由于不同进程是在不同GPU上执行的，因此可实现真正的并行。

[[回调函数]](https://www.zhihu.com/question/19801131)

回调函数（callback）：当func结束时，会调用回调函数；回调函数的参数即func的返回值。
显然，为了实现回调，我们需要将callback函数传递给func。
回调函数使得功能剥离，更灵活。

</details>

<details>
<summary><b>OS</b></summary>

也可以使用Python3自带的最新模块PATHLIB。

> 创建路径

判断路径是否存在，若不存在则创建：

```python3
if not os.exists(ADir):
    os.makedirs(ADir)
```

> 合成路径

```python3
import os.path as op
os.path.join("/home", "usrname")
```

> 提取最高层文件夹名

```python3
os.path.basename("/home/usrname/xxx.yuv").split(".")[0]
```

> 删除路径

```python3
os.removedirs(ADir)  # 只能删除空路径
```

> 获取当前工作路径

```python3
print(os.getcwd())
```

</details>

<details>
<summary><b>PATHLIB</b></summary>

> 和繁杂的`os.path`说拜拜。

```python3
from pathlib import Path

root_path = Path('C:/Files')  # 你没看错，无论系统，都用正斜杠即可！
file_path = root_path / 'file.csv'  # 比op简单多了

file_path.stem  # file
file_path.name  # file.csv
file_path.suffix  # csv
file_path.exists()  # True

a_Path_object.mkdir(parents=True)  # 可以代替makedirs的功能

a_path = Path('/aa/bb/cc')
a_path.name -> 'cc'

str(a_path) -> 转变回正常字符串，可以执行`split`等操作

a_path.rename('/foo')  --> 字符串或Path对象都可以
```

</details>

<details>
<summary><b>SHUTIL</b></summary>

```python3
shutil.rmtree(APath)  # 递归删除文件夹及文件
```

</details>

<details>
<summary><b>TIME</b></summary>

- `time.time()`：返回时间戳

</details>

<details>
<summary><b>TQDM</b></summary>

> 基础用法

```python3
from tqdm import tqdm

for i in tqdm(range(1e3)):
    pass
```

> 简化

```python3
from tqdm import trange

for i in trange(1e3):
    pass
```

> 手动控制更新

```python3
from tqdm import tqdm

with tqdm(total=1e3) as pbar:
    for i in range(1e2):
        pbar.update(10)  # 每次更新，进度+10
```

> 设置文字描述

```python3
from tqdm import tqdm

pbar = tqdm([name1, name2, name3])
for name in pbar:
    pbar.set_description("processing %s" % name)
```

> 进一步设置属性（如宽度和描述）

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

> 关闭对象

如果有多个pbar，一定要在每个pbar完成使命后`pbar.close()`，否则不换行。

</details>
