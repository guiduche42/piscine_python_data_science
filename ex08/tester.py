from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm


def test_tqdm():
    """
    Test function to compare the behavior or ft_tqdm and tqdm
    """
    for elem in ft_tqdm(range(333)):
        sleep(0.005)
        print()
    for elem in tqdm(range(333)):
        sleep(0.005)
        print()


def main():
    test_tqdm()


if __name__ == "__main__":
    main()
