import sys


NESTED_MORSE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}


def encode_to_morse(message):
    """
    Encodes a message into Morse code.

    The encode_to_morse function takes a string message as input and
    encodes it into Morse code using a predefined mapping of characters
    to Morse code. Each letter in the message is converted to its Morse
    code equivalent, and spaces are represented by a slash ('/').

    Parameters:
    message (str): The input message to be encoded in Morse code.

    Returns:
    str: A string representing the encoded message in Morse code.

    Example:
    >>> encode_to_morse("SOS")
    '... --- ...'
    >>> encode_to_morse("HELLO WORLD")
    '.... . .-.. .-.. --- / .-- --- .-. .-.. -..'
    """
    encoded_message = []
    for char in message.upper():
        assert char in NESTED_MORSE, "the arguments are bad"
        encoded_message.append(NESTED_MORSE[char])
    return ' '.join(encoded_message)


def main():
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        morse_message = encode_to_morse(sys.argv[1])
        print(morse_message)
    except AssertionError as e:
        print(f"AssertionError {e}")


if __name__ == "__main__":
    main()
