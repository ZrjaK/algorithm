# 题目：52.N皇后 II
# 难度：HARD
# 最后提交：2022-10-18 17:38:44 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def totalNQueens(self, n: int) -> int:
        def p(i, pre):
            if i == n:
                return 1
            res = 0
            for j in range(n):
                if all(j != k for k in pre) and all(i-k!=j-pre[k] and i-k!=pre[k]-j for k in range(len(pre))):
                   res += p(i+1, pre+[j])
            return res
        return p(0, [])