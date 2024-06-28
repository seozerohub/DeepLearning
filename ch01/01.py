import numpy as np

# 넘파이의 산술 연산
x = np.array([1,2,3])
y = np.array([4,5,6])
print(x+y)

a = np.array([[1,2],[3,4]])
print(a.shape)
print(a.dtype)

# 브로드캐스트
A = np.array([[1,2], [3,4]])
B = np.array([10,20])
print(A*B)

# 원소 접근
X = np.array([[1,2], [3,4], [5,6]])
X = X.flatten() # 1차원 배열로 평탄화
print(X) # [1 2 3 4 5 6]
print(X[np.array([0,2,4])]) # 인덱스 0,2,4 [1 3 5]

