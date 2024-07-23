from ft_package import count_in_list


def test_package():
    print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
    print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0


def main():
    test_package()


if __name__ == "__main__":
    main()
