import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os


load_dotenv()
EMAIL_ADDRESS=os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD=os.getenv("EMAIL_PASSWORD")


def welcome_mail(to_email: str, username: str):
    subject = "🎉 Welcome to the Employee Tracker!"
    body = f"""
Hi {username},

Welcome aboard! We're thrilled to have you with us.

Your activity will now be tracked to help improve focus and productivity.

If you have any questions, feel free to reach out!

Cheers,  
The Tracker Bot 🚀
"""
    send(to_email, subject, body)
def send(to_email: str, subject: str, body: str):
    try:
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email
        msg.set_content(body)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        print(f"✅ Email sent to {to_email} with subject: {subject}")
    except Exception as e:
        print(f"❌ Failed to send email to {to_email}: {e}")