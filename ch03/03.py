import numpy as np

# 다차원 배열
A = np.array([1,2,3,4])
print(np.ndim(A))
print(A.shape)
print(A.shape[0])

# 행렬의 곱
B = np.array([5,6,7,8])
X = np.array([[1,2],[3,4]])
Y = np.array([[5,6],[7,8]])
print(np.dot(A,B))
print(np.dot(X,Y))