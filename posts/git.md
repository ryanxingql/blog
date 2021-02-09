# GIT

- [GIT](#git)
  - [SSH](#ssh)
  - [Repository](#repository)
  - [与远程仓库互动](#与远程仓库互动)

## SSH

- 生成密钥：`ssh-keygen -t rsa -C <email>`。

<details>
<summary><b>免密登陆</b></summary>
<p>

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

</p>
</details>

## Repository

<details>
<summary><b>submodule</b></summary>
<p>

可以调用一个仓库，作为当前仓库的一个子模块。例如：

```bash
# clone PythonUtils，存为utils
git submodule add git@github.com:RyanXingQL/PythonUtils.git utils/
```

更新子模块需要进入子模块手动更新。

- 当前库只记录子仓库的当前版本，不会自动更新。
- 假设有两个本地仓库对应同一个远程仓库；如果不手动更新子仓库，会出现两个本地仓库来回扯皮版本号的情况。

</p>
</details>

<details>
<summary><b>清空 commit 记录</b></summary>
<p>

```bash
git checkout --orphan latest_branch

git add -A

git commit -am "Init"

git branch -D main

git branch -m main

git push -f origin main
```

我认为可以将 `-am` 改为 `-m`。没试。

参考 [STACKOVER](https://stackoverflow.com/questions/13716658/how-to-delete-all-commit-history-in-github)。

</p>
</details>

<details>
<summary><b><code>git commit -am</code></b></summary>
<p>

如果文件已经处于 tracked 状态，那么 `git commit -am` 可以自动将没有 add 的变化 stage，然后一起 commit。

如果文件没有 tracked，则必须先 add。

</p>
</details>

## 与远程仓库互动

- 只克隆最新的 commit：`git clone --depth=1 url`。
- 删除对应的远程仓库地址：`git remote remove origin`。

<details>
<summary><b>仓库初始化，推送至远端</b></summary>
<p>

```bash
echo > README.md
git init
git add README.md
git commit -m "Init"
git remote add origin <git_url>
git push -u origin master
```

</p>
</details>

<details>
<summary><b>初始化身份</b></summary>
<p>

```bash
git config --global user.name <usr_name>
git config --global user.email <email>
```

</p>
</details>
