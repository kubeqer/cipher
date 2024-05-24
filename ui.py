from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QLabel,
    QFileDialog,
    QMessageBox,
    QStyle,
    QHBoxLayout,
)
from encode_decode import encode_to_image, decode_from_image


class EncodeWindow(QWidget):
    """
    A widget for encoding text into an image using steganography.
    The user can select a text file and an image file, then encode the text into the image.

    Attributes:
        nInput (QLineEdit): Input field for the cycle number used in encoding.
        textFilePath (QLineEdit): Displays the path of the selected text file.
        textFileBtn (QPushButton): Button to trigger the file dialog for selecting a text file.
        photoFilePath (QLineEdit): Displays the path of the selected image file.
        photoFileBtn (QPushButton): Button to trigger the file dialog for selecting an image file.
        encodeBtn (QPushButton): Button to start the encoding process.
    """

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """
        Initializes the user interface components of the encode window.
        """
        self.setWindowTitle("Encoder")
        self.setGeometry(200, 200, 600, 400)

        layout = QVBoxLayout()

        icon = self.style().standardIcon(QStyle.SP_DirIcon)
        self.nInput = QLineEdit()
        self.textFilePath = QLineEdit()
        self.textFileBtn = QPushButton()
        self.photoFilePath = QLineEdit()
        self.photoFileBtn = QPushButton()
        self.encodeBtn = QPushButton("Encode")

        factorial_layout = QHBoxLayout()
        factorial_layout.addWidget(QLabel("Enter Positive Number:"))
        factorial_layout.addWidget(self.nInput)
        layout.addLayout(factorial_layout)

        self.textFileBtn.setIcon(icon)
        self.textFileBtn.clicked.connect(self.select_text_file)
        text_file_layout = QHBoxLayout()
        text_file_layout.addWidget(QLabel("Text File Path:"))
        text_file_layout.addWidget(self.textFilePath)
        text_file_layout.addWidget(self.textFileBtn)
        layout.addLayout(text_file_layout)

        self.photoFileBtn.setIcon(icon)
        self.photoFileBtn.clicked.connect(self.select_photo_file)
        photo_file_layout = QHBoxLayout()
        photo_file_layout.addWidget(QLabel("Photo File Path:"))
        photo_file_layout.addWidget(self.photoFilePath)
        photo_file_layout.addWidget(self.photoFileBtn)
        layout.addLayout(photo_file_layout)

        self.encodeBtn.clicked.connect(self.encode)
        layout.addWidget(self.encodeBtn)

        self.setLayout(layout)

    def select_text_file(self):
        """
        Opens a file dialog to select a text file and updates the text file path input field.
        """
        fname, _ = QFileDialog.getOpenFileName(
            self, "Select Text File", "", "Text files (*.txt)"
        )
        self.textFilePath.setText(fname)

    def select_photo_file(self):
        """
        Opens a file dialog to select a photo file and updates the photo file path input field.
        """
        fname, _ = QFileDialog.getOpenFileName(
            self, "Select Photo File", "", "Image files (*.bmp *.png)"
        )
        self.photoFilePath.setText(fname)

    def encode(self):
        """
        Encodes the selected text file into the selected image file using the specified cycle number.
        Displays error messages if the input is invalid or files are not selected.
        """
        n = self.nInput.text()
        text_path = self.textFilePath.text()
        photo_path = self.photoFilePath.text()

        if not n.isdigit() or int(n) < 0:
            QMessageBox.warning(self, "Error", "N must be a positive integer.")
            return

        if not text_path or not photo_path:
            QMessageBox.warning(
                self, "Error", "Both text and photo files must be selected."
            )
            return

        encoded_image_path = encode_to_image(text_path, photo_path, int(n))
        QMessageBox.information(
            self, "Success", f"Encoded image saved as {encoded_image_path}"
        )


class DecodeWindow(QWidget):
    """
    A widget for decoding text from an image encoded with steganography.
    The user can select an encoded image file and decode the text from it.

    Attributes:
        nInput (QLineEdit): Input field for the cycle number used in decoding.
        photoFilePath (QLineEdit): Displays the path of the selected image file.
        photoFileBtn (QPushButton): Button to trigger the file dialog for selecting an image file.
        decodeBtn (QPushButton): Button to start the decoding process.
    """

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """
        Initializes the user interface components of the decode window.
        """
        self.setWindowTitle("Decode Photo")
        self.setGeometry(200, 200, 600, 400)

        layout = QVBoxLayout()

        icon = self.style().standardIcon(QStyle.SP_DirIcon)
        self.nInput = QLineEdit()
        self.photoFilePath = QLineEdit()
        self.photoFileBtn = QPushButton()
        self.decodeBtn = QPushButton("Decode")

        self.photoFileBtn.clicked.connect(self.select_photo_file)
        factorial_layout = QHBoxLayout()
        factorial_layout.addWidget(QLabel("Enter Positive Number:"))
        factorial_layout.addWidget(self.nInput)
        layout.addLayout(factorial_layout)

        self.photoFileBtn.setIcon(icon)
        self.photoFileBtn.clicked.connect(self.select_photo_file)
        photo_file_layout = QHBoxLayout()
        photo_file_layout.addWidget(QLabel("Photo File Path:"))
        photo_file_layout.addWidget(self.photoFilePath)
        photo_file_layout.addWidget(self.photoFileBtn)
        layout.addLayout(photo_file_layout)

        self.decodeBtn.clicked.connect(self.decode)
        layout.addWidget(self.decodeBtn)

        self.setLayout(layout)

    def select_photo_file(self):
        """
        Opens a file dialog to select an image file and updates the image file path input field.
        """
        fname, _ = QFileDialog.getOpenFileName(
            self, "Select Photo File", "", "Image files (*.jpg *.jpeg *.png)"
        )
        self.photoFilePath.setText(fname)

    def decode(self):
        """
        Decodes text from the selected image file using the specified cycle number.
        Displays error messages if the input is invalid or a file is not selected.
        """
        n = self.nInput.text()
        photo_path = self.photoFilePath.text()

        if not n.isdigit() or int(n) < 0:
            QMessageBox.warning(self, "Error", "N must be a positive integer.")
            return
        if not photo_path:
            QMessageBox.warning(self, "Error", "A photo file must be selected.")
            return

        decoded_text = decode_from_image(photo_path, int(n))
        QMessageBox.information(self, "Decoded Text", decoded_text)
