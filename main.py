import argparse

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
    parser.add_argument('-F', '--fichier',
                        help='Mettre pour avoir le diagramme en fichier',
                        required=False,
                        action='store_true')
    parser.add_argument('-TM', '--temp-mort',
                        help='Mettre le flag pour appliquer la correction de Temp-mort',
                        required=False,
                        action='store_true')

    return parser.parse_args(args)


def Coincident(Array1, Array2):
    roundedArray1 = set(np.around(Array1[:, 1], 0))
    roundedArray2 = set(np.around(Array2[:, 1], 0))

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



def main():
    args = check_arg()

    data_prim = np.genfromtxt(args.nameprim, delimiter=',')
    data_sec = np.genfromtxt(args.namesec, delimiter=',')

    Coincide,NonCoincide = Coincident(data_prim, data_sec)
    Coincide = sorted(Coincide)
    #print(Coincide)


    plt.ylabel('Rate')
    plt.xlabel('Amplitude (mV)')
    plt.semilogx()
    plt.title('Amplitude lue selon le temps')
    plt.grid()
    plt.hist(Coincide[:], bins=np.logspace(1, 3, num=20), histtype='step', color = 'RED',label = 'Coincident')
    plt.hist(NonCoincide[:], bins=np.logspace(1, 3, num=20), histtype='step', color = 'GREEN',label = 'Non Coincident')
    plt.hist(data_prim[:,2], bins=np.logspace(1,3, num = 20 ), histtype='step', color = 'BLUE',label = 'Tous les évènements' )
    plt.legend(loc = 'best', prop={'size': 10} )
    plt.show()

    if args.fichier:
        plt.savefig("Amplitude_lue_selon_le_temps.png", dpi=300)

    else:
        plt.show()

    print("fin du programme")


if __name__ == '__main__':
    main()