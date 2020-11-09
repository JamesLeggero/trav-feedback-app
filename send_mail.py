import smtplib
from email.mime.text import MIMEText

from dotenv import load_dotenv
load_dotenv()
import os

def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = os.environ.get('MAIL_USERNAME')
    password = os.environ.get('MAIL_PASSWORD')
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'james.m.leggero@gmail.com'
    receiver_email = 'james.m.leggero@gmail.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    #Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
