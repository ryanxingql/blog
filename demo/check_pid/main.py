import argparse
import ast
import copy
import subprocess
import time
from getpass import getpass


def check_connection(login_info):
    try:
        cmd = f'ssh {login_info} "exit"'
        subprocess.call(cmd, shell=True, stdout=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False


def check_pid(login_info, pid, if_local=False):
    if if_local:
        cmd = f"ps -o pid= -p {pid}"
    else:
        cmd = f'ssh {login_info} "ps -o pid= -p {pid}"'
    try:
        subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, check=True)
        return True
    except subprocess.CalledProcessError:
        return False


def ret_time():
    return time.strftime("%H:%M", time.localtime())


def ret_overview(profiles):
    ret_str = f"Time: {ret_time()}\n"
    for status, pros in profiles.items():
        if pros:  # not empty
            ret_str += f"{status.capitalize()}:\n"
            count = 0
            for exp_name, pro in pros.items():
                count += 1
                host = pro["host"]
                ret_str += f"{count}. {exp_name} @ {host}\n"
    return ret_str


parser = argparse.ArgumentParser()
parser.add_argument("-m", "--monitor", type=str, default="tao9")
parser.add_argument(
    "-c",
    "--cfg",
    type=str,
    default=r"{'basicvsrpp_vimeo_sep': {'host': '40901', 'pid': 26550}}",
)
parser.add_argument(
    "--check-inter-sec", type=int, default=600, help="check once every N seconds"
)
parser.add_argument(
    "--regular-report-inter-sec",
    type=int,
    default=36000,
    help="report safety once every N seconds",
)
parser.add_argument("--if-email", action="store_false")
parser.add_argument(
    "--mail-host", type=str, default="smtp.qq.com", help="sender email host"
)
parser.add_argument(
    "--mail-name", type=str, default="ryan", help="sender/receiver name"
)
parser.add_argument(
    "--mail-sender", type=str, default="ryan@foxmail.com", help="sender email address"
)
parser.add_argument(
    "--mail-receivers",
    type=str,
    default="ryan@foxmail.com",
    help="receiver email address",
)
args = parser.parse_args()

profiles = dict(running=ast.literal_eval(args.cfg), lost=dict(), ended=dict())

overview = ret_overview(profiles)
print("\n" + overview)

if args.if_email:
    from send_email import send_email_silent

    mail_license = getpass("Please enter your mail license: ")
    email_cfg = dict(
        mail_host=args.mail_host,
        name=args.mail_name,
        mail_sender=args.mail_sender,
        mail_license=mail_license,
        mail_receivers=args.mail_receivers,
        subject_content=f"Automatic PID Check @ {args.monitor}",
    )
    send_email_silent(body_content=overview, **email_cfg)
    print("Sent.")
    latest_email_timestamp = time.time()

while True:
    profiles_backup = copy.deepcopy(profiles)
    for exp_name, profile in profiles_backup["running"].items():
        host = profile["host"]
        pid = profile["pid"]

        # SSH connection check
        login_info = host
        if_local = True if host == args.monitor else False
        if not if_local:
            if_connected = check_connection(login_info=login_info)
            if not if_connected:
                profiles["lost"][exp_name] = profile
                del profiles["running"][exp_name]
                continue  # skip checking

        # PID check
        if_running = check_pid(login_info=login_info, pid=pid, if_local=if_local)
        if not if_running:
            profiles["ended"][exp_name] = profile
            del profiles["running"][exp_name]

    # report
    if profiles != profiles_backup:  # something changed
        overview = ret_overview(profiles)
        print("\n" + overview)
        send_email_silent(body_content=overview, **email_cfg)
        print("Sent.")
        latest_email_timestamp = time.time()
    else:
        email_gap = int(time.time() - latest_email_timestamp)
        if args.if_email and email_gap > args.regular_report_inter_sec:
            overview = ret_overview(profiles)
            print("\n" + overview)
            send_email_silent(body_content=overview, **email_cfg)
            print("Sent.")
            latest_email_timestamp = time.time()

    time.sleep(args.check_inter_sec)
