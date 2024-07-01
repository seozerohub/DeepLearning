import numpy as np

# 항등함수
def Identity(x):
    return x

# 소프트맥스 함수
a = np.array([0.3, 2.9, 4.0])
exp_a = np.exp(a)
sum_exp_a = sum(exp_a)
y = exp_a / sum_exp_a

# 소프트맥스 함수 (오버플로 문제 해결)
a = np.array([0.3, 2.9, 4.0])
c = np.max(a)
y = np.exp(a-c)/ np.sum(np.exp(a-c))

def softmax(a):
    c = np.max(a)
    y = np.exp(a - c) / np.sum(np.exp(a - c))
    return y

# 소프트맥스의 확률적인 특징

per = np.array([0.3, 2.9, 4.0])
print(softmax(per))
print(np.sum(softmax(per)))