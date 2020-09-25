# PAPER NOTE

- [PAPER NOTE](#paper-note)

**CBDNet**

- 用TV loss监督噪声图（惩罚纹理，鼓励平滑），迫使其建模平滑的噪声水平预测map。

**DBIQ**

- 已知JPEG是4x4分块，因此块效应一定存在于4x4块之间。
  - 但其他压缩图像，例如HEVC，不是这么回事。

**EDVR**

- 在特征层次上的alignment，其可视化效果与flow-based me+mc的效果差不多。
  - [ ] 难道fusion前的理想状态就是：相邻特征要趋近于当前帧的形态？
    - [[paper]](https://arxiv.org/pdf/2009.07265.pdf)

**MFQE**

- 编码本身hierarchy，因此QE反其道而行之。不同于一般视频，压缩视频的PQF是很有意义的，通常质量较高。
- 加入了MC loss，首先让MC网络收敛。
  - [x] 但在TOFlow一文中也揭示了：MC并非得追求一致，因为存在遮挡等问题。
    - end-to-end training，或改用feature-wise alignment。

**Model-blind**

- 必须fine-tune，否则前几帧训练是完全不够的。
- 前几帧效果肯定差。
- 存在遮挡等情况时，光流补偿无法获取合格的训练对。
- [ ] 多帧输入如何采样，从而抑制过拟合：Learning Model-Blind Temporal Denoisers without Ground Truths

**NASNet**

- 搜索block而不是整个network。
  - [ ] 对于多任务而言，每个block最好不同。

**Noise2Self**

- 唯一的假设：噪声相对独立，而图像内容相关性较强。
  - 其实噪声和图像也有耦合成分。
- 将去噪方法简单分为两类：一类依赖于单一假设，假设不成立则失败；另一类则是数据驱动方法。
- 认为Noise2Noise的测试图像需要被测量很多次（用于训练），而实际情况可能不允许。

**QGCN**

- 把量化图和JPEG图像一起送入网络（图2）。而量化图是JPEG文件本身携带的。
- 所谓的global feature（图3），即对输入图像降采样，然后再提取特征。出发点类似于octave cnn。
- 图像块被随机压缩，压缩系数从1到60随机采样。

**RANet**

- 和MSDNet一样，基于阈值退出。
  - [ ] 比较盲目，需要预先随机设定阈值。

**STDF**

- DCN的offset prediction，joint prediction比pair prediction效果更好！
  - 所谓的joint，就是同时生成多张feature map（在一起），每一部分服务于不同帧的deformable convolution（group size=input channel number）。
  - [ ] 不知道所谓的pair-wise prediction是怎么做的？参数量反而更少了。问问作者。
  - 作者观点：可能是因为R1、2和3互相借鉴，所以效果更好。但该规律不恒成立，去噪、SR等结果都可能不同。

**VESPCN**

- 经典MEMC处理视频。
- 多通道重排，完成超分辨。
