# 题目：1239.串联字符串的最大长度
# 难度：MEDIUM
# 最后提交：2022-08-26 03:40:27 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        l = []
        for i in arr:
            t = 0
            for j in i:
                t |= 1 << ord(j)-97
            if t.bit_count() == len(i):
                l.append(t)
        ans = 0
        def p(i, t):
            if i == n:
                nonlocal ans
                ans = max(ans, t.bit_count())
                return
            if i < len(l) and not l[i] & t:
                p(i+1, t|l[i])
            p(i+1, t)
        p(0, 0)
        return ans