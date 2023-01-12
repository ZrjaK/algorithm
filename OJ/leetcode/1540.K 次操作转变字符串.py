# 题目：1540.K 次操作转变字符串
# 难度：MEDIUM
# 最后提交：2023-01-08 02:56:54 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        
        counts = [0] * 26
        for si, ti in zip(s, t):
            difference = ord(ti) - ord(si)
            if difference < 0:
                difference += 26
            counts[difference] += 1
        
        for i, count in enumerate(counts[1:], 1):
            maxConvert = i + 26 * (counts[i] - 1)
            if maxConvert > k:
                return False
        
        return True
