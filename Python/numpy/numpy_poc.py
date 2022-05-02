# https://pianofisica.hatenablog.com/entry/2019/04/08/160002
import numpy as np

A = np.matrix([
[2, 1],
[1, 3]
])

Y = np.matrix([
[3],
[4]
])
print(np.linalg.solve(A,Y))
