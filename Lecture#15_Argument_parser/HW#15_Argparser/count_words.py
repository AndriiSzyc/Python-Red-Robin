import argparse
import string


def count_words(file_name):
    with open(file_name, "r") as file:
        text = file.read()
        text = text.translate(text.maketrans("", "", string.punctuation))
        print(len(text.split()))


def main():
    parser = argparse.ArgumentParser("Counts numbers of words in file")
    parser.add_argument("-f", action="store_true", help="Count words")
    parser.add_argument("infile", type=str, help="Input file")
    args = parser.parse_args()
    if args.f:
        count_words(args.infile)


if __name__ == "__main__":
    main()
