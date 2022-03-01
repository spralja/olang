import code
from .parser import parse


def run(source):
    pass


def run_console():
    c = code.InteractiveConsole()
    c.runcode('from olang import __base__')
    try:
        while True:
            i = input('¥¥¥:')
            l = i
            while i and (i[-1] == ':' or i[-1] == '!' or i[0] == '\t'):
                print('c: ' + i[0])
                i = input('...:')
                l += '\n' + i
            c.runcode(parse(l))
    except KeyboardInterrupt:
        exit()


def run_file(file):
    with open(file, 'r') as file:
        run(file.read())
