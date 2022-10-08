# 题目：870.优势洗牌
# 难度：MEDIUM
# 最后提交：2022-10-08 00:07:31 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from sortedcontainers import SortedList
        s = SortedList(nums1)
        ans = []
        for i in nums2:
            t = s.bisect_right(i)
            if t < len(s):
                ans.append(s.pop(t))
            else:
                ans.append(s.pop(0))
        return ans