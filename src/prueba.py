import numpy as np

vec1 = [1, 2, 3, 4, 5, 6]
vec2 = [0, 12, 23, 34, 45, 56]

equal, x_ind, y_ind = np.intersect1d(vec1, vec2, return_indices=True)

print(equal)
print(x_ind)
print(y_ind)
