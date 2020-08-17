# GIT

- [GIT](#git)
  - [新机器初始化，生成密钥](#新机器初始化生成密钥)
  - [新仓库初始化，推送至远端](#新仓库初始化推送至远端)
  - [免密登陆](#免密登陆)
  - [清空`commit`记录](#清空commit记录)
  - [其他](#其他)

## 新机器初始化，生成密钥

- 设置身份
  
  ```bash
  git config --global user.name usrname
  git config --global user.email xx@xx
  ```

- 生成密钥
  
  ```bash
  ssh-keygen -t rsa -C xx@xx
  ```

- 把公钥提供给github
  - 找到`~\.ssh`下的公钥`id_rsa.pub`，打开，复制。
  - 放到github里。
  - 否则，私人仓库没法clone。

## 新仓库初始化，推送至远端

```bash
echo "# gitzone" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:xxx/gitzone.git
git push -u origin master
```

## 免密登陆

如果经常访问一个地址，建议彼此之间保存公私钥。

- 首先编辑`C:\Users\xxx\.ssh\config`
  
  ```jason
  Host xxx
    HostName 000.000.00.000
    User xx
  IdentityFile C:\Users\xxx\.ssh\id_rsa
  ```
  
  即指定了本地的私钥位置。
- 然后将公钥`id_rsa.pub`传到服务器的`~/.ssh/`路径下。
- 执行：`cat x1c.pub >> authorized_keys`，即将公钥加入可信列表。

今后，直接`ssh xxx`，就可以免密登录啦！

## 清空`commit`记录

[[ref]](https://stackoverflow.com/questions/13716658/how-to-delete-all-commit-history-in-github)

```bash
git checkout --orphan latest_branch

git add -A

git commit -am "haha"

git branch -D master

git branch -m master

git push -f origin master
```

注意：如果想清空仓库，要先删除文件、`add`、`commit`，然后创建一个新文件，例如`README.md`，再执行上述操作。否则第二步`git add -A`将为空，`lastest_branch`将不存在，倒数第二步将会报错。

## 其他

- 只克隆最新的commit：`git clone --depth=1 url`
- 删除对应的远程仓库地址：`git remote remove origin`
