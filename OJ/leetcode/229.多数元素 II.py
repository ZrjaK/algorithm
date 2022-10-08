# 题目：229.多数元素 II
# 难度：MEDIUM
# 最后提交：2022-04-13 08:56:55 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        res = []
        for i, j in d.items():
            if j > len(nums)//3:
                res.append(i)
        return res