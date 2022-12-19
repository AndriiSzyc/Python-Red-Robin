# import sys
#
# def main():
#     print('Your passed the following argument')
#     message = sys.argv[1]
#     print(message)
#     print(sys.argv[1])
#
# if __name__ == '__main__':
#     main()

import argparse

# def main():
#     parser = argparse.ArgumentParser('Text formatter')
#     parser.add_argument('-u', action='store_true', help='Upper case mode')
#     parser.add_argument('message', type=str, help='Text message')
#     args = parser.parse_args()
#
#     if args.u:
#         print(args.message.upper())
#     else:
#         print(args.message)
#
# if __name__ == '__main__':
#      main()

def my_func():
    parser = argparse.ArgumentParser('Text formatter')
    parser.add_argument('message', help='Enter your message')
    parser.add_argument('count', help='How many times your message display', type=int)
    #parser.add_argument('-u', help='Some help text', type=bool, default=False) # -u True -> get upper
    parser.add_argument('-u', help='Some help text', action='store_true')       # -u      -> get upper
    args = parser.parse_args()

    for i in range(args.count):
        if args.u:
            print(args.message.upper())
        else:
            print(args.message)

if __name__ == '__main__':
     my_func()