import sys
from argparse import ArgumentParser
from signers import Signer


def args_parser() -> ArgumentParser:
    parser = ArgumentParser(description='Very strong decoder')
    parser.add_argument(
        "--secret", type=str, required=True, help="Secret key for encode / decode."
    )
    parser.add_argument(
        "--salt", type=str, required=True, help="Secret key for encode / decode."
    )
    parser.add_argument(
        "--using",
        choices=["pyjwt", "itsdangerous"],
        required=True,
        help="Package to encode / decode.",
    )
    parser.add_argument("--action", choices=["encode", "decode"], required=True)
    parser.add_argument(
        "--input_file", type=str, required=True, help="Input filename *.json"
    )
    parser.add_argument(
        "--output_file", type=str, required=True, help="Output filename *.json"
    )
    return parser


if __name__ == "__main__":
    parser = args_parser()
    namespace = parser.parse_args(sys.argv[1:])
    sign = Signer(secret=namespace.secret, salt=namespace.salt)
    print(sign)
