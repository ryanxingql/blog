# PYTHON

- [PYTHON](#python)
  - [文件读写](#文件读写)
  - [`os`](#os)
  - [`shutil`](#shutil)
  - [`numpy`](#numpy)
  - [`tqdm`](#tqdm)
  - [`time`](#time)
  - [utils](#utils)
    - [`yuv_import`](#yuv_import)
    - [`y_import`](#y_import)
    - [`cal_psnr`](#cal_psnr)

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

## utils

### `yuv_import`

```Python
import numpy as np

def yuv_import(video_path, startfrm, nfs, height_frame=0,
        width_frame=0, opt_bar=False, opt_clear=False):
    """ryanxing 200520
    import Y U V channels from a yuv video.

    nfs: num of frames that you need.
    startfrm: start from 0.

    return: Y, U, V, each with (nfs, height, width), [0, 255], uint8
        if startfrm excesses the file len, return [] & no error.
    """
    fp = open(video_path, 'rb')  # 0101...bytes

    # retrieve resolution info from video path
    if height_frame == 0:
        res = video_path.split("-")[2].split("_")[0]
        width_frame = int(res.split("x")[0])
        height_frame = int(res.split("x")[1])

    d0 = height_frame // 2
    d1 = width_frame // 2
    y_size = height_frame * width_frame
    u_size = d0 * d1
    v_size = d0 * d1

    # target at startfrm
    blk_size = y_size + u_size + v_size
    fp.seek(blk_size * startfrm, 0)

    # init
    y_batch = []
    u_batch = []
    v_batch = []

    # extract
    for ite_frame in range(nfs):

        if ite_frame == 0:
            tmp_c = fp.read(1)
            if tmp_c == b'':  # startfrm > the last frame
                return [], [], []
            fp.seek(-1, 1)  # offset=-1, start from the present position

        y_frame = [ord(fp.read(1)) for i in range(y_size)]  # bytes -> ascii
        y_frame = np.array(y_frame, dtype=np.uint8).reshape((height_frame, width_frame))
        y_batch.append(y_frame)

        u_frame = [ord(fp.read(1)) for i in range(u_size)]
        u_frame = np.array(u_frame, dtype=np.uint8).reshape((d0, d1))
        u_batch.append(u_frame)

        v_frame = [ord(fp.read(1)) for i in range(v_size)]
        v_frame = np.array(v_frame, dtype=np.uint8).reshape((d0, d1))
        v_batch.append(v_frame)

        if opt_bar:
            print("\r<%d, %d>" % (ite_frame, nfs - 1), end="", flush=True)
    if opt_clear:
        print("\r" + 20 * " ", end="\r", flush=True)
        
    fp.close()

    y_batch = np.array(y_batch)
    u_batch = np.array(u_batch)
    v_batch = np.array(v_batch)
    return y_batch, u_batch, v_batch
```

### `y_import`

```Python
import numpy as np

def y_import(video_path, height_frame, width_frame, nfs,
        startfrm, opt_bar=False, opt_clear=False):
    """
    import Y channel from a yuv 420p video.
    startfrm: start from 0
    return: y_batch, (nfs * height * width), dtype=uint8
    """
    fp_data = open(video_path, 'rb')

    y_size = height_frame * width_frame
    u_size = height_frame // 2 * (width_frame // 2)
    v_size = u_size

    # target at startfrm
    blk_size = y_size + u_size + v_size
    fp_data.seek(blk_size * startfrm, 0)

    # extract
    y_batch = []
    for ite_frame in range(nfs):
        
        y_frame = [ord(fp_data.read(1)) for k in range(y_size)]
        y_frame = np.array(y_frame, dtype=np.uint8).reshape((height_frame, width_frame))
        fp_data.read(u_size + v_size)  # skip u and v
        y_batch.append(y_frame)

        if opt_bar:
            print("\r<%d, %d>" % (ite_frame, nfs - 1), end="", flush=True)
    if opt_clear:
        print("\r" + 20 * " ", end="\r", flush=True)

    fp_data.close()
    
    y_batch = np.array(y_batch)
    return y_batch
```

### `cal_psnr`

```Python
import numpy as np
import math

def cal_psnr(img1, img2, data_range=1.0):
    """
    calculate psnr of two imgs
    
    img1, img2: (C H W), [0, data_range]
    
    return ave of psnrs of all channels], np.float32
    """
    assert (len(img1.shape) == 3), "len(img1.shape) != 3!"
    assert (img1.shape == img2.shape), "img1.shape != img2.shape!"
    img1, img2 = _as_floats(img1, img2) # necessary!!!
    mse_channels = [cal_mse(img1[i], img2[i]) for i in range(img1.shape[0])]
    if min(mse_channels) == 0:
        return float('inf')
    psnr_channels = [10 * math.log10(float(data_range**2) / mse) for mse in mse_channels]
    return np.mean(psnr_channels, dtype=np.float32)


def cal_mse(img1, img2):
    """
    calculate mse (mean squared error) of two imgs.
    
    img1, img2: (H W)
    
    return mse, np.float32
    """
    assert (len(img1.shape) == 2), "len(img1.shape) != 2!"
    assert (img1.shape == img2.shape), "img1.shape != img2.shape!"
    img1, img2 = _as_floats(img1, img2) # necessary!!!
    # default to average flattened array. so no need to reshape into 1D array
    return np.mean((img1 - img2)**2, dtype=np.float32)


def _as_floats(img1, img2):
    """
    promote im1, im2 to nearest appropriate floating point precision.
    """
    float_type = np.result_type(img1.dtype, img2.dtype, np.float32)
    img1 = np.asarray(img1, dtype=float_type)
    img2 = np.asarray(img2, dtype=float_type)
    return img1, img2
```
