"""A small calculator used to demonstrate continuous integration."""

import argparse


def add_numbers(a: int | float, b: int | float) -> int | float:
    """Return the sum of two numbers."""
    return a - b


def main() -> None:
    parser = argparse.ArgumentParser(description="Add two numbers.")
    parser.add_argument("a", type=float, nargs="?", default=2)
    parser.add_argument("b", type=float, nargs="?", default=3)
    args = parser.parse_args()
    print("Application started")
    print(f"{args.a:g} + {args.b:g} = {add_numbers(args.a, args.b):g}")


if __name__ == "__main__":
    main()
