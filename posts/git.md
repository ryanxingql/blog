# GIT

- [GIT](#git)
  - [SSH](#ssh)
  - [Repository](#repository)

## SSH

<details>
<summary><b>机器初始化，生成密钥</b></summary>

设置身份：
  
```bash
git config --global user.name usrname
git config --global user.email xx@xx
```

生成密钥：
  
```bash
ssh-keygen -t rsa -C xx@xx
```

把公钥提供给 GITHUB；否则私人仓库没法 clone。

- 找到 `~\.ssh` 下的公钥 `id_rsa.pub`，打开，复制。
- 放到 GITHUB 里。

</details>

<details>
<summary><b>免密登陆</b></summary>

如果经常访问一个地址，建议彼此之间保存公私钥。

首先在本地编辑`C:\Users\xxx\.ssh\config`或`~/.ssh/config`（没有就新建）：
  
```jason
Host xxx
  HostName 000.000.00.000
  User xx
IdentityFile C:\Users\xxx\.ssh\id_rsa
```

最后一行指定了本地的私钥位置。会自动发送给服务器，和以下的公钥合作，以识别身份。

然后将本地公钥 `id_rsa.pub` 传到服务器的 `~/.ssh/` 路径下：
  
```bash
scp id_rsa.pub xxx:~/.ssh/hello.pub
```
  
一定要改名！！！不要覆盖了服务器的 `id_ras.pub`！

在服务器 `~/.ssh/` 下执行
  
```bash
cat hello.pub >> authorized_keys
```

即将公钥加入可信列表。

今后，直接 `ssh xxx`，就可以免密登录啦！

</details>

## Repository

<details>
<summary><b>只克隆最新的 commit</b></summary>

```bash
git clone --depth=1 url
```

</details>

<details>
<summary><b>仓库初始化，推送至远端</b></summary>

```bash
echo "# gitzone" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:xxx/gitzone.git
git push -u origin master
```

</details>

<details>
<summary><b>submodule</b></summary>

可以调用一个仓库，作为当前仓库的一个子模块。例如：

```bash
# clone PythonUtils，存为utils
git submodule add git@github.com:RyanXingQL/PythonUtils.git utils/
```

更新子模块需要进入子模块手动更新。

- 当前库只记录子仓库的当前版本，不会自动更新。
- 假设有两个本地仓库对应同一个远程仓库；如果不手动更新子仓库，会出现两个本地仓库来回扯皮版本号的情况。

</details>

<details>
<summary><b>删除对应的远程仓库地址</b></summary>

```bash
git remote remove origin
```

</details>

<details>
<summary><b>清空 commit 记录</b></summary>

```bash
git checkout --orphan latest_branch

git add -A

git commit -am "haha"

git branch -D main

git branch -m main

git push -f origin main
```

[【stackover 某 up】](https://stackoverflow.com/questions/13716658/how-to-delete-all-commit-history-in-github)

</details>
