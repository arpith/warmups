import argparse
from ee101 import ee101

def main():
    """Parse command-line arguments and pass them to print_marquee()"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", help="Voltage")
    parser.add_argument("-i", help="Current")
    parser.add_argument("-r", help="Resistance")
    args = parser.parse_args()
    print ee101(args)

if __name__ == '__main__':
    main()
