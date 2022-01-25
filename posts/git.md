# Git

- [Git](#git)
  - [权威](#权威)
  - [追踪和暂存](#追踪和暂存)
    - [不追踪指定文件](#不追踪指定文件)
    - [已追踪，忽略后续修改](#已追踪忽略后续修改)
    - [删除文件](#删除文件)
    - [一键 add 和 commit](#一键-add-和-commit)
    - [commit 多条信息](#commit-多条信息)
    - [清空 commit 记录](#清空-commit-记录)
  - [远程仓库](#远程仓库)
    - [生成 SSH 密钥](#生成-ssh-密钥)
    - [初始化 git 身份](#初始化-git-身份)
    - [指定远程仓库并推送](#指定远程仓库并推送)
    - [shallow clone](#shallow-clone)
    - [大文件存储](#大文件存储)
  - [submodule](#submodule)
    - [添加子仓库](#添加子仓库)
    - [含子仓库的 clone](#含子仓库的-clone)
    - [删除子仓库](#删除子仓库)

## 权威

[[手册 1]](https://git-scm.com/docs)

[[手册 2]](https://git.wiki.kernel.org/index.php/Main_Page)

## 追踪和暂存

### 不追踪指定文件

将文件记录在 `.gitignore` 里即可。
注意，如果文件已经被追踪，那么该操作无效。

注意文件格式：

- `logs/  # 所有 logs/ 文件夹，包括子文件夹中的 logs/ 文件夹`
- `/logs/  # 当前路径下的 logs/ 文件夹，不包括子文件夹中的`

如果一个项目中包含多个子项目，每个子项目的 ignore 需求不同，那么可以在每个子项目文件夹下单独放置 `.gitignore` 文件。各子文件夹的 `.gitignore` 互不影响。

### [已追踪，忽略后续修改](http://git-scm.com/docs/git-update-index/)

如果希望 git 保存一个模板文件，然后忽略该文件的后续修改（例如上传一个配置文件，其他人在本地进行修改，而不通过 git 追踪），则需要执行以下操作：

```bash
git update-index --assume-unchanged [<file> ...]
```

此时，若远端仓库的该文件发生了修改，那么 pull 时会发生错误，提示冲突。解决冲突的方法有两个：

1. 用版本库的文件替代本地文件：`git checkout -- <file>`
2. 恢复追踪：
   1. 快速找出所有 git 冻结文件：`git ls-files -v | grep "^[a-z]"`
   2. `git update-index --no-assume-unchanged [<file> ...]`

### 删除文件

- `git rm <file>`：把文件从 working tree 和 index 中同时删除。即，文件从本地消失，且 git 不再追踪该文件。该删除操作会被 git 自动记录。
- 直接删除：只从 working tree 中删除了，文件还在 index 里。为了记录这一个删除操作，必须手动 add，最终效果和 `git rm <file>` 一样。
- `git rm --cached <file>`：只从 index 中删除，在 working tree 中的文件不受影响。即 git 停止追踪该文件，且本地文件也没有被删除。一旦同步到远端，远端仓库最新版本中该文件将消失。如果需要永远停止追踪，需要手动将文件加入 `.gitignore`。

### 一键 add 和 commit

```bash
git commit -am 'update'
```

将所有文件的修改（包括删除）commit；但对尚未 track 的文件无影响。

`-a`：all。

### commit 多条信息

```bash
git commit -m msg1 -m msg2
```

多条信息会被 concat 为一条信息、多个段落。

### [清空 commit 记录](https://stackoverflow.com/questions/13716658/how-to-delete-all-commit-history-in-github)

以 main 主分支为例：

```bash
git checkout --orphan latest_branch
git add -A
git commit -am "Init"
git branch -D main
git branch -m main
git push -f origin main
```

慎用。除非 commit 很糟糕，例如包含了大文件，或有敏感信息。

## 远程仓库

### 生成 SSH 密钥

```bash
ssh-keygen -t rsa -C <email>
```

把公钥告知 GitHub，方便后续同步。

### 初始化 git 身份

```bash
git config --global user.name <usr_name>
git config --global user.email <email>
```

### 指定远程仓库并推送

```bash
git remote add origin <git-url>
git push -u origin main
```

- 将 `<git-url>` 命名为 origin。还可以是别的代号，随便起。
- 将 upstream 设置为刚命名的 origin。今后 pull 或 push 时，默认上游就是 origin，即 `-u` 参数可以省略。
- 推送至 origin 的 main 分支。可以是其他 git 仓库或其他分支。

### shallow clone

```bash
git clone --depth=1 <git-url> [<dir>]
```

- 只 clone 最新版本。
- 默认只 clone 主分支，即 `--single-branch`。
- 如果有子仓库，同时也希望浅拷贝，则需指定 `--shallow-submodules`。
- 可以拷贝到一个不同命名的文件夹，用 `dir` 指定。

### [大文件存储](https://git-lfs.github.com/)

Large File Storage

1. `git lfs track "*.zip"`
2. `git add .gitattributes`

第一步：在 git 仓库下指定需要大文件存储的文件格式。
其结果是，指定格式被记录在了 `.gitattributes`，即该文件被编辑了。
因此需要第二步，把 `.gitattributes` 用 git 追踪。
其他 git 操作没有区别。

如果仓库中有一些大文件，那么 git 需要存储大文件的多个历史版本，导致 clone 很慢。

为了解决这个问题，github 提供了大文件存储方法。只需要指定哪些属于大文件，其余 git 操作都相同。在之后和远程仓库的互动过程中，大文件都上传到独立的大文件仓库，并从大文件仓库中下载，速度会有一定提升。

## [submodule](https://git-scm.com/docs/git-submodule)

### 添加子仓库

```bash
git submodule add <git-url> [<dir>]
```

在某个 git 仓库下，执行该操作，使另一个 git 仓库存放为 `<dir>` 文件夹。

子模块是独立的 git 仓库。主仓库只追踪子仓库的版本号，不追踪内容。

### 含子仓库的 clone

在 clone 时，加入循环参数：

```bash
git clone --recurse-submodules <git-url>
```

如果 clone 没有执行该操作，子仓库就是一个无法访问的空文件。此时可以执行以下操作，获取文件：

```bash
git submodule update --init --recursive <pathspec>
```

### [删除子仓库](https://stackoverflow.com/a/1260982)

有两部分：

1. 和主仓库解耦。
2. 删除子仓库内容（危险）。
