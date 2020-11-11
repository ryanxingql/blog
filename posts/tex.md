# TEX

- [TEX](#tex)
  - [写完论文检查](#写完论文检查)
  - [安装MikTeX + TeXstudio](#安装miktex--texstudio)
  - [Ubuntu 20.04 安装LaTeX + TeXstudio](#ubuntu-2004-安装latex--texstudio)

## 写完论文检查

- 作者和致谢
  - 每一段致谢要用单独的一个`\thanks{}`。
  - 换行也有空格的作用。所以在最后一个author后，添加一个`%`取缔空格，连接到下一行的`\thanks`。
- 标题
  - 不要用公式和数学符号。
  - 换行：`\title{Bare Demo of IEEEtran.cls\\ for IEEE Journals}`
  - 大小写：Titles are generally capitalized except for words such as a, an, and, as, at, but, by, for, in, nor, of, on, or, the, to and up, which are usually not capitalized unless they are the first or last word of the title.
- 模板
  - 最好不要用`space`，可能被拒。
- 数字
  - 如果要表达1e-3，代码：`1e{-3}`，否则负号和3距离过大。
- 文字
  - 可以规定断词：`\hyphenation{op-tical net-works semi-conduc-tor}`
  - 如果有不允许打断的空格（nonbreaking spaces），用`~`。如：`\author{Michael~Shell,~\IEEEmembership{Member,~IEEE,}}`，因为职称和人名都不可打断。
- 图表
  - `\includegraphics`、`\caption`、`\label`要按顺序：
  
    ```tex
    \begin{figure}[!t]
    \centering
    \includegraphics[width=2.5in]{myfigure}
    \caption{Network.}
    \label{fig_net}
    \end{figure}
    ```
  
  - 期刊通常不用`[h]`
  - IEEE通常不会在第一页或第一个column放floats。

## 安装MikTeX + TeXstudio

- 按顺序下载和安装。
- 重启。
- TexStudio里要设置zh_CN语言，将`pdflatex`改为`xzelatex`。

## Ubuntu 20.04 安装LaTeX + TeXstudio

Ubuntu 20.04暂不支持MikTeX。——20200913

安装LaTeX：`$ sudo apt install texlive-full`

注意一定是`full`。

安装TeXstudio：`$ sudo apt install texstudio`

Build中选择pdflatex，图像可正常显示。
