"""
Main entry point for the classroom chatbot application
"""

from chatbot.chatbot import ClassroomChatbot

def main():
    # Initialize the chatbot with CR details
    chatbot = ClassroomChatbot(
        cr_name="John Doe",
        cr_contact="john.doe@email.com"
    )
    
    print("Classroom Assistant Chatbot")
    print("Type 'quit' to exit")
    print("-" * 30)
    
    while True:
        # Get user input
        user_input = input("\nYou: ").strip()
        
        # Check for quit command
        if user_input.lower() == 'quit':
            print("\nGoodbye!")
            break
        
        # Process the query and print response
        response = chatbot.process_query(user_input)
        print(response)

if __name__ == "__main__":
    main()