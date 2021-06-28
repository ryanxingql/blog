# PAPER

## 图像生成

### Alias-Free Generative Adversarial Networks

[[2021 arXiv]](https://arxiv.org/abs/2106.12423)

问题：作者发现，GAN 生成图像严重依赖于坐标，而不是物体本身。具体而言，coarse feature 仅仅会影响 fine feature 的 presence，而不控制其 position；而 position 更多地与 coordinate 有关。[项目主页](https://nvlabs.github.io/alias-free-gan/)有动态视频说明。作者称之为 “texture sticking”。图 1 具体说明了这一问题：令 latent vector 在某个小邻域移动，然后将得到的 generated images 取平均；结果，生成图像是锐利而非模糊的，说明生成纹理与位置高度相关。

> 作者称之为 aliasing（混淆），我不太理解。可能是参考了[这篇文章](https://arxiv.org/abs/2008.09604)。混淆指的是采样不合理，高频信号受损无法复原。这里可能是想说降采样、升采样不合理，因此引入了位置信息。

目标：让 coarse feature 主导 fine feature 的 position。

分析：引入（泄露）的位置信息主要有两大来源。（1）不合理的升采样（例如简单的双三次），使得升采样图像中有 faint after-images。（2）一些 point-wise 非线性操作，例如 ReLU。

思考：混淆在信号处理理论中是如何解决的呢？从奈奎斯特采样理论出发，要让离散采样和连续表示可等价。再进一步，网络中有太多的 nonequivalent translation，导致混淆的出现。

方法、实验和局限性分析没细看。
