# MARKDOWN

- [MARKDOWN](#markdown)

<details>
<summary><b>TOC</b></summary>

自动生成TOC列表（不是`[toc]`），github或纯文本编辑器可查看

- 在VSCODE编辑时，建议安装MARKDOWN ALL IN ONE插件。
- `f1`，输入`toc`，可以在指定位置创建TOC列表。
- 每次`ctrl + s`保存时，该列表自动更新，非常方便。

</details>

<details>
<summary><b>多级目录</b></summary>

- TAB键缩进，`shift + tab`回退。
- 实践发现，多级有序列表的TAB会转化为3个空格，无序列表为2个空格，不一样！
- 因此不要敲空格，敲TAB。

</details>

<details>
<summary><b>列表内多行</b></summary>

- 行末要加两个空格，表示line break。
- TAB对齐内容。

</details>

<details>
<summary><b>定制插入图像</b></summary>

可指定图像的宽度和高度：

```markdown
<img src="http://static.runoob.com/images/runoob-logo.png" width="50%">
```

<img src="http://static.runoob.com/images/runoob-logo.png" width="50%">

</details>

<details>
<summary><b>页内跳转</b></summary>

```markdown
LET'S [TRY](#a_tag)!

<span id="a_tag">Hi!</span>
```

LET'S [TRY](#a_tag)!

<span id="a_tag">Hi!</span>

</details>

<details>
<summary><b>展开详情</b></summary>

```markdown
<details>
<summary><b>展开详情</b></summary>

xxx  # 一定要在上方空一行

</details>
```

</details>
