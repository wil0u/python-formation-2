# src/hello_argparse/cli.py
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="hello",
        description="Une CLI Hello World avec argparse",
    )

    parser.add_argument(
        "--name",
        "-n",
        type=str,
        required=False,
        dest="name",
        default="world",
        help="Nom à saluer",
    )

    args = parser.parse_args()

    print(f"Hello {args.name}!")


if __name__ == "__main__":
    main()