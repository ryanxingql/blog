# 自动监测程序运行情况并发邮件通知

需求：自动监测在多台服务器上运行的程序的状态；若程序停止，自动发邮件通知。

总体流程：

1. 配置 SSH config。
2. 获取邮件服务器授权码。
3. 编辑、运行程序。

以下为具体流程。

## 配置 SSH config

假设我要在服务器 remote#1 上运行自动监测程序，待查程序（所有实验）可运行在 remote#1/2/3 上。

在 remote#1 生成 SSH 公钥：

```bash
ssh-keygen -t ed25519
```

> ED25519 相比于 RSA 对 VS Code 更友好。

修改（或新增）remote#1 的 SSH config（通常位于「~/.ssh/config」）：

```txt
Host remote#2
    HostName xx.xxx.xxx.x
    User ryan
    identityfile ~/.ssh/id_ed25519

Host remote#3
    HostName xx.xxx.xxx.x
    User ryan
    identityfile ~/.ssh/id_ed25519
```

把 remote#1 的公钥发送到 remote#2/3 上，方便之后 remote#1 通过 SSH 连接并查看 remote#2/3。在 remote#1 上执行：

```bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub remote#2
ssh-copy-id -i ~/.ssh/id_ed25519.pub remote#3
```

## 获取邮件服务器授权码

我使用的是 QQ 邮箱发送提醒邮件。还可以使用 163 邮箱等，请参考[文章](https://zhuanlan.zhihu.com/p/89868804)。

拿到授权码请记录下来。

## 修改并运行程序

逻辑：

- 通过输入参数，将待查程序的名称、所在服务器、以及 PID 输入监测程序。
- 程序要求输入邮箱授权码。为了安全，授权码不以明文方式记录下来。
- 程序发送第一封邮件，表示邮件系统正常。
- 间隔一段时间查一次。如果有异常，发送邮件；否则静默。
- 通过监测 PID 状态来判断程序运行情况。
  - 如果待查程序和监测程序不在同一服务器上，需要通过 SSH 连接。
- 如果距离上一次发邮件过去了较长时间，发送一封报平安邮件。

最终的主程序在[这里](../demo/check_pid/main.py)。直接运行即可。注意修改其输入参数。

重要参数解释：

- `monitor`：运行该监测程序的服务器名称。如果待查程序运行在同一服务器上，则监测无需 SSH，否则需要 SSH。
- `cfg`：按照字典格式，将待查程序的实验名称、所在服务器、以及 PID（选择一个进程的 PID 就行）记录为字符串。
