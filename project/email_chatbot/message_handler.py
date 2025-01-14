"""
Handles messaging functionality for the chatbot
"""

from .email_service import EmailService

class MessageHandler:
    def __init__(self, cr_name, cr_contact):
        self.cr_name = cr_name
        self.cr_contact = cr_contact
        self.email_service = EmailService()
    
    def notify_cr(self, student_query):
        """
        Sends an email notification to the CR about an unanswered query
        """
        subject = "Unhandled Student Query"
        message = f"""
Dear {self.cr_name},

A student has asked a question that the chatbot couldn't answer:

Query: "{student_query}"

Please address this query at your earliest convenience.

Best regards,
Classroom Assistant Chatbot
"""
        
        # Send email
        if self.email_service.send_email(self.cr_contact, subject, message):
            print(f"\nNotification email sent to CR ({self.cr_name})")
        else:
            print(f"\nFailed to send email notification to CR ({self.cr_name})")
            # Fallback to console notification
            print(f"Contact: {self.cr_contact}")
            print(f"Unhandled student query: '{student_query}'")