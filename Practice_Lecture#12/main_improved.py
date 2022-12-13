import sys
import json
from argparse import ArgumentParser
from signers import Signer


def args_parser() -> ArgumentParser:
    parser = ArgumentParser(description="Very strong decoder.")
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


def coding(using, action, input_file, output_file):
    global sing
    with open(input_file) as file:
        try:
            data = json.load(file)
        except json.decoder.JSONDecodeError:
            raise "invalid input data..."
    code: list = []
    print(using)
    for count, line in enumerate(data):
        if using == "pyjwt" and action == "encode":
            code.append(sign.jwt_encode(line))
        if using == "pyjwt" and action == "decode":
            code.append(sign.jwt_decode(line))
        if using == "itsdangerous" and action == "encode":
            code.append(sign.itsdangerous_encode(line))
        if using == "itsdangerous" and action == "decode":
            code.append(sign.itsdangerous_decode(line))
    print(code)
    with open(output_file, mode="w") as file:
        file.write(json.dumps(code))


if __name__ == "__main__":
    parser = args_parser()
    namespace = parser.parse_args(sys.argv[1:])
    print(f"Namespace: {namespace}")
    sign = Signer(secret=namespace.secret, salt=namespace.salt)

    coding(
        namespace.using, namespace.action, namespace.input_file, namespace.output_file
    )
