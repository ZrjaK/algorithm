# 题目：1636.按照频率将数组升序排序
# 难度：EASY
# 最后提交：2022-09-19 00:11:24 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        return sorted(nums, key=lambda x: (c[x], -x))