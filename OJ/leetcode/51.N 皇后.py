# 题目：51.N 皇后
# 难度：HARD
# 最后提交：2022-10-18 17:37:45 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def p(i, pre):
            nonlocal res
            if i == n:
                h = [["."] * n for _ in range(n)]
                for k in range(n):
                    h[k][pre[k]] = "Q"
                res.append(["".join(i) for i in h])
                return
            for j in range(n):
                if all(j != k for k in pre) and all(i-k!=j-pre[k] and i-k!=pre[k]-j for k in range(len(pre))):
                   p(i+1, pre+[j])
        p(0, [])
        return res