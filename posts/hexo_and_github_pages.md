# Hexo & GitHub Pages

## 目录

- [Hexo & GitHub Pages](#hexo--github-pages)
  - [目录](#目录)
  - [完整流程](#完整流程)
    - [选择模板](#选择模板)
    - [安装 Hexo](#安装-hexo)
      - [Windows](#windows)
      - [macOS](#macos)
    - [本地调整模板](#本地调整模板)
    - [部署](#部署)
  - [调试](#调试)
    - [node: command not found](#node-command-not-found)
    - [无法解析 GitHub hostname](#无法解析-github-hostname)
    - [单引号](#单引号)

## 完整流程

我以我的 [GitHub Page](https://ryanxingql.github.io/) 为例。

### 选择模板

首先确定自己的需求。我希望建一个美观且简洁的网站，挂载我的 CV。我并不希望建立一个功能复杂的博客网站。

因此我首先搜寻一个合适的模板，在此基础上修改就好了。找到了两个，也都尝试过：

- [Al-Folio](https://github.com/alshedivat/al-folio)：很好看，在 CV 的基础上有一个小博客，挺好。可惜 Jekyll 编译太慢，而且调模板需要一定 HTML 基础。
- [Academic](https://themes.gohugo.io/academic/)：功能完善，贡献者很多，但 CV 实在不简洁：没有人想点击多次、分别查看 publications 和 education 等等。Hugo 倒是很快。

最后，我看中了[后者的精简版](https://github.com/PhosphorW/hexo-theme-academia)。

### 安装 Hexo

#### Windows

首先要把 Hexo 及其依赖装好。随便找一个 [Windows + Hexo 的教程](https://www.jianshu.com/p/343934573342)，照着做就行。注意先别远程部署。

然后根据[主题教程](https://github.com/PhosphorW/hexo-theme-academia)操作。

#### macOS

在博客所在文件夹下安装就行，虽然不能全局使用 hexo，但是安装过程简单，不会遇到各种权限问题。

```bash
npm install hexo-cli -g
```

### 本地调整模板

主要是调整根目录下和 `themes/Academia` 下的 `_config.yml`。

建议在根目录先执行：`hexo s`，即开启 server，会自动跟踪变动，F5 刷新网站即可查看效果，边看边改。

这个模板是极度简化的，貌似没有 post（就是一个页面多个博客条目），只有 page（一页就是一个条目）。如果要增加条目，操作：`hexo new page <name>`。

在 `source/<name>` 文件夹内，添加一个 Markdown 文件。在抬头加上 `academia: true` 即可。该内容就会显示在对应页面上。

如果一个文件夹下有多个文件，貌似会按顺序全文显示。

### 部署

在个人 GitHub 账户新建一个空的 `<usr_name>.github.io` 仓库，将该 `.git` 链接填到根目录下 `_config.yml` 最后的 `deploy` 里。

每次部署分三步：

1. 首先注意要清理掉 `public` 的旧文件：`hexo clean`。
2. 然后生成新文件：`hexo g`（generate）。
3. 最后一键部署：`hexo d`（deploy）；非常简单，不需要手动 `git add/commit/push`。

可以简化为一步：`hexo g -d`。

## 调试

### node: command not found

首先 `node -v` 确定 `node` 找不到了。重新下载 `node.js` 的安装文件，选择 `repair` 即可。

### 无法解析 GitHub hostname

用热点，别用校园网。

### 单引号

不要用 `'`，编译出来会变成中文；要用 HTML 语言，即 `&apos;`。

