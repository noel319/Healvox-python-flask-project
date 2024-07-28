from flask_mail import Message
import os
from app.extensions import mail


def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=os.getenv('MAIL_DEFAULT_SENDER'),
    )
    mail.send(msg)
