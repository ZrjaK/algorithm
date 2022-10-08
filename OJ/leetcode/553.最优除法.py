# 题目：553.最优除法
# 难度：MEDIUM
# 最后提交：2022-07-05 19:55:06 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        res = "/".join([str(i) for i in nums])
        if len(nums) == 2:
            return res
        t = res.index("/")
        return res[:t+1] + "(" + res[t+1:] + ")"