# this class generates data: the set of (x,y)'s

import numpy as np
import pandas as pd


class Data:
    def __init__(self):
        pass

    k = 0.05  # coefficient for the closest neighbours
    n = 2  # number of dimensions
    m = 100   # number of columns
    max_value = -1  # highest value in dataset
    max_value_index = -1  # point that has highest value - least densely located

    # actual name of the column with highest value (it will not coincide with index after discarding)
    max_value_number = -1

    df = pd.DataFrame(data=np.zeros((n+1, m)), index=['X', 'Y', 'Value'])  # initial DataFrame
    new_df = df  # DataFrame after discarding some points
    center = np.zeros(2)  # center of ellipse - average by X and Y coordinates

    def calculate_center(self, dataframe):
        # calculating average X coordinate
        self.center[0] = float(sum(dataframe.iloc[0, :])) / len(dataframe.iloc[0, :])
        # calculating average Y coordinate
        self.center[1] = float(sum(dataframe.iloc[1, :])) / len(dataframe.iloc[1, :])

    # finding max value and its index
    def refresh_values(self, dataframe, verbose):
            self.max_value = np.amax(dataframe.iloc[2, :])
            self.max_value_index = dataframe.iloc[2, :].tolist().index(self.max_value)
            self.max_value_number = dataframe.columns.values[self.max_value_index]
            if verbose:
                print("Point " + str(self.max_value_number) + " with index " + str(self.max_value_index)
                      + " has max value. It is " + str(self.max_value) + ".\n")

    # generating data
    def generate(self):

        self.df.iloc[0:2, :] = 10 * np.random.randn(self.n, self.m)
        # adding a few outliers to the set of points:
        for i in range(2):
            self.df.iloc[i, 50] = 100 * np.random.randn()
            self.df.iloc[i, 60] = 100 * np.random.randn()
            self.df.iloc[i, 80] = 100 * np.random.randn()
            self.df.iloc[i, 40] = 100 * np.random.randn()
            self.df.iloc[i, 1] = 100 * np.random.randn()

        # calculating value for each point
        dist = np.zeros((self.m, self.m))  # creating an array of distances between each two points
        # filling it with 2nd norm distances
        for j in range(self.m):
            for k in range(j, self.m):  # filling upper triangle of the symmetric matrix 'dist'
                dist[j, k] = np.linalg.norm(self.df.iloc[0:2, j] - self.df.iloc[0:2, k])  # subtraction of vectors
                if j != k:
                    dist[k, j] = dist[j, k]  # using symmetry of distances, i.e. dist should be symmetric
        # for each point counting sum of distances from the k*m nearest neighbours
        for j in range(self.m):
            dist_sort = sorted(dist[j, :])
            self.df.iloc[2, j] = np.sum([dist_sort[1:int(np.ceil(self.k * self.m)+1)]])  # sum from 1 to k*m (0th is 0)

        self.refresh_values(self.df, False)

        self.calculate_center(self.df)

        # normalizing values
        for j in range(self.m):
            self.df.iloc[2, j] = float(self.df.iloc[2, j]) / self.max_value

        self.new_df = self.df

    # discarding least densely located point
    def discard_point(self, verbose):
        self.new_df = self.new_df.drop(columns=[self.max_value_number])  # delete column (point) by its name
        if verbose:
            print("Point " + str(self.max_value_number) + " with index "
                  + str(self.max_value_index) + " has been discarded.\n")
        self.refresh_values(self.new_df, verbose)
        self.calculate_center(self.new_df)
        if verbose:
            print("New candidate to be discarded is " + str(self.max_value_number) + " with index "
                  + str(self.max_value_index) + ".\n")
            print("New center is " + str(self.center) + ".\n")
