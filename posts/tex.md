# TEX

推荐使用 OVERLEAF 提供的模板，特别是官方模板。

## UBUNTU/WINDOWS + TEXLIVE + VSCODE + LATEX WORKSHOP

推荐使用 OVERLEAF。

参见 [LATEX WORKSHOP 指南](https://zhuanlan.zhihu.com/p/166523064)。建议复制文中配置。如果随意配置，会很慢（每次编译都执行 4 次）。

搜索：反向搜索（根据 PDF 搜 TEX）为 `ctrl` 加鼠标左键，正向搜索需要先确定光标位置，然后 `ctrl` 加 `alt` 加 `J`。

## UBUNTU + TEXLIVE + TEXSTUDIO

不推荐。

安装 LATEX：`sudo apt install texlive-full`；注意一定是 `full`。

安装 TEXSTUDIO：`sudo apt install texstudio`。

`Build` 中选择 `PDFLATEX`，图像可正常显示。

## 提交论文前检查

作者和单位信息：

- 每一段要用单独的一个 `\thanks{}`。
- 换行也有空格的作用。所以在最后一个 author 后，添加一个 `%` 取缔空格，连接到下一行的 `\thanks`。
- 作者单位多多益善，例如高工。否则以后评奖没资格。

标题：

- 不要用公式和数学符号。
- 换行：`\title{Bare Demo of IEEEtran.cls\\ for IEEE Journals}`
- 大小写：
  > Titles are generally capitalized except for words such as a, an, and, as, at, but, by, for, in, nor, of, on, or, the, to and up, which are usually not capitalized unless they are the first or last word of the title.

常用词：

`i.e.` 和 `e.g.` 应使用 `\ie` 和 `\eg`。

数字：

- 如果要表达 `1e-3`，代码为：`1e{-3}`，否则负号和 3 距离过大。

连词：

- 可以规定断词：`\hyphenation{op-tical net-works semi-conduc-tor}`
- 如果有不允许打断的空格（nonbreaking spaces），用 `~`。如：`\author{Michael~Shell,~\IEEEmembership{Member,~IEEE,}}`，因为职称和人名都不可打断。

图表：

- 期刊通常不用 `[h]`。
- IEEE 通常不会在第一页或第一个 column 放 floats。
- `\includegraphics`、`\caption` 和 `\label` 要按顺序。

  ```tex
  \begin{figure}[!t]
  \centering
  \includegraphics[width=2.5in]{myfigure}
  \caption{Network.}
  \label{fig_net}
  \end{figure}
  ```

致谢：ARXIV 和 CR 版本记得都加一下致谢。

引用：

- 最好用 CROSSREF 的 BIBTEX 信息，比较规范。IEEE 格式中作者名不全。
- 有些期刊规定不使用 CITE 包，例如 TPAMI。

排版：

全文最好不要用 `vspace`，否则可能被拒，特别是会议。
