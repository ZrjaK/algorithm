# 题目：1186.删除一次得到子数组最大和
# 难度：MEDIUM
# 最后提交：2022-07-13 17:46:07 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[arr[0]] * 2 for _ in range(n)]
        for i in range(1, n):
            dp[i][0] = max(arr[i], dp[i-1][0]+arr[i])
            dp[i][1] = max(dp[i-1][0], dp[i-1][1]+arr[i])
        return max(max(i) for i in dp)