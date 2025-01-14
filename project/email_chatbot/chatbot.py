"""
Main chatbot class that coordinates all components
"""

from .response_generator import ResponseGenerator
from .message_handler import MessageHandler

class ClassroomChatbot:
    def __init__(self, cr_name, cr_contact):
        self.response_generator = ResponseGenerator()
        self.message_handler = MessageHandler(cr_name, cr_contact)
    
    def process_query(self, query):
        """
        Process a student query and return appropriate response
        """
        response = self.response_generator.get_response(query)
        
        if response:
            return f"Chatbot: {response}"
        else:
            self.message_handler.notify_cr(query)
            return "Chatbot: I'm not sure about that. I've notified the CR who will help you with this query."