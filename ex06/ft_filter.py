def ft_filter(s: str, n: int) -> list:
    """
    Filters words in a string based on their length.

    The ft_filter function takes a string and an integer as input.
    It splits the string into words and returns a list of words that
    have a length greater than or equal to the specified integer.

    Parameters:
    s (str): The input string containing words to be filtered.
    n (int): The minimum length of words to be included in the returned list.

    Returns:
    list: A list of words from the input string that have a length
          greater than or equal to the specified integer.

    Example:
    >>> ft_filter("This is a test string", 3)
    ['This', 'test', 'string']
    """
    ls = s.split()
    new_ls = [word for word in ls if len(word) >= n]
    return new_ls
