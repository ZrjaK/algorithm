# 题目：1691.堆叠长方体的最大高度
# 难度：HARD
# 最后提交：2022-12-10 11:10:01 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        n = len(cuboids)
        for i in range(n):
            cuboids[i].sort()
        cuboids.sort(key = lambda x: (x[2], x[1], x[0]))
        dp = [0] * n
        for i in range(n):
            ma = 0
            for j in range(i):
                if cuboids[j][0] <= cuboids[i][0] and cuboids[j][1] <= cuboids[i][1]:
                    ma = max(ma, dp[j])
            dp[i] = ma + cuboids[i][2]
        return max(dp)