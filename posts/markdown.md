# Markdown

## 目录

- [Markdown](#markdown)
  - [目录](#目录)
  - [生成可自动更新的 TOC](#生成可自动更新的-toc)
  - [GitHub Support](#github-support)
  - [多级目录](#多级目录)
  - [列表内多行](#列表内多行)
  - [定制插入图像](#定制插入图像)
  - [页内跳转](#页内跳转)
  - [展开详情](#展开详情)

## 生成可自动更新的 TOC

不推荐，因为 GitHub 和 VSCode 都支持纵览了。

使用 Markdown all in One 插件；每次保存文档时自动更新。

## GitHub Support

[\[简要说明\]](https://enterprise.github.com/downloads/en/markdown-cheatsheet.pdf)

Emoji：[\[Link\]](https://www.webfx.com/tools/emoji-cheat-sheet/)

Languages：[\[Link\]](https://github.com/github/linguist/blob/master/lib/linguist/languages.yml)

## 多级目录

- Tab 键缩进；`shift + tab` 回退。
- 不要敲空格，敲 Tab：实践发现，多级有序列表的 Tab 会转化为 3 个空格，无序列表为 2 个空格，不一样！

## 列表内多行

- 行末加两个空格，表示 line break；或直接空一行，但注意空行也要缩进。
- 注意用 Tab 调整级别；级别要相同。

## 定制插入图像

可指定图像的宽度和高度：

```markdown
<img src="<im_url>" width="50%">
```

## 页内跳转

```markdown
LET'S [TRY](#a_tag)!

<span id="a_tag">Hi!</span>
```

LET'S [TRY](#a_tag)!

<span id="a_tag">Hi!</span>

## 展开详情

```markdown
<details>
<summary><b>title</b></summary>
<p>

content

</p>
</details>
```
