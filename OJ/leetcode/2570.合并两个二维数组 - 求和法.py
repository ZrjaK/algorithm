# 题目：2570.合并两个二维数组 - 求和法
# 难度：EASY
# 最后提交：2023-02-19 10:31:15 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        for i, j in nums1:
            d[i] += j
        for i, j in nums2:
            d[i] += j
        ans = []
        for i in sorted(d):
            ans.append([i, d[i]])
        return ans