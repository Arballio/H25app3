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

    return parser.parse_args(args)

def coincidence(array1, array2):
    row1_array1, row2_array1 = array1[:,0], array1[:,1]
    row1_array2, row2_array2 = array2[:,0], array2[:,1]

    intersecting_values = np.intersect1d(row1_array1, row1_array2)

    intersect_frequencies = []

    for value in intersecting_values:
        # Get frequencies of the value in the second row of both arrays
        if(value in row1_array1):
            freq1 = np.count_nonzero(row1_array1 == value)
        else:
            freq1 = 0
        intersect_frequencies.append(freq1)

    # Construct a result 2D array
    result = np.array([intersecting_values, intersect_frequencies])

    return result

def main():
    args = check_arg()

    data_prim = np.genfromtxt(args.nameprim, delimiter=',')
    data_sec = np.genfromtxt(args.namesec, delimiter=',')


    intersect = coincidence(data_prim[:,1:3], data_sec[:,1:3])
    print(len(intersect))
    plt.step(intersect[0], intersect[1])
    
    plt.ylabel('Rate')
    plt.xlabel('Amplitude (mV)')
    plt.semilogx()
    plt.title('Amplitude lue selon le temps')
    #plt.hist(data_prim[:, 2], bins=np.logspace(1, 3, 20), histtype='step')
    plt.show()





if __name__ == '__main__':
    main()