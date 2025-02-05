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
    args = check_arg()

    dataPrim = np.genfromtxt(args.nameprim, delimiter=',')
    dataSec = np.genfromtxt(args.namesec, delimiter=',')

    print('np =',args.nameprim,'ns =',args.namesec)


    plt.ylabel('Rate')
    plt.xlabel('Amplitude (mV)')
    plt.semilogx()
    plt.title('Amplitude lue selon le temps')
    plt.hist(dataPrim[:, 2], bins=100)
    plt.show()