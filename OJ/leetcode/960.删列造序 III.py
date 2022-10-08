# 题目：960.删列造序 III
# 难度：HARD
# 最后提交：2022-09-26 16:00:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m, n = len(strs), len(strs[0])
        @cache
        def p(j, pre):
            if j == n:
                return 0
            if pre != -1 and any(strs[i][j] < strs[i][pre] for i in range(m)):
                return p(j+1, pre)
            return max(1+p(j+1, j), p(j+1, pre))
        return n-p(0, -1)