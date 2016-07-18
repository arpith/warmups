import argparse
import ast
from flatten import flatten

def main():
    """Parse command-line arguments and print flattened list"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", help="List to be flattened")
    args = parser.parse_args()
    l = ast.literal_eval(args.l)
    print flatten(l)

if __name__ == '__main__':
    main()
