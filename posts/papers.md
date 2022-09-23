# 论文阅读

| 年份 | 论文 | 关键词 | 核心贡献 | 图 | 笔记 |
| :- | :- | :- | :- | :- | :- |
| 2022 | Joint Image Compression and Denoising via Latent-Space Scalability | 图像编解码；图像去噪 | 用额外的码流，支持去噪模型 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202209151433281.png) | 简单粗暴 |
| 2022 | Synergistic Self-supervised and Quantization Learning | 对比学习 | 通过对比学习，拉近不同量化后模型表征的距离，从而让习得模型适应量化，维持模型量化后的性能 |  |  |
| 2022 | AI Illustrator: Translating Raw Descriptions into Images by Prompt-based Cross-Modal Generation | 图像生成 | 根据文字生成图像 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202209091303094.png) | 利用CLIP和styleGAN，分别完成文字到图像的特征转换，以及基于图像特征的图像生成 |
| 2022 | Metric Learning based Interactive Modulation for Real-World Super-Resolution | 图像复原 | 交互式图像复原，使得复原强度可控 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202209091024407.png) | 现有的方法：在全监督训练时覆盖一些常见的失真，而对于其他失真就失效了。本文：用非监督方法，学习一个metric space中的非量化失真指标。虽然无监督，但需要定义最极端情况作为anchor；这好比，虽然是NR-IQA，但本质也是有参考的 |
| 2022 | Bringing Old Films Back to Life | 视频增强 | 基于类似BasicVSR的增强框架实现老电影修复 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202208221011981.png) | 貌似没用到三域方法。上色是基于关键帧的方法 |
| 2022 | Optimizing Image Compression via Joint Learning with Denoising | 图像编解码；图像去噪 | 先去噪，再压缩，降低压缩负担 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202209151439763.png) | 分开处理去噪和压缩是欠佳的。去噪力度不好把握，可能会导致过度平滑，丢掉了一些对压缩有益的信息。本文先用干净图像训练压缩器，然后再在有噪图像上finetune。有点失望。这种方法类似于Modeling Lost Information in Lossy Image Compression这篇工作里的蒸馏，让编码器鲁棒 |
| 2022 | Vision Transformer with Deformable Attention | Transformer | DAT：类似显著性，K/V只对重要区域求，任意Q都和这些K/V配对算 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202208221013585.png) | DAT并非万金油；跟在Swin后用效果好，单独用效果差 |
| 2022 | NTIRE 2022 Challenge on Super-Resolution and Quality Enhancement of Compressed Video: Dataset, Methods and Results | 视频复原 | NTIRE赛事成绩官方背书 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202208131930121.png) | 整合了一个LDV v2数据库 |
| 2022 | Progressive Training of A Two-Stage Framework for Video Restoration | 视频复原 | NTIRE比赛论文，数据是真实实验数据 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202208131928338.png) | 主要介绍了两阶段结构和pre-training训练方法 |
| 2022 | Exploring CLIP for Assessing the Look and Feel of Images | 图像质量评估 | 用CLIP来表达图像质量 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202209111829503.png) | 开宗明义：图像质量和人类语言是强耦合的 |
| 2022 | [动态分辨率编码](https://mp.weixin.qq.com/s/Gx8SpGf9HGnVnCdvtth7Fw) | 视频压缩 | 分辨率可以针对内容自适应，从而在保证QoE的同时降低码率需求 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202208131920861.png) | |
| 2022 | ELIC: Efficient Learned Image Compression with Unevenly Grouped Space-Channel Contextual Adaptive Coding | 图像编解码 |  | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202209231115958.png) | [[视频]](https://www.zhihu.com/zvideo/1526166844448321536) |
| 2021 | TANet: Target Attention Network for Video Bit-Depth Enhancement | 视频增强 | 增大视频的色彩深度 |  | |
| 2021 | IICNet: A Generic Framework for Reversible Image Conversion | 图像转换 | 用一个统一的可逆架构完成多种图像转换任务，例如图像隐写、抠图、放缩等 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202209181555733.png) | |
| 2021 | Enhanced Invertible Encoding for Learned Image Compression | 图像编解码 | 用可逆网络来实现特征、图像之间的转换 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202209131009318.png) | 不再关注熵模型，而是关注特征、图像之间的转换。用可逆网络代替传统的可变分自编码器。可逆网络有很多局限性；为此，本文提出了注意力通道压缩层以及特征增强模块，和INN搭配使用。本文对基于深度学习的图像编解码方法review得很好，值得一读 |
| 2021 | CLIP4Caption: CLIP for Video Caption | 视频概述 | 利用基于CLIP预训练的图像特征提取器；因为它和文本高度相关，因此能服务于后续的文本生成 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202209111813464.png) | |
| 2021 | ActionCLIP: A New Paradigm for Video Action Recognition | 视频动作识别 | ActionCLIP：把传统的分类问题，转换为动作、文字匹配问题 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202209111800185.png) | 传统方法：视频到one-hot向量，两个域之间的映射问题。现在的方法：视频到表征，分类到表征，从而在表征上进行匹配；这是三个域 |
| 2021 | Learning Transferable Visual Models From Natural Language Supervision | 预训练 | CLIP：用海量的（文本，图像）对进行预训练，提高视觉模型泛化能力 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202209111750548.png) | |
| 2021 | Blind Image Super-Resolution: A Survey and Beyond | 图像复原 | TPAMI综述 |  | |
| 2021 | Unsupervised Degradation Representation Learning for Blind Super-Resolution | 图像复原 | DASR：用对比学习得到不同噪声强度的表征 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202209091520063.png) | 当自监督训练完成后，模型可以感知未知噪声输入的噪声强度 |
| 2021 | Multi-Stage Progressive Image Restoration | 图像复原 | MPRNet：性能很强的baseline结构 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202208221013219.png) | 整体上是一个可提前退出的多阶段结构。底层阶段用UNet，高层结构用ORSNet。大量使用了CAB。UNet中encoder和skip connections都用CAB处理；升采样则使用bilinear+conv，而不是transposed conv，以避免棋盘效应。CSFF就是add。SAM是学残差，残差是根据该阶段输出图像简单卷积得到的。ORSNet由多个ORB组成，而ORB是CAB的堆叠 |
| 2021 | Learning face image super-resolution through facial semantic attribute transformation and self-attentive structure enhancement | 人脸复原 | 先变换人脸属性，再复原人脸边缘结构 |  |  |
| 2020 | Invertible Image Rescaling | 图像放缩 | 利用可逆网络，同时使用了随机采样技巧降低图像容量 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202209141048995.png) | |
| 2020 | Multi-level Wavelet-based Generative Adversarial Network for Perceptual Quality Enhancement of Compressed Video | 视频复原 | 验证压缩视频主观质量和高频分量最相关，进而增强高频分量 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202209091600286.png) | |
| 2020 | CompressAI: a PyTorch library and evaluation platform for end-to-end compression research | 图像编解码 | CompressAI：基于深度学习的压缩方法框架 |  | |
| 2020 | Modeling Lost Information in Lossy Image Compression | 图像编解码 | 用随机采样代替图像中某个呈高斯分布的变量 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202209132300387.png) | 压缩网络中有量化，导致INN训练不稳定。为解决这个问题，作者同时也引入了比较鲁棒的自编码器网络，通过知识蒸馏，让不稳定的INN靠近自编码器，即产生的y相近。显然这是一种折衷，此时INN就显得多余 |
| 2020 | Spatio-Temporal Deformable Convolution for Compressed Video Quality Enhancement | 视频复原 | STDF：用特征域上的可形变卷积代替传统的MEMC，完成时序对齐 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202208221018409.png) | |
| 2020 | Lossy Image Compression with Normalizing Flows | 图像编解码 | 第一个用normalizing flows做图像编解码，突破自编码器范式 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202209132248522.png) | 低码率下表现不佳 |
| 2020 | Bringing Old Photos Back to Life | 图像增强 | 老照片复原新范式 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202208221014261.png) | 先检测缺损，然后nonlocal避开缺损。每个VAE有3个loss：第一个KL loss让特征分布趋于正态分布；第二个loss惩罚重建像素失真；第三个loss惩罚重建特征失真。用一个监督器和对抗loss来迫使真实和伪造假照片的分布趋于一致 |
| 2020 | Early Exit or Not: Resource-Efficient Blind Quality Enhancement for Compressed Images | 图像复原 | RBQE：不同编码模式的复原可以共享推理结构和特征；真正的盲复原 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202208221014443.png) | 用PSNR随网络深度增加的斜率表征复原难度，用QP简单表征以训练；这种对复原难度的衡量及刻画很初浅。此外，虽然计算复杂度降低了，但时间复杂度上去了；因为使用了可分离卷积 |
| 2020 | Learned Image Compression with Discretized Gaussian Mixture Likelihoods and Attention Modules | 图像编解码 | 用GMM搭建熵模型；在$g_a$和$g_s$中使用注意力机制 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202209181405695.png) | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202209181400486.png) |
| 2020 | A Unified End-to-End Framework for Efficient Deep Image Compression | 图像编解码 | Flickr2W数据集 |  |  |
| 2019 | Video Enhancement with Task-Oriented Flow | 视频复原 | TOFlow：端到端光流 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202209141108771.png) | 受任务目标的制约，此光流并非精确的光流，但却是最有意义的光流。本文还提出了Vimeo-90K视频序列数据集 |
| 2019 | MFQE 2.0: A New Approach for Multi-Frame Quality Enhancement on Compressed Video | 视频复原 | MFQEv2：相邻帧具有相关性；编码视频存在关键帧；先提取视频中的关键帧，然后充分利用关键帧对非关键帧进行质量提升，有效缓和质量波动情况 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202208221015804.png) | 只考虑了LDP模式，其关键帧分布比较规律，因此提取也更容易。此外，IQA采用NIQE，和目标PSNR不一致 |
| 2019 | Path-Restore: Learning Network Path Selection for Image Restoration | 图像复原 | Path-Restore：用一个多路径CNN，处理一张图像内不同纹理强度、不同失真程度的区域；用RL学一个路径决策器 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/20220812170655.png) | 每个dynamic block共享一个path finder，只能通过loss来迫使每个block输入分布一致。性能上和CNN有差距。为了避免棋盘效应，特别提出了Mask模式，即输入图整图而不是块；我猜后续CNN仍然是按块处理，因为被mask为0的区域可以跳过CNN，从而节约计算量；如果按图输入CNN，即使某个区域置零也无法跳过 |
| 2019 | Deep Defocus Map Estimation using Domain Adaptation | 失焦预测 | DMENet：用深度学习预测defocus blur | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202208221015499.png) | 建库：基于深度图像库，采用thin-lens模型和高斯模糊生成defocus图像。domain adaption：使用对抗学习，聚焦真实图像。每个loss都很重要，参见图3 |
| 2018 | Crafting a Toolchain for Image Restoration by Deep Reinforcement Learning | 图像复原 | RL-Restore：用RL选择工具箱的其中一个工具，来复原图像 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202208141608716.png) | 工具箱中的工具可以有不同的复杂度、不同的功能（去噪、去压缩伪影等），因此比较灵活 |
| 2018 | Neural Nearest Neighbors Networks | 图像复原 | N-3 Net：把不可差分的non-local KNN匹配用可差分松弛近似，从而用神经网络端到端训练 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202208131906865.png) | 其实就是对相似块加权，权重类似NCE。比传统的BM3D更高效 |
| 2018 | Joint Autoregressive and Hierarchical Priors for Learned Image Compression | 图像编解码 | 将编码前后的信息，作为context，指导高斯变量的熵编码 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202209221122529.png) |  |
| 2018 | Joint denoising and decompression using CNN regularization | 图像解码；图像去噪 | 在基于小波变换的压缩图像的解码时，考虑图像去噪 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202209151342115.png) | 大致意思：噪声强度和小波系数之间有一定相关性。详细参见：JOINT DENOISING AND DECOMPRESSION: A PATCH-BASED BAYESIAN APPROACH |
| 2018 | Film Grain Synthesis for AV1 Video Codec | 视频压缩 | 影视节目中需要颗粒感，但这种颗粒噪声很难压缩。本文提出一种生成颗粒感的方法 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202209151448163.png) | In many films and photographs, film grain gives a lived-in, weathered, and textured look |
| 2018 | Variational image compression with a scale hyperprior | 图像编解码 | 将熵模型拆解，使得交叉熵预测更精确 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202209151106687.png) | 从factorized到hyper的演化讲得很清楚，值得一读 |
| 2017 | End-to-end Optimized Image Compression | 图像编解码 |  | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202209221003014.png) | 和End-to-end optimization of nonlinear transform codes for perceptual quality异曲同工 |
| 2017 | Combined Internal and External Category-Specific Image Denoising | 图像复原 | 平滑块简单复原，纹理块参考外部图像复原 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/20220813111334.png) | 需要知道噪声强度来判断平滑/纹理（用的是SNR） |
| 2017 | Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks | 图像转换 | CycleGAN：增加逆向监督，稳定非监督图像转换过程 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202209111143261.png) |  |
| 2017 | Density estimation using real NVP | 密度估计 | Real NVP：设计一个学习、采样、推理、评估可追溯的网络来估计密度 |  | |
| 2016 | End-to-end optimization of nonlinear transform codes for perceptual quality | 图像编解码 | 要读懂LIC，得从这篇文章开始 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202209221003014.png) | 将不可差分的量化替换为加性均匀噪声，用以优化 |
| 2016 | Layer Normalization | 规范化 | LN：针对每个sample处理，使得LN不受batch size影响 | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202208221016906.png) | LN是对每一个sample单独进行normalize，使得每个sample分布接近，减小sample之间的差异，但保留了sample内部的差异（例如token差异）。在transformer中，LN不仅针对不同sample处理，还针对不同位点处理，使得可变长sample不受长度差异影响。BN是在C上对NHW做norm，即减小C差异，保留NHW。考虑到CV中卷积核是在C上学，因此C上的NHW分布可控（例如高斯分布），可以让卷积更好学。总结：LN从保留sample内部差异的角度理解，BN从保证NHW一致性的角度理解。可参考[知乎](https://www.zhihu.com/question/487766088/answer/2422936310)和自己的[程序](https://gist.github.com/ryanxingql/f27d93c8fcc06488da9773d76fbd85a9) |
| 2015 | Deep Learning Face Attributes in the Wild | 人脸属性分类 | 判断输入人脸图像是否在微笑、有胡须等 |  | 先执行人脸定位，再执行属性预测。两个子网络分别预训练，再一起训练 |
| 2014 | Nice: Non-linear independent components estimation | 密度估计 |  | | INNs的非线性表征能力通常较差 |
| 2014 | TESTIMAGES: a Large-scale Archive for Testing Visual Devices and Basic Image Processing Algorithms | 图像数据库 | Tecnick数据集：旧版包含100张1200x1200图像 | |  |
| 2014 | Method and apparatus for automatically tuning a parameter of an image enhancement algorithm based on an attribute of an original image | 图像增强 | 判断输入图像的特征（characterist），做相对应的增强 | | 图像的属性（attribute）有很多，例如平均像素强度、像素强度范围、高/低强度区域比例、高/低强度区域细节数量等。我们调整X/Y方向采样率、高斯滤波器参数、alpha blending值等 |

## 工具/教程

| 名称 | 核心贡献 | 图 | 笔记 |
| :- | :- | :- | :- |
| [ImgBot](https://imgbot.net) | 压缩项目中图体积 | | 用户如果等待图加载太久，很可能就离开了 |
| [einops](https://github.com/arogozhnikov/einops) | 一种深度学习算子 | | 我们关注的是变换前后的格式；而代码关注的是变换过程；二者错位让人非常痛苦。可参考[知乎](https://zhuanlan.zhihu.com/p/342675997) |
| [Open MMLab Runner & Hook](https://b23.tv/USoGoJY) | 底层可拓展 |  | val方法为什么不用hook，而是作为runner的一个方法？因为val的过程中也有可能调用其他hook，hook调用hook不合理 |
| [Exploring Invertibility in Image Processing and Restoration](https://www.bilibili.com/video/BV1654y177ew?spm_id_from=333.337.search-card.all.click&vd_source=1b8561cfaa0a59ea70f8de6dc0131790) | 利用近乎可逆的过程 | | ISP，图像编解码，图像恢复 |
| [PCS 2018 – Learned Image Compression](https://www.youtube.com/watch?v=x_q7cZviXkY) | LIC | ![](https://raw.githubusercontent.com/ryanxingql/picgo/main/202209230925043.png) | LIC避免了各组件分别优化导致的块效应、振铃效应等。上世纪的工作（基于变换的编码）主要基于线性变换 |
