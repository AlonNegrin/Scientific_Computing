#!/usr/bin/env python3


import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import numpy as np
from pathlib import Path


def load_table(data: Path):
    f = data.open()
    results = {}
    ### Complete this function
    f.readline()
    for line in f:
        buff = line.split()
        results[buff[0]] = np.array(list(map(float, buff[1:])))
    ###
    f.close()
    return results


def lp(x, y, p=2):
    ### Complete this function

    return (sum((np.abs(x - y)) ** p)) ** (1 / p)


###


def cosine(x, y):
    ### Complete this function
    return 1 - (x.reshape(1, -1) @ y.reshape(-1, 1)) / (np.sqrt(x @ x) * (np.sqrt(y @ y)))


###


def weighted_jaccard_similarity(x, y):
    ### Complete this function
    return np.sum(np.min([x, y], axis=0)) / np.sum(np.max([x, y], axis=0))


###


def weighted_jaccard_distance(x, y):
    return 1 - weighted_jaccard_similarity(x, y)


def samples2distances_table(samples):
    results = {}
    ### Complete this function
    # you may create a tuple of pairs, where each pair is a name of a function (as a string)
    # and the function pointer, then loop over the tuple and fill a dictionary.

    indicators = [("L2", lp), ('Cosine', cosine), ('WJD', weighted_jaccard_distance)]
    for fn, fptr in indicators:
        i, j = 0, 0
        data = np.zeros((len(samples.values()), len(samples.values())))

        for x in samples.values():
            j = 0
            for y in samples.values():
                data[i][j] = fptr(x, y)
                j += 1
            i += 1
            results[fn] = data
    return results


def plot_distances(results, labels, figure):
    fig, ax = plt.subplots(1, len(results))
    ### Complete this function
    functions = ('L2', 'Cosine', 'WJD')
    for i in range(len(functions)):
        ax[i].set_xticks(range(len(labels)), labels, rotation=90)
        ax[i].set_yticks(range(len(labels)), labels, rotation=90)
        ax[i].imshow(results[functions[i]], cmap='gray')
        ax[i].set_title(functions[i])
    ###
    if figure is None:
        fig.show()
    else:
        fig.savefig(figure)


def run(data: Path, figure):
    data_table = load_table(data)
    print(data_table)
    distances = samples2distances_table(data_table)
    print(distances)
    plot_distances(distances, list(data_table.keys()), figure)


if __name__ == '__main__':
    run(Path('data.tsv'),  # Replace ... with the path to the datafile
        'fig1')
