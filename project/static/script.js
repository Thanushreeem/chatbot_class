class ChatBot {
    constructor() {
        this.messageInput = document.getElementById('message-input');
        this.sendButton = document.getElementById('send-button');
        this.chatMessages = document.getElementById('chat-messages');
        
        this.setupEventListeners();
        this.addMessage('Hello! :D', 'bot');
    }

    setupEventListeners() {
        this.sendButton.addEventListener('click', () => this.handleSendMessage());
        this.messageInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.handleSendMessage();
            }
        });
    }

    async handleSendMessage() {
        const message = this.messageInput.value.trim();
        if (!message) return;

        // Clear input
        this.messageInput.value = '';

        // Add user message to chat
        this.addMessage(message, 'user');

        // Get bot response
        const response = await this.getBotResponse(message);
        this.addMessage(response, 'bot');
    }

    async getBotResponse(message) {
        try {
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message })
            });
            
            const data = await response.json();
            return data.response;
        } catch (error) {
            console.error('Error:', error);
            return "Sorry, I'm having trouble connecting to my brain right now.";
        }
    }

    addMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}`;
        
        const avatar = document.createElement('div');
        avatar.className = 'message-avatar';
        
        const content = document.createElement('div');
        content.className = 'message-content';
        content.textContent = text;
        
        const time = document.createElement('div');
        time.className = 'message-time';
        time.textContent = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        
        messageDiv.appendChild(avatar);
        messageDiv.appendChild(content);
        messageDiv.appendChild(time);
        
        this.chatMessages.appendChild(messageDiv);
        this.chatMessages.scrollTop = this.chatMessages.scrollHeight;
    }
}

// Initialize the chatbot when the page loads
document.addEventListener('DOMContentLoaded', () => {
    new ChatBot();
});