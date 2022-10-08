# 题目：696.计数二进制子串
# 难度：EASY
# 最后提交：2021-10-23 14:51:58 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        l = list(map(len, s.replace('01', '0 1').replace('10', '1 0').split()))
        return sum(min(a,b) for a,b in zip(l,l[1:]))