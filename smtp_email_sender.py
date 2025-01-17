import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_personalized_email(sender_email, sender_password, recipients, subject, body):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    for recipient_email in recipients:
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))
        server.send_message(message)
    server.quit()


# 使用示例
sender_email = "your_email@gmail.com"
sender_password = "your_password"
recipients = ["recipient1@example.com", "recipient2@example.com"]
subject = "Hello"
body = "This is a test email."
send_personalized_email(sender_email, sender_password, recipients, subject, body)
