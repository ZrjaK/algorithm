# 题目：93.复原 IP 地址
# 难度：MEDIUM
# 最后提交：2022-09-14 11:04:41 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []
        for i in range(1, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    t = ".".join([s[:i], s[i:j], s[j:k], s[k:]])
                    if all([0<=int(i)<=255 and i == str(int(i)) for i in t.split(".")]):
                        res.append(t)
        return res