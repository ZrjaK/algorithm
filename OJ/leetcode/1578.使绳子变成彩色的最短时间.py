# 题目：1578.使绳子变成彩色的最短时间
# 难度：MEDIUM
# 最后提交：2022-07-18 20:32:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans, n = 0, len(neededTime)
        for i in range(1, n):
            if colors[i] == colors[i-1]:
                if neededTime[i] < neededTime[i-1]:
                    ans += neededTime[i]
                    neededTime[i] = neededTime[i-1]
                else:
                    ans += neededTime[i-1]
        return ans