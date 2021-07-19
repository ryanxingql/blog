# TeX

推荐使用 Overleaf 提供的模板，特别是官方模板。

## Nonbreaking space

当一行文本过长时，LaTeX 可能会打断单词至下一行，并用连词符标注。如果有不允许打断的空格（nonbreaking spaces），需要用 `~` 标记。

如：`\author{Michael~Shell,~\IEEEmembership{Member,~IEEE}}`，因为职称和人名都不建议打断放在两行。

## Ubuntu/Windows + TeX Live + VSCode + LaTeX Workshop

参见 [LaTeX Workshop 指南](https://zhuanlan.zhihu.com/p/166523064)。建议复制文中配置。如果随意配置，会很慢（每次编译都执行 4 次）。

搜索：反向搜索（根据 PDF 搜 TeX）为 `ctrl` 加鼠标左键，正向搜索需要先确定光标位置，然后 `ctrl` 加 `alt` 加 `J`。

## Ubuntu + TeX Live + TeXstudio

不推荐。

安装 LaTeX：`sudo apt install texlive-full`；注意一定是 `full`。

安装 TeXstudio`sudo apt install texstudio`。

`Build` 中选择 `PDFLATEX`，图像可正常显示。
