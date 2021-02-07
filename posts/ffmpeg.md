# FFMPEG

- [FFMPEG](#ffmpeg)

<details>
<summary><b>安装</b></summary>

参考[博客](https://blog.csdn.net/u013314786/article/details/89682800)。

不需要编译，直接下载使用（没有 sudo 权限时特别方便）

</details>

<details>
<summary><b>基础指令</b></summary>

```bash
ffmpeg [global_options] {[input_file_options] -i input_url} ... {[output_file_options] output_url} ...

ffmpeg -i [输入文件名] [参数选项] -f [格式] [输出文件]
```

参数选项

- `-i`：设定输入流
- `-s`：设定画面的分辨率，例如`352x278`
- `-y`：输出时覆盖输出目录已存在的同名文件

还有很多很多，参考[官方文档](https://ffmpeg.org/ffmpeg.html)。

</details>

<details>
<summary><b>Y4M to YUV</b></summary>

```bash
ffmpeg.exe -i test.y4m -vsync 0 test.yuv -y
```

</details>

<details>
<summary><b>YUV to PNG</b></summary>

YUV 格式需要指定分辨率。假设只要前 300 帧。

```bash
ffmpeg -i yuv_path -s 832x480 -vframes 300 -vsync 0 png_path/%4d.png -y
```

</details>

<details>
<summary><b>计算 PSNR</b></summary>

逐帧计算两个视频的 Y、U、V 通道的 PSNR，输出到 `stats_file` 指定文件。
注意 log 中帧数从 1 开始。

```bash
ffmpeg -s 832x480 -i video1.yuv -s 832x480 -i video2.yuv -lavfi psnr="stats_file=psnrlog.log" -f null -
```

</details>

<details>
<summary><b>H265</b></summary>

参考 [H265 文档](https://trac.ffmpeg.org/wiki/Encode/H.265)。其中 CRF 模式需要参考 [H264 文档](https://trac.ffmpeg.org/wiki/Encode/H.264#crf)。

```bash
ffmpeg -i input -c:v libx265 -crf 37 -preset medium -tune film -y output.mp4
```

- `-c:v`: video codec
- `-crf`: 类似于 CQP 模式，适用于不知道目标码率的情况，推荐。0--51，0 为无损。
- `-preset`：不同模式下，速度不同，质量不同。默认为 medium。越慢质量越好。
- `-tune`：输入类型，例如电影，动画等。为了减小 deblocking，根据 X264 手册，我们选择 film 输入。
- `-y`: overwrite output files without asking.

</details>
