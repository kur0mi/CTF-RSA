# openssl 生成私钥
openssl genrsa -out key.pem 1024

# 从私钥文件提取公钥
openssl rsa -in key.pem -pubout -out pubkey.pem

# 公钥加密
openssl rsautl -encrypt -in m -out c -pubin -inkey pubkey.pem

# 私钥解密
openssl rsautl -decrypt -in c -out m2 -inkey pubkey.pem

# 从公钥文件提取 n, e
openssl rsa -pubin -in pubkey.pem -text -modulus -noout

# 从私钥文件提取
openssl rsa -in key.pem -text -modulus -noout
