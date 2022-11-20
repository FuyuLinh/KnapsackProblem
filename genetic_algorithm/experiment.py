from read import read_experiment
import argparse
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser()
parser.add_argument("size", type=str, help="the size")
args = parser.parse_args()
def visualization(size):
    n, time_computing = read_experiment(size)
    ax = plt.subplot()
    plt.plot(time_computing,n)
    plt.xlabel("Time (s)")
    plt.ylabel("Number of items")
    plt.show()

if __name__ == '__main__':
    visualization(args.size)


