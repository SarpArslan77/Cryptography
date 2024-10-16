import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QLineEdit, QTextEdit, QPushButton, QButtonGroup
)
from PyQt5.QtCore import Qt
from substitution_ciphers import Substition_Ciphers

class GUI(QWidget):
    def __init__(self, substitution_ciphers: Substition_Ciphers):
        """
        Initialize the GUI for the cryptography application.

        Parameters:
        - substitution_ciphers: An instance of Substition_Ciphers to handle encryption methods.
        """
        super().__init__()
        self.substitution_ciphers = substitution_ciphers  # Store the instance of substitution ciphers
        self.item_name = None  # Variable to hold the currently selected encryption method
        
        # Set window title
        self.setWindowTitle("Learn Cryptography 101")
        
        # Create tree widget for displaying encryption methods
        self.encryption_tree_widget = QTreeWidget(self)
        self.encryption_tree_widget.setHeaderLabel("Encryption Methods")  # Set the header of the tree widget
        self.encryption_tree_widget.move(50, 50)  # Position of the tree widget
        self.encryption_tree_widget.setFixedSize(300, 300)  # Fixed size for the tree widget
        self.encryption_tree_widget.itemClicked.connect(self.on_item_clicked)  # Connect item clicked signal to the handler

        # create tree widget for displaying decryption methods
        self.decryption_tree_widget = QTreeWidget(self)
        self.decryption_tree_widget.setHeaderLabel("Decryption Methods")
        self.decryption_tree_widget.move(50, 400)
        self.decryption_tree_widget.setFixedSize(300, 300)
        self.decryption_tree_widget.itemClicked.connect(self.on_item_clicked)
        
        # Create output text box widget for displaying results
        self.output_text = QTextEdit(self)
        self.output_text.move(500, 100)  # Position of the output text box
        self.output_text.setFixedSize(800, 800)  # Fixed size for the output text box
        self.output_text.setReadOnly(True)  # Set the output text box to read-only
        
        # Create input line for user input
        self.input_line = QLineEdit(self)
        self.input_line.move(500, 50)  # Position of the input line
        self.input_line.setFixedSize(800, 25)  # Fixed size for the input line
        
        # create a default button for the languages
        self.button_default = QPushButton(self)
        self.button_default.setText("Default")
        self.button_default.move(375, 100)
        self.button_default.setCheckable(True)

        # create a English button for the languages
        self.button_english = QPushButton(self)
        self.button_english.setText("English")
        self.button_english.move(375, 150)
        self.button_english.setCheckable(True)

        # create a button group and add buttons to the group
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.button_default)
        self.button_group.addButton(self.button_english)

        # connect the button group to a function
        self.button_group.buttonClicked.connect(self.on_button_clicked)

        # Populate the tree with encryption methods and connect signals
        self.populate_tree()  # Call to populate the tree widget
        self.input_line.returnPressed.connect(self.process_input)  # Connect return pressed signal to the handler

        # all the possible encryption/decryption methods for the getattr function
        self.all_encryption_functions: list[str] = ["caeser_cipher", "random_substition"]
        self.all_decryption_functions: list[str] = ["brute_force_caesers_cipher"]


        # Show the application window in fullscreen
        self.showFullScreen()

    def process_input(self):
        """
        Process the user input when the return key is pressed.

        Encrypts the input text using the selected encryption method and displays
        the results in the output text box.
        """
        if self.item_name:  # Check if an encryption method is selected
            input_text = self.input_line.text()  # Get the text from the input line
            if self.item_name in self.all_encryption_functions:
                # Encrypt the input text using the selected method
                encrypted_text = self.substitution_ciphers.encrypt(self.item_name, input_text)
                # Append the input and encrypted text to the output text box
                self.output_text.append(f"Input: {input_text}")
                self.output_text.append(f"Encrypted ({self.item_name}): {encrypted_text}\n")
            else:
                # decrypt the input text using the selected method
                decrypted_text = self.substitution_ciphers.decrypt(self.item_name, input_text)
                # append the input and decrypted text to the output text box
                self.output_text.append(f"Input: {input_text}")
                self.output_text.append(f"Decrypted: ({self.item_name}) : {decrypted_text}")
        else:
            self.output_text.append("Please select an encryption/decryption method first.\n")  # Warning if no method is selected
        self.input_line.clear()  # Clear the input line after processing

    def on_item_clicked(self, item: QTreeWidgetItem, column: int):
        """
        Handle the event when a tree widget item is clicked.

        Sets the selected encryption method based on the clicked item.

        Parameters:
        - item: The clicked QTreeWidgetItem.
        - column: The column index of the clicked item.
        """
        if item.parent():  # Only set item_name for child items (actual methods)
            self.item_name = item.text(column)  # Store the selected method's name
            self.output_text.append(f"Selected method: {self.item_name}\n")  # Display selected method in output

    def populate_tree(self):
        """
        Populate the tree widget with encryption methods.
        Adds a parent item for substitution methods and its child items.
        """
        substitution_methods = QTreeWidgetItem(self.encryption_tree_widget, ["Substitution Methods"])  # Parent item
        QTreeWidgetItem(substitution_methods, ["caeser_cipher"])  # Child item for Caesar cipher
        QTreeWidgetItem(substitution_methods, ["random_substition"])  # Child item for random substitution

        decryption_methods = QTreeWidgetItem(self.decryption_tree_widget, ["Decryption Methods"])
        QTreeWidgetItem(decryption_methods, ["brute_force_caesers_cipher"])

        self.encryption_tree_widget.expandAll()  # Expand all items in the tree widget

    def on_button_clicked(self, button: QPushButton):
        self.substitution_ciphers.decryption_language = button.text()

    def keyPressEvent(self, event):
        """
        Handle key press events.

        Closes the application if the Escape key is pressed.

        Parameters:
        - event: The QKeyEvent object containing the event information.
        """
        if event.key() == Qt.Key_Escape:  # Check if the Escape key is pressed
            self.close()  # Close the application

# just testing it is here, normally should be in main.py
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create the application
    sus = Substition_Ciphers()  # Instantiate the Substition_Ciphers class
    window = GUI(sus)  # Create the GUI window
    sys.exit(app.exec_())  # Start the application event loop
