# 题目：1959.K 次调整数组大小浪费的最小总空间
# 难度：MEDIUM
# 最后提交：2022-09-28 13:20:00 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # 预处理数组 g
        g = [[0] * n for _ in range(n)]
        for i in range(n):
            # 记录子数组的最大值
            best = float("-inf")
            # 记录子数组的和
            total = 0
            for j in range(i, n):
                best = max(best, nums[j])
                total += nums[j]
                g[i][j] = best * (j - i + 1) - total
        
        f = [[float("inf")] * (k + 2) for _ in range(n)]
        for i in range(n):
            for j in range(1, k + 2):
                for i0 in range(i + 1):
                    f[i][j] = min(f[i][j], (0 if i0 == 0 else f[i0 - 1][j - 1]) + g[i0][i])

        return f[n - 1][k + 1]
