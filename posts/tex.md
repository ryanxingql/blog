# TeX

## 目录

- [TeX](#tex)
  - [目录](#目录)
  - [配置](#配置)
    - [TeX Live plus VSCode LaTeX workshop](#tex-live-plus-vscode-latex-workshop)
  - [使用](#使用)
    - [Image placeholder](#image-placeholder)
    - [Nonbreaking space](#nonbreaking-space)

## 配置

软件：Overleaf（远程协作）+ VSCode LaTeX workshop（本地编辑）+ TeX Live（本地编译）。

理由：

1. 不受限于网速。
2. 方便导师修改和协作：可以在 Overleaf 中开启审阅模式，或使用 Overleaf 的 Git 功能，通过 Git commit history 查看修改细节也很方便。

模板：Overleaf 提供的模板，特别是其中的官方模板，如 IEEE 官方模板。

### TeX Live plus VSCode LaTeX workshop

参见 [LaTeX workshop 指南](https://zhuanlan.zhihu.com/p/166523064)，安装并配置。

TeX Live 可通过 TeX Live Manager 更新。

配置改动：

- `"latex-workshop.latex.autoBuild.run": "onSave"`

## 使用

### [Image placeholder](https://tex.stackexchange.com/questions/231738/example-images-in-latex/231741#231741)

轻松引入图像的占位符，即示例图片。

```tex
\documentclass[12pt,a4paper]{article}
\usepackage{graphicx}

\begin{document}

\noindent\includegraphics[width=3cm]{example-image-a}\qquad
\includegraphics[width=3cm]{example-image-golden}\qquad
\includegraphics[width=3cm]{example-grid-100x100pt}

\noindent\includegraphics[height=5cm]{example-image-b}

\noindent\includegraphics[scale=0.5]{example-image-c}

\noindent\includegraphics[width=3cm]{example-image}

\end{document}
```

我个人喜欢用：

```tex
\begin{figure*}[!t]
  \centering
  \includegraphics[width=0.5\linewidth]{example-image-golden}
  \caption{placeholder}
  \label{fig:placeholder}
\end{figure*}
```

### Nonbreaking space

当一行文本过长时，LaTeX 可能会打断单词至下一行，并用连词符标注。如果有不允许打断的空格（nonbreaking spaces），需要用 `~` 标记。

如：`\author{Michael~Shell,~\IEEEmembership{Member,~IEEE}}`，因为职称和人名都不建议打断放在两行。
