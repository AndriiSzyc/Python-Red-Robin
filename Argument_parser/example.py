import argparse

def math_action():
    parser = argparse.ArgumentParser('Do it math action')
    parser.add_argument('first_number', type=int, help='Enter first number')
    parser.add_argument('second_number', type=int, help='Enter second number')
    parser.add_argument('math_action', type=str, choices=['*', '/', '+', '-'], help='Choise the action')
    args = parser.parse_args()

    if args.math_action == '*':
        print(args.first_number * args.second_number)
    elif args.math_action == '/':
        print(args.first_number / args.second_number)
    elif args.math_action == '+':
        print(args.first_number + args.second_number)
    elif args.math_action == '-':
        print(args.first_number - args.second_number)

if __name__ == '__main__':
     math_action()