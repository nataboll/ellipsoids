# testing if q(...) was built right

import numpy as np

x = np.array(([1, 1, 1], [3, 4, 5]))


def f(a, z, y):
    return a + z - y


print(np.sum(f(6, x[0, :], x[1, :])))
