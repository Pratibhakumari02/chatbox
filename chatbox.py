import tkinter as tk
from tkinter import scrolledtext

class ChatBoxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Box")
        
        self.chat_window = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, state='disabled')
        self.chat_window.grid(row=0, column=0, columnspan=2)
        
        self.msg_label = tk.Label(self.root, text="Message:")
        self.msg_label.grid(row=1, column=0)
        
        self.msg_entry = tk.Entry(self.root, width=80)
        self.msg_entry.grid(row=1, column=1)
        
        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.grid(row=2, column=1, sticky='e')
        
        self.root.bind('<Return>', self.send_message)
        
    def send_message(self, event=None):
        message = self.msg_entry.get()
        if message.strip():
            self.display_message("You", message)
            self.msg_entry.delete(0, tk.END)
            self.generate_response(message)
        
    def display_message(self, sender, message):
        self.chat_window.config(state='normal')
        self.chat_window.insert(tk.END, f"{sender}: {message}\n")
        self.chat_window.config(state='disabled')
        self.chat_window.yview(tk.END)
        
    def generate_response(self, message):
        # A simple example of a chatbot with predefined responses
        response = self.chatbot_response(message)
        self.display_message("Bot", response)
        
    def chatbot_response(self, message):
        # Basic predefined responses for demonstration
        message = message.lower()
        if "hello" in message:
            return "Hello! How can I help you today?"
        elif "how are you" in message:
            return "I'm just a bot, but I'm doing fine. How about you?"
        elif "bye" in message:
            return "Goodbye! Have a great day!"
        elif "How are you ?" in message:
            return "I am good"
        else:
            return "I'm not sure how to respond to that."

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatBoxApp(root)
    root.mainloop()