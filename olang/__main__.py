import argparse
from .interpreter import run_file, run_console


def main():
    parser = argparse.ArgumentParser(prog='olang')
    parser.add_argument('file', nargs='?')

    args = vars(parser.parse_args())
    if args.pop('file'):
        run_file('file')
    else:
        run_console()


if __name__ == '__main__':
    main()