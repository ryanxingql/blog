# 写作规范

清晰易读即可。不要追求完美主义。

面向 Markdown。

参考：

- [中文技术文档写作规范](https://github.com/ruanyf/document-style-guide)
- [中文文案排版指北](https://github.com/sparanoid/chinese-copywriting-guidelines)

## 标点符号

（1）中文文档多用直角引号`「」`替换双引号；更醒目。

> 原：请参见“README.md”。
>
> 改：请参见「README.md」。

## 字间距

（1）全角中文字符与半角英文字符之间使用一个半角空格。

> 正确：这是我的 blog。
>
> 错误：这是我的blog。

（2）全角中文字符与半角阿拉伯数字之间使用一个半角空格。

> 正确：我吃了 1 碗面。
>
> 错误：我吃了1碗面。

（3）全角标点符号与半角英文字符或半角阿拉伯数字之间均不使用空格。

> 正确：这是我的 blog。
>
> 错误：这是我的 blog 。

全角标点符号虽然是全角，但视觉上是半角。

（4）半角阿拉伯数字和单位之间使用一个半角空格。

> 正确：这是 16 GB 的显卡。
>
> 错误：这是 16GB 的显卡。

注意，`2K`中的`K`不是单位，而是缩写，因此不适用空格。`10%`中的`%`同理。

## 英文

（1）中英文混合时，应使用双引号将英文部分括起来。

> 例：我的口号是「Keep moving!」。

（2）「专有名词」中每个单词的首字母均大写，括号给出缩写。

> 例：「Better Portable Graphics (BPG) is a image format based on the intra-frame encoding of the High Efficiency Video Coding (HEVC) standard.”」

（3）尊重「专有名词」的原有大小写。

> 例：「I am using GitHub/LaTeX/VS Code/iPad/iPhone/iOS/iCloud/macOS/tmux.」

如果出现在句首，首字母必须大写。

> 例：「Tmux is a terminal multiplexer.」

## 代码

（1）文件名使用引号括起，表示是一个整体。中文文档用双引号或直角引号，英文文档用英文双引号。

> 例：「Please refer to "README.md".
>
> 例：「请参见「README.md」。」。

（2）变量名、变量值等代码成分作为行内代码处理。

> 参考代码：
>
> ```markdown
> 函数 `func_demo` 输出值 `1`。
> ```
>
> 渲染效果：函数 `func_demo` 输出值 `1`。

## 缩写

（1）用`TPAMI'19`表示`TPAMI 2019`。

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
> MFQEv2 数据库[^mfqev2]是常用的一个数据库。
>
> [^mfqev2]: *MFQE 2.0: A New Approach for Multi-frame Quality Enhancement on Compressed Video*, 2019.
> ```
>
> 渲染效果：MFQEv2 数据库[^mfqev2]是常用的一个数据库。

[^mfqev2]: *MFQE 2.0: A New Approach for Multi-frame Quality Enhancement on Compressed Video*, 2019.
