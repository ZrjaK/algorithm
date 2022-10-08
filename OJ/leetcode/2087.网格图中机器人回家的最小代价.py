# 题目：2087.网格图中机器人回家的最小代价
# 难度：MEDIUM
# 最后提交：2022-09-09 17:14:42 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        ans = 0
        if startPos[0] < homePos[0]:
            for i in range(startPos[0]+1, homePos[0]+1):
                ans += rowCosts[i]
        else:
            for i in range(startPos[0]-1, homePos[0]-1, -1):
                ans += rowCosts[i]
        
        if startPos[1] < homePos[1]:
            for i in range(startPos[1]+1, homePos[1]+1):
                ans += colCosts[i]
        else:
            for i in range(startPos[1]-1, homePos[1]-1, -1):
                ans += colCosts[i]
        return ans