# 写作规范

清晰易读即可。不要追求完美主义。

参考：

- [中文技术文档写作规范](https://github.com/ruanyf/document-style-guide)
- [中文文案排版指北](https://github.com/sparanoid/chinese-copywriting-guidelines)

## 默认

- 使用 Markdown。
- 中文表述使用全角字符和全角标点符号；英文表述使用半角字符和半角标点符号。

## 标点符号

（1）中文文档多用直角引号（`「」`）代替双引号；更醒目。

> 这就是所谓的「边际效应」。

## 空格（半角）

（1）中文字符与英文字符之间使用一个空格。

> 这是我的 blog。

（2）中文字符与阿拉伯数字之间使用一个空格。

> 我吃了 3 碗面。

（3）全角标点符号与英文字符或阿拉伯数字之间均不使用空格。

> 这是我的新 iPad，Mac 和 iPhone 14。

（4）阿拉伯数字和单位之间使用一个空格。

> 这是一张 16 GB 的显卡。

注意，「2K 分辨率」中的「K」不是单位，而是缩写，因此不使用空格。「10% 利润率」中的「%」同理。

## 英文

（1）中文表述包含英文表述时，应使用双引号（或直角引号）将英文部分括起。英文表述包含中文表述时，也应使用双引号将中文部分括起。

> 我的口号是「Keep moving!」。

（2）专有名词中每个单词的首字母均大写，括号给出缩写。

> Better Portable Graphics (BPG) is a image format based on the intra-frame encoding of the High Efficiency Video Coding (HEVC) standard.

（3）尊重专有名词的原有大小写。

> 我在使用 GitHub/LaTeX/BibTeX。
>
> 我在使用 VS Code。
>
> 我在使用 iPad/iPhone/iOS/iCloud/macOS。
>
> 我在使用 dblp/tmux。

如果专有名词出现在英文句首，首字母必须大写。

> Tmux is a terminal multiplexer.

## 代码

（1）文件名使用引号括起，表示是一个整体。

> Please refer to "README.md".
>
> 请参见「README.md」。

（2）变量名、变量值等代码成分作为行内代码处理。注意行内代码前后使用一个空格与正文（除标点符号外）隔开。

> 参考代码：
>
> ```markdown
> 函数 `func_demo` 输出值 `1`。
> ```
>
> 渲染效果：函数 `func_demo` 输出值 `1`。

（3）指令前不使用美元符号。

> 请执行 `python main.py`。

## 缩写

（1）用 `TPAMI'19` 表示 `TPAMI 2019`。

## 引用

（1）通常使用链接功能即可。

> 参考代码：
>
> ```markdown
> 参见我的 [GitHub](https://github.com/ryanxingql)。
> ```
>
> 渲染效果：参见我的 [GitHub](https://github.com/ryanxingql)。

（2）如果链接需要进一步解释，如文献名称，则使用脚注。

> 参考代码：
>
> ```markdown
> MFQEv2 数据库[^mfqev2]是一个常用的数据库。
>
> [^mfqev2]: *MFQE 2.0: A New Approach for Multi-frame Quality Enhancement on Compressed Video*, 2019.
> ```
>
> 渲染效果：MFQEv2 数据库[^mfqev2]是一个常用的数据库。

[^mfqev2]: *MFQE 2.0: A New Approach for Multi-frame Quality Enhancement on Compressed Video*, 2019.
