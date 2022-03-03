import argparse
from .scanner import Scanner
from .feed import Feed

scanner = Scanner()

def run_prompt():
    while True:
        feed = Feed(input("¥: "))
        tokens = scanner.scan(feed)
        print([str(token) for token in tokens])

def main():
    parser = argparse.ArgumentParser(prog='olang')
    parser.add_argument('file', nargs='?')

    args = vars(parser.parse_args())
    if args.pop('file'):
        run_file('file')
    else:
        run_prompt()


if __name__ == '__main__':
    main()
