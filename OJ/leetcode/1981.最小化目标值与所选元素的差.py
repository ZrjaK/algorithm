# 题目：1981.最小化目标值与所选元素的差
# 难度：MEDIUM
# 最后提交：2022-07-22 03:33:23 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        m, n = len(mat), len(mat[0])
        # 什么都不选时和为 0
        f = {0}
        for i in range(m):
            g = set()
            for x in mat[i]:
                for j in f:
                    g.add(j + x)
            f = g
        
        ans = float("inf")
        for x in f:
            ans = min(ans, abs(x - target))
        return ans