import matplotlib.pyplot as plt
import numpy as np


def main():
    # data values from scalene
    times = np.array([0, 0.14, 0.965, 33.35, 33.421, 33.426])
    memory = np.array([0, 771, 1499, 2244, 1534, 0])
    fig, ax = plt.subplots()
    ax.plot(times, memory)
    ax.set_xlabel("Time in seconds")
    ax.set_ylabel("Memory in MB")
    plt.savefig("memory.jpg")
    plt.show()


main()
