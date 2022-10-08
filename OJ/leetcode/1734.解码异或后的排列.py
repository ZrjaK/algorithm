# 题目：1734.解码异或后的排列
# 难度：MEDIUM
# 最后提交：2022-08-26 16:43:17 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded)
        t = 0
        for i in range(1, n+2):
            t ^= i
        for i in encoded[::2]:
            t ^= i
        res = [t]
        for i in encoded[::-1]:
            res.append(res[-1] ^ i)
        return res[::-1]