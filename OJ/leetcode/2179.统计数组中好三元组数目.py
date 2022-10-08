# 题目：2179.统计数组中好三元组数目
# 难度：HARD
# 最后提交：2022-04-11 20:43:26 +0800 CST
# 语言：python3
# 作者：ZrjaK

from sortedcontainers import SortedList
class Solution:       
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        d = {nums2[i]:i for i in range(len(nums2))}
        h = [d[i] for i in nums1]
        s = SortedList()
        l = []
        for i in h:
            l.append(s.bisect_left(i))
            s.add(i)
        s.clear()
        r = []
        for i in h[::-1]:
            r.append(len(s) - s.bisect_left(i))
            s.add(i)
        r = r[::-1]
        ans = 0
        for i, j in zip(l, r):
            ans += i * j
        return ans