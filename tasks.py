from celery import Celery
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from decouple import config

app = Celery('task', broker='amqp://guest@localhost//')

@app.task
def send_email_task(email: str, talktome: str = None):
    message = MIMEMultipart()
    message['From'] = config('USER_EMAIL')
    message['To'] = email
    message['Subject'] = "Email communication"
    body = "Hello, this is a test email sent from a Python application."
    if talktome:
        body += f"\n\nAdditional message: {talktome}"
    message.attach(MIMEText(body, "plain"))
    
    server = smtplib.SMTP_SSL(config('EMAIL_HOST'), config('PORT'))
    server.login(config('USER_EMAIL'), config('GMAIL_THIRD_PARTY_PASSWORD'))
    server.sendmail(config('USER_EMAIL'), email, message.as_string())
    server.quit()
