#!usr/bin/env python2
import gmpy2

p = 3487583947589437589237958723892346254777
q = 8767867843568934765983476584376578389
e = 65537

n = p * q
fn = (p - 1) * (q - 1)

d = gmpy2.invert(e, fn)

assert(e*d % fn == 1)
print d
