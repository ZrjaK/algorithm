# 题目：1947.最大兼容性评分和
# 难度：MEDIUM
# 最后提交：2022-07-21 04:13:12 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m, n = len(students), len(students[0])
        @cache
        def calc(i, j):
            res = 0
            for k in range(n):
                if students[i][k] == mentors[j][k]:
                    res += 1
            return res
        @cache
        def p(vs, vm):
            res = 0
            for i in range(m):
                if 1<<i & vs:
                    continue
                for j in range(m):
                    if 1<<j & vm:
                        continue
                    res = max(res, p(vs|1<<i, vm|1<<j) + calc(i, j))
            return res
        return p(1<<m, 1<<m)