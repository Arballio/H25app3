import argparse
import sys
import numpy as np
import matplotlib.pyplot as plt

def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Script to learn basic argparse')
    parser.add_argument('-NP', '--nameprim',
                        help='Nom du fichier primaire à analyser',
                        required=True,
                        default='')

    parser.add_argument('-NS', '--namesec',
                        help='Nom du fichier secondaire à analyser',
                        required=True,
                        default='')

    return parser.parse_args(args)


if __name__ == '__main__':
    np = check_arg(sys.argv[1:])
    ns = check_arg(sys.argv[2:])

    dataPrim = np.genfromtxt(np, delimiter=',')

    dataSec = np.genfromtxt(ns, delimiter=',')

    print('np =',np,'ns =',ns)


    plt.hist(dataPrim[:,1], bins=100)
    plt.show()