import argparse
from counter import counter

def main():
    """Parse command-line arguments and pass them to print_marquee()"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", help="String to be used as list of letters (to be counted)")
    args = parser.parse_args()
    counts = counter(list(args.s))
    print counts

if __name__ == '__main__':
    main()
