# 自动检查程序运行情况并发邮件通知

需求：自动检查多台服务器上的程序运行情况，如果程序停止，自动发邮件通知。

大致流程：

1. 配置 SSH config。
2. 获取邮件服务器授权码。
3. 配置其他所需信息。
4. 运行程序。

以下为具体流程。

## 配置 SSH config

假设我要在服务器 remote-1 上运行自动检查程序，程序可能运行在 remote-1/2/3 上。那么修改 remote-1 的 SSH config：

```txt
Host remote-2
    HostName xx.xxx.xxx.x
    User ryan
    identityfile ~/.ssh/id_rsa

Host remote-3
    HostName xx.xxx.xxx.x
    User ryan
    identityfile ~/.ssh/id_rsa
```

把 remote-1 的公钥发送到 remote-2/3 上，方便之后 remote-1 检查 remote-2/3 的情况。在 remote-1 上执行：

```bash
$ ssh-copy-id -i ~/.ssh/id_rsa.pub remote-2
$ ssh-copy-id -i ~/.ssh/id_rsa.pub remote-3
```

## 获取邮件服务器授权码

我使用的是 QQ 邮箱发送提醒邮件。还可以使用 163 邮箱等，请参考[文章](https://zhuanlan.zhihu.com/p/89868804)。

拿到授权码请记录下来。

## 配置其他所需信息

以下为样例，请参考备注修改，保存为 config.yaml。

```yaml
time_step: 10 # X分钟查一次
regular_send_time_step: 8 # X小时报一次平安

# 服务器
# 通过密钥认证登陆，因此第一步需要配置 SSH config
hosts:
  remote-1:
    user: ryan # 登陆用户名
    if_local: True # 就是本机，不需要 SSH
  remote-2:
    user: ryan
  remote-3:
    user: ryan

# 待检程序
profiles:
  exp1: # 实验名；随便起
    host: remote-1 # 在 remote-1 上运行
    pid: 2721185 # 用 nvidia-smi 查看 PID；多进程记录一个 PID 即可
  exp2:
    host: remote-3
    pid: 68239

# 邮件部分
if_email: True # 是否开启邮件提醒功能
email_cfg:
  mail_host: smtp.qq.com # 发件邮箱
  name: ryan # 收发件人名；随便起
  mail_sender: ryanyyds@foxmail.com # 发信地址
  mail_license: aabbcc # 发信邮箱授权码
  mail_receivers: ryanyyds@foxmail.com # 收信地址；可以简单设置为自己发给自己
  subject_content: "Auto PID Check" # 邮件标题
```

## 运行程序

将以下两个程序与「config.yaml」放置在同一路径下，然后直接运行：`$ python main.py`

```txt
toolbox/
|-- config.yaml
|-- main.py
`-- send_email.py
```

程序：「send_email.py」

```python
# https://zhuanlan.zhihu.com/p/89868804
# https://stackoverflow.com/a/52442331
import smtplib
from contextlib import contextmanager, redirect_stderr, redirect_stdout
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import devnull


@contextmanager
def suppress_stdout_stderr():
    """A context manager that redirects stdout and stderr to devnull"""
    with open(devnull, 'w') as fnull:
        with redirect_stderr(fnull) as err, redirect_stdout(fnull) as out:
            yield (err, out)


def send_email(
    mail_host,
    name,
    mail_sender,
    mail_license,
    mail_receivers,
    subject_content,
    body_content,
):
    mm = MIMEMultipart('related')

    mm['From'] = f'{name}<{mail_sender}>'
    mm['To'] = f'{name}<{mail_receivers}>'

    mm['Subject'] = Header(subject_content, 'utf-8')

    message_text = MIMEText(body_content, 'plain', 'utf-8')
    mm.attach(message_text)

    stp = smtplib.SMTP()
    stp.set_debuglevel(2)
    stp.connect(mail_host, 587)
    stp.login(mail_sender, mail_license)
    stp.sendmail(mail_sender, mail_receivers, mm.as_string())
    stp.quit()


def send_email_silent(
    mail_host,
    name,
    mail_sender,
    mail_license,
    mail_receivers,
    subject_content,
    body_content,
    if_silent=True,
):
    if if_silent:
        with suppress_stdout_stderr():
            send_email(
                mail_host=mail_host,
                name=name,
                mail_sender=mail_sender,
                mail_license=mail_license,
                mail_receivers=mail_receivers,
                subject_content=subject_content,
                body_content=body_content,
            )
    else:
        send_email(
            mail_host=mail_host,
            name=name,
            mail_sender=mail_sender,
            mail_license=mail_license,
            mail_receivers=mail_receivers,
            subject_content=subject_content,
            body_content=body_content,
        )


if __name__ == '__main__':
    send_email_silent(
        mail_host='smtp.qq.com',
        name='ryan',
        mail_sender='ryanyyds@foxmail.com',
        mail_license='aabbcc',
        mail_receivers='ryanyyds@foxmail.com',
        subject_content='Test',
        body_content='Test.',
    )
```

程序：「main.py」

```python
import subprocess
import time
import yaml

with open('config.yaml', 'r') as f:
    cfg = yaml.safe_load(f)

time_step = cfg['time_step'] * 60
hosts = cfg['hosts']
profiles = cfg['profiles']
if_email = cfg['if_email']

if if_email:
    from send_email import send_email_silent

    regular_send_time_step = cfg['regular_send_time_step'] * 3600
    email_cfg = cfg['email_cfg']

    last_time_stamp = time.time()
    send_email_silent(
        body_content="Auto check has started.",
        **cfg['email_cfg'],
    )

if if_email:
    if_emailed = dict()
    for exp_name in profiles:
        if_emailed[exp_name] = False


def check_connection(login_info, port=22):
    try:
        cmd = f'ssh -p {port} {login_info} "exit"'
        subprocess.call(cmd, shell=True, stdout=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False


def check_pid(login_info, pid, if_local=False, port=22):
    if if_local:
        cmd = f'ps -o pid= -p {pid}'
    else:
        cmd = f'ssh -p {port} {login_info} "ps -o pid= -p {pid}"'
    try:
        subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, check=True)
        return True
    except subprocess.CalledProcessError:
        return False


while True:
    print(f"\nStart: [{time.strftime('%H:%M', time.localtime())}]")

    lost_hosts = []
    for exp_name, profile in profiles.items():
        host = profile['host']
        host_profile = hosts[host]
        if host in lost_hosts:
            print(f'Skip: [{exp_name}]')
            continue

        if_local = (True if ('if_local' in host_profile
                             and host_profile['if_local']) else False)

        login_info = f"{host_profile['user']}@{host}"
        if not if_local:
            if_connected = check_connection(
                login_info=login_info,
                port=22,
            )
            if not if_connected:
                warn_info = f'CONNECTION LOST: [{login_info}]'
                print(warn_info)
                lost_hosts.append(host)
                if if_email and (not if_emailed[exp_name]):
                    send_email_silent(
                        body_content=warn_info,
                        **cfg['email_cfg'],
                    )
                    if_emailed[exp_name] = True
                continue

        pid = profile['pid']
        if_running = check_pid(
            login_info=login_info,
            pid=pid,
            port=22,
            if_local=if_local,
        )
        if if_running:
            print(f'Running: [{host}] - [{exp_name}]')
            if_emailed[exp_name] = False

        else:
            warn_info = f'PID NOT FOUND: [{host}] - [{exp_name}]'
            print(warn_info)
            if if_email and (not if_emailed[exp_name]):
                send_email_silent(
                    body_content=warn_info,
                    **cfg['email_cfg'],
                )
                if_emailed[exp_name] = True

    normal_gap = int(time.time() - last_time_stamp)
    if if_email and normal_gap > regular_send_time_step:
        send_email_silent(
            body_content='Checking normally.',
            **cfg['email_cfg'],
        )
    last_time_stamp = time.time()

    print(f'Sleep for {time_step:d}s: '
          f"[{time.strftime('%H:%M', time.localtime())}]")
    time.sleep(time_step)
```
