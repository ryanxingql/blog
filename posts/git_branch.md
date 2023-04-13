# Git 分支管理

代码总结如下：

```bash
# 创建子分支 auto-greeting 再开发
$ git checkout -b auto-greeting
Develop feature ...

# 更新本地的主分支
$ git switch main
$ git pull

# 解决冲突
$ git switch auto-greeting
$ git rebase main
Solve conflict ...
$ git rebase --continue

# 汇入主分支
$ git switch main
$ git merge --no-ff -m "Merge branch 'auto-greeting'" auto-greeting
```

具体流程如下。

## 开发新功能

最原始的主分支（main 分支）如图：

![image-20230413153618091](./git_branch.assets/image-20230413153618091.png)

可见，主分支是一根光秃秃的直线。

为了开发新功能（例如自动打招呼），我们不要直接修改主分支，而是从当前节点（主分支的最新节点）切出一个子分支（可以命名为 auto-greeting 分支），在子分支上开发。

```bash
$ git checkout -b auto-greeting
```

子分支可以随意造，大不了毁灭删掉。我通常是直线开发，且通常会有多个提交：

![image-20230413154740740](./git_branch.assets/image-20230413154740740.png)

如图，我们从当时主分支的最新提交 57558c5e 切出子分支，然后在子分支产生了 3 次提交。

开发完毕，我们希望将新功能汇入主分支。

## 解决冲突

首先要更新本地的主分支。其他团队或者自己在其他笔记本上可能向远端的主分支提交了新代码，因此 57558c5e 可能已经不是主分支最新的提交。

```bash
$ git switch main
$ git pull
```

果然，主分支出现了更新的提交（e5839d56）：

![image-20230413160901037](./git_branch.assets/image-20230413160901037.png)

理想情况下，我们应当从主分支最新提交切出子分支。我们使用 rebase 功能：

```bash
$ git switch auto-greeting
$ git rebase main
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
error: could not apply a6c5fcc... Add version
hint: Resolve all conflicts manually, mark them as resolved with
hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
hint: You can instead skip this commit: run "git rebase --skip".
hint: To abort and get back to the state before "git rebase", run "git rebase --abort".
Could not apply a6c5fcc... Add version
```

不幸的是，主分支最新提交和子分支修改了同一个文件（如 README.md）；因此我们需要手动解决冲突。

直接打开 README.md，手动修改文件，然后执行：

```bash
$ git add README.md
$ git rebase --continue
```

此时实际上是在修改子分支的最新提交。冲突解决后，子分支改为从主分支最新提交（e5839d56）切出，然后重新执行了原有的 3 次提交。注意，这 3 次提交的 ID 都是新的。

![image-20230413161819376](./git_branch.assets/image-20230413161819376.png)

## 汇入主分支

最后，我们将子分支汇入主分支。由于之前完成了 rebase，说明子分支和主分支不存在冲突了。因此 merge 会很顺利。

```bash
$ git switch main
$ git merge --no-ff -m "Merge branch 'auto-greeting'" auto-greeting
```

![image-20230413162231626](./git_branch.assets/image-20230413162231626.png)

如图，merge 会产生一次提交，从而产生子分支和主分支的一个交汇节点。Merge 相当于把子分支所有提交汇总成了一个提交，然后应用在主分支的最新提交上。
