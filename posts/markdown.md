# MARKDOWN

- **生成可自动更新的 TOC**：使用 MARKDOWN ALL IN ONE 插件；每次保存文档时自动更新。

<details>
<summary><b>MARKDOWN 基础 + GITHUB 支持</b></summary>
<p>

参见[此处](https://enterprise.github.com/downloads/en/markdown-cheatsheet.pdf)。

GITHUB 支持的 EMOJI [在此](https://www.webfx.com/tools/emoji-cheat-sheet/)。

</p>
</details>

<details>
<summary><b>多级目录</b></summary>
<p>

- TAB 键缩进；`shift + tab` 回退。
- 不要敲空格，敲 TAB：实践发现，多级有序列表的 TAB 会转化为 3 个空格，无序列表为 2 个空格，不一样！

</p>
</details>

<details>
<summary><b>列表内多行</b></summary>
<p>

- 行末加两个空格，表示 line break；或直接空一行，但注意空行也要缩进。
- 注意用 TAB 调整级别；级别要相同。

</p>
</details>

<details>
<summary><b>定制插入图像</b></summary>
<p>

可指定图像的宽度和高度：

```markdown
<img src="<im_url>" width="50%">
```

</p>
</details>

<details>
<summary><b>页内跳转</b></summary>
<p>

```markdown
LET'S [TRY](#a_tag)!

<span id="a_tag">Hi!</span>
```

LET'S [TRY](#a_tag)!

<span id="a_tag">Hi!</span>

</p>
</details>

<details>
<summary><b>展开详情</b></summary>
<p>

```markdown
<details>
<summary><b>title</b></summary>
<p>

content

</p>
</details>
```

</p>
</details>
