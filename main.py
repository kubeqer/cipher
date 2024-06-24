import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QSizePolicy,
)
from ui import EncodeWindow, DecodeWindow


class MainWindow(QMainWindow):
    """
    The main window of the application, providing options to access encoding and decoding functionalities.

    Attributes:
        encodeButton (QPushButton): A button that opens the encoding window when clicked.
        decodeButton (QPushButton): A button that opens the decoding window when clicked.
    """

    def __init__(self):
        """
        Initializes the main window with a title, geometry, and layout containing buttons for encoding and decoding.
        """
        super().__init__()
        self.setWindowTitle("Cipher")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.encodeButton = QPushButton("Encode text")
        self.encodeButton.clicked.connect(self.show_encode_window)
        self.encodeButton.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        layout.addWidget(self.encodeButton)

        self.decodeButton = QPushButton("Decode photo")
        self.decodeButton.clicked.connect(self.show_decode_window)
        self.decodeButton.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        layout.addWidget(self.decodeButton)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def show_encode_window(self):
        """
        Creates and displays the encode window when the encode button is clicked.
        """
        self.encodeWindow = EncodeWindow()
        self.encodeWindow.show()

    def show_decode_window(self):
        """
        Creates and displays the decode window when the decode button is clicked.
        """
        self.decodeWindow = DecodeWindow()
        self.decodeWindow.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
