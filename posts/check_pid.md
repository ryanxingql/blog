# 自动检查程序运行情况并发邮件通知

需求：自动检查多台服务器上的程序运行情况，如果程序停止，自动发邮件通知。

大致流程：

1. 配置 SSH config。
2. 获取邮件服务器授权码。
3. 运行程序。

以下为具体流程。

## 配置 SSH config

假设我要在服务器 remote#1 上运行自动检查程序，程序可能运行在 remote#1/2/3 上。那么修改 remote#1 的 SSH config（通常位于 "~/.ssh/config"）：

```txt
Host remote#1
    HostName xx.xxx.xxx.x
    User ryan
    identityfile ~/.ssh/id_rsa

Host remote#3
    HostName xx.xxx.xxx.x
    User ryan
    identityfile ~/.ssh/id_rsa
```

把 remote#1 的公钥发送到 remote#2/3 上，方便之后 remote#1 通过 SSH 连接并查看 remote#2/3。在 remote#1 上执行：

```bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub remote#2
ssh-copy-id -i ~/.ssh/id_ed25519.pub remote#3
```

> 如果公钥不存在，需要先生成：
>
> ```bash
> ssh-keygen -t ed25519
> ```

## 获取邮件服务器授权码

我使用的是 QQ 邮箱发送提醒邮件。还可以使用 163 邮箱等，请参考[文章](https://zhuanlan.zhihu.com/p/89868804)。

拿到授权码请记录下来。

## 修改并运行程序

将以下两个程序放置在同一路径下，然后直接运行：`python main.py`

```txt
toolbox
|-- send_email.py
`-- main.py
```

程序：「send_email.py」

```python
import smtplib
from contextlib import contextmanager, redirect_stderr, redirect_stdout
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import devnull


@contextmanager
def suppress_stdout_stderr():
    """A context manager that redirects stdout and stderr to devnull."""
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
        mail_sender='ryan@foxmail.com',
        mail_license='aaabbbccc',
        mail_receivers='ryan@foxmail.com',
        subject_content='Test',
        body_content='Test.',
    )
```

程序：「main.py」

```python
import argparse
import ast
import copy
import subprocess
import time


def check_connection(login_info):
    try:
        cmd = f'ssh {login_info} "exit"'
        subprocess.call(cmd, shell=True, stdout=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False


def check_pid(login_info, pid, if_local=False):
    if if_local:
        cmd = f'ps -o pid= -p {pid}'
    else:
        cmd = f'ssh {login_info} "ps -o pid= -p {pid}"'
    try:
        subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, check=True)
        return True
    except subprocess.CalledProcessError:
        return False


def ret_time():
    return time.strftime('%H:%M', time.localtime())


def ret_overview(profiles):
    ret_str = f'Time: {ret_time()}\n'
    for status, pros in profiles.items():
        if pros:  # not empty
            ret_str += f'{status.capitalize()}:\n'
            count = 0
            for exp_name, pro in pros.items():
                count += 1
                host = pro['host']
                ret_str += f'{count}. {exp_name} @ {host}\n'
    return ret_str


parser = argparse.ArgumentParser()
parser.add_argument('-m', '--monitor', type=str, default='remote#1')
parser.add_argument(
    '-c',
    '--cfg',
    type=str,
    default=r"{'exp1': {'host': 'remote#1', 'pid': 26550}, 'exp2': {'host': 'remote#3', 'pid': 1200}}")
parser.add_argument('--check-inter-sec',
                    type=int,
                    default=600,
                    help='check once every N seconds')
parser.add_argument('--regular-report-inter-sec',
                    type=int,
                    default=36000,
                    help='report safety once every N seconds')
parser.add_argument('--if-email', action='store_false')
parser.add_argument('--mail-host',
                    type=str,
                    default='smtp.qq.com',
                    help='sender email host')
parser.add_argument('--mail-name',
                    type=str,
                    default='ryan',
                    help='sender/receiver name')
parser.add_argument('--mail-sender',
                    type=str,
                    default='ryan@foxmail.com',
                    help='sender email address')
parser.add_argument('--mail-license',
                    type=str,
                    default='aaabbbccc',
                    help='sender email key')
parser.add_argument('--mail-receivers',
                    type=str,
                    default='ryan@foxmail.com',
                    help='receiver email address')
args = parser.parse_args()

profiles = dict(running=ast.literal_eval(args.cfg), lost=dict(), ended=dict())

overview = ret_overview(profiles)
print('\n' + overview)

if args.if_email:
    from send_email import send_email_silent

    email_cfg = dict(mail_host=args.mail_host,
                     name=args.mail_name,
                     mail_sender=args.mail_sender,
                     mail_license=args.mail_license,
                     mail_receivers=args.mail_receivers,
                     subject_content=f'Automatic PID Check @ {args.monitor}')
    send_email_silent(body_content=overview, **email_cfg)
    latest_email_timestamp = time.time()

while True:
    profiles_backup = copy.deepcopy(profiles)
    for exp_name, profile in profiles_backup['running'].items():
        host = profile['host']
        pid = profile['pid']

        # SSH connection check
        login_info = host
        if_local = True if host == args.monitor else False
        if not if_local:
            if_connected = check_connection(login_info=login_info)
            if not if_connected:
                profiles['lost'][exp_name] = profile
                del profiles['running'][exp_name]
                continue  # skip checking

        # PID check
        if_running = check_pid(login_info=login_info,
                               pid=pid,
                               if_local=if_local)
        if not if_running:
            profiles['ended'][exp_name] = profile
            del profiles['running'][exp_name]

    # report
    if profiles != profiles_backup:  # something changed
        overview = ret_overview(profiles)
        print('\n' + overview)
        send_email_silent(body_content=overview, **email_cfg)
        latest_email_timestamp = time.time()
    else:
        email_gap = int(time.time() - latest_email_timestamp)
        if args.if_email and email_gap > args.regular_report_inter_sec:
            overview = ret_overview(profiles)
            print('\n' + overview)
            send_email_silent(body_content=overview, **email_cfg)
            latest_email_timestamp = time.time()

    time.sleep(args.check_inter_sec)
```

调整「main.py」的参数，直接运行「main.py」即可。重要参数解释：

- `monitor`：运行该检查程序的服务器名称。如果待查程序正好位于该服务器上，则无需 SSH，否则需要 SSH。
- `cfg`：按照字典格式，将待查程序的实验名称、所在服务器、以及 PID（选择一个进程的 PID 就行）记录为字符串。
- `mail-license`：邮箱授权码。

逻辑：

1. 解析 `cfg`，得到待查程序字典。将待查字典发送邮件。
2. 通过检查 PID 状态来判断程序运行情况。需要借助 SSH 连接其他服务器。
3. 每 `check-inter-sec` 秒查一次。如果有异常，发送邮箱，否则静默。
4. 如果距离上一次发邮件超过 `regular-report-inter-sec` 秒，发送一封报平安邮件。
