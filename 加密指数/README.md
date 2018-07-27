加密指数 e 过大或过小 会遭受 wiener 攻击 直接计算出 d

如果使用相同的加密指数 e 加密相同的信息 发送给 e 个不同的人，可能受到 低加密指数广播攻击





ps: 进行多轮RSA加密会造成 e 过大
c1 = m1 ^ e1 mod n
c2 = c1 ^ e2 mod n
c3 = c2 ^ e3 mod n

==> c3 = m1 ^ (e1 + e2 + e3) mod n
或 c3 = m1 ^ [(e1 + e2 + e3)(mod n)] mod n
