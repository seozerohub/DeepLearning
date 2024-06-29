import numpy as np

# AND 게이트
def AND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    t = np.sum(x*w)+b
    if t<=0:
        return 0
    else:
        return 1

print(AND(1,1))

# NAND 게이트
def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    t = np.sum(x*w)+b
    if t<=0:
        return 0
    else:
        return 1

print(NAND(0,0))

# OR 게이트
def OR(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5, 0.5])
    b = - 0.2
    t = np.sum(x*w)+b
    if t<=0:
        return 0
    else:
        return 1

print(OR(0,0))

# XOR 게이트
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)

    return y
