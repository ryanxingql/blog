# PAPER DAILY

**Learning Enriched Features for Real Image Restoration and Enhancement**

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

交互具有选择性，如图2所示，本质就是基于注意力融合。

空域和通道域注意力见图3。一般操作。

总的来说就是集大成，设计没啥特别的，但效果好（我怀疑速度很慢）。

**BBN: Bilateral-Branch Network with Cumulative Learning for Long-Tailed Visual Recognition**

> BBN：长尾分类当年SOTA。
> 分开训练特征提取和分类器。
> CVPR 2020
> 20-10-16

标签：图像分类
标签：长尾分布
