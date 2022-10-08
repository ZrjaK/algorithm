# 题目：131.分割回文串
# 难度：MEDIUM
# 最后提交：2022-04-05 20:32:17 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def f(st, tu):
            t = list(tu)
            if not st:
                res.append(t)
            for i in range(1, len(st)+1):
                t = list(tu)
                k = st[:i]
                if k == k[::-1]:
                    t.append(k)
                    f(st[i:], tuple(t))
        f(s, tuple([]))
        return res
            
            