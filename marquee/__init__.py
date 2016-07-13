import argparse

def print_marquee(s):
    if s is None:
        s = "Hi!"
    for i, v in enumerate(s):
        print s[:i+1]

def main():
    """Parse command-line arguments and pass them to print_marquee()"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", help="String to use to print marquee")
    args = parser.parse_args()
    print_marquee(args.s)

if __name__ == '__main__':
    main()
