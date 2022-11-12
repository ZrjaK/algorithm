# 题目：2463.最小移动总距离
# 难度：HARD
# 最后提交：2022-11-06 10:50:30 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        n, m = len(robot), len(factory)
        robot.sort()
        factory.sort()
        @cache
        def p(i, j):
            if i == n:
                return 0
            if j == m:
                return 1e99
            s = 0
            res = p(i, j+1)
            pos, limit = factory[j]
            for k in range(limit):
                if i + k >= n:
                    break
                s += abs(robot[i+k] - pos)
                res = min(res, s + p(i+k+1, j+1))
            return res
        return p(0, 0)