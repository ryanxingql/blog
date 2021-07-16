# Paper Reading

## 图像生成

### Alias-Free Generative Adversarial Networks

[[2021 arXiv]](https://arxiv.org/abs/2106.12423)

问题：作者发现，GAN 生成图像严重依赖于坐标，而不是物体本身。具体而言，coarse feature 仅仅会影响 fine feature 的 presence，而不控制其 position；而 position 更多地与 coordinate 有关。[项目主页](https://nvlabs.github.io/alias-free-gan/)有动态视频说明。作者称之为 “texture sticking”。图 1 具体说明了这一问题：令 latent vector 在某个小邻域移动，然后将得到的 generated images 取平均；结果，生成图像是锐利而非模糊的，说明生成纹理与位置高度相关。

> 作者称之为 aliasing（混淆），我不太理解。可能是参考了[这篇文章](https://arxiv.org/abs/2008.09604)。混淆指的是采样不合理，高频信号受损无法复原。这里可能是想说降采样、升采样不合理，因此引入了位置信息。

目标：让 coarse feature 主导 fine feature 的 position。

分析：引入（泄露）的位置信息主要有两大来源。（1）不合理的升采样（例如简单的双三次），使得升采样图像中有 faint after-images。（2）一些 point-wise 非线性操作，例如 ReLU。

思考：混淆在信号处理理论中是如何解决的呢？从奈奎斯特采样理论出发，要让离散采样和连续表示可等价。再进一步，网络中有太多的 nonequivalent translation，导致混淆的出现。

方法、实验和局限性分析没细看。

## 图像质量评估

[[My PPT Slides]](https://mq1zrs2eey.feishu.cn/file/boxcnRPBZEPNcXEFYzYpomUAEpg)

### The Unreasonable Effectiveness of Deep Features as a Perceptual Metric

[[2018 CVPR]](https://arxiv.org/abs/1801.03924)

用深度学习方法判断两张图的相似度是可行的。提出了 Learned perceptual image patch similarity（LPIPS）指标。

无论是无监督/有监督/自监督学习方法，VGG/AlexNet/SqueezeNet 网络架构，都是可行的。

构建了一个大规模相似度评价数据库，包括传统失真和真实算法失真。

主观测试对象是从 RAISE 和 MIT-Adobe FiveK Dataset 中裁剪出的 64x64 的块共 161k 个；这是避免 semantic 对质量评估的影响。由于网络是全卷积的，因此测试时可以输入更大的图像，性能差不多（根据作者反馈）。

为了防止主观受试者在无法做出判断时强行决策，添加了 JND 实验，含相同图像对和不同图像对。实验结果验证了可靠性。

### The 2018 PIRM Challenge on Perceptual Image Super-resolution

[[2018 ECCVW]](https://openaccess.thecvf.com/content_ECCVW_2018/papers/11133/Blau_2018_PIRM_Challenge_on_Perceptual_Image_Super-resolution_ECCVW_2018_paper.pdf)

综合 NIQE 和 MA，得到 Perception index（PI）指标用于图像感知质量超分辨竞赛。

### GANs Trained by a Two Time-Scale Update Rule Converge to a Local Nash Equilibrium

[[2017 NIPS]](https://arxiv.org/abs/1706.08500)

非主要贡献：提出了 Fréchet inception distance（FID）指标，用来评价 GANs 的生成能力。

### Learning a no-reference quality metric for single-image super-resolution

[[2016 CVIU]](https://www.sciencedirect.com/science/article/abs/pii/S107731421630203X)

在 PCA、DCT、小波域上同时评估超分图像的质量。得到特征以后，通过 regression forest，学习特征与主观评分之间的关系；库是用 180 张图像和 9 个超分算法生成的；共 50 个受试者。

### Making a “Completely Blind” Image Quality Analyzer

[[2012 IEEE SPL]](https://ieeexplore.ieee.org/abstract/document/6353522)

在 BRISQUE 的基础上，作者提出：不需要训练 SVM 拟合与人类主观评分的关系；只需要测量自然图像/失真图像的多维高斯分布之间的距离，即可用来衡量失真图像的失真程度。由此提出了 naturalness image quality evaluator（NIQE）指标。

### Image quality assessment: from error visibility to structural similarity

[[2004 IEEE TIP]](https://ieeexplore.ieee.org/document/1284395)

从三个维度（人眼相对敏感的维度：亮度，对比度，结构信息）刻画待测图像和参考图像之间的相似度。

亮度建模为 patch 均值；对比度建模为 patch 标准差；用一个相似度公式刻画待测 patch 和 参考 patch 的亮度相似度和对比度相似度。

结构信息相似度直接用 patch 之间的相关系数表示。

最后三个相似度取幂相乘，得到总相似度。

操作时，需要对图片滑块操作，每个块计算相似度。

### No-Reference Image Quality Assessment in the Spatial Domain

[[2012 TIP]](https://ieeexplore.ieee.org/document/6272356)

本文提出了一种无参考图像质量评价指标 blind/referenceless image spatial quality evaluator（BRISQUE）。

根据其他文献，图像中的归一化像素值 mean subtracted contrast normalized（MSCN）具有类似高斯分布特性。此外，相邻的 MSCN 之间也具有相关性，大致也呈高斯分布。因此，我们去学习 MSCN 分布及相邻 MSCN 点积分布的高斯参数，一共可获取 36 个可学习参数；利用 SVM 学习这 36 维参数和主观质量评分之间的关系。

本文的假设：自然图像已经具有足够的统计量，可以用来评估图像质量；我们只需要统计这些统计量的偏移量，即可判断失真程度；不需要把图像变换到其他域（例如小波域，频域），也不需要针对特定失真进行设计。

## 提升学习效率

动态网络；课程学习等。

[[My PPT slides]](https://mq1zrs2eey.feishu.cn/file/boxcnEWArytyt2DLq0G5xgCeGRe)

## 多任务学习

[[My PPT slides]](https://mq1zrs2eey.feishu.cn/file/boxcnxSGhbZlvdNxzkUZY4uuOaf)
