import numpy as np
import time

# Multiply the three matrices: A, B, and C;  i.e., you are expected to find the matrix D where D=(A*B)*C.
# A, B, and, C contain random numbers in the range of (0,1) and the dimensions of the matrices are as follows.
# A is a matrix with dimension 10^6 x 10^3.
# B is a matrix with dimension 10^3 x 10^6.
# C is a matrix with dimension 10^6 x 1


def main():
    start = time.perf_counter_ns()
    n = 10000
    m = 10000
    arrA = np.random.random((n, m))
    arrB = np.random.random((m, n))
    arrC = np.random.random((n, 1))
    arrD = arrA.dot(arrB).dot(arrC)
    elapsed = time.perf_counter_ns() - start
    print(f"Time elapsed: {elapsed/1000000:.2f}ms")


if __name__ == "__main__":
    main()
