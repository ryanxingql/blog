# TeX

## 编译器

推荐使用 Overleaf 提供的模板，特别是官方模板。

如果翻墙稳定且图文较少，建议使用 Overleaf；否则，建议下载 Overleaf 源码，在本地使用 VSCode LaTeX workshop 编译。

如果是多人协作，推荐在 Overleaf 中开启审阅模式。

### TeX Live + VSCode + LaTeX Workshop

参见 [LaTeX Workshop 指南](https://zhuanlan.zhihu.com/p/166523064)，安装并配置。

TeX Live 可通过 TeX Live Manager 更新。

配置改动：

- `"latex-workshop.latex.autoBuild.run": "onSave"`

## Nonbreaking space

当一行文本过长时，LaTeX 可能会打断单词至下一行，并用连词符标注。如果有不允许打断的空格（nonbreaking spaces），需要用 `~` 标记。

如：`\author{Michael~Shell,~\IEEEmembership{Member,~IEEE}}`，因为职称和人名都不建议打断放在两行。
