# 题目：169.多数元素
# 难度：EASY
# 最后提交：2022-09-23 23:35:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = 0
        c = 0
        for i in nums:
            if not c:
                ans = i
            if ans == i:
                c += 1
            else:
                c -= 1
        return ans
