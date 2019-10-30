import argparse
from src.parser.SBMLParser import SBMLParser

def main(fp, **kwargs):
    text   = fp.read()
    parser = SBMLParser(**kwargs)
    for line in text.split('\n')[:-1]:
        parser.parse(line);

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='runs an SBML file')
    parser.add_argument('fp',
                        metavar='filename',
                        type=argparse.FileType('r'),
                        help='the script to be executed')
    parser.add_argument('--debug',
                        '-d',
                        default=False,
                        action='store_true',
                        help='enable debugging (for ply)')
    parser.add_argument('--verbose',
                        '-v',
                        default=False,
                        action='store_true',
                        help='prints the AST')
    args = vars(parser.parse_args())
    main(**args)
