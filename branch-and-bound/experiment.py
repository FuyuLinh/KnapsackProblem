
import argparse
import csv

import matplotlib.pyplot as plt


def read_experiment():
    path = './experiments/experiment.txt'
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        List = [item for item in csv_reader]
        n = []
        time_computing = []
        for num_size, time in List:
            n.append(int(num_size))
            time_computing.append(float(time))
        n, time_computing = (list(t) for t in zip(*sorted(zip(n, time_computing))))
    return n, time_computing

def visualization():
    n, time_computing = read_experiment()
    ax = plt.subplot()
    plt.plot(time_computing, n)
    plt.xlabel("Time (s)")
    plt.ylabel("Number of items")
    plt.show()


if __name__ == '__main__':
    visualization()
