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


def Coincident(Array1, Array2):
    roundedArray1 = set(np.around(Array1[:, 1], 0))
    roundedArray2 = set(np.around(Array2[:, 1], 0))
    #roundedArray1 = set(Array1[:,1])
    #roundedArray2 = set(Array2[:, 1])

    #roundedArray1 = list(roundedArray1)
    temp = roundedArray1.intersection(roundedArray2)
    temp = sorted(temp)
    temp = list(temp)
    roundedArray1 = sorted(roundedArray1)
    roundedArray1 = list(roundedArray1)
    indexTemp = 0
    length = len(temp)
    resultat = [0]*len(roundedArray1)
    resultat2 = [0]*len(roundedArray1)
    for i in range(len(roundedArray1)):
        j = indexTemp
        while j < length:
            if roundedArray1[i] == temp[j]:
                resultat[i] = Array1[i,2]
                indexTemp = j
                break

            j += 1

        if length == j:
            resultat2[i] = Array1[i,2]



    return resultat, resultat2

def nonCoincident(Array1, Array2):
    roundedArray1 = set(np.around(Array1[:, 1], 1))
    roundedArray2 = set(np.around(Array2[:, 1], 1))

    #roundedArray1 = list(roundedArray1)
    temp = roundedArray1.intersection(roundedArray2)
    temp = sorted(temp)
    temp = list(temp)
    roundedArray1 = sorted(roundedArray1)
    roundedArray1 = list(roundedArray1)

    length = len(temp)
    resultat = [0]*len(roundedArray1)

    for i in range(len(roundedArray1)):
        for j in range(len(temp)):
            if roundedArray1[i] != temp[j]:
                resultat[i] = Array1[i,2]
                #break

    return resultat

def main():
    args = check_arg()

    data_prim = np.genfromtxt(args.nameprim, delimiter=',')
    data_sec = np.genfromtxt(args.namesec, delimiter=',')

    Coincide,NonCoincide = Coincident(data_prim, data_sec)
    Coincide = sorted(Coincide)
    print(Coincide)
    #NonCoincident = nonCoincident(data_prim, data_sec)
    '''# print('np =',args.nameprim,'ns =',args.namesec)

    Attend = sorted(data_prim[:,2])
    setAttend = sorted(set(Attend))
    listAttend = list(setAttend)

    lenSetAttend = len(listAttend)
    print('setAttend =',listAttend)

    temp = [0]*lenSetAttend

    j = 0




    #print('Z = ',z)
'''
    #print(NonCoincide)
   # print(data_prim[:,2])
    plt.ylabel('Rate')
    plt.xlabel('Amplitude (mV)')
    plt.semilogx()
    plt.title('Amplitude lue selon le temps')
    plt.grid()
    plt.hist(Coincide[:], bins=np.logspace(1, 3, num=20), histtype='step', color = 'RED')
    plt.hist(NonCoincide[:], bins=np.logspace(1, 3, num=20), histtype='step', color = 'GREEN')
    plt.hist(data_prim[:,2], bins=np.logspace(1,3, num = 20 ), histtype='step', color = 'BLUE' )
    plt.show()


if __name__ == '__main__':
    main()