# coding = utf-8
# 已知 p，q 求 d
"""
d = computeD(phi, e)

"""


def computeD(fn, e):
    (x, y, r) = extendedGCD(fn, e)
    if y < 0:
        return fn + y
    return y


def extendedGCD(a, b):
    if b == 0:
        return (1, 0, a)
    x1 = 1
    y1 = 0
    x2 = 0
    y2 = 1
    while b != 0:
        q = a // b
        r = a % b
        a = b
        b = r
        x = x1 - q*x2
        x1 = x2
        x2 = x
        y = y1 - q*y2
        y1 = y2
        y2 = y
    return(x1, y1, a)


'''
p = 3487583947589437589237958723892346254777
q = 8767867843568934765983476584376578389
e = 65537

n = p * q
fn = (p - 1) * (q - 1)

d = computeD(fn, e)
print d
'''
