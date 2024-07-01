import numpy as np
# 입력층 -> 1층
# 다차원 배열을 이용한 입력 신호의 총합 구하기
X = np.array([1,0.5])
W1 = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
B1 = np.array([0.1,0.2,0.3])

A1 = np.dot(X, W1)+ B1
print(A1)

# 활성화 함수 시그모이드 사용
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

Z1 = sigmoid(A1)
print(Z1)

# 1층 -> 2층
W2 = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
B2 = np.array([0.1,0.2])

A2 = np.dot(Z1,W2)+B2
print(A2)
Z2 = sigmoid(A2)
print(Z2)

# 2층 -> 출력층
def Identity(x):
    return x

W3 = np.array([[0.1,0.3],[0.2,0.4]])
B3 = np.array([0.1,0.2])
A3 = np.dot(Z2,W3)+ B3
Y = Identity(A3)