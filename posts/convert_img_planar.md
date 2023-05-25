# 图像及 planar 格式转换

HM 等一些软件需要输入 planar 格式文件。所谓 planar 格式，是指将各个通道的像素分开存储。

YUV 就是典型的 planar 格式；对于一个 YUV 视频，第一帧的 Y 通道按行依次存储，然后是第一帧的 U 通道，其次是第一帧的 V 通道，之后是第二帧，后续帧同理。

代码参考：https://github.com/ryanxingql/powerqe/blob/v3/tools/data/convert_img_planar.py
