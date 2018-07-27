1. 针对 RSA 潜在攻击类型

   + 加密指数

     - 低加密指数（e=3）

       - CopperSmith部分信息攻击（高比特已知分解）

         要求已知 p（或 m） 的大部分比特

         - 已知 消息 m 的大部分比特，可还原 完整消息
         - 已知 素数 p 的大部分比特，可分解 n

       - 广播攻击（boradcast attack）

         - 加密指数/低指数加密广播攻击/crack.py（python2）

     - 高加密指数

       - 对消息进行多轮加密（从而导致加密指数过高）

       - wiener（e 太大）

         基于连分数的特殊攻击

         - 加密指数/e很大/rsa-wiener-attack/RSAwienerReallyHack.py
         - 加密指数/e很大/crack.py（使用 python3 的 owiener 库）

     - 短填充攻击（short pad attack）

   + 解密指数

     + 暴漏解密指数攻击

       已知d之后，利用概率算法对n进行因式分解，从而对未来的信息进行解密

     + 低解密指数攻击

       - wiener（运用连分数的特殊攻击）

   + 模

     - 分解 n

       - http://factordb.com/（基于数据库）

       - yafu（p,q 相近或很远）（利用Fermat方法与Pollard rho方法）

         https://www.cnblogs.com/pcat/p/7508205.html

       - 公约数分解

         分解n得到p,q之后，可求 d

         d 是 e 对于 phi 的 模反元素，d = e-1 mod phi(n)

     + 共模攻击（common modulus attack）

   + 明文攻击

     + 短信息攻击（short message attack）

       短信息 必须用随即比特进行填充（防止爆破）

     + 循环攻击（cycling attack）

       密文是明文的一个置换，密文的连续加密最终将得到明文

     + 公开信息攻击（unconcealed message attack）

   + 执行攻击

     + 时序攻击（timing attack）
     + 能量攻击（power attack）

2. 其他问题

   sage 安装

   - https://err0rzz.github.io/2017/11/16/sage%E5%AE%89%E8%A3%85/

   在线运行 sage 代码

   - https://sagecell.sagemath.org/

3. 过多的递归爆栈

   import   sys
   sys.setrecursionlimit(10000000)

4. yafu 报错 括号不匹配

   ```
   yafu-x64 "factor(@)" -batchfile pcat.txt
   ```

