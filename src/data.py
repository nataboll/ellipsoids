# this class generates data: the set of (x,y)'s

import numpy as np
import pandas as pd


__author__ = 'natasha'


class Data:
    def __init__(self):
        pass

    k = 0.05  # coefficient for the closest neighbours
    n = 2  # number of rows
    m = 100   # number of columns
    x = np.zeros((n, m))    # n strings of m indexes: x and y
    values = np.zeros(m)  # array for density parameter of a point
    df = pd.DataFrame(data=x)  # empty DataFrame

    # generating data
    def generate(self):
        self.x = 10 * np.random.randn(self.n, self.m)
        # adding a few outliers to the set of points:
        for i in range(2):
            self.x[i, 50] = 100 * np.random.randn()
            self.x[i, 60] = 100 * np.random.randn()
            self.x[i, 80] = 100 * np.random.randn()
            self.x[i, 40] = 100 * np.random.randn()
            self.x[i, 1] = 100 * np.random.randn()

        # creating an array of distances between each two points
        dist = np.zeros((self.m, self.m))
        # filling it with 2nd norm distances
        for j in range(self.m):
            for k in range(j, self.m):  # filling upper triangle of the symmetric matrix 'dist'
                dist[j, k] = np.linalg.norm(self.x[:, j] - self.x[:, k])
                if j != k:
                    dist[k, j] = dist[j, k]  # using symmetry of distances, i.e. dist should be symmetric
        # for each point counting sum of distances from the k*m nearest neighbours
        for j in range(self.m):
            distSort = sorted(dist[j, :])
            self.values[j] = np.sum([distSort[1:int(np.ceil(self.k * self.m)+1)]])
        # normalizing values
        for j in range(self.m):
            self.values[j] = float(self.values[j]) / np.amax(self.values)

    # creating DataFrame with coordinates and value
    def toDataFrame(self):
        # adding empty row for 'value'
        newData = np.append(self.x, [self.values], axis=0)
        # creating DataFrame itself
        self.df = pd.DataFrame(data=newData, index=['X', 'Y', 'Value'])
