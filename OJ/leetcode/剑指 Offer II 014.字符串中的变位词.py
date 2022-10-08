# 题目：剑指 Offer II 014.字符串中的变位词
# 难度：MEDIUM
# 最后提交：2022-10-04 17:11:11 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        c1 = Counter(s1)
        c2 = Counter(s2[:n])
        if c1 == c2:
            return True
        l = 0
        for r in range(n, m):
            c2[s2[r]] += 1
            c2[s2[l]] -= 1
            l += 1
            if c1 == c2:
                return True
        return False