import argparse
import ast
from fizzfactory import fizzfactory

def main():
    """Parse command-line arguments and print flattened list"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="Fizz Factory")
    args = parser.parse_args()
    factory = ast.literal_eval(args.i)
    print factory
    print '\n'.join(fizzfactory(factory))

if __name__ == '__main__':
    main()
