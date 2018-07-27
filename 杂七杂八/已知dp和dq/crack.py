'''
dp=d%(p-1)
dq=d%(q-1)
'''

InvQ = gmpy2.invert(q, p)
mp = pow(c, dp, p)
mq = pow(c, dq, q)
m = (((mp-mq)*InvQ) % p)*q+mq
print '{:x}'.format(m).decode('hex')
