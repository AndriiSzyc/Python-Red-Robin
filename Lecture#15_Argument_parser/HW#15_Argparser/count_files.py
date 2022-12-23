import argparse
import os
from os.path import getctime

def fcount(path):
    count = 0
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            count += 1
    return count

def last_file(path):
   """ Name last file in directory """
   date = {}
   for f in os.listdir(path):
       if f not in date:
           date[f] = getctime(f)
       else:
           date[f] = getctime(f)

   lst = list()
   for key, val in date.items():
       lst.append((val,key))
   lst.sort(reverse=True)
   return lst[0][1]
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
        print(last_file(os.getcwd()))


if __name__ == '__main__':
     main()