# PAPERS

- [PAPERS](#papers)
  - [可视化数据恢复](#可视化数据恢复)
    - [应用CNNs](#应用cnns)
    - [数据库](#数据库)
    - [应用注意力](#应用注意力)
    - [应用可形变卷积](#应用可形变卷积)
    - [多帧融合](#多帧融合)
    - [节能加速](#节能加速)
    - [利用附加信息](#利用附加信息)
    - [考虑图像特性](#考虑图像特性)
    - [建模高频细节](#建模高频细节)
  - [视频编码](#视频编码)
    - [标准](#标准)
  - [图像质量评估](#图像质量评估)
  - [图像识别](#图像识别)
    - [对长尾分布的处理](#对长尾分布的处理)
    - [应用注意力](#应用注意力-1)
    - [应用课程学习&蒸馏学习](#应用课程学习蒸馏学习)
    - [节能加速](#节能加速-1)
    - [数据库](#数据库-1)
    - [应用CNNs](#应用cnns-1)
  - [高效CNNs结构设计及探究](#高效cnns结构设计及探究)
    - [改进卷积核](#改进卷积核)
    - [改进连接方式](#改进连接方式)
    - [节能加速](#节能加速-2)
    - [NAS](#nas)
  - [学习理论](#学习理论)
    - [多任务](#多任务)
    - [自监督学习](#自监督学习)
  - [NLP](#nlp)
    - [建模注意力](#建模注意力)

## 可视化数据恢复

包括：去噪，去压缩失真，超分辨等底层视觉任务。

### 应用CNNs

- [ ] DeepGenerativePrior
  - 基于DIP启发，用GANs的生成器实现DIP原理，同时用GANs的监督器进行监督。此外，生成器的参数需要适当fine-tune。
  - 注意仍然是无监督的。判别器和生成器都一起预训练好的。本文将生成器给样本之间的距离作为损失函数。
  - https://www.zhihu.com/column/mmlab-ai

- [ ] DeepImagePrior
  - CNNs本身即具有压缩数据、再解码数据的功能，因此能渐进地完成降噪。注意，该CNNs不需要训练，而是随机初始化的。需要迭代的是输入的随机向量。
  - 无监督地完成了去噪、修复等任务。

- [x] DnCNN
  - 用CNN去噪的早期工作。
  - 所谓盲：混合训练所有QF的样本。即使这样，也是具有开创意义的；毕竟传统方法可没这么简单。
  - Beyond a Gaussian Denoiser: Residual Learning of Deep CNN for Image Denoising, TIP 2017

- [x] DCAD
  - 解码端HEVC图像质量增强早期工作。
  - 奠基了很多实验设置，例如测BDBR。
  - A Novel Deep Learning-Based Method of Improving Coding Efficiency from the Decoder-End for HEVC, DCC 2017

- [x] AR-CNN
  - 用CNN去JPEG压缩失真的早期工作。
  - Compression Artifacts Reduction by a Deep Convolutional Network, ICCV 2015

- [x] SRCNN
  - 用CNN SR的早期工作。
  - 说明：稀疏编码可以表示为卷积，后者更灵活，训练e2e。
  - Image Super-Resolution Using Deep Convolutional Networks, TPAMI 2015

### 数据库

- [x] TOFlow

- [x] DIV2K
  - 1000张2040x1000 (2k)图像，按800/100/100划分。
  - https://data.vision.ee.ethz.ch/cvl/DIV2K/
  - NTIRE 2017 Challenge on Single Image Super-Resolution: Dataset and Study, CVPRW 2017

- [x] BSD500
  - 500张321x481图像，按200/200/100划分。初衷是用于分割。
  - https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/resources.html
  - Contour Detection and Hierarchical Image Segmentation, TPAMI 2011

- [x] Kodak
  - 24张图像，768x512或512x768。
  - http://r0k.us/graphics/kodak/

### 应用注意力

- [x] PAN
  - 比channel attention、spatial attention更进一步：pixel attention。本质上是让不同通道的spatial attention独立。
  - 参数量只有272K，是AIM2020某SR赛道冠军。
  - Efficient Image Super-Resolution
Using Pixel Attention, ECCVW 2020

- [x] A-CubeNet
  - 没开源。
  - 在通道、空域和hierarchy特征三个层次建模attention。
  - Attention Cube Network for Image Restoration, ACM MM 2020

- [x] PANet
  - 开源，作者很nice。很慢，但效果不错。
  - 根据coarse-scale attention，指导fine-scale attention，形成一个attention金字塔。
  - 在ResNet的前、中、后加一个attention block。
  - Pyramid Attention Networks for Image Restoration, arXiv 2020

- [x] PFNL
  - 渐进融合+NL。
  - Progressive Fusion Video Super-Resolution Network via Exploiting Non-Local Spatio-Temporal Correlations, ICCV 2019

- [x] EDVR
  - 可形变卷积完成feature alignment；通道注意力。
  - 在特征层次上的alignment，其可视化效果与flow-based MEMC的效果差不多。
    - [ ] 难道fusion前的理想状态就是：相邻特征要趋近于当前帧的形态？
      - [[paper]](https://arxiv.org/pdf/2009.07265.pdf)
  - Video Restoration with Enhanced Deformable Convolutional Networks, CVPRW 2019

### 应用可形变卷积

- [x] STDF
  - 用可形变卷积代替MEMC，完成fusion。
  - 输入7帧全部concat，输入UNet，学习7帧的offset和mask（类似于spatial attention）；7帧、offset和mask一起送入可形变卷积，完成fusion，最后是QE。
  - 用一个UNet单独学习每一帧的offset和mask（即不concat输入学习），效果更差。
    - [ ] 为什么联合优化可以学得更好？值得探究。
  - Spatio-Temporal Deformable Convolution for Compressed Video Quality Enhancement, AAAI 2020

- [x] EDVR

### 多帧融合

- [x] PFNL

- [x] FastDVDnet
  - 无需MEMC，相邻帧两两融合。
  - FastDVDnet: Towards Real-Time Deep Video Denoising Without Flow Estimation, CVPR 2019

- [x] TOFlow
  - ME不应趋近GT，而应根据任务不同、遮挡情况不同等自行学习。
  - 此外还提供了Vimeo-90K数据库。
  - Video Enhancement with Task-Oriented Flow, IJCV 2019

- [x] VESPCN
  - 视频超分辨的早期工作，包含一个当时较好的MEMC模块。
  - 多通道重排，完成超分辨。
  - Real-Time Video Super-Resolution with Spatio-Temporal Networks and Motion Compensation, CVPR 2017

### 节能加速

- [x] RBQE
  - 渐进增强，质量达标则退出。
  - 切比雪夫矩仅适用于检测模糊效应和块效应。
  - Early Exit or Not: Resource-Efficient Blind Quality Enhancement for Compressed Images, ECCV 2020

- [x] Path-Restore
  - 多个不同难度子路径CNN，加一个RL-based path-finder，根据增强难度选择路径。
  - 难度依据是训练时的MSE loss。
  - Path-Restore: Learning Network Path Selection for Image Restoration, arXiv 2019

- [x] DifficultyAwareSR
  - 分easy和hard支路，分别增强easy和hard图像区域。
  - 预测难度，gt为bicubic PSNR。
  - Difficulty-aware Image Super Resolution via Deep Adaptive Dual-Network, ICME 2019

- [x] MobiSR
  - 根据图像纹理复杂度（TV），用简单或复杂网络SR。TV有阈值。
  - 根据帕累托原则（Pareto front），要劫富济贫，让平均幸福感更高。因为在资源有限的情况下，接济穷人更容易产生幸福感，接济富人几乎没有效果。
  - MobiSR: Efficient On-Device Super-Resolution through Heterogeneous Mobile Processors, MobiCom 2019

### 利用附加信息

- [x] QGCN
  - 把量化图和JPEG图像一起送入网络（图2）。而量化图是JPEG文件本身携带的。
  - 所谓的global feature（图3），即对输入图像降采样，然后再提取特征。出发点类似于octave cnn。
  - 图像块被随机压缩，压缩系数从1到60随机采样。
  - Learning a Single Model with a Wide Range of Quality Factors for JPEG Image Artifacts Removal, TIP 2020

- [x] CBDNet
  - 学习noise map，完成盲去噪（训练过程中noise map的gt就是附加信息）。
  - 噪声图的GT就是高斯方差。训练过程中用TV正则项迫使习得噪声图平滑。
  - Toward Convolutional Blind Denoising of Real Photographs, CVPR 2019

### 考虑图像特性

**特殊噪声的零期望**

- [x] ModelBlindN2N
  - 对视频前几帧执行N2N，fine-tune盲去噪模型。
  - 依赖光流和遮挡mask的精度。否则相邻帧对不齐，N2N学习有问题。
  - 前几帧训练，样本实在太少了。
    - [ ] 多帧输入如何采样，从而抑制过拟合：Learning Model-Blind Temporal Denoisers without Ground Truths
  - Model-Blind Video Denoising via Frame-To-Frame Training, CVPR 2019

- [x] Noise2Self
  - N2N需要让同一GT产生不同LQ来配对训练。N2S提出用自己x2配对即可，几乎不会导致恒等映射。
  - 关键是式1和第四章证明。
  - 没太看明白，和N2V很像，但要求更严格，有理论保障。参见[[ref]](https://arxiv.org/pdf/2006.09450.pdf)。
  - Noise2Self: Blind Denoising by Self-Supervision, ICML 2019

- [x] Noise2Void
  - 遵循N2N原理，但从自身学习期望。
  - 卷积时要挖掉中间点，否则会学成trivial的恒等映射。
  - Noise2Void - Learning Denoising From Single Noisy Images, CVPR 2019

- [x] Noise2Noise
  - 噪声图像的期望是干净的自然图像，而神经网络的学习目标正是自然图像的期望。因此，gt可以用有噪图像，无需干净图像。
  - 文中说input和'gt'的gt可以不同。但应该相同会更好，即用相同gt制作有噪的input和'gt'。
  - Noise2Noise: Learning image restoration without clean data, ICML 2018

**分层编码视频的质量波动性**

- [x] MFQEv2
  - 好帧补差帧。编码本身hierarchy，因此QE反其道而行之。不同于一般视频，压缩视频的PQF是很有意义的，通常质量较高。
  - 网络结构优化，参数仅255k，性能突出。
  - 加入了MC loss，首先让MC网络收敛。
    - [x] 但在TOFlow一文中也揭示了：MC并非得追求一致，因为存在遮挡等问题。
      - end-to-end training，或改用feature-wise alignment。
  - MFQE 2.0: A New Approach for Multi-frame Quality Enhancement on Compressed Video, TPAMI 2019

- [x] MFQEv1
  - See MFQEv2.
  - Multi-frame Quality Enhancement for Compressed Video, CVPR 2018

### 建模高频细节

- [x] IRN
  - 如何保留/建模传输过程中要丢弃的信息？
  - 在图像downsampling时，仅保留低频细节。高频细节被INN映射至一个case-agnostic的高斯分布及LR，映射方式记录在IRN内。LR的GT为HR的bicubic下采样。
  - 其实LR->HR和GAN很像，也是加上一个随机向量。但IRN让互逆过程联合，使得downsampling更稳定。可逆性是IRN的特点。
  - 注意，在一般的LQ->HQ过程中，输入的fy是量化后的图像，需要反量化后才是IRN学习的对象。因此网络末端还处理了不可差分的量化梯度传播。
  - 用于其他互逆过程，例如去噪？可以考虑，让网络学习HQ->LQ可能是有好处的。但作者在GH issue中说，IRN在SR中表现一般，因为参数量实在太少。IRN主要特点还是可逆。
  - Invertible Image Rescaling, ECCV 2020

## 视频编码

### 标准

- [x] HEVCTest18
  - HEVC的18个标准测试序列。
  - Comparison of the Coding Efficiency of Video Coding Standards—Including High Efficiency Video Coding (HEVC), TCSVT 2012

## 图像质量评估

- [x] DBIQ
  - 一种基于切比雪夫矩的块效应图像质量评估方法。
  - 评估平滑区域的块效应和纹理区域的模糊效应。前者是重点。
  - 已知JPEG是4x4分块，因此块效应一定存在于4x4块之间。
    - 但其他压缩图像，例如HEVC，不是这么回事。
  - No-reference quality assessment of deblocked images, Neurocomputing 2016

- [ ] NIQE

## 图像识别

包括：图像分类，动作识别，目标检测等中高层视觉任务。

### 对长尾分布的处理

- [ ] De-confound-TDE
  - 在训练时学习对头部类别的倾斜度，在测试时予以消除。
  - 2020的长尾SOTA。
  - Long-tailed classification by keeping the good and removing the bad momentum causal effect, NIPS 2020

- [ ] VC R-CNN
  - 学习一个字典，消除confounder。
  - Visual commonsense r-cnn, CVPR 2020

### 应用注意力

- [ ] VIT 
  - 将图像切成patch，每个patch线性变换以后，直接输入transformer。
  - 文中说当数据库较小时，表现和ResNet相近；当数据库增大时，表现很好。
  - 非常消耗资源，一般人玩不起。
  - An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale, ICLR 2021 under review

### 应用课程学习&蒸馏学习

- [x] ImprovedMSDNet
  - 在MSDNet中，靠前分类器的梯度非常大而且不稳定（假定分类器之间iid，方差也增大了，见式3）。
  - 此外还采用课程学习方法：浅层分类器也从深层分类器的预测结果中学习。
  - Improved Techniques for Training Adaptive Deep Networks, ICCV 2019

- [x] DistillationMultiExit
  - 对提前退出网络采用蒸馏学习。
  - Distillation-Based Training for Multi-Exit Architectures, ICCV 2019

### 节能加速

- [x] RANet
  - 先对图像降采样，若分类足够自信，则提前退出。否则继续处理。
  - 基于一连串设定阈值。
  - Resolution Adaptive Networks for Efficient Inference, CVPR 2019

### 数据库

- [x] RAISE
  - 8,156张高分辨率无损图像数据库。
  - 初衷是检测是否被JPEG压缩过。
  - RAISE: a raw images dataset for digital image forensics, MMSys 2015

- [ ] ImageNet

### 应用CNNs

- [ ] AlexNet
  - 62.4M参数。normalization，dropout和数据扩增都用来防止过拟合。

## 高效CNNs结构设计及探究

### 改进卷积核

- [ ] 3DConv

- [ ] DCN

- [ ] GoogLeNet
  - 不同于加深，该网络加宽，且使用multi-scale卷积核。
  - 一共4条支路：1x1卷积，1x1+3x3卷积，1x1+5x5卷积，3x3+1x1卷积，最后concat。

- [ ] VGG
  - 打破传统大卷积核、大步长惯例，使用3x3小卷积核和1x1小步长，特征更精干，训练更简单。

### 改进连接方式

- [ ] DenseNet
  - 增加冗余性，提升健壮性。

- [x] UNet++
  - 将U-Net层层嵌套、稠密连接，可模型剪裁。
  - UNet++: A Nested U-Net Architecture for Medical Image Segmentation, DLMIA 2018

- [x] FractalNet
  - 类分形结构提供连接辅路，规律可拓展。
  - FractalNet: Ultra-Deep Neural Networks without Residuals, ICLR 2017

- [ ] U-Net

- [ ] FCN

- [ ] ResNet
  - VGG已经证明越深越好，而ResNet通过残差结构实现更深的网络。
  - [x] ResNetEnsembles
    - ResNet高效的原因：通过丰富的residual connection，降低了ResBlock之间的依赖，提升冗余的同时提高容错性。
    - ResNet相当于建立了大量子网络（不同子网络走的路径不同），因此建立了ensembles。
    - 实际执行路径非常短，因此梯度得以保留。
    - Residual Networks Behave Like Ensembles of Relatively Shallow Networks, NIPS 2016

### 节能加速

- [x] RDI-Nets
  - 第一次在对抗攻击网络中加入提前退出机制。
  - 达到3者平衡：高精度，高健壮性，低延迟。前两者通过增大网络达到，后者通过提前退出实现。
  - 给每一个出口设置准出阈值。
  - 训练样本中包含原始样本和对抗样本（加噪声）。
  - Triple Wins: Boosting Accuracy, Robustness and Efficiency Together by Enabling Input-Adaptive Inference, ICLR 2020

- [x] DynamicInference
  - 在MSDNet的block-wise提前退出基础上，增加input-wise提前退出。
  - 例如，赛跑视频和静止视频识别难度不同，所需帧数不同。
  - 如图2d，输入帧被打散（0357一组，1246一组）。第一组输入浅层分类器，若不退出，则再经深层分类器（再输入第二组）处理。
  - Dynamic Inference: A New Approach Toward Efficient Video Action Recognition, CVPRW 2019

- [x] MSDNet
  - block-wise提前退出。为了抑制串扰，设置多个层级。
  - 基于一连串设定阈值。
  - Multi-Scale Dense Networks for Resource Efficient Image Classification, ICLR 2018

- [x] SkipNet
  - block-wise提前退出；RL-based退出决策器。
  - SkipNet: Learning Dynamic Routing in Convolutional Networks, ECCV 2018

- [x] SACT
  - 在特征图上也设置推理暂停。
  - Spatially Adaptive Computation Time for Residual Networks, CVPR 2017

- [x] ACT
  - RNN中每一个时间步的计算复杂度可以不同。
  - 例如一个句子中，每个单词的重要性不同。
  - 有监督学习，惩罚项加入计算复杂度：每一个时间步的退出不确定性（1-退出置信度）和推导步数。
    - [ ] 没太看懂式18的分类讨论，解决离散问题。可参见SACT。

### NAS

**定义**

- 一个嵌套的优化问题：内层是面向训练loss最小化的权重最优化，外层是面向验证集loss最小化的结构最优化。
- 大白话：比较各种不同的结构。光有结构不行，还得已知每个结构的最优参数组合，才能输出各自的最优结构进行对比。找参数的过程理论上也需要验证集？但麻烦，差不多在训练集上拟合就完了。然后在验证集上测试得到该结构下的精度结果。

- [ ] GHN
  - 传统NAS慢，是因为内层优化（见定义）耗时耗力：对于每一个结构，寻找其最优参数组合都是一个漫长的迭代过程。而本文希望学习一个hypernetwork，本质是一个参数化方程估计，用来**一步生成某结构下的较优参数**，无需迭代搜索最优参数。该hypernetwork与SGD高度相关，因此预测又快又准。
  - 本文还提出用计算图表征网络拓扑结构，从而完成结构采样。结合上述二者，该工作被称为Graph HyperNetwork。
  - 为了实现NAS，作者随机采样结构，相应较优网络权重可一步产生，进一步得到验证集精度；然后比较不同结构的精度即可。
  - 还能完成不可差分的anytime prediction网络架构搜索。

- [x] NASNet
  - 在小数据集上学，在大数据集上用。
  - 搜索block而不是整个network。
    - [ ] 对于多任务而言，每个block最好不同。
  - Learning Transferable Architectures for Scalable Image Recognition, CVPR 2018

- [ ] SMASH
  - 将HyperNetwork用于NAS，可生成部分权重。
  - Smash: one-shot model architecture search through hypernetworks, ICLR 2018

- [ ] HyperNetwork
  - 为其他网络生成权重。
  - Hypernetworks, ICLR 2017

## 学习理论

### 多任务

- [ ] MTL

- [ ] Taxonomy

### 自监督学习

[[知乎1]](https://zhuanlan.zhihu.com/p/150224914) [[知乎2]](https://zhuanlan.zhihu.com/p/108625273)

常用做法：

1. 构造pretext (proxy) task，训练特征提取器。一般也是自监督任务。
2. 迁移训练好的特征提取器，完成目标自监督任务。

常用评估方法：

- 评估特征提取器：将提取的特征用于high-level任务（称为downstream task），再执行评估。

难点：

- pretext task的设置
  - pretext task和target task差异较大，容易产生domain gap，即特征不适用。
  - 再进一步，低熵（高确定性）的先验在迁移时更有意义，见知乎1链接。稳定可靠的先验？
  - 还可以训练特征空间，使得不同图像经过特征变换后距离尽可能大，同一图像的不同变换距离尽可能小。这种contrastive方法比generative方法更接近自监督问题本质，更简单（不要求重建，只要求能根据关键特征辨别），参见知乎2链接。
- 评估无通用做法。

## NLP

### 建模注意力

- [ ] Transformer
  - 用FC+attention取代CNN和RNN。不是随便取代，而是有精妙的设计，还需要编码绝对、相对位置信息。
  - 放弃了RNN的时序建模关系；放弃了CNN的inductive bias，例如平移不变性和局部性。
  - https://zhuanlan.zhihu.com/p/48508221
  - Attention is all you need, NIPS 2017
