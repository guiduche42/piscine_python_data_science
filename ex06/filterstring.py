import sys
from ft_filter import ft_filter
import string


def is_valid_string(s: str) -> bool:
    invisible_characters = {chr(i) for i in range(32)} | {chr(127)}
    for char in s:
        if char in string.punctuation or char in invisible_characters:
            return False
    return True


def main():
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        assert sys.argv[2].isdigit(), "the arguments are bad"
        assert is_valid_string(sys.argv[1]), "the arguments are bad"
        ls = ft_filter(sys.argv[1], int(sys.argv[2]))
        print(ls)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
