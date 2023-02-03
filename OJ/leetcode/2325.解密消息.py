# 题目：2325.解密消息
# 难度：EASY
# 最后提交：2023-02-01 02:17:40 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        a = 97
        d = {}
        for i in key:
            if i == " " or i in d:
                continue
            d[i] = chr(a)
            a += 1
        v = [0] * len(message)
        l = list(message)
        for i, j in d.items():
            for k in range(len(l)):
                if v[k] == 1:
                    continue
                if l[k] == i:
                    l[k] = j
                    v[k] = 1
        return "".join(l)