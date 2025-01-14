# Classroom Assistant Chatbot

A Python-based chatbot that answers classroom-related queries and notifies the CR via email for unanswered questions.

## Setup
 virtual enviornment name is "chatbot"
1. Configure email settings:
   - Open `chatbot/config.py`
   - Replace `SENDER_EMAIL` with your Gmail address
   - Replace `SENDER_PASSWORD` with your Gmail App Password
     - To get an App Password:
       1. Go to your Google Account settings
       2. Enable 2-Step Verification if not already enabled
       3. Go to Security → App passwords
       4. Generate a new app password for "Mail"

2. Run the chatbot:
   ```bash
   python main.py
   ```

## Features
- Answers common classroom queries
- Sends email notifications to CR for unanswered questions
- Easy to extend knowledge base

## Note
Make sure to use an App Password and not your regular Gmail password. This is a security requirement from Google.