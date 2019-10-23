import argparse
from src.parser.SBMLParser import SBMLParser

def main(fp, **kwargs):
    text   = fp.read()
    parser = SBMLParser()
    parser.parse(text);

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
                        help='enable debugging (TODO: enables logging)')
    args = vars(parser.parse_args())
    print(args)
    main(**args)
