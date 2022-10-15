# 题目：1349.参加考试的最大学生数
# 难度：HARD
# 最后提交：2022-10-13 18:27:04 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        @cache
        def p(i, pre):
            if i == m:
                return 0
            t = 0
            for j in range(n):
                k = pre>>j+1 & 1 == 0 and seats[i][j] == "."
                if j:
                    k &= pre>>j-1 & 1 == 0
                if k:
                    t |= 1<<j
            res = p(i+1, 0)
            f = t
            while t:
                if not any(t>>j & 1 == t>>j+1 & 1 == 1 for j in range(n)):
                    res = max(res, t.bit_count() + p(i+1, t))
                t = f & (t-1)
            return res
        return p(0, 0)
            
            