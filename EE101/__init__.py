import argparse
from ee101 import ee101

def main():
    """Parse command-line arguments and pass them to print_marquee()"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", help="Voltage")
    parser.add_argument("-i", help="Current")
    parser.add_argument("-r", help="Resistance")
    args = parser.parse_args()
    values = {}
    if args.v:
        values['v'] = int(args.v)
    if args.i:
        values['i'] = int(args.i)
    if args.r:
        values['r'] = int(args.r)
    print ee101(values)

if __name__ == '__main__':
    main()
