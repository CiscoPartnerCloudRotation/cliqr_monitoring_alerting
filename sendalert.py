import smtplib
from email.mime.text import MIMEText as text
import base64

def send_email_alert(msg):
    
    sender = 'cliqr@cliqrtech.com'
    receiver = 'hunter.kaemmerling@gdt.com'
    subject = "Something really bad broke somewhere"
    Password = base64.b64decode("Z2xvY2sxNzIz")
    server = smtplib.SMTP('smtp.1and1.com')
    server.starttls()
    #server.set_debuglevel(1)
    #server.ehlo_or_helo_if_needed()

    message = """From: %s
    To: %s
    Subject: %s
    %s 
    """ % (sender, receiver, subject, msg)


    server.login("hunter@mykcrew.net",Password)
    server.sendmail(sender, receiver, message)
    #print smtplib.SMTPAuthenticationError
    #print smtplib.SMTPConnectError
    #print smtplib.SMTPException
    #print smtplib.SMTPHeloError
    server.quit()


