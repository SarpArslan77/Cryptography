import sys
import random

from PyQt5.QtWidgets import (
    QApplication, QWidget, QTreeWidget, QTreeWidgetItem, QLineEdit, 
    QTextEdit, QPushButton, QFileDialog
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from simple_substitution_ciphers import Simple_Substition_Ciphers
from polyalphabetic_ciphers import Polyalphabetic_Ciphers
from transposition_ciphers import Transposition_Ciphers

#TODO: add scrolling

class GUI(QWidget):

    def __init__(self, substitution_ciphers: Simple_Substition_Ciphers, polyalphabetic_ciphers: Polyalphabetic_Ciphers, transposition_ciphers: Transposition_Ciphers):
        """
        Initialize the GUI for the cryptography application.

        Parameters:
        - substitution_ciphers: Instance of Substition_Ciphers for encryption/decryption
        - polyalphabetic_ciphers: Instance of Polyalphabetic_Ciphers for encryption/decryption
        """
        super().__init__()
        self.substitution_ciphers = substitution_ciphers
        self.polyalphabetic_ciphers = polyalphabetic_ciphers
        self.transposition_ciphers = transposition_ciphers
        self.item_name = None  # Currently selected encryption/decryption method

        self.setWindowTitle("Learn Cryptography 101")
        self.setWindowIcon(QIcon("C:/Users/Besitzer/Desktop/Python/In Progress/Cryptology/images/web_logo.png"))
        
        # Setup UI components
        self.encryption_tree_widget = QTreeWidget(self)
        self.encryption_tree_widget.setHeaderLabel("Encryption Methods")
        self.encryption_tree_widget.move(50, 50)
        self.encryption_tree_widget.setFixedSize(300, 300)
        self.encryption_tree_widget.itemClicked.connect(self.on_item_clicked)
        self.encryption_tree_widget.itemClicked.connect(self.update_text_holder)

        self.decryption_tree_widget = QTreeWidget(self)
        self.decryption_tree_widget.setHeaderLabel("Decryption Methods")
        self.decryption_tree_widget.move(50, 400)
        self.decryption_tree_widget.setFixedSize(300, 300)
        self.decryption_tree_widget.itemClicked.connect(self.on_item_clicked)
        self.decryption_tree_widget.itemClicked.connect(self.update_text_holder)
        
        self.output_text = QTextEdit(self)
        self.output_text.move(400, 100)
        self.output_text.setFixedSize(800, 800)
        self.output_text.setReadOnly(True)

        self.note_area1 = QTextEdit(self)
        self.note_area1.move(1300, 50)
        self.note_area1.setFixedSize(150, 150)
        self.copy_note_area1 = QPushButton("Copy Note 1", self)
        self.copy_note_area1.move(1300, 200)
        self.copy_note_area1.setFixedSize(75, 30)
        self.copy_note_area1.clicked.connect(lambda: self.copy_note(self.note_area1))


        self.note_area2 = QTextEdit(self)
        self.note_area2.move(1300, 300)
        self.note_area2.setFixedSize(150, 150)
        self.copy_note_area2 = QPushButton("Copy Note 2", self)
        self.copy_note_area2.move(1325, 450)
        self.copy_note_area2.clicked.connect(lambda: self.copy_note(self.note_area2))

        self.note_area3 = QTextEdit(self)
        self.note_area3.move(1300, 550)
        self.note_area3.setFixedSize(150, 150)
        self.copy_note_area3 = QPushButton("Copy Note 3", self)
        self.copy_note_area3.move(1325, 700)
        self.copy_note_area3.clicked.connect(lambda: self.copy_note(self.note_area3))    
    
        self.note_area4 = QTextEdit(self)
        self.note_area4.move(1300, 800)
        self.note_area4.setFixedSize(150, 150)
        self.copy_note_area4 = QPushButton("Copy Note 4", self)
        self.copy_note_area4.move(1325, 950)
        self.copy_note_area4.clicked.connect(lambda: self.copy_note(self.note_area4))
        
        self.save_text_button = QPushButton("Save as .txt", self)
        self.save_text_button.move(400, 925)
        self.save_text_button.clicked.connect(lambda: self.save_text())

        self.load_text_button = QPushButton("Load a text", self)
        self.load_text_button.move(525, 925)
        self.load_text_button.clicked.connect(lambda: self.load_text())

        self.random_text_generator_button = QPushButton("Create a random text", self)
        self.random_text_generator_button.move(650, 925)
        self.random_text_generator_button.clicked.connect(lambda: self.create_random_text(self.input_line_first.text().upper()))


        # Input fields for text and key
        self.input_line_first = QLineEdit(self)
        self.input_line_first.move(400, 50)
        self.input_line_first.setFixedSize(500, 25)
        self.input_line_first.setPlaceholderText("Choose a encryption/decryption method to see the needed inputs")
        self.input_line_first.setStyleSheet("QlineEdit {color:ligthgray; }")

        self.input_line_second = QLineEdit(self)
        self.input_line_second.move(925, 50)
        self.input_line_second.setFixedSize(275, 25)
        self.input_line_second.setPlaceholderText("Choose a encryption/decryption method to see the needed inputs")
        self.input_line_second.setStyleSheet("QlineEdit {color:ligthgray; }")

        self.populate_tree()
        self.input_line_first.returnPressed.connect(self.process_input)
        self.input_line_second.returnPressed.connect(self.process_input)

        # Available encryption/decryption methods
        self.encryption_simple_substitution_functions: list[str] = ["caeser_cipher", "random_substition"]
        self.decryption_simple_substitution_functions: list[str] = ["brute_force_caesers_cipher", "frequency_analysis"]

        self.encryption_polyalphabetic_functions: list[str] = ["vigenere_cipher", "vernam_cipher"]
        self.decryption_polyalphabetic_functions: list[str] = ["crack_polyalphabetic_cipher"]

        self.encryption_transposition_functions: list[str] = ["rail_fence"]

        # open the app in windowed-full-screen mode
        self.screen_geometry = QApplication.desktop().screenGeometry()
        self.setGeometry(0, 0, self.screen_geometry.width(), self.screen_geometry.height())

        self.show()

    def process_input(self):
        """
        Process user input and perform encryption/decryption based on selected method.
        Displays results in the output text box.
        """

        if not self.item_name:
            self.output_text.append("Please select an encryption/decryption method first.\n")
            return

        if (self.item_name in self.encryption_simple_substitution_functions) or (self.item_name in self.decryption_simple_substitution_functions):

            self.substitution_ciphers.input_text = self.input_line_first.text().upper()
            
            if self.item_name in self.encryption_simple_substitution_functions:
                encrypted_text = self.substitution_ciphers.encrypt(self.item_name)
                self.output_text.append(f"Input: {self.substitution_ciphers.input_text}")
                self.output_text.append(f"Encrypted ({self.item_name}): {encrypted_text}\n")
            else:
                self.substitution_ciphers.decrypted_final_text = self.substitution_ciphers.decrypt(self.item_name)
                self.output_text.append(f"Input: {self.substitution_ciphers.input_text}")
                self.output_text.append(f"Decrypted ({self.item_name}) : {self.substitution_ciphers.decrypted_final_text}")

        elif (self.item_name in self.encryption_polyalphabetic_functions) or (self.item_name in self.decryption_polyalphabetic_functions):

            self.polyalphabetic_ciphers.input_text = self.input_line_first.text().upper()
            self.polyalphabetic_ciphers.input_key = self.input_line_second.text().upper()

            if (not self.polyalphabetic_ciphers.input_key) or (not self.polyalphabetic_ciphers.input_text):
                self.output_text.append("Either key or the input is missing")
                return
            
            if self.item_name in self.encryption_polyalphabetic_functions:
                self.polyalphabetic_ciphers.encrypted_final_text = self.polyalphabetic_ciphers.encrypt(self.item_name)
                self.output_text.append(f"Input: {self.polyalphabetic_ciphers.input_text}")
                self.output_text.append(f"Encrypted ({self.item_name}): {self.polyalphabetic_ciphers.encrypted_final_text}\n")
            else:
                self.polyalphabetic_ciphers.decrypted_final_text = self.polyalphabetic_ciphers.decrypt(self.item_name)
                self.output_text.append(f"Input: {self.polyalphabetic_ciphers.input_text}")
                self.output_text.append(f"Decrypted ({self.item_name}) : {self.polyalphabetic_ciphers.decrypted_final_text}")

        elif (self.item_name in self.encryption_transposition_functions):

            self.transposition_ciphers.input_text = self.input_line_first.text().upper()
            self.transposition_ciphers.depth = self.input_line_second.text().upper()

            if (not self.transposition_ciphers.depth) or (not self.transposition_ciphers.input_text):
                self.output_text.append("Either depth or the input is missing")
                return
            
            if self.item_name in self.encryption_transposition_functions:
                self.transposition_ciphers.encrypted_final_text = self.transposition_ciphers.encrypt(self.item_name)
                self.output_text.append(f"Input: {self.transposition_ciphers.input_text}")
                self.output_text.append(f"Encrypted ({self.item_name}): {self.transposition_ciphers.encrypted_final_text}\n")

        self.input_line_first.clear()
        self.input_line_second.clear()

    def on_item_clicked(self, item: QTreeWidgetItem, column: int):
        """
        Handle tree widget item selection and update the current encryption/decryption method.
        """
        if item.parent():
            self.item_name = item.text(column)
            self.output_text.append(f"Selected method: {self.item_name}\n")

    def populate_tree(self):
        """
        Populate the tree widgets with available encryption and decryption methods.
        """
        # Create the main "Substitution Ciphers" parent node
        substitution_ciphers = QTreeWidgetItem(self.encryption_tree_widget, ["Substitution Ciphers"])

        # Create "Simple Substitution Cipher" category under main parent
        simple_substitution = QTreeWidgetItem(substitution_ciphers, ["Simple Substitution Cipher"])
        QTreeWidgetItem(simple_substitution, ["caeser_cipher"])
        QTreeWidgetItem(simple_substitution, ["random_substition"])

        # Create "Polyalphabetic Ciphers" category under main parent
        polyalphabetic_ciphers = QTreeWidgetItem(substitution_ciphers, ["Polyalphabetic Ciphers"])
        QTreeWidgetItem(polyalphabetic_ciphers, ["vigenere_cipher"])
        QTreeWidgetItem(polyalphabetic_ciphers, ["vernam_cipher"])

        transposition_ciphers = QTreeWidgetItem(self.encryption_tree_widget, ["Transposition Ciphers"])
        
        QTreeWidgetItem(transposition_ciphers, ["rail_fence"])

        decryption_methods_substitution_ciphers = QTreeWidgetItem(self.decryption_tree_widget, ["Substitution Ciphers"])
        QTreeWidgetItem(decryption_methods_substitution_ciphers, ["brute_force_caesers_cipher"])
        QTreeWidgetItem(decryption_methods_substitution_ciphers, ["crack_polyalphabetic_cipher"])
        QTreeWidgetItem(decryption_methods_substitution_ciphers, ["frequency_analysis"])


        self.encryption_tree_widget.expandAll()

    def keyPressEvent(self, event):
        """Handle Escape key press to close the application."""
        if event.key() == Qt.Key_Escape:
            self.close()

    def update_text_holder(self, item):

        if (self.item_name in self.encryption_simple_substitution_functions) or (self.item_name in self.decryption_simple_substitution_functions):
            self.input_line_first.setPlaceholderText("Enter your text here")
            self.input_line_second.setPlaceholderText("-is not needed-")
        elif (self.item_name in self.encryption_polyalphabetic_functions) or (self.item_name in self.decryption_polyalphabetic_functions):
            self.input_line_first.setPlaceholderText("Enter your text here")
            self.input_line_second.setPlaceholderText("Enter your key here")
        elif (self.item_name in self.encryption_transposition_functions):
            self.input_line_first.setPlaceholderText("Enter your text here")
            self.input_line_second.setPlaceholderText("Enter your depth here")            

    def copy_note(self, item: QTextEdit):
        text = item.toPlainText()
        clipboard = QApplication.clipboard()
        clipboard.setText(text)
        print(text)

    def save_text(self):
        text = self.output_text.toPlainText()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)")

        if file_name:
            with open(file_name, "w") as file:
                file.write(text)

    def load_text(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)")
        print(file_name, _)
        if file_name:
            with open(file_name, "r") as file:
                file_content = file.read()

            self.output_text.append(file_content)

    def create_random_text(self, item: QTextEdit):
        random_text: str = ""
        for _ in range(int(item)):
            random_text = random_text + random.choice(list(self.substitution_ciphers.letter_frequency.keys()))
        self.input_line_first.setText(random_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sus = Simple_Substition_Ciphers()
    baka = Polyalphabetic_Ciphers()
    amogus = Transposition_Ciphers()
    window = GUI(sus, baka, amogus)
    sys.exit(app.exec_())
