import sys
import time


def ft_tqdm(iterable):
    """
    Mimics the tqdm progress bar for a given iterable.

    :param iterable: The iterable to process.
    """
    total = len(iterable)
    length = 50
    fill = '█'
    print_end = "\r"

    def print_progress_bar(iteration, last_printed):
        percent = 100 * (iteration / float(total))
        filled_length = int(length * iteration // total)
        bar = fill * filled_length + ' ' * (length - filled_length)
        if int(percent) != last_printed and (int(percent) % 6 == 0 or int(percent) == 100):
            print(f'\r{int(percent)}% |{bar}| {iteration}/{total}', end=print_end)
            return int(percent)
        return last_printed

    last_printed = 0
    # Initial call to print progress bar
    last_printed = print_progress_bar(0, last_printed)

    # Iterate over the iterable
    for i, item in enumerate(iterable):
        yield item
        last_printed = print_progress_bar(i + 1, last_printed)

    # Print new line on complete
    print()


def main():
    return



if __name__ == "__main__":
    main()
