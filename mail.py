import os
from flask_mail import Message

def send_reset_email(user):
    from app import app, mail
    token = user.get_reset_token()
    domain = os.getenv('FLASK_DOMAIN')
    msg = Message('Password Reset Request',
                  sender=app.config['MAIL_DEFAULT_SENDER'],
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{domain}/reset_password/{token}

If you did not make this request, simply ignore this email and no changes will be made.
'''
    mail.send(msg)