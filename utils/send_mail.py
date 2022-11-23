import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

def send_email(sender, receiver, password, subject, body):

    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
   
    session = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    session.connect("smtp.gmail.com", 465)

    session.login(sender, password)
    text = message.as_string()
    session.sendmail(sender, receiver, text)

    session.quit()
    print('email sent!')