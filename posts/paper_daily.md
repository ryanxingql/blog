# PAPER DAILY

- [PAPER DAILY](#paper-daily)
  - [Learning Enriched Features for Real Image Restoration and Enhancement](#learning-enriched-features-for-real-image-restoration-and-enhancement)
  - [BBN: Bilateral-Branch Network with Cumulative Learning for Long-Tailed Visual Recognition](#bbn-bilateral-branch-network-with-cumulative-learning-for-long-tailed-visual-recognition)

## Learning Enriched Features for Real Image Restoration and Enhancement

> MIRNet：开源完善；声称是图像恢复的SOTA。
> 注意力、多尺度集大成。
> ECCV 2020
> 20-10-15

标签：图像恢复
标签：注意力

前人工作大多处理全分辨图像，或处理渐进的低分辨率表示。作者认为前者空域建模准确但语义建模不健壮，后者反之。本文希望在网络中保持高分辨率表示，同时从低分辨率表示中获取较好的语义信息。

大致集成了以下模块：多尺度卷积及其信息交互，空域和通道域注意力建模，基于注意力的多尺度特征融合。

经过如此繁杂的处理，作者认为提取的特征是enriched的。在多个image benchmark上达到了SOTA。

网络整体如图1所示，是一个块堆叠结构。每个块内部有两个多尺度残差块，多尺度残差块内部类似RANet结构，即降分辨率得到低分辨率表示，然后与高分辨率表示之间有交互。

![fig](../imgs/pd_201015_1.jpeg)

交互具有选择性，如图2所示，本质就是基于注意力融合。

![fig](../imgs/pd_201015_2.jpeg)

空域和通道域注意力见图3。一般操作。

![fig](../imgs/pd_201015_3.jpeg)

总的来说就是集大成，设计没啥特别的，但效果好（我怀疑速度很慢）。

## BBN: Bilateral-Branch Network with Cumulative Learning for Long-Tailed Visual Recognition

> BBN：长尾分类当年SOTA。
> 分开训练特征提取和分类器。
> CVPR 2020
> 20-10-17

标签：图像分类
标签：长尾分布

首先作者揭示，广泛用于长尾分布的重采样技术，虽然会增强分类器的学习，但在一定程度上会损害特征学习。

之后是一个有趣的实验。作者先用三种方式训练网络，然后冻结主干网络（所谓的特征提取部分），从零重训分类器，得到如图2结果。本文的motivation就出来了。

![fig](../imgs/pd_201017_1.jpeg)

本文就希望同时兼顾二者的训练。

如图3，作者搭建了一个双路网络，称为BBN。在上路，数据是均匀采样的；在下路，数据是重均衡采样的。双路输出的特征通过加权组合，等价于双路的loss加权组合得到最终的loss。作者也将这种策略归为课程学习。

权重$\alpha$是变化的：在初始阶段更重视上路，在后期更重视下路。

具体而言，$\alpha = 1 - \left(\frac{T}{T_{max}}\right)^2$，$T$是epoch数。随着epoch增加，$\alpha$会加速减小。即给初始阶段提供了足够的时间。补充材料图7也说明了这一点，但貌似没有实验。

![fig](../imgs/pd_201017_2.jpeg)

注意特征提取模块的参数是共享的。
