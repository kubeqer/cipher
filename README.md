# Steganography Encoder and Decoder

This project provides a steganography tool for encoding text into images and decoding text from images. The tool is implemented in Python and uses the PyQt5 library for the graphical user interface (GUI). The encoding process modifies the least significant bits of image pixels to embed the text data, while the decoding process extracts and interprets this data.

## Features

- **Text Encoding**: Encodes text from a file into an image by modifying the least significant bits of the image pixels.
- **Text Decoding**: Decodes text from an encoded image by extracting the least significant bits of the image pixels.
- **GUI**: Provides a user-friendly interface for selecting files and performing encoding and decoding operations.

## Requirements

- Python 3.x
- PyQt5
- Pillow (PIL)
- NumPy

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/kubeqer/cipher.git
    cd cipher
    ```

2. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Application

To start the application, run the following command:

```bash
python main.py
```
### Encode Text into an Image
- Launch the application.
- Select the "Encoder" option.
- Enter a positive number for the cycle value.
- Select a text file containing the text to encode.
- Select an image file to embed the text into.
- Click the "Encode" button. The encoded image will be saved and displayed.
### Decode Text from an Image
- Launch the application.
- Select the "Decoder" option.
- Enter the same positive number used during encoding.
- Select the encoded image file.
- Click the "Decode" button. The decoded text will be displayed in a message box.
## File Structure
- **main.py:** Entry point of the application. 
- **encode_decode.py:** Contains functions for encoding and decoding text.
- **ui.py:** GUI components for the encoding functionality and the decoding functionality.
- **requirements.txt:** Lists the required Python packages.