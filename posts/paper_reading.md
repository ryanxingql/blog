# 论文阅读

## 底层视觉增强

| 标题 | 首发年度 | 解决问题 | 前提条件 | 基础工作 | 关键方法 | 实验设计 | 数据集 | 代码开源 | 实验结果 | 讨论及未来方向 |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
| Early Exit or Not: Resource-Efficient Blind Quality Enhancement for Compressed Images | 2020 | 压缩图像增强 | 不同编码模式的增强可以共享推理结构和特征 | 动态网络 | 动态网络设计，退出质量判决 | | RAISE | [GitHub](https://github.com/RyanXingQL/RBQE) | 节约FLOPS | 用PSNR随网络深度增加的斜率表征增强难度，用QP简单表征以训练；这种对增强难度的衡量及刻画很初浅 |
| MFQE 2.0: A New Approach for Multi-Frame Quality Enhancement on Compressed Video | 2019 | 压缩视频增强 | 相邻帧具有相关性；编码视频存在关键帧 | 视频超分 | 关键帧选择和融合 | | MFQEv2数据集；18个HEVC标准测试序列 | [GitHub](https://github.com/RyanXingQL/MFQEv2.0) | 有效提升非关键帧质量，缓解质量波动 | 只考虑了LDP模式，而LDP的层次化编码比较规律，关键帧节点也规律；IQA是基于NIQE的，和PSNR指标不一致 |
| ESRGAN: Enhanced Super-Resolution Generative Adversarial Networks | 2018 | 图像超分 | | SRGAN | 把对抗loss由判断绝对真伪改为判断相对真伪；组合网络参数而非图像，以实现保真和感知的trade-off；把perceptual loss由激活后改为激活前测量 | | | [GitHub](https://github.com/RyanXingQL/PowerQE) |