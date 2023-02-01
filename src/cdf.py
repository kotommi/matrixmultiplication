import numpy as np
import matplotlib.pyplot as plt


def main():
    arrA = np.random.random((1000, 100)).flatten()
    fig, ax = plt.subplots(figsize=(8, 4))
    n, bins, patches = ax.hist(
        arrA, 100, density=True, histtype='step', cumulative=True, label='Empirical')
    ax.grid(True)
    ax.set_xlabel("Value")
    ax.set_ylabel("Cumulative probability")
    plt.savefig("cdf.jpg")
    plt.show()


main()
