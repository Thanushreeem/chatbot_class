"""
Generates responses for the chatbot
"""

from .knowledge_base import QA_DATABASE

class ResponseGenerator:
    def __init__(self):
        self.qa_database = QA_DATABASE
    
    def get_response(self, query):
        """
        Generates a response based on the input query
        """
        # Convert query to lowercase for case-insensitive matching
        query = query.lower().strip()
        
        # Check for exact matches
        if query in self.qa_database:
            return self.qa_database[query]
            
        # Check for partial matches
        for key in self.qa_database:
            if query in key or key in query:
                return self.qa_database[key]
        
        return None