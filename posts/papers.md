# PAPERS

- [PAPERS](#papers)
  - [Paper List](#paper-list)
    - [一般图像恢复](#一般图像恢复)
    - [去噪](#去噪)
    - [Deformable Convolution](#deformable-convolution)
    - [Distortion Attribution](#distortion-attribution)
    - [Dynamic Inference](#dynamic-inference)
    - [General CNNs](#general-cnns)
    - [Milestone](#milestone)
  - [超分辨](#超分辨)
  - [分类](#分类)
  - [分割和检测](#分割和检测)
  - [识别和理解](#识别和理解)
  - [质量评估](#质量评估)
  - [鉴识（鉴伪）](#鉴识鉴伪)
  - [视频编码标准](#视频编码标准)
  - [Paper Note](#paper-note)

## Paper List

**原则**

- 从宽到窄。例如可用于一般图像恢复的去噪方法，将被归为图像恢复而非去噪。

### 一般图像恢复

**建模注意力**

- A-CubeNet
  - 在通道、空域和hierarchy特征三个层次建模attention。
  - Attention Cube Network for Image Restoration, ACM MM 2020

### 去噪

**利用附加信息**

|Abbr.|Summary|Title|Where|
|:-|:-|:-|:-|
|QGCN|将JPEG本身的量化图一起输入网络|Learning a Single Model with a Wide Range of Quality Factors for JPEG Image Artifacts Removal|TIP 2020|
|CBDNet|学习noise map，完成盲去噪（训练过程中noise map的gt就是附加信息）|Toward Convolutional Blind Denoising of Real Photographs|CVPR 2019|

### Deformable Convolution

|Abbr.|Summary|Title|Where|
|:-|:-|:-|:-|
|**STDF**|用可形变卷积代替MEMC，完成fusion|Spatio-Temporal Deformable Convolution for Compressed Video Quality Enhancement|AAAI 2020|

### Distortion Attribution

|Abbr.|Summary|Title|Where|
|:-|:-|:-|:-|
|**MFQEv2**|好帧补差帧，提前融合|MFQE 2.0: A New Approach for Multi-frame Quality Enhancement on Compressed Video|TPAMI 2019|
|**MFQEv1**|好帧补差帧，渐进融合|Multi-frame Quality Enhancement for Compressed Video|CVPR 2018|

### Dynamic Inference

|Abbr.|Summary|Title|Where|
|:-|:-|:-|:-|
|**RBQE**|渐进增强，质量达标则退出|Early Exit or Not: Resource-Efficient Blind Quality Enhancement for Compressed Images|ECCV 2020|
|**Noise2Noise**|噪声图像的期望是干净图像|Noise2Noise: Learning image restoration without clean data|ICML 2018|

### General CNNs

|Abbr.|Summary|Title|Where|
|:-|:-|:-|:-|
|FastDVDNet|有点像progressive fusion，无需MEMC|FastDVDnet: Towards Real-Time Deep Video Denoising Without Flow Estimation|CVPR 2019|

### Milestone

|Abbr.|Summary|Title|Where|
|:-|:-|:-|:-|
|**DnCNN**|用CNN去噪的早期工作|Beyond a Gaussian Denoiser: Residual Learning of Deep CNN for Image Denoising|TIP 2017|
|**AR-CNN**|用CNN去压缩失真的早期工作|Compression Artifacts Reduction by a Deep Convolutional Network|ICCV 2015|

**去噪**

|Abbr.|Summary|Title|Where|
|:-|:-|:-|:-|
|Model-blind|对视频前几帧执行Noise2Noise，训练盲去噪模型|Model-Blind Video Denoising via Frame-To-Frame Training|CVPR 2019|
|**Noise2Self**||Noise2Self: Blind Denoising by Self-Supervision|ICML 2019|
|Noise2Void|从自身找相似性；遵循N2N原理。卷积时要挖掉中间点，否则会学成trivial的恒等映射|Noise2Void - Learning Denoising From Single Noisy Images|CVPR 2019|
|**Path-Restore**|多个不同难度子路径CNN，加一个path-finder，根据增强难度选择路径。依据是训练时的MSE loss|Path-Restore: Learning Network Path Selection for Image Restoration|arXiv 2019|
|**TOFlow**|ME不应趋近GT，而应根据任务不同、遮挡情况不同等自行学习。此外还提供了Vimeo-90K数据库|Video Enhancement with Task-Oriented Flow|IJCV 2019|
|QE-CNN|提出所谓的I/P帧分离、融合处理。但实际功效是否达到理想设定未验证|Enhancing Quality for HEVC Compressed Videos|TCSVT 2018|
|**DCAD**|解码端图像质量增强早期工作，奠基了很多实验设置，例如测BDBR|A Novel Deep Learning-Based Method of Improving Coding Efficiency from the Decoder-End for HEVC|DCC 2017|
|DIV2K|||CVPRW 2017|


## 超分辨

|Abbr.|Summary|Title|Where|
|:-|:-|:-|:-|
|D3Dnet|||SPL 2020|
|DifficultySR|分easy和hard支路，分别增强easy和hard图像区域；预测难度，gt为bicubic PSNR|Difficulty-aware Image Super Resolution via Deep Adaptive Dual-Network|ICME 2019|
|**EDVR**|可形变卷积完成feature alignment；通道注意力|Video Restoration with Enhanced Deformable Convolutional Networks|CVPRW 2019|
|VESPCN|视频超分辨的早期工作，包含一个当时较好的MEMC模块|Real-Time Video Super-Resolution with Spatio-Temporal Networks and Motion Compensation|CVPR 2017|

## 分类

|Abbr.|Summary|Title|Where|
|:-|:-|:-|:-|
|**RANet**|先对图像降采样，若分类足够自信，则提前退出。否则继续处理|Resolution Adaptive Networks for Efficient Inference|CVPR 2019|
|**MSDNet**|block-wise提前退出。为了抑制串扰，设置多个层级|MULTI-SCALE DENSE NETWORKS FOR RESOURCE EFFICIENT IMAGE CLASSIFICATION|ICLR 2018|
|**SkipNet**|block-wise提前退出以及RL-based退出决策器|SkipNet: Learning Dynamic Routing in Convolutional Networks|ECCV 2018|

## 分割和检测

|Abbr.|Summary|Title|Where|
|:-|:-|:-|:-|
|**UNet++**|将U-Net层层嵌套、稠密连接，可模型剪裁|UNet++: A Nested U-Net Architecture for Medical Image Segmentation|DLMIA 2018|

## 识别和理解

|Abbr.|Summary|Title|Where|
|:-|:-|:-|:-|
|DynamicInference|在MSDNet的block-wise提前退出基础上，增加input-wise提前退出。例如，赛跑视频和静止视频识别难度不同，所需帧数不同|Dynamic Inference: A New Approach Toward Efficient Video Action Recognition|CVPRW 2019|

## 质量评估

|Abbr.|Summary|Title|Where|
|:-|:-|:-|:-|
|DBIQ|一种基于切比雪夫矩的块效应图像质量评估方法|No-reference quality assessment of deblocked images|Neurocomputing 2016|
|LIVE VQA|一个大型库LIVE，组合当时通用的VQA指标进行评价|Study of Subjective and Objective Quality Assessment of Video|TIP 2010|

## 鉴识（鉴伪）

|Abbr.|Summary|Title|Where|
|:-|:-|:-|:-|
|RAISE|8k张高分辨率无损图像数据库|RAISE: a raw images dataset for digital image forensics|MMSys 2015|

## 视频编码标准

|Abbr.|Summary|Title|Where|
|:-|:-|:-|:-|
|**Test18HEVC**|HEVC的18个标准测试序列|Comparison of the Coding Efficiency of Video Coding Standards—Including High Efficiency Video Coding (HEVC)|TCSVT 2012|









## Paper Note

- STDF
  - 输入7帧全部concat，输入UNet，学习7帧的offset和mask（类似于spatial attention）；7帧、offset和mask一起送入可形变卷积，完成fusion，最后是QE。
  - 用一个UNet单独学习每一帧的offset和mask（即不concat输入学习），效果更差。
    - [ ] 联合优化可以学得更好？