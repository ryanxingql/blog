# PAPERS

- [PAPERS](#papers)
  - [RBQE](#rbqe)
    - [关键数据](#关键数据)
    - [关键模组](#关键模组)
    - [对比算法](#对比算法)
  - [MFQEv2](#mfqev2)
    - [关键数据](#关键数据-1)
    - [关键模组](#关键模组-1)
    - [对比算法](#对比算法-1)

## RBQE

> Early Exit Or Not: Resource-Efficient Blind Quality Enhancement for Compressed Images, ECCV 2020

### 关键数据

- RAISE
  - 8k张高分辨率无损图像数据库。
  - RAISE: a raw images dataset for digital image forensics, MMSys 2015

### 关键模组

- UNet++
  - U-Net的层层嵌套、稠密连接版，可用于模型剪裁。
  - 我们将其改造为多输出网络。
  - UNet++: A Nested U-Net Architecture for Medical Image Segmentation, DLMIA 2018
- DBIQ
  - 一种基于切比雪夫矩的块效应图像质量评估方法。
  - 我们将超参数优化，并予以代码实现。
  - No-reference quality assessment of deblocked images, Neurocomputing 2016

### 对比算法

- CBDNet
  - 一种盲去噪方法。通过建模noise map，来完成盲去噪。
  - 基于U-Net和TV loss。
  - Toward Convolutional Blind Denoising of Real Photographs, CVPR 2019
- QE-CNN
  - 提出所谓的I/P帧分离、融合处理。但实际功效是否达到理想设定未验证。
  - 基础CNN。
  - Enhancing Quality for HEVC Compressed Videos, TCSVT 2018
- DCAD
  - 解码端质量增强的早期工作，奠基了很多实验设置，例如BDBR。
  - 基础CNN，较深，效果在对比的图像（单帧）方法中较好。
  - A novel deep learning-based method of improving coding efficiency from the decoder-end for HEVC, DCC 2017
- DnCNN
  - 用CNN去噪的早期工作。
  - 基础CNN，较深，效果尚可。
  - Beyond a Gaussian Denoiser: Residual Learning of Deep CNN for Image Denoising, TIP 2017

## MFQEv2

> MFQE 2.0: A New Approach for Multi-frame Quality Enhancement on Compressed Video, TPAMI 2019

### 关键数据

- HEVC的18个标准测试序列
  - Comparison of the Coding Efficiency of Video Coding Standards—Including High Efficiency Video Coding (HEVC), TCSVT 2012
- JCT-VC等提供的开源视频序列。

### 关键模组

- VESPCN
  - 视频超分辨的早期工作，包含一个当时较好的ME + MC模块。
  - 我们借鉴了该模块，并增加了一个未下采样分支。
  - Real-Time Video Super-Resolution with Spatio-Temporal Networks and Motion Compensation, CVPR 2017
- LIVE VQA数据库使用的质量评价方法
  - 提供了一个VQA大型数据库LIVE，并集成了当时通用的客观VQA指标，结合主观实验来评估VQA方法。
  - 我们用来生成36维的质量评估向量。
  - Study of Subjective and Objective Quality Assessment of Video, TIP 2010
- 还部分参考了BiLSTM，DenseNet和BN，但不关键。

### 对比算法

- MFQEv1
  - 好帧补偿差帧。
  - 解码端多帧质量增强早期工作。
  - Multi-frame Quality Enhancement for Compressed Video, CVPR 2018
- QE-CNN
  - 提出所谓的I/P帧分离、融合处理。但实际功效是否达到理想设定未验证。
  - 基础CNN。
  - Enhancing Quality for HEVC Compressed Videos, TCSVT 2018
- DCAD
  - 解码端质量增强的早期工作，奠基了很多实验设置，例如BDBR。
  - 基础CNN，较深，效果在对比的图像（单帧）方法中最佳。
  - A Novel Deep Learning-Based Method of Improving Coding Efficiency from the Decoder-End for HEVC, DCC 2017
- Li et al.
  - 用CNN去块效应的早期工作。
  - 基础CNN。
  - An efficient deep convolutional neural networks model for compressed image deblocking, ICME 2017
- DnCNN
  - 用CNN去噪的早期工作。
  - 基础CNN，较深，效果尚可。
  - Beyond a Gaussian Denoiser: Residual Learning of Deep CNN for Image Denoising, TIP 2017
- AR-CNN
  - 用CNN去压缩失真的早期工作。
  - 基础CNN，基于SRCNN。
  - Compression Artifacts Reduction by a Deep Convolutional Network, ICCV 2015
