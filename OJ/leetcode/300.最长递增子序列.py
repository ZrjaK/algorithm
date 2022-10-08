# 题目：300.最长递增子序列
# 难度：MEDIUM
# 最后提交：2022-09-30 08:28:28 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        h = []
        for i in nums:
            t = bisect_left(h, i)
            if t < len(h):
                h[t] = i
            else:
                h.append(i)
        return len(h)