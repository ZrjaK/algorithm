# 题目：1521.找到最接近目标值的函数值
# 难度：HARD
# 最后提交：2022-10-13 16:53:09 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        c = [0] * 20
        n = len(arr)
        l = 0
        ans = 1e99
        for r in range(n):
            for j in range(20):
                c[j] += arr[r]>>j & 1
            t = 0
            for j in range(20):
                if c[j] == r-l+1:
                    t |= 1<<j
            ans = min(ans, abs(t-target))
            while l < r and t < target:
                for j in range(20):
                    c[j] -= arr[l]>>j & 1
                l += 1
                t = 0
                for j in range(20):
                    if c[j] == r-l+1:
                        t |= 1<<j
                ans = min(ans, abs(t-target))
        return ans