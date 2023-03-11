# 题目：2574.左右元素和的差值
# 难度：EASY
# 最后提交：2023-02-26 10:31:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        s = 0
        ans = []
        rs = sum(nums)
        for i in nums:
            rs -= i
            ans.append(abs(s - rs))
            s += i
        return ans