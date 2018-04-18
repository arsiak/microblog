from app import mail
from flask_mail import Message

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender, recipients)
    msg.body = text_body
    msg.html_body = html_body
    mail.send(msg)

