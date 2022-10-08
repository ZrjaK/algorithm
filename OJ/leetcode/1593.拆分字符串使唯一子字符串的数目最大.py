# 题目：1593.拆分字符串使唯一子字符串的数目最大
# 难度：MEDIUM
# 最后提交：2022-09-14 13:36:30 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        def p(i, v):
            if i == n:
                return len(v)
            res = 0
            for j in range(i+1, n+1):
                if s[i:j] in v:
                    continue
                v.add(s[i:j])
                res = max(res, p(j, set(i for i in v)))
                v.remove(s[i:j])
            return res
        return p(0, set())