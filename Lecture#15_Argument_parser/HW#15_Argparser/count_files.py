import argparse
import os

def fcount(path):
    count = 0
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            count += 1
    return count

def main():
    parser = argparse.ArgumentParser(description='Counts files in directory')
    parser.add_argument('-c',  action='store_true', help='Counts files in script directory')
    parser.add_argument('-l', '--last', action='store_true', help='Swows name of last file')
    parser.add_argument('-d', action='store_true', help='Directory path')
    parser.add_argument('path', type=str, help='Name directory path', nargs='?')
    args = parser.parse_args()

    if args.c and args.d:
        print(fcount(args.path))
    elif args.c:
        print(fcount(os.getcwd()))
    elif args.last:
        print(os.listdir(os.getcwd())[fcount(os.getcwd()) - 1])


if __name__ == '__main__':
     main()