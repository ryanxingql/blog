# FFmpeg

从事音视频，FFmpeg 是必备技能。

我还没有系统学习 FFmpeg，这里只记录琐碎细节。

## 用 libx265 将 PNG 无损压缩为 mkv

```bash
ffmpeg -i ./001/%3d.png -c:v libx265 -x265-params lossless=1 001.mkv
```

要注意，`libx265` 中 `qp = 4` 才是无损压缩。这一点比较奇葩，和 `libx264` 不同。

[[参考]](https://x265.readthedocs.io/en/stable/lossless.html) [[参考]](https://forum.doom9.org/showthread.php?t=175638)

如果重新解压得到 PNG，你可能会发现 PNG 变大了。别慌，这是因为 FFmpeg 默认不压缩，而你的原始 PNG 执行了无损压缩。

[[参考]](https://stackoverflow.com/questions/48114173/why-ffmpeg-png-image-compression-output-file-bigger-than-input-file) [[参考]](https://www.howtogeek.com/203979/is-the-png-format-lossless-since-it-has-a-compression-parameter/)

为了比较两张 PNG 的编码内容是否相同，我们可以利用 FFmpeg 和 md5：

```bash
ffmpeg -loglevel error -i 001.png -f md5 -
```

## 查看视频分辨率、帧数、帧率等信息

通过 FFprobe 可以很方便地查阅上述信息。在 Python 中可以用字典形式存储上述信息：

```python
def _check_video_info_ffprobe(vid_path, ffprobe_path):
    info_ = json.loads(subprocess.check_output(
        f'{ffprobe_path} -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate -of json {vid_path}',
        shell=True))
    width = info_['streams'][0]['width']
    height = info_['streams'][0]['height']

    # https://video.stackexchange.com/questions/20789/ffmpeg-default-output-frame-rate
    # for MP4, ffmpeg defaults to constant-frame rate, where it picks r_frame_rate as the value.
    fr = float(eval(info_['streams'][0]['r_frame_rate']))

    # https://stackoverflow.com/questions/2017843/fetch-frame-count-with-ffmpeg
    nfrms = int(subprocess.check_output(
        f'{ffprobe_path} -v error -select_streams v:0 -count_packets -show_entries stream=nb_read_packets -of csv=p=0 {vid_path}',
        shell=True))

    return width, height, nfrms, fr
```

## 视频转码

转为 YUV420P 格式：

```bash
ffmpeg -i 001.mkv -pix_fmt yuv420p 001_960x540_250.yuv
```

由于这种格式没有任何头文件，因此强烈建议在文件名中记录后续操作所需信息。

## 视频降采样

在操作前，为了避免转码导致的压缩失真，建议先将视频转为纯像素格式 YCbCr。

```bash
ffmpeg -pix_fmt yuv420p -s 960x540 -i 001_960x540_250.yuv -vf scale=480x270:flags=bicubic 001_480x270_250.yuv
```

## 视频分辨率裁剪

在操作前，为了避免转码导致的压缩失真，建议先将视频转为纯像素格式 YCbCr。

```bash
# 默认从中心裁
ffmpeg -pix_fmt yuv420p -s 960x540 -i 001_960x540_250.yuv -vf "crop=960:536" 001_480x270_250.yuv

# 从左上裁
ffmpeg -pix_fmt yuv420p -s 960x540 -i 001_960x540_250.yuv -vf "crop=960:536:0:0" 001_480x270_250.yuv
```

## 用 YCbCr 无损保存 RGB24

[[参考]](https://trac.ffmpeg.org/wiki/Scaling)

必须是 YCbCr 444 10bit。我猜测是因为矩阵操作存在精度损失。
