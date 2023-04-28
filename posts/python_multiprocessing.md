# Python 多进程最佳实践

工作中经常用到多进程。例如，我们要用编译好的 HM 编码器同时编码 100 个视频。如果我们简单写一个 Bash 脚本串行执行 100 条指令，那么同期只有 1 个进程在工作，时间长、CPU 空闲。

## Demo 脚本

Python 提供了内置的 [multiprocessing](https://docs.python.org/3/library/multiprocessing.html) 库来实现多进程。以下是一个 demo 脚本：

```python
import multiprocessing as mp
import time


def func_demo(proc_id):
    print(f"start {proc_id}")
    time.sleep(3)
    print(f"end {proc_id}")


if __name__ == '__main__':
    pool = mp.Pool(processes=2)  # 最多 2 个进程并行
    proc_id_list = list(range(4))  # 0 -> 3
    for proc_id in proc_id_list:
        pool.apply_async(func=func_demo, args=(proc_id, ))  # 异步、非阻塞地调用
        # 函数 func_demo，参数为 proc_id
    pool.close()  # 禁止新进程加入
    pool.join()  # 阻塞，等所有子进程结束（再执行后续代码）
```

输出：

```txt
start 0
start 1
end 0
end 1
start 2
start 3
end 2
end 3
```

可见，同期只有 2 个进程在执行。即当 0、1 执行后，循环阻塞，直至 0 先结束后，2、3 才开始执行。

## 回调函数

以 tqdm 为例，即我们想查看程序进度，获取 ETA（预计结束时间）。此时，我们在 `pool.apply_async` 中加入 `callback` 函数，令其为 tqdm 进度条的更新函数。程序可以修改为：

```python
import multiprocessing as mp
import time
from tqdm import tqdm


def func_demo():
    time.sleep(3)


if __name__ == '__main__':
    pool = mp.Pool(processes=2)  # 最多 2 个进程并行
    pbar = tqdm(total=4, ncols=0)
    for _ in range(4):
        pool.apply_async(
            func=func_demo,
            callback=lambda _: pbar.update())  # 异步、非阻塞地调用函数 func_demo
    pool.close()  # 禁止新进程加入
    pool.join()  # 阻塞，等所有子进程结束（再执行后续代码）
    pbar.close()
```

在上例中，每当 `func_demo` 执行完毕，`callback` 函数就会接收到其返回结果。虽然例中 `func_demo` 没有返回值，但 `callback` 仍然会接收到 `None`；因此 `callback` 设置了一个形参。

输出：

```txt
100% 4/4 [00:06<00:00,  1.50s/it]
```

可见，耗时 6 秒完成了 4 次调用，而每次调用至少需要 3 秒，因此同时至少有 2 个进程在执行。

## 几点注意

- 根据系统情况选择合适的进程池大小；配合 htop 监控运行情况。
- 把主程序写在 `if __name__ == '__main__':` 里，防止被子程序调用。
- 子程序 `func_demo` 尽量不要使用全局变量。即越简洁越好。
- 这里使用的是多进程而不是多线程。可参考[知乎](https://zhuanlan.zhihu.com/p/76343641)。
