# 题目：813.最大平均值和的分组
# 难度：MEDIUM
# 最后提交：2022-11-28 09:38:19 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        h = [0] + list(accumulate(nums))
        @cache
        def calc(i, j):
            return (h[j]-h[i]) / (j-i)
        @cache
        def p(i, rest):
            if rest == 0:
                if i != len(nums):
                    return -1e99
                return 0
            res = 0
            for j in range(i+1, len(nums)+1):
                res = max(res, p(j, rest-1) + calc(i, j))
            return res
        return p(0, k)