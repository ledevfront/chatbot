from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import QDate, QTime, Qt

class ChatbotApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chatbot in Python - PyQt5")
        self.setGeometry(100, 100, 400, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.create_widgets()
        self.say_hello()

    def create_widgets(self):
        self.chatbox = QTextEdit(self)
        self.chatbox.setReadOnly(True)

        self.chat_input = QLineEdit(self)

        send_button = QPushButton("Send", self)
        send_button.clicked.connect(self.handle_chat)

        layout = QVBoxLayout(self.central_widget)
        layout.addWidget(self.chatbox)
        layout.addWidget(self.chat_input)
        layout.addWidget(send_button)

    def say_hello(self):
        # Message de salutation
        hello_message = "Hello! I'm your chatbot. How can I assist you today?"
        self.chatbox.append(f"Bot: {hello_message}")

        # Obtenir la date et l'heure actuelles
        current_date = QDate.currentDate().toString(Qt.DefaultLocaleLongDate)
        current_time = QTime.currentTime().toString(Qt.DefaultLocaleLongDate)

        # Afficher la date et l'heure dans la zone de texte du chat
        self.chatbox.append(f"Bot: Today's date is {current_date}.")
        self.chatbox.append(f"Bot: The current time is {current_time}.\n")

    def handle_chat(self):
        user_message = self.chat_input.text().strip()
        if not user_message:
            return

        # Simuler la réponse du chat (remplacez par une logique réelle)
        response = "Thinking... (PyQt5 version)"

        # Mettre à jour la zone de texte du chat
        self.chatbox.append(f"User: {user_message}")
        self.chatbox.append(f"Bot: {response}")
        self.chatbox.append("")

        # Effacer l'entrée
        self.chat_input.clear()

if __name__ == "__main__":
    app = QApplication([])
    window = ChatbotApp()
    window.show()
    app.exec_()
