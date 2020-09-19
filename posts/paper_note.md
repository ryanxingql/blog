# PAPER NOTE

- [PAPER NOTE](#paper-note)

**EDVR**

- 在特征层次上的alignment，其可视化效果与flow-based me+mc的效果差不多。
  - 难道fusion前的理想状态就是：相邻特征要趋近于当前帧的形态？
  - [[paper]](https://arxiv.org/pdf/2009.07265.pdf)

**MFQE**

- 编码本身hierarchy，因此QE反其道而行之。不同于一般视频，压缩视频的PQF是很有意义的，通常质量较高。
- 加入了MC loss，首先让MC网络收敛。但在TOFlow一文中也揭示了：MC并非得追求一致。
  - [solution] end-to-end training，或改用feature-wise alignment。

**NASNet**

- 搜索block而不是整个network。
  - 对于多任务而言，每个block最好不同。

**RANet**

- 和MSDNet一样，基于阈值退出。
  - 比较盲目，需要预先随机设定阈值。

**STDF**

- Joint prediction比pair prediction效果更好！
  - 作者观点：可能是因为R1、2和3互相借鉴。该规律不一致成立，去噪、SR等结果都可能不同。
  - pair的参数量反而更少，没明白，得问问作者。