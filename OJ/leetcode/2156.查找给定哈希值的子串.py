# 题目：2156.查找给定哈希值的子串
# 难度：MEDIUM
# 最后提交：2022-05-25 23:06:08 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        mult = 1   # power^k mod modulo
        n = len(s)
        pos = -1   # 第一个符合要求子串的起始下标
        h = 0   # 子串哈希值
        # 预处理计算最后一个子串的哈希值和 power^k mod modulo
        for i in range(n - 1, n - k - 1, -1):
            h = (h * power + (ord(s[i]) - ord('a') + 1)) % modulo
            if i != n - k:
                mult = mult * power % modulo
        if h == hashValue:
            pos = n - k
        # 向前计算哈希值并尝试更新下标
        for i in range(n - k - 1, -1, -1):
            h = ((h - (ord(s[i+k]) - ord('a') + 1) * mult % modulo + modulo) * power + (ord(s[i]) - ord('a') + 1)) % modulo
            if h == hashValue:
                pos = i
        return s[pos:pos+k]