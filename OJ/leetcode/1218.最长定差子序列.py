# 题目：1218.最长定差子序列
# 难度：MEDIUM
# 最后提交：2022-07-14 01:52:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        d = {}
        for i in arr:
            d[i] = d.get(i-difference, 0) + 1
        return max(d.values())