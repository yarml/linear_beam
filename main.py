import numpy as np

N = 1000
R = 1

# Negative 1 matrix
N1 = np.full((N, N), -1)
# Diagonal 2 matrix
D2 = np.diag(np.full((N, N), 2).diagonal())

A = D2 + np.diag(N1.diagonal(1), 1) + np.diag(N1.diagonal(-1), -1)

eigen = np.linalg.eig(A).eigenvalues
minEigen = min(eigen)
minPL2 = N*N * minEigen * R

print(len(eigen))
print(min(eigen))
print(f"min(P) = {minPL2} L²")
