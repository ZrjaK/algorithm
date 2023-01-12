# 题目：2032.至少在两个数组中出现的值
# 难度：EASY
# 最后提交：2022-12-30 00:58:05 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        h = [nums1, nums2, nums3]
        ans = []
        for i in range(1, 101):
            c = 0
            for lst in h:
                if i in lst:
                    c += 1
            if c >= 2:
                ans.append(i)
        return ans