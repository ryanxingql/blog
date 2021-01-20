# TEX

- [TEX](#tex)

<details>
<summary><b>TEXLIVE + VSCODE + LATEX WORKSHOP</b></summary>

[[基础模板]](https://gist.github.com/RyanXingQL/f1e0802bc7427b5d444261160a44e126)

[[LATEX WORKSHOP指南]](https://zhuanlan.zhihu.com/p/106167792)

包括快捷键和省心选项。

为了删除`.synctex.gz`，我在`latex-workshop.latex.clean.fileTypes`中添加了`*.synctex.gz`。这样，点击按钮就可以一键删除中间文件。

</details>

<details>
<summary><b>UBUNTU + TEXLIVE + TEXSTUDIO【放弃】</b></summary>

安装LATEX：`$ sudo apt install texlive-full`

注意一定是`full`。

安装TEXSTUDIO：`$ sudo apt install texstudio`

Build中选择PDFLATEX，图像可正常显示。

</details>

<details>
<summary><b>MIKTEX + TEXSTUDIO【放弃】</b></summary>

- 按顺序下载和安装。
- 重启。
- TEXSTUDIO里要设置zh_CN语言，将`pdflatex`改为`xzelatex`。

</details>

<details>
<summary><b>提交论文前检查</b></summary>

> 作者和致谢

- 每一段致谢要用单独的一个`\thanks{}`。
- 换行也有空格的作用。所以在最后一个author后，添加一个`%`取缔空格，连接到下一行的`\thanks`。
- 作者单位多多益善，例如高工。否则以后评奖没资格。

> 标题

- 不要用公式和数学符号。
- 换行：`\title{Bare Demo of IEEEtran.cls\\ for IEEE Journals}`
- 大小写：Titles are generally capitalized except for words such as a, an, and, as, at, but, by, for, in, nor, of, on, or, the, to and up, which are usually not capitalized unless they are the first or last word of the title.

> 数字

- 如果要表达1e-3，代码：`1e{-3}`，否则负号和3距离过大。

> 连词

- 可以规定断词：`\hyphenation{op-tical net-works semi-conduc-tor}`
- 如果有不允许打断的空格（nonbreaking spaces），用`~`。如：`\author{Michael~Shell,~\IEEEmembership{Member,~IEEE,}}`，因为职称和人名都不可打断。

> 图表

- 期刊通常不用`[h]`
- IEEE通常不会在第一页或第一个column放floats。
- `\includegraphics`、`\caption`、`\label`要按顺序：

```tex
\begin{figure}[!t]
\centering
\includegraphics[width=2.5in]{myfigure}
\caption{Network.}
\label{fig_net}
\end{figure}
```

> 引用

最好用CROSSREF的BIBTEX信息。

TPAMI规定不使用CITE包。

> 全文

最好不要用`space`，否则可能被拒，特别是会议。
