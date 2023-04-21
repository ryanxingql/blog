# 图像及 planar 格式转换

HM 等一些软件需要输入 planar 格式文件。所谓 planar 格式，是指将各个通道的像素分开存储。YUV 就是典型的 planar 格式；对于一个 YUV 视频，第一帧的 Y 通道按行依次存储，然后是第一帧的 U 通道，其次是第一帧的 V 通道，之后是第二帧，后续帧同理。

以下为图像、planar 格式转换函数及其测试代码：

```python
import cv2
import numpy as np


def write_planar(img, planar_path):
    """
    img: list of (h, w) array; each list item represents a channel.
    """
    planar_file = open(planar_path, 'wb')
    for cha in img:
        h, w = cha.shape
        for ih in range(h):
            for iw in range(w):
                planar_file.write(cha[ih, iw])
    planar_file.close()


def read_planar(planar_path, fmt=((1080, 1920), (1080, 1920), (1080, 1920))):
    """
    fmt: tuple of (h, w) tuple; each tuple item represents a channel.

    https://numpy.org/doc/stable/reference/generated/numpy.fromfile.html
    """
    planar_file = np.fromfile(planar_path, dtype=np.uint8)
    img = []
    accum = 0
    for res in fmt:
        h, w = res
        cha = planar_file[accum:(accum + h * w)].reshape(h, w)
        img.append(cha)
        accum += h * w
    return img


if __name__ == '__main__':
    img_path = 'data/div2k/valid/gt/0801.png'
    planar_path = './tmp/0801.yuv'
    restored_img_path = './tmp/0801_restored.png'

    # PNG -> YCbCr420 planar
    bgr = cv2.imread(img_path)
    h, w = bgr.shape[:2]
    ycrcb444 = cv2.cvtColor(bgr, cv2.COLOR_BGR2YCrCb)
    ycbcr420 = []
    ycbcr420.append(ycrcb444[..., 0])
    ycbcr420.append(
        cv2.resize(
            ycrcb444[..., 2], (w // 2, h // 2),
            interpolation=cv2.INTER_AREA))  # note: (dx, dy)
    ycbcr420.append(
        cv2.resize(
            ycrcb444[..., 1], (w // 2, h // 2),
            interpolation=cv2.INTER_AREA))  # note: (dx, dy)
    write_planar(ycbcr420, planar_path)

    # YCbCr420 planar -> PNG
    ycbcr420_read = read_planar(planar_path,
                                ((h, w), (h // 2, w // 2), (h // 2, w // 2)))
    ycrcb444_restored = np.empty((h, w, 3), np.uint8)
    ycrcb444_restored[..., 0] = ycbcr420_read[0]
    ycrcb444_restored[..., 1] = cv2.resize(
        ycbcr420_read[2], (w, h),
        interpolation=cv2.INTER_CUBIC)  # note: (dx, dy)
    ycrcb444_restored[..., 2] = cv2.resize(
        ycbcr420_read[1], (w, h),
        interpolation=cv2.INTER_CUBIC)  # note: (dx, dy)
    bgr_restored = cv2.cvtColor(ycrcb444_restored, cv2.COLOR_YCrCb2BGR)
    # cv2.imwrite(restored_img_path, bgr_restored)

    print(cv2.PSNR(ycbcr420[0], ycbcr420_read[0]))  # Y-PSNR
    print(cv2.PSNR(ycbcr420[1], ycbcr420_read[1]))  # Cb-PSNR
    print(cv2.PSNR(ycbcr420[2], ycbcr420_read[2]))  # Cr-PSNR
    print(cv2.PSNR(ycrcb444_restored, ycrcb444))
    print(cv2.PSNR(bgr_restored, bgr))
```

输出结果：

```txt
361.20199909921956
361.20199909921956
361.20199909921956
49.974684359896585
45.25883084118979
```

在上例中，我们对 DIV2K 数据集的 0801.png 进行测试，结果转换前后的 BGR-PSNR 为 45 dB。
