import numpy as np

matrix = [[1, 2],
          [3, 4],
          [5, 6]]

np_matrix = np.array(matrix)
t_matrix = np_matrix.T

print(t_matrix.shape[0] + np_matrix.shape[0])
