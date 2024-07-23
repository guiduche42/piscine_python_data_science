import sys
import string


def count_characters(text):
    """
    The count_characters function takes a text input and returns a
    dictionary describing the types of characters found in the text.

    The dictionary contains counts for the following types of characters:
    - 'char': Total number of characters
    - 'upper': Number of uppercase letters
    - 'lower': Number of lowercase letters
    - 'punctuation': Number of punctuation marks
    - 'spaces': Number of spaces
    - 'digits': Number of digits

    Parameters:
    text (str): The input text to be analyzed.

    Returns:
    dict: A dictionary with counts of different character types.
    """
    counts = {
        'char': 0,
        'upper': 0,
        'lower': 0,
        'punctuation': 0,
        'spaces': 0,
        'digits': 0
    }

    for char in text:
        counts['char'] += 1
        if char.isupper():
            counts['upper'] += 1
        elif char.islower():
            counts['lower'] += 1
        elif char in string.punctuation:
            counts['punctuation'] += 1
        elif char.isspace():
            counts['spaces'] += 1
        elif char.isdigit():
            counts['digits'] += 1

    return counts


def main():
    if len(sys.argv) == 1:
        user_input = input("What is the text to count?\n")
        sys.argv.append(user_input)
    try:
        assert len(sys.argv[1:]) == 1, "more than one argument is provided"
    except AssertionError as e:
        print(f"AssertionError: {e}")
    counts = count_characters(sys.argv[1])
    print(f"The text contains {counts['char']} characters:")
    print(f"{counts['upper']} upper letters")
    print(f"{counts['lower']} lower letters")
    print(f"{counts['punctuation']} punctuation marks")
    print(f"{counts['spaces']} spaces")
    print(f"{counts['digits']} digits")


if __name__ == "__main__":
    main()
