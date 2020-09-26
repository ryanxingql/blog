# PAPERS

- [PAPERS](#papers)
  - [图像恢复](#图像恢复)
    - [General](#general)
    - [去噪](#去噪)
    - [去压缩失真](#去压缩失真)
    - [超分辨](#超分辨)
  - [图像分类&动作识别&网络结构](#图像分类动作识别网络结构)
  - [图像质量评估](#图像质量评估)
  - [机器学习&深度学习理论](#机器学习深度学习理论)
  - [NAS](#nas)
  - [视频编码](#视频编码)
    - [视频标准](#视频标准)
  - [图像分割&目标检测](#图像分割目标检测)
  - [图像鉴识](#图像鉴识)
  - [对抗攻击](#对抗攻击)

**原则**

- 分类先尝试往大类放，不合适再放到小类。例如可用于一般图像恢复的去噪方法，将被归为【一般图像恢复】而非【去噪】。而考虑了JPEG特性的恢复方法，只能放在【去压缩失真】。
- 里程碑工作将放在原类别。

## 图像恢复

### General

**建模注意力**

- A-CubeNet
  - 没开源。
  - 在通道、空域和hierarchy特征三个层次建模attention。
  - Attention Cube Network for Image Restoration, ACM MM 2020

- PANet
  - 开源，作者很nice。很慢，但效果不错。
  - 根据coarse-scale attention，指导fine-scale attention，形成一个attention金字塔。
  - 在ResNet的前、中、后加一个attention block。
  - Pyramid Attention Networks for Image Restoration, arXiv 2020

- PFNL
  - 渐进融合+NL。
  - Progressive Fusion Video Super-Resolution Network via Exploiting Non-Local Spatio-Temporal Correlations, ICCV 2019

**可形变卷积**

- STDF
  - 用可形变卷积代替MEMC，完成fusion。
  - 输入7帧全部concat，输入UNet，学习7帧的offset和mask（类似于spatial attention）；7帧、offset和mask一起送入可形变卷积，完成fusion，最后是QE。
  - 用一个UNet单独学习每一帧的offset和mask（即不concat输入学习），效果更差。
    - [ ] 为什么联合优化可以学得更好？值得探究。
  - Spatio-Temporal Deformable Convolution for Compressed Video Quality Enhancement, AAAI 2020

**渐进融合**

- PFNL
  - See above.
- FastDVDnet
  - 无需MEMC，相邻帧两两融合。
  - FastDVDnet: Towards Real-Time Deep Video Denoising Without Flow Estimation, CVPR 2019

**光流**

- TOFlow
  - ME不应趋近GT，而应根据任务不同、遮挡情况不同等自行学习。
  - 此外还提供了Vimeo-90K数据库。
  - Video Enhancement with Task-Oriented Flow, IJCV 2019

**难度自适应**

- Path-Restore
  - 多个不同难度子路径CNN，加一个RL-based path-finder，根据增强难度选择路径。
  - 难度依据是训练时的MSE loss。
  - Path-Restore: Learning Network Path Selection for Image Restoration, arXiv 2019

**数据库**

- TOFlow
  - See above.
- DIV2K
  - 1000张2040x1000 (2k)图像，按800/100/100划分。
  - https://data.vision.ee.ethz.ch/cvl/DIV2K/
  - NTIRE 2017 Challenge on Single Image Super-Resolution: Dataset and Study, CVPRW 2017
- BSD500
  - 500张321x481图像，按200/200/100划分。初衷是用于分割。
  - https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/resources.html
  - Contour Detection and Hierarchical Image Segmentation, TPAMI 2011
- Kodak
  - 24张图像，768x512或512x768。
  - http://r0k.us/graphics/kodak/

### 去噪

**里程碑**

- DnCNN
  - 用CNN去噪的早期工作。
  - 所谓盲：混合训练所有QF的样本。即使这样，也是具有开创意义的；毕竟传统方法可没这么简单。
  - Beyond a Gaussian Denoiser: Residual Learning of Deep CNN for Image Denoising, TIP 2017

**利用附加信息**

- QGCN
  - 把量化图和JPEG图像一起送入网络（图2）。而量化图是JPEG文件本身携带的。
  - 所谓的global feature（图3），即对输入图像降采样，然后再提取特征。出发点类似于octave cnn。
  - 图像块被随机压缩，压缩系数从1到60随机采样。
  - Learning a Single Model with a Wide Range of Quality Factors for JPEG Image Artifacts Removal, TIP 2020
- CBDNet
  - 学习noise map，完成盲去噪（训练过程中noise map的gt就是附加信息）。
  - 噪声图的GT就是高斯方差。训练过程中用TV正则项迫使习得噪声图平滑。
  - Toward Convolutional Blind Denoising of Real Photographs, CVPR 2019

**利用噪声图像的零期望（假设）**

- Model-blind
  - 对视频前几帧执行N2N，fine-tune盲去噪模型。
  - 依赖光流和遮挡mask的精度。否则相邻帧对不齐，N2N学习有问题。
  - 前几帧训练，样本实在太少了。
    - [ ] 多帧输入如何采样，从而抑制过拟合：Learning Model-Blind Temporal Denoisers without Ground Truths
  - Model-Blind Video Denoising via Frame-To-Frame Training, CVPR 2019
- [ ] Noise2Self
  - 唯一的假设：噪声相对独立，而图像内容相关性较强。
  - 其实噪声和图像也有耦合成分。
  - 将去噪方法简单分为两类：一类依赖于单一假设，假设不成立则失败；另一类则是数据驱动方法。
  - 认为Noise2Noise的测试图像需要被测量很多次（用于训练），而实际情况可能不允许。
  - Noise2Self: Blind Denoising by Self-Supervision, ICML 2019
- Noise2Void
  - 遵循N2N原理，但从自身学习期望。
  - 卷积时要挖掉中间点，否则会学成trivial的恒等映射。
  - Noise2Void - Learning Denoising From Single Noisy Images, CVPR 2019
- Noise2Noise
  - 噪声图像的期望是干净的自然图像，而神经网络的学习目标正是自然图像的期望。因此，gt可以用有噪图像，无需干净图像。
  - 文中说input和'gt'的gt可以不同。但应该相同会更好，即用相同gt制作有噪的input和'gt'。
  - Noise2Noise: Learning image restoration without clean data, ICML 2018

### 去压缩失真

**里程碑**

- DCAD
  - 解码端HEVC图像质量增强早期工作。
  - 奠基了很多实验设置，例如测BDBR。
  - A Novel Deep Learning-Based Method of Improving Coding Efficiency from the Decoder-End for HEVC, DCC 2017
- AR-CNN
  - 用CNN去JPEG压缩失真的早期工作。
  - Compression Artifacts Reduction by a Deep Convolutional Network, ICCV 2015

**利用质量波动性（分层编码）**

- MFQEv2
  - 好帧补差帧。编码本身hierarchy，因此QE反其道而行之。不同于一般视频，压缩视频的PQF是很有意义的，通常质量较高。
  - 网络结构优化，参数仅255k，性能突出。
  - 加入了MC loss，首先让MC网络收敛。
    - [x] 但在TOFlow一文中也揭示了：MC并非得追求一致，因为存在遮挡等问题。
      - end-to-end training，或改用feature-wise alignment。
  - MFQE 2.0: A New Approach for Multi-frame Quality Enhancement on Compressed Video, TPAMI 2019
- MFQEv1
  - See MFQEv2.
  - Multi-frame Quality Enhancement for Compressed Video, CVPR 2018

**动态退出**

- RBQE
  - 渐进增强，质量达标则退出。
  - 切比雪夫矩仅适用于检测模糊效应和块效应。
  - Early Exit or Not: Resource-Efficient Blind Quality Enhancement for Compressed Images, ECCV 2020

### 超分辨

**MEMC**

- VESPCN
  - 视频超分辨的早期工作，包含一个当时较好的MEMC模块。
  - 多通道重排，完成超分辨。
  - Real-Time Video Super-Resolution with Spatio-Temporal Networks and Motion Compensation, CVPR 2017

**可形变卷积**

- EDVR
  - 可形变卷积完成feature alignment；通道注意力。
  - 在特征层次上的alignment，其可视化效果与flow-based MEMC的效果差不多。
    - [ ] 难道fusion前的理想状态就是：相邻特征要趋近于当前帧的形态？
      - [[paper]](https://arxiv.org/pdf/2009.07265.pdf)
  - Video Restoration with Enhanced Deformable Convolutional Networks, CVPRW 2019

**注意力**

- EDVR
  - See above.

**难度自适应**

- Difficulty-Aware_SR
  - 分easy和hard支路，分别增强easy和hard图像区域。
  - 预测难度，gt为bicubic PSNR。
  - Difficulty-aware Image Super Resolution via Deep Adaptive Dual-Network, ICME 2019
- MobiSR
  - 根据图像纹理复杂度（TV），用简单或复杂网络SR。TV有阈值。
  - 根据帕累托原则（Pareto front），要劫富济贫，让平均幸福感更高。因为在资源有限的情况下，接济穷人更容易产生幸福感，接济富人几乎没有效果。
  - MobiSR: Efficient On-Device Super-Resolution through Heterogeneous Mobile Processors, MobiCom 2019

## 图像分类&动作识别&网络结构

**课程学习&蒸馏学习**

- Improved_MSDNet
  - 在MSDNet中，靠前分类器的梯度非常大而且不稳定（假定分类器之间iid，方差也增大了，见式3）。
  - 此外还采用课程学习方法：浅层分类器也从深层分类器的预测结果中学习。
  - Improved Techniques for Training Adaptive Deep Networks, ICCV 2019
- Distillation-Based_Training
  - 对提前退出网络采用蒸馏学习。
  - Distillation-Based Training for Multi-Exit Architectures, ICCV 2019

**提前退出**

- Dynamic_Inference
  - 在MSDNet的block-wise提前退出基础上，增加input-wise提前退出。
  - 例如，赛跑视频和静止视频识别难度不同，所需帧数不同。
  - 如图2d，输入帧被打散（0357一组，1246一组）。第一组输入浅层分类器，若不退出，则再经深层分类器（再输入第二组）处理。
  - Dynamic Inference: A New Approach Toward Efficient Video Action Recognition, CVPRW 2019
- RANet
  - 先对图像降采样，若分类足够自信，则提前退出。否则继续处理。
  - 基于一连串设定阈值。
  - Resolution Adaptive Networks for Efficient Inference, CVPR 2019
- MSDNet
  - block-wise提前退出。为了抑制串扰，设置多个层级。
  - 基于一连串设定阈值。
  - Multi-Scale Dense Networks for Resource Efficient Image Classification, ICLR 2018
- SkipNet
  - block-wise提前退出；RL-based退出决策器。
  - SkipNet: Learning Dynamic Routing in Convolutional Networks, ECCV 2018
- [ ] SACT
- ACT
  - RNN中每一个时间步的计算复杂度可以不同。
  - 例如一个句子中，每个单词的重要性不同。
  - 有监督学习，惩罚项加入计算复杂度：每一个时间步的退出不确定性（1-退出置信度）和推导步数。
    - [ ] 没太看懂式18的分类讨论，解决离散问题。可参见SACT。

**增加网络冗余&制造ensembles**

- FractalNet
  - 类分形结构，规律可拓展。
  - FractalNet: Ultra-Deep Neural Networks without Residuals, ICLR 2017

**数据库**

- ImageNet

## 图像质量评估

- DBIQ
  - 一种基于切比雪夫矩的块效应图像质量评估方法。
  - 评估平滑区域的块效应和纹理区域的模糊效应。前者是重点。
  - 已知JPEG是4x4分块，因此块效应一定存在于4x4块之间。
    - 但其他压缩图像，例如HEVC，不是这么回事。
  - No-reference quality assessment of deblocked images, Neurocomputing 2016
- [ ] NIQE

## 机器学习&深度学习理论

- ResNet_Ensembles
  - ResNet高效的原因：通过丰富的residual connection，降低了ResBlock之间的依赖，提升冗余的同时提高容错性。
  - ResNet相当于建立了大量子网络（不同子网络走的路径不同），因此建立了ensembles。
  - 实际执行路径非常短，因此梯度得以保留。
  - Residual Networks Behave Like Ensembles of Relatively Shallow Networks， NIPS 2016

## NAS

- NASNet
  - 在小数据集上学，在大数据集上用。
  - 搜索block而不是整个network。
    - [ ] 对于多任务而言，每个block最好不同。
  - Learning Transferable Architectures for Scalable Image Recognition, CVPR 2018

## 视频编码

### 视频标准

- HEVC_Test18
  - HEVC的18个标准测试序列。
  - Comparison of the Coding Efficiency of Video Coding Standards—Including High Efficiency Video Coding (HEVC), TCSVT 2012

## 图像分割&目标检测

**网络设计**

- UNet++
  - 将U-Net层层嵌套、稠密连接，可模型剪裁。
  - UNet++: A Nested U-Net Architecture for Medical Image Segmentation, DLMIA 2018

## 图像鉴识

**数据库**

- RAISE
  - 8,156张高分辨率无损图像数据库。
  - 初衷是检测是否被JPEG压缩过。
  - RAISE: a raw images dataset for digital image forensics, MMSys 2015

## 对抗攻击

**提前退出**

- RDI-Nets
  - 第一次在对抗攻击网络中加入提前退出机制。
  - 达到3者平衡：高精度，高健壮性，低延迟。前两者通过增大网络达到，后者通过提前退出实现。
  - 给每一个出口设置准出阈值。
  - 训练样本中包含原始样本和对抗样本（加噪声）。
  - Triple Wins: Boosting Accuracy, Robustness and Efficiency Together by Enabling Input-Adaptive Inference, ICLR 2020
