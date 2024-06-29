import numpy as np
import matplotlib.pylab as plt

# 시그모이드 함수
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

a = np.arange(-5, 5, 0.1)
b = sigmoid(a)
plt.plot(a,b)
plt.ylim(-0.1,1.1)
plt.show()

# ReLU 함수
def relu(x):
    return np.maximum(0,x)