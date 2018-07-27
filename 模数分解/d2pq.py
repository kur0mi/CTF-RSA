# coding: utf-8
# 已知 d，求 p，q

import random


def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


def getpq(n, e, d):
    p = 1
    q = 1
    while p == 1 and q == 1:
        k = d * e - 1
        g = random.randint(0, n)
        while p == 1 and q == 1 and k % 2 == 0:
            k /= 2
            y = pow(g, k, n)
            if y != 1 and gcd(y-1, n) > 1:
                p = gcd(y-1, n)
                q = n/p
    return p, q
