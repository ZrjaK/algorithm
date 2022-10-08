# 题目：1131.绝对值表达式的最大值
# 难度：MEDIUM
# 最后提交：2022-09-16 10:39:20 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)
        ans = 0
        # 枚举四个方向
        for dx, dy in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
            maxv = -1e99
            minv = 1e99
            # 计算当前方向上的曼哈顿距离最小值和最大值
            for i in range(n):
                maxv = max(maxv, arr1[i] * dx + arr2[i] * dy + i)
                minv = min(minv, arr1[i] * dx + arr2[i] * dy + i)
            # 更新答案
            ans = max(ans, maxv - minv)
        return ans