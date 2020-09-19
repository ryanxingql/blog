# PAPER NOTE

- [PAPER NOTE](#paper-note)

**EDVR**

- 在特征层次上的alignment，其可视化效果与flow-based me+mc的效果差不多。难道fusion前的理想状态就是：相邻特征要趋近于当前帧的形态？[[最新作者发文]](https://arxiv.org/pdf/2009.07265.pdf)

**MFQE**

- 编码本身hierarchy，因此QE反其道而行之。不同于一般视频，压缩视频的PQF是很有意义的，通常质量较高。
- 加入了MC loss，和QE loss一起监督。但在TOFlow一文中也揭示了：MC并非得追求一致。

**STDF**

- joint prediction比pair prediction效果更好！这是因为视频差异导致的吗？正是我最新工作在考虑的。
