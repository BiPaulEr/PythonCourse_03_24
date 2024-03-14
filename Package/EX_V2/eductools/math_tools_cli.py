import argparse

from eductools.math_tools import add, subtract

def calcul_cli():
    parser = argparse.ArgumentParser(description="math cli")
    parser.add_argument("a", type=int, help="")
    parser.add_argument("b", type=int, help="")
    args = parser.parse_args()
    result = add(args.a, args.b)
    print("Result {args.a} + {args.b} = {result}")

calcul_cli()
