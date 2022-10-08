# 题目：1191.K 次串联后最大子数组之和
# 难度：MEDIUM
# 最后提交：2022-04-20 13:37:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = ma = 0
        for i in range(n*2):
            if dp < 0:
                dp = arr[i%n]
            else:
                dp += arr[i%n]
            ma = max(ma, dp)
            if i == n-1 and k == 1:
                return ma
        return (max(0, sum(arr))*(k-2) + ma) % int(1e9+7)
