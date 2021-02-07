# HEXO AND GITHUB PAGES

- [HEXO AND GITHUB PAGES](#hexo-and-github-pages)
  - [完整流程](#完整流程)
  - [调试](#调试)

## 完整流程

我以我的 [GITHUB PAGE](https://ryanxingql.github.io/) 为例。

<details>
<summary><b>选择模板</b></summary>

首先确定自己的需求。我希望建一个美观且简洁的网站，挂载我的 CV。我并不希望建立一个功能复杂的博客网站。

因此我首先搜寻一个合适的模板，在此基础上修改就好了。找到了两个，也都尝试过：

- [al-folio](https://github.com/alshedivat/al-folio)。很好看，在 CV 的基础上有一个小博客，挺好。可惜 JEKYLL 编译太慢，而且调模板需要一定HTML基础。
- [Academic](https://themes.gohugo.io/academic/)。功能完善，贡献者很多，但 CV 实在不简洁：没有人想点击多次、分别查看 publications 和 education 等等。HUGO 倒是很快。

最后，我看中了[后者的精简版](https://github.com/PhosphorW/hexo-theme-academia)。

</details>

<details>
<summary><b>安装 HEXO</b></summary>

首先要把 HEXO 及其依赖装好。随便找一个 WINDOWS + HEXO 的[教程](https://www.jianshu.com/p/343934573342)，照着做就行。注意先别远程部署。

然后根据[主题教程](https://github.com/PhosphorW/hexo-theme-academia)操作。

</details>

<details>
<summary><b>本地调整模板</b></summary>

主要是调整根目录下和 `themes->Academia` 下的 `_config.yml`。

建议在根目录先执行：`hexo s`，即开启 server，会自动跟踪变动，F5 刷新网站即可查看效果，边看边改。

这个模板是极度简化的，貌似没有post（就是一个页面多个博客条目），只有 page（一页就是一个条目）。如果要增加条目，操作：`hexo new page <name>`。

在 `source-><name>` 文件夹内，添加一个 MARKDOWN 文件。在抬头加上 `academia: true` 即可。该内容就会显示在对应页面上。

如果一个文件夹下有多个文件，貌似会按顺序全文显示。

</details>

<details>
<summary><b>部署</b></summary>

在个人 GITHUB 账户新建一个空的`<用户名>.github.io` 仓库，将该 `.git` 链接填到根目录下 `_config.yml` 最后的 `deploy` 里。

每次部署分三步：

1. 首先注意要清理掉 `public` 的旧文件：`hexo clean`。
2. 然后生成新文件：`hexo g`，generate 的意思。
3. 最后一键部署：`hexo d`，deploy 的意思。非常简单，不需要手动 `git add/commit/push`。

</details>

## 调试

<details>
<summary><b>node: command not found</b></summary>

首先 `node -v` 确定 `node` 找不到了。重新下载 `node.js` 的安装文件，选择 `repair` 即可。

</details>
