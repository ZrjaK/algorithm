# 题目：1043.分隔数组以得到最大和
# 难度：MEDIUM
# 最后提交：2022-07-13 00:19:32 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        @cache
        def p(i):
            res = 0
            ma = 0
            for j in range(i, min(len(arr), i+k)):
                ma = max(ma, arr[j])
                res = max(res, p(j+1) + ma*(j-i+1))
            return res
        return p(0)