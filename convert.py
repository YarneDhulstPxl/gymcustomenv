import pickle
import h5py
import numpy as np
import csv
import sys
import bz2
import _pickle as cPickle

# Pickle a file and then compress it into a file with extension 
def compressed_pickle(title, data):
    with bz2.BZ2File(title + '.pbz2', 'w') as f: 
        cPickle.dump(data, f)

if __name__ == "__main__":
    csv.field_size_limit(sys.maxsize)
    with open("q_table.pickle", 'rb') as f:
        q_table = pickle.load(f)

    compressed_pickle('filename', q_table) 

    # f = open('numbers3.csv', 'w')

    # with f:

    #     writer = csv.writer(f)
    #     writer.writerows(list(q_table))

    # my_list = []
    # bo = True

    # with open('numbers3.csv', 'r') as f:
    #     reader = csv.reader(f)
    #     for row in reader:
    #         my_list.append(row)
    #         if (bo):
    #             print(row)
    #             bo = False

    # with open("csvtopkl.pickle", "wb") as f:
    #     pickle.dump(my_list, f)