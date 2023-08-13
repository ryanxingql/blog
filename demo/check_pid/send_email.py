import smtplib
from contextlib import contextmanager, redirect_stderr, redirect_stdout
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import devnull


@contextmanager
def suppress_stdout_stderr():
    """A context manager that redirects stdout and stderr to devnull."""
    with open(devnull, "w") as fnull:
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
    mm = MIMEMultipart("related")

    mm["From"] = f"{name}<{mail_sender}>"
    mm["To"] = f"{name}<{mail_receivers}>"

    mm["Subject"] = Header(subject_content, "utf-8")

    message_text = MIMEText(body_content, "plain", "utf-8")
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


if __name__ == "__main__":
    send_email_silent(
        mail_host="smtp.qq.com",
        name="ryan",
        mail_sender="ryan@foxmail.com",
        mail_license="aaabbbccc",
        mail_receivers="ryan@foxmail.com",
        subject_content="Test",
        body_content="Test.",
    )
