import argparse
import sys
import numpy as np
import matplotlib as plt

def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Script to learn basic argparse')
    parser.add_argument('-N', '--name',
                        help='Nom du fichier à analyser',
                        required=True,
                        default='')

    results = parser.parse_args(args)
    return results.name

if __name__ == '__main__':
    n = check_arg(sys.argv[1:])
    print('n =',n)