# 题目：1335.工作计划的最低难度
# 难度：HARD
# 最后提交：2022-09-15 23:21:43 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n:
            return -1
        @cache
        def p(i, f, k):
            if i == n:
                if k == 0:
                    return f
                else:
                    return 1e99
            res = p(i+1, max(f, jobDifficulty[i]), k)
            if k:
                res = min(res, f+p(i+1, jobDifficulty[i], k-1))
            return res
        return p(0, 0, d)