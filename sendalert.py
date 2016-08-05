import smtplib
from email.mime.text import MIMEText
import base64

"""
Change Sendter Email Address.
Change Receiver address.
Change the Subject to what you need it to me.

Enter the login info for the SMTP Server.
"""


def send_email_alert(msg):
    msg = MIMEText(msg)
    sender = 'WHO IS THIS EMAIL COMING FROM'
    receiver = 'ENTER THE EMAIL ADDRESS YOU WANT TO SEND THIS EMAIL TOO'
    subject = 'ENTER SUBJECT'
    Username = 'ENTER THE EMAIL USER NAME'
    Password = 'EMAIL Account Password'
    server = smtplib.SMTP('SMTP HOST')
    server.starttls()
    #server.set_debuglevel(1)
    server.ehlo_or_helo_if_needed()


    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    #print msg.as_string()

    server.login(Username,Password)
    server.sendmail(sender, [receiver], msg.as_string())
    server.quit()