import os

from PIL import Image
import numpy as np

SPECIAL_SYMBOLS = [
    "=",
    "{",
    "[",
    "}",
    "|",
    "<",
    ">",
    ".",
    "?",
    "`",
    "~",
    "!",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "(",
    ")",
    "_",
    "-",
    "+",
]


def encode_text(text: str, n: int) -> list:
    """
    Encodes the input text using a cycle-based character shifting method, where each
    alphabetic character is shifted by a cycle position, and non-alphabetic characters
    are shifted but kept the same. The encoded text is then converted into a list of binary
    integers.

    Args:
        text (str): The text to be encoded.
        n (int): The maximum value of the cycle used for character shifting.

    Returns:
        list: A list representing the binary encoded text.
    """
    result = []
    cycle_position = 0
    for char in text:
        if char.isalpha():
            encoded_char = chr((ord(char) + cycle_position) % 256)
            result.append(encoded_char)
            for _ in range(cycle_position):
                cycle_position = (cycle_position + 1) % (n + 1)
                encoded_symbol = chr(
                    (
                        ord(SPECIAL_SYMBOLS[cycle_position % len(SPECIAL_SYMBOLS)])
                        + cycle_position
                    )
                    % 256
                )
                result.append(encoded_symbol)
        else:
            result.append(chr(ord(char) + cycle_position))
        cycle_position = (cycle_position + 1) % (n + 1)
    result.append(chr(ord("@") + cycle_position % 256))
    result.append(chr(ord("@") + ((cycle_position + 1) % (n + 1)) % 256))
    for i in result:
        print(str(i), end="")
    binary_result = "".join(["{:08b}".format(ord(x)) for x in result])
    binary_result = [int(x) for x in binary_result]
    return binary_result


def encode_to_image(text_path: str, image_path: str, n: int):
    """
    Encodes text from a given file into an image by modifying the least significant bits
    of the image pixels to include the encoded text data.

    Args:
        text_path (str): Path to the file containing the text to encode.
        image_path (str): Path to the image file where the text will be encoded.
        n (int): The maximum value of the cycle used for encoding text.

    Returns:
        str: Path to the saved image with encoded text.
    """
    with open(text_path, "r") as file:
        text = file.read()
    encoded_text = encode_text(text, n)

    encoded_text_length = len(encoded_text)
    with Image.open(image_path) as image:
        width, height = image.size
        image_data = np.array(image)

    image_data = np.reshape(image_data, width * height * 3)

    image_data[:encoded_text_length] = (
        image_data[:encoded_text_length] & ~1 | encoded_text
    )

    image_data = np.reshape(image_data, (height, width, 3))

    output_dir = "encoded_images"
    try:
        os.makedirs(output_dir)
    except Exception:
        pass

    encoded_image_path = os.path.join(
        output_dir, f"encoded_{os.path.basename(image_path)}"
    )
    image = Image.fromarray(image_data)
    image.save(encoded_image_path)
    image.show()
    return encoded_image_path


def decode_text(image_data, n: int) -> str:
    """
    Decodes the text from image data extracted, considering the encoding cycle.

    Args:
        image_data (list): The binary data extracted from an image.
        n (int): The maximum value of the cycle used for encoding text.

    Returns:
        str: The decoded text from the image.
    """
    result = ""
    cycle_position = 0
    for byte in image_data:
        decoded_byte = chr((int(byte) - cycle_position) % 256)
        if decoded_byte.isprintable():
            result += decoded_byte
        cycle_position = (cycle_position + 1) % (n + 1)
        if result[-2:] == "@@":
            result = result[:-2]
            break
    result = "".join(i for i in result if i not in SPECIAL_SYMBOLS)
    return result


def bits_to_bytes(bits):
    """
    Converts a list of bits into a list of bytes.

    Args:
        bits (list): The list of bits to convert.

    Returns:
        list: The corresponding list of byte values.
    """
    bytes_list = []
    for i in range(0, len(bits), 8):
        byte = bits[i : i + 8]
        byte_value = int("".join(map(str, byte)), 2)
        bytes_list.append(byte_value)
    return bytes_list


def decode_from_image(image_path: str, n: int) -> str:
    """
    Decodes text from an image by extracting the least significant bits of each pixel,
    converting those bits to bytes, and then decoding the bytes into text.

    Args:
        image_path (str): Path to the image with encoded text.
        n (int): The maximum value of the cycle used for decoding text.

    Returns:
        str: The decoded text from the image.
    """
    with Image.open(image_path) as encoded_image:
        width, height = encoded_image.size
        image_data = np.array(encoded_image)

    image_data = np.reshape(image_data, width * height * 3)
    image_data = image_data & 1
    image_data = bits_to_bytes(image_data)

    return decode_text(image_data, n)
