def ft_filter(s: str, n: int) -> list:
    ls = s.split()
    new_ls = [word for word in ls if len(word) >= n]
    return new_ls
