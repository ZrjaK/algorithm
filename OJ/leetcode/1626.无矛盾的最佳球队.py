# 题目：1626.无矛盾的最佳球队
# 难度：MEDIUM
# 最后提交：2022-07-19 03:12:35 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        arr = list(zip(scores, ages))
        arr.sort(key=lambda x:x[0])
        arr.sort(key=lambda x:x[1])
        dp = [0] * n
        for i in range(n):
            dp[i] = arr[i][0]
            for j in range(i):
                if arr[j][0] <= arr[i][0]:
                    dp[i] = max(dp[i], dp[j]+arr[i][0])
        return max(dp)