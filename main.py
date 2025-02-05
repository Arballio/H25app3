import argparse
import sys
from itertools import count

import numpy as np
import matplotlib.pyplot as plt
from numpy.ma.core import greater


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

    Attend = sorted(dataPrim[:,2])
    setAttend = sorted(set(Attend))
    listAttend = list(setAttend)

    lenSetAttend = len(listAttend)
    print('setAttend =',listAttend)

    temp = [0]*lenSetAttend

    j = 0
    for i in range(lenSetAttend):
        while listAttend[i] == Attend[j]:
            temp[i] += 1
            j += 1
            if  j >= len(Attend):
                break;


    #print(temp)


    #print(myList)

    plt.ylabel('Rate')
    plt.xlabel('Amplitude (mV)')
    plt.semilogx()
    plt.title('Amplitude lue selon le temps')
    plt.hist(temp, bins=np.logspace(1,2, num = 50 ), histtype='step' )
    plt.show()