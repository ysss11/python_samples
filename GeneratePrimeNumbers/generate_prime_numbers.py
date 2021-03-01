import numpy as np
import math


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


if __name__ == '__main__':
    arr = np.arange(2, 101)
    vec = np.vectorize(is_prime)
    print(arr[vec(arr)])

