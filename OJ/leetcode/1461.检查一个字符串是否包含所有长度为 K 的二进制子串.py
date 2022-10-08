# 题目：1461.检查一个字符串是否包含所有长度为 K 的二进制子串
# 难度：MEDIUM
# 最后提交：2022-08-26 16:25:22 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        v = [0] * (1<<k)
        for i in range(n-k+1):
            t = int(s[i:i+k], 2)
            v[t] = 1
        return sum(v) == len(v)