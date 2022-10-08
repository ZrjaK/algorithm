# 题目：2348.全 0 子数组的数目
# 难度：MEDIUM
# 最后提交：2022-07-23 22:41:57 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        c  = ans = 0
        for i in nums:
            if i == 0:
                c += 1
            else:
                ans += (1+c) * c // 2
                c = 0
        ans += (1+c) * c // 2
        return ans