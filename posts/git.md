# Git

[[书籍]](https://git-scm.com/book/en/v2)

[[手册]](https://git-scm.com/docs)

## 一键 add 和 commit

如果文件没有 tracked，则必须先 add。

如果文件已经处于 tracked 状态，那么 `git commit -am` 可以自动将没有 add 的变化 stage，然后一起 commit。

## 清空 commit 记录

```bash
git checkout --orphan latest_branch

git add -A

git commit -am "Init"

git branch -D main

git branch -m main

git push -f origin main
```

参考 [Stack Overflow](https://stackoverflow.com/questions/13716658/how-to-delete-all-commit-history-in-github)。

## 忽略本地文件变化

如果不希望 track，那么要在 add 前，将文件记录在 `.gitignore` 里。

```txt
logs/  # 所有 logs/ 文件夹，包括子文件夹中的 logs/ 文件夹
/logs/  # 当前路径下的 logs/ 文件夹，不包括子文件夹中的
```

如果一个项目中包含多个子项目，每个子项目的 ignore 需求不同，那么可以在每个子项目文件夹下单独放置 `.gitignore` 文件。各子文件夹的 `.gitignore` 互不影响。

## 上传模板文件，忽略本地修改

如果希望 git 保存一个模板文件，然后忽略该文件的后续修改（例如上传一个配置文件，其他人在本地进行修改，而不通过 git 追踪），则需要执行[以下操作](http://git-scm.com/docs/git-update-index/)：

```bash
git update-index --assume-unchanged [<file> ...]
```

此时，若远端仓库的该文件发生了修改，那么 pull 时会发生错误，提示冲突。解决冲突的方法有两个：（1）用版本库的文件替代本地文件，即 `git checkout -- <file>`；（2）恢复追踪，见下面。

快速找出所有 git 冻结文件：`git ls-files -v | grep "^[a-z]"`。

如果希望恢复追踪：

```bash
git update-index --no-assume-unchanged [<file> ...]
```

## 执行 git 删除而不删除本地文件

```bash
git rm --cached <file>
```

类似于告诉 git 执行 delete 任务；一旦同步到远端，远端仓库的该文件将消失。

建议操作次序：

1. 执行该操作。
2. 若不再希望同步，应将其添加到 `.gitignore`。
3. 若希望重新上传，则应重新 add + commit。


## 远程仓库

### SSH 基础

#### 生成密钥

```bash
ssh-keygen -t rsa -C <email>
```

#### 免密登陆

如果经常访问一个地址，建议彼此之间保存公私钥。

首先在本地编辑 `C:\Users\<usr_name>\.ssh\config` 或 `~/.ssh/config`（没有则新建）：

```jason
Host <host_name>
  HostName <000.000.00.000>
  User <xx>
IdentityFile C:\Users\<usr_name>\.ssh\id_rsa
```

最后一行指定了本地的私钥位置。会自动发送给服务器，和以下的公钥合作，以识别身份。

然后将本地公钥 `id_rsa.pub` 传到服务器的 `~/.ssh/` 路径下：

```bash
scp id_rsa.pub <host_name>:~/.ssh/hello.pub
```

一定要改名！不要覆盖了服务器的 `id_ras.pub`！

在服务器 `~/.ssh/` 下执行

```bash
cat hello.pub >> authorized_keys
```

即将公钥加入可信列表。

今后，直接 `ssh <host_name>`，就可以免密登录啦！

### 初始化身份

```bash
git config --global user.name <usr_name>
git config --global user.email <email>
```

### 仓库初始化，推送至远端

```bash
echo > README.md
git init
git add README.md
git commit -m "Init"
git remote add origin <git_url>
git push -u origin master
```

### 只克隆最新 commit

```bash
git clone <url> --depth=1
```

### Submodule

可以调用一个仓库，作为当前仓库的一个子模块，使其在路径下可见。添加方式：

```bash
# clone PythonUtils，存为utils
git submodule add git@github.com:RyanXingQL/PythonUtils.git utils/
```

子模块是独立更新的；更新子模块需要进入子模块路径手动更新。

- 当前库只记录子模块的当前版本，不会自动更新。
- 假设有两个本地仓库对应同一个远程仓库；如果不手动更新子模块，会出现两个本地仓库来回扯皮版本号的情况。

拉取含子模块的仓库时，必须增加循环参数，否则子模块是空的：

```bash
git clone --recursive <git_url>  # 不能简化为 -r

git pull --recurse-submodules
```

或正常拉取后（此时子模块是空的），初始化、更新子模块：

```bash
git submodule update --init --recursive
```

上一步拉取以后，拉取下来的子模块默认与原仓库是分离的（显示头指针分离于 xxx，具体表现为与原子模块无联系，无法正常上传和下拉）。如果想建立联系：

```bash
git submodule foreach -q --recursive 'git checkout $(git config -f $toplevel/.gitmodules submodule.$name.branch || echo main)'
```

注意这里子模块的默认主分支为 `main`。此时，修改了子模块以后，也能往原仓库对比、提交。

[[参考链接]](https://git-scm.com/book/zh/v2/Git-工具-子模块)

删除子模块：

```bash
# Remove the submodule entry from .git/config
git submodule deinit -f path/to/submodule

# Remove the submodule directory from the superproject's .git/modules directory
rm -rf .git/modules/path/to/submodule

# Remove the entry in .gitmodules and remove the submodule directory located at path/to/submodule
git rm -f path/to/submodule
```
