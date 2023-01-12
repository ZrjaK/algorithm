# 题目：面试题 17.10.主要元素
# 难度：EASY
# 最后提交：2023-01-06 10:09:01 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = -1
        c = 0
        for i in nums:
            if not c:
                ans = i
            if i == ans:
                c += 1
            else:
                c -= 1
        return ans if nums.count(ans) > len(nums) // 2 else -1