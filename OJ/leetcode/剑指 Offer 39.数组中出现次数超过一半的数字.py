# 题目：剑指 Offer 39.数组中出现次数超过一半的数字
# 难度：EASY
# 最后提交：2022-10-03 11:21:12 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = -1
        c = 0
        for i in nums:
            if c == 0:
                ans = i
            if i == ans:
                c += 1
            else:
                c -= 1
        return ans