"""
Email service for sending notifications
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from .config import SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD

class EmailService:
    @staticmethod
    def send_email(recipient_email, subject, message):
        """
        Send an email using SMTP
        """
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = SENDER_EMAIL
            msg['To'] = recipient_email
            msg['Subject'] = subject

            # Add body
            msg.attach(MIMEText(message, 'plain'))

            # Create SMTP session
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(SENDER_EMAIL, SENDER_PASSWORD)
                server.send_message(msg)
            
            return True
        except Exception as e:
            print(f"Failed to send email: {str(e)}")
            return False