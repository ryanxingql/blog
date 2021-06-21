# PYTHON

多看手册，少参考博客和书籍。

## ARGPARSE

[[手册]](https://docs.python.org/3/library/argparse.html?highlight=argparse#module-argparse)

常规用法：

- 设置长 + 短命名，注意引用时为长命名。
- 设置默认值，使用时可缺省，方便。
- 写一段话，描述参数的含义，方便理解。

```python3
parser = argparse.ArgumentParser()
parser.add_argument('-io_v', '--io_val', type=str, \
    default="disk", \
    help="IO backend for validation: (lmdb | disk*)."
    )

opts = parser.parse_args()
print(opts.io_val)

opts_dict = vars(opts)  # 转换成字典，方便 log 逐行打印
log_fo.write(opts_dict['io_val'] + '\n')
```

也可以输入列表：

```python
parser = argparse.ArgumentParser()
parser.add_argument('gpu', metavar='N', type=int, nargs='+')
args = parser.parse_args()
print(args.gpu)

python test.py 0 1 2 3
```

有时可以对参数分组（例如训练集和测试集都有相同含义的参数）：

```python
group1 = parser.add_argument_group("group 1")
group2 = parser.add_argument_group("group 2")

group1.add_argument("--option1")
group2.add_argument("--option2")
```

## ASSERT statement

[[手册]](https://docs.python.org/3/reference/simple_stmts.html#assert)

```python3
# 最基础用法
assert expression1

# 进阶用法
assert not op.exists(a_path), "ALREADY EXISTS!"

a = "haha"
b = "hahha"
assert a in b, (f"{a} is not in "
    f"{b}!")
```

## Built-in

[[手册]](https://docs.python.org/3/library/functions.html?highlight=built%20open#built-in-functions)

### 字符串

#### 查找子串

```python3
str.find(sub[, start[, end]])
```

- 从 `str` 中查找子串 `sub` 的**位置**；返回第一个子串的初始索引；若没找到，返回 `-1`。
- 如果只是想判断是否存在，用 `in` 即可。

#### 多行字符串

最简单的办法是用 `\n`。

此外还有三双引号写法。

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

不要缩进，否则输出也有缩进。

#### 拼接

```python
a = 'Hello ' + 'World!'
print(a)

b = (
    'Hello '  # 不要加逗号，否则就变成 tuple 了
    'World!'
    )
print(b)
```

```bash
Hello World!
Hello World!
```

#### Format

应该是 3.8 的新特性。

```python
name = 'Ryan'
print(f'My name is {name}.')
```

```bash
My name is Ryan.
```

### 读写

#### `open`

[[参数]](https://docs.python.org/3/library/functions.html?highlight=built%20open#open)

如果打不开，会报错。

#### `readline`

```python3
with open('somefile') as openfileobject:
    for line in openfileobject:
        do_something()

# 当 EOF 时，会一直返回 ''，即 False；注意空行是 \n，不是 ''
while True:
    line = fo.readline()
    if not line:
        break
```

## MATPLOTLIB

### 堆积柱状图

每次 `bar` 建立在 `old_bar` 之上。

```python3
plt.bar(x, height, width=0.8, bottom=old_bar, align='center')
```

## MULTIPROCESSING

### 基操

```python3
def func_demo(proc_id):
    print(f"start {proc_id}")
    time.sleep(3)
    print(f"end {proc_id}")

if __name__ == '__main__':  # WINDOWS 下要写在里面
    pool = mp.Pool(processes=2)  # 最多 2 个进程并行
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

- `apply_async`：支持异步，非阻塞，返回结果后回调。
- `map`：阻塞，直至结果返回。
- `close`：关闭进程池，不再接受新任务。
- `join`：主进程阻塞，等待子进程退出。要在 `close` 后使用。

可以看到，同时只有 2 个进程并行。即当 0 和 1 执行后，循环阻塞，直至 0 结束后，2 或 3 才开始执行。

### 回调函数

曾经在 `pool.apply_asygn(func)` 下一行写 `pbar.update()`。后果是，pbar 速度飞快，然而 `func()` 却没有执行完。通过查看 htop 可知，`apply_sygn(func)` 是创建了众多进程，并且不受外部代码影响（不堵塞），直到 `pool.close()`。因此，因写一个 `callback` 函数，并将 `pbar.update()` 放到 `callback` 内部。

```python
callback=lambda x :pbar.update(1)
```

注意得有一个形参 x 。因为 `callback` 必须接收参数，哪怕是无用的。能放到 `func()` 里吗？貌似可以，但冲突很严重，速度慢。

### 背景知识

进程 vs. 线程，参考[知乎](https://zhuanlan.zhihu.com/p/76343641)。

当我们启动程序时，系统中至少启动了一个对应进程。而一个进程可以包含多个线程。
这些线程可以共享进程空间中的内存空间。如果不加以管理，程序容易发生逻辑错误。
因此常用锁或信号量等机制来限制公共资源的使用。

作者开启了 PYTHON 中的多线程，发现单线程和多线程在速度上几乎没有区别。
原因：在 PYTHON 中，同一时刻只有一个线程运行，约束方式即 GIL 锁。
因此，PYTHON 的多线程不是并行，而是并发。

![python-1](../imgs/python_1.jpg)

如图，PYTHON 在工作一段时间（check interval）后，会主动释放 GIL，让其他线程也参与工作。
在 PYTHON 中，该间隔为 15 ms。

为了sidestep GIL 问题，我们可以使用多进程而不是多线程。
由于不同进程是在不同 GPU 上执行的，因此可实现真正的并行。

回调函数参考[知乎](https://www.zhihu.com/question/19801131)。

## NUMPY

### 读写

```python3
np.fromfile(file, dtype=float, count=-1, sep='', offset=0)
```

- 读取文本或二进制文件 `file`，生成数组。
- `count` 即数组大小。
- `sep` 即 item 在 `file` 中的分隔符。对二进制文件，`sep` 为空即可。

### RANDOM

- `np.random.choice(a, size=None, replace=True, p=None)`：从一个列表中随机采样，生成一个新列表。
  - 如果 `a` 是一个数，那么列表就是 `np.arange(a)`。
  - `replace=True`，即为放回采样；否则为不放回采样。

### `reshape` vs. `resize`

`np.resize()` 会返回一个新 array（数据不共享），而 `ndarray.resize()` 是 in-place 操作。

`b = np.reshape(a, newshape)` 返回的是一个形状不同、但指向相同数据（危险）的数组。`reshape` 也有 in-place 操作。

## PATHLIB

[[手册]](https://docs.python.org/3/library/pathlib.html#module-pathlib)

输入 `str()` 即可转换为普通字符串。

### 判断路径是否存在

```python3
src_path.exists()  # True or False
```

### 创建文件夹

创建文件不用多说，类似写文件就行。

```python3
src_path.mkdir(parents=False, exist_ok=False)
```

`parents` 默认开，即不存在的父路径也会创建；`exist_ok` 默认关，即已存在会报错。

### 合成路径

```python3
tar_path = src_path / 'subfolder' / 'hello.py'
```

### 路径绝对化

如果路径中含有相对路径，例如 `.` 和 `..`，可以用以下函数整理：

```python3
src_path.resolve()
```

### 遍历路径

```python3
a = src_path.iterdir()
next(a)
```

- 生成一个 generator。
- 不包含 `.` 和 `..`。
- 随机顺序。
- 如果创建 generator 后，删除了某个路径，那么 generator 是否还包含该路径是未知的。

### 路径分解

```python3
file_path = Path('C:/Files/file.csv')
file_path.stem  # file
file_path.name  # file.csv
file_path.suffix  # csv

a_path = Path('/aa/bb/cc')
a_path.name # 'cc'
```

### 路径重命名

```python3
src_path.rename(tar_path)  # src_path不会变，但打不开
```

`target` 可以是字符串，可以是 `Path` 对象；如果真是一个文件，那么会替换原文件。

### 获取当前工作路径

```python3
pathlib.Path.cwd()
```

在哪执行 PYTHON，就会显示哪里的路径。例如，在 `/a/b` 执行 `python c/d.py`，会显示 `/a/b` 而不是 `/a/b/c`。

进一步，如果想获取当前文件的绝对路径：

```python3
pathlib.Path(__file__).resolve()
```

进一步，如果想获取当前文件所在文件夹的绝对路径：

```python3
pathlib.Path(__file__).resolve().parent  # resolve不可少，否则输出.
```

### 删除空文件夹

```python3
src_path.rmdir()
```

如果文件夹非空，参见 SHUTIL 库。

### 删除文件或软链接

```python3
src_path.unlink(missing_ok=False)
```

`missing_ok` 默认关，即如果不存在，会报错。

### IO

```python3
fo_path = pathlib.Path('demo.txt')
content = fo_path.open().read()
```

## PANDAS

[[官方手册]](https://pandas.pydata.org/docs/reference/index.html)

### CSV

#### 读

使用 `read_csv` 函数，将 CSV 文件内容读入并转换为 DataFrame 格式。默认为 `,` 分隔。

- 可以跳过某些行：`iqa_data = pd.read_csv(csv_path, skiprows=range(4))  # 跳过前四行`。

#### 写

[[`to_csv`]](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html)

- 不要序号列（推荐）：`index=False`。
- 不要抬头行（不推荐）：`header=False`。
- 自定义顺序：`cols=[header1, header2]`。
- 追加列（左侧）：先读再一起写。不能追加，追加模式是追加行。

    ```python3
    try:
        df = pd.read_csv(logger)
        df['mean_value'] = mean_value_lst
    except:
        df = pd.DataFrame(dict(mean_value=mean_value_lst))
    ```

## SHUTIL

这是一个高级文件操作函数。

### 删除非空文件夹

```python3
shutil.rmtree(src_dir)
```

把整个路径树都删了，即递归操作。路径不能是软链接。

## TQDM

```python3
from tqdm import tqdm  # 别搞错了哦

# 基础用法
for i in tqdm(range(1e3)):
    pass

# 简化的基础用法
for i in trange(1e3):
    pass

# 手动控制更新
with tqdm(total=1e3) as pbar:
    for i in range(1e2):
        pbar.update(10)  # 每次更新，进度 + 10

# 或这样

pbar = tqdm(total=1e3)
for i in range(1e2):
    pbar.update()
pbar.close()  # 最好在每个 pbar 完成使命后关闭；否则不换行。

# 设置文字描述
pbar = tqdm([name1, name2, name3])
for name in pbar:
    pbar.set_description("processing %s" % name)

# 可以进一步编辑属性
# 可以把 eta 等去掉，只保留描述，百分比和 bar
with tqdm(
    total=60*24,
    ncols=40,  # 可以避免太宽导致的换行显示
    bar_format='{desc}{percentage:.1f}% |{bar}|'
    ) as pbar:
    pbar.update(accum_minute)
```
