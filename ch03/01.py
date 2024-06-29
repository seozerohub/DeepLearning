import numpy as np
import matplotlib.pylab as plt

# 넘파이 배열 bool, int형 변환
x = np.array([-1.0,2.0,3.0])
y = x>0 # [False  True  True]
print(y.astype(int)) # [0 1 1]

# 계단함수
def step_np(x):
    y = x>0
    return y.astype(int)

a = np.arange(-5,5,0.1)
b = step_np(a)
plt.plot(a,b)
plt.ylim(-0.1,1.1)
plt.show()
