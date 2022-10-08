# 题目：77.组合
# 难度：MEDIUM
# 最后提交：2022-09-14 10:55:25 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def p(i, rest, a):
            if not rest:
                res.append(a)
                return
            if i > n:
                return
            p(i+1, rest, a)
            p(i+1, rest-1, a+[i])
        p(1, k, [])
        return res