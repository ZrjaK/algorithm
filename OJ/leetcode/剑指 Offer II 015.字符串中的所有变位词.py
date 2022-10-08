# 题目：剑指 Offer II 015.字符串中的所有变位词
# 难度：MEDIUM
# 最后提交：2022-10-04 17:54:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        c1 = Counter(s[:m])
        c2 = Counter(p)
        res = []
        if c1 == c2:
            res.append(0)
        l = 0
        for r in range(m, n):
            c1[s[r]] += 1
            c1[s[l]] -= 1
            l += 1
            if c1 == c2:
                res.append(r-m+1)
        return res