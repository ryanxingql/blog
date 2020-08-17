# FFMPEG

- [FFMPEG](#ffmpeg)
  - [基础指令](#基础指令)
  - [常用指令](#常用指令)
    - [y4m2yuv](#y4m2yuv)
    - [yuv2png](#yuv2png)
    - [计算PSNR](#计算psnr)
  - [JPEG2000](#jpeg2000)
  - [H265](#h265)
  - [安装](#安装)


## 基础指令

```bash
ffmpeg [global_options] {[input_file_options] -i input_url} ... {[output_file_options] output_url} ...

ffmpeg -i [输入文件名] [参数选项] -f [格式] [输出文件] 
```

参数选项

- `-i`：设定输入流
- `-s`：设定画面的分辨率，例如`352x278`
- `-y`：输出时覆盖输出目录已存在的同名文件

还有很多很多，参考：[文档](https://ffmpeg.org/ffmpeg.html)

## 常用指令

### y4m2yuv

```bash
ffmpeg.exe -i test.y4m -vsync 0 test.yuv -y
```

### yuv2png

只要前300帧。由于是yuv，指定分辨率。

```bash
ffmpeg -i yuv_path -s 832x480 -vframes 300 -vsync 0 png_path/%4d.png -y
```

### 计算PSNR

逐帧计算两个视频的Y、U、V通道的PSNR，输出到stats_file指定文件。
注意log中帧数从1开始。

```bash
ffmpeg -s 832x480 -i video1.yuv -s 832x480 -i video2.yuv -lavfi psnr="stats_file=psnrlog.log" -f null -
```

## JPEG2000

没成功。用pillow吧。

## H265

[[H265文档]](https://trac.ffmpeg.org/wiki/Encode/H.265)

其中CRF模式需要参考[[H264文档]](https://trac.ffmpeg.org/wiki/Encode/H.264#crf)

```bash
ffmpeg -i input -c:v libx265 -crf 37 -preset medium -tune film -y output.mp4
```

- -c:v: video codec
- -crf: 类似于QP模式，适用于不知道目标码率的情况，推荐。0-51，0为无损。
- -preset：不同模式下，速度不同，质量不同。默认为medium。越慢质量越好。
- -tune：输入类型，例如电影，动画等。为了减小deblocking，根据x264手册，我们选择film输入。
- -y: overwrite output files without asking

## 安装

- 不需要编译，直接下载使用（没有sudo权限时特别方便）
  - [[ref]](https://blog.csdn.net/u013314786/article/details/89682800)
