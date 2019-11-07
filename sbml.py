# ensure that src/.. can be imported
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import argparse

from src.parser.SBMLParser import SBMLParser

def run_console(parser):
    keep_running = True
    try:
        while keep_running:
            line = input("> ")
            if line == '.quit':
                keep_running = False
            else:
                result = parser.parse(line);
                if result is not None: print(result)
    except Exception as e:
        print(e)

def run_file(fp, parser):
    text   = fp.read()
    for line in text.split('\n')[:-1]:
        result = parser.parse(line);
        if result is not None: print(result)

def main(fp, debug=False, **kwargs):
    parser = SBMLParser(debug=debug, **kwargs)
    if fp is None:
        run_console(parser)
    else:
        run_file(fp, parser)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='runs an SBML file or starts a  console session if no file is given.')
    parser.add_argument('fp',
                        metavar='filename',
                        type=argparse.FileType('r'),
                        default=None,
                        nargs='?',
                        help='the script to be executed')
    parser.add_argument('--debug',
                        '-d',
                        default=False,
                        action='store_true',
                        help='enable debugging (for ply)')
    args = vars(parser.parse_args())
    main(**args)
