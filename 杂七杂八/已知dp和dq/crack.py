'''
dp=d%(p-1)
dq=d%(q-1)

p, q, dp, dq, c ==> m
'''

InvQ = gmpy2.invert(q, p)   # 模反元素  (q * InvQ) mod p == 1
mp = pow(c, dp, p)          # mp = c ^ dp (mod p)
mq = pow(c, dq, q)          # mq = c ^ dq (mod q)
m = (((mp-mq)*InvQ) % p)*q+mq
print '{:x}'.format(m).decode('hex')
