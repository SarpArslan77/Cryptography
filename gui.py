import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QLineEdit, QTextEdit, QPushButton, QButtonGroup
)
from PyQt5.QtCore import Qt
from substitution_ciphers import Substition_Ciphers
from polyalphabetic_ciphers import Polyalphabetic_Ciphers

#TODO: reduce the input_text line in encryption/decryption for the substitution ciphers

class GUI(QWidget):
    def __init__(self, substitution_ciphers: Substition_Ciphers, polyalphabetic_ciphers: Polyalphabetic_Ciphers):
        """
        Initialize the GUI for the cryptography application.

        Parameters:
        - substitution_ciphers: An instance of Substition_Ciphers to handle encryption methods.
        """
        super().__init__()
        self.substitution_ciphers = substitution_ciphers  # Store the instance of substitution ciphers
        self.polyalphabetic_ciphers = polyalphabetic_ciphers
        self.item_name = None  # Variable to hold the currently selected encryption method
        
        
        self.setWindowTitle("Learn Cryptography 101") # Set window title
        
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
        self.input_line_first = QLineEdit(self)
        self.input_line_first.move(500, 50)  # Position of the input line
        self.input_line_first.setFixedSize(500, 25)  # Fixed size for the input line

        # create a second input line for the user
        self.input_line_second = QLineEdit(self)
        self.input_line_second.move(1025, 50)
        self.input_line_second.setFixedSize(275, 25)

        # Populate the tree with encryption methods and connect signals
        self.populate_tree()  # Call to populate the tree widget
        self.input_line_first.returnPressed.connect(self.process_input)  # Connect return pressed signal to the handler
        self.input_line_second.returnPressed.connect(self.process_input)

        # all the possible encryption/decryption methods for the getattr function
        self.encryption_substitution_functions: list[str] = ["caeser_cipher", "random_substition", ""]
        self.decryption_substitution_functions: list[str] = ["brute_force_caesers_cipher"]


        # Show the application window in fullscreen
        #self.showFullScreen()
        self.show()

    def process_input(self):
        """
        Process the user input when the return key is pressed.

        Encrypts the input text using the selected encryption method and displays
        the results in the output text box.
        """
        if self.item_name:  # Check if an encryption method is selected
            if (self.item_name in self.encryption_substitution_functions) or (self.item_name in self.decryption_substitution_functions):
                input_text = self.input_line_first.text()  # Get the text from the input line
                if self.item_name in self.encryption_substitution_functions:
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

            elif (self.item_name in self.polyalphabetic_ciphers.encryption_polyalphabetic_functions) or (self.item_name in self.polyalphabetic_ciphers.decryption_polyalphabetic_functions):
                self.polyalphabetic_ciphers.input_text = self.input_line_first.text().upper()  # Get the text from the input line
                self.polyalphabetic_ciphers.key = self.input_line_second.text().upper()
                print("inputting done")
                if self.item_name in self.polyalphabetic_ciphers.encryption_polyalphabetic_functions:
                    print("condition done")
                    self.polyalphabetic_ciphers.encrypted_final_text = self.polyalphabetic_ciphers.encrypt(self.item_name)
                    self.output_text.append(f"Input: {self.polyalphabetic_ciphers.input_text}")
                    self.output_text.append(f"Encrypted ({self.item_name}): {self.polyalphabetic_ciphers.encrypted_final_text}\n")
        else:
            self.output_text.append("Please select an encryption/decryption method first.\n")  # Warning if no method is selected
        self.input_line_first.clear()  # Clear the input line after processing
        self.input_line_second.clear()

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
        substitution_ciphers = QTreeWidgetItem(self.encryption_tree_widget, ["Substitution Ciphers"])  # Parent item
        QTreeWidgetItem(substitution_ciphers, ["caeser_cipher"])  # Child item for Caesar cipher
        QTreeWidgetItem(substitution_ciphers, ["random_substition"])  # Child item for random substitution

        polyalphabetic_ciphers = QTreeWidgetItem(self.encryption_tree_widget, ["Polyalphabetic Ciphers"])
        QTreeWidgetItem(polyalphabetic_ciphers, ["vigenere_cipher"])

        decryption_methods = QTreeWidgetItem(self.decryption_tree_widget, ["Decryption Methods"])
        QTreeWidgetItem(decryption_methods, ["brute_force_caesers_cipher"])

        self.encryption_tree_widget.expandAll()  # Expand all items in the tree widget

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
    baka = Polyalphabetic_Ciphers()
    window = GUI(sus, baka)  # Create the GUI window
    sys.exit(app.exec_())  # Start the application event loop
