# 题目：1921.消灭怪物的最大数量
# 难度：MEDIUM
# 最后提交：2022-09-01 13:56:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        h = sorted(zip(dist, speed), key=lambda x: x[0] / x[1])
        for i in range(len(h)):
            if h[i][0] / h[i][1] <= i:
                return i
        return len(h)