import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QLineEdit, QTextEdit, QPushButton
)
from PyQt5.QtCore import Qt
from substitution_ciphers import Substition_Ciphers
from gui import GUI

#TODO: add color schemes to the gui

if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create the application
    sus = Substition_Ciphers()  # Instantiate the Substition_Ciphers class
    window = GUI(sus)  # Create the GUI window
    sys.exit(app.exec_())  # Start the application event loop
