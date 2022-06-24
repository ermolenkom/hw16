import os
from dotenv import load_dotenv
import smtplib
from pathlib import Path

from email.message import EmailMessage
load_dotenv()
def f_sendemail(addr_to, subj, text, attach: str) -> None:
    '''Send EMail'''
    my_mail = os.getenv("my_email")
    mail_pass = os.getenv("my_pass") 
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(my_mail, mail_pass)
    msg = EmailMessage()
    msg["From"] = my_mail 
    msg["Subject"] = subj
    msg["To"] = addr_to
    msg.set_content(text)
    for i in [Path("main.py").absolute(), Path("sendemail.py").absolute(), Path("location.py").absolute(), Path("currency.py").absolute()]:
        msg.add_attachment(open(i, "r").read(), filename=os.path.basename(i))
    if attach:
        msg.add_attachment(open(attach, "r").read(), filename=os.path.basename(attach))
    server.send_message(msg)
    print("send_message")
    server.close()


