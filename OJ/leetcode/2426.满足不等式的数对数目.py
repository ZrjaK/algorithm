# 题目：2426.满足不等式的数对数目
# 难度：HARD
# 最后提交：2022-10-01 22:54:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        h = [i-j for i, j in zip(nums1, nums2)]
        from sortedcontainers import SortedList
        s = SortedList()
        ans = 0
        for i in h:
            # print(i, s)
            t = s.bisect_right(i+diff)
            ans += t
            s.add(i)
        return ans