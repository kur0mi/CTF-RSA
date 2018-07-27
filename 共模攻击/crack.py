# coding=utf-8

"""
选择相同的模 n 加密相同的信息 m

"""

helpstr = '''
usage:
    c1 = m ^ e1 % n
    c2 = m ^ e2 % n
'''


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def main():
    print(helpstr)
    n = int(input("input n: "))
    c1 = int(input("input c1: "))
    c2 = int(input("input c2: "))
    e1 = int(input("input e1: "))
    e2 = int(input("input e2: "))
    s = egcd(e1, e2)
    s1 = s[1]
    s2 = s[2]
    # 求模反元素
    if s1 < 0:
        s1 = - s1
        c1 = modinv(c1, n)
    elif s2 < 0:
        s2 = - s2
        c2 = modinv(c2, n)
    m = (c1**s1)*(c2**s2) % n
    print(m)


if __name__ == '__main__':
    main()
