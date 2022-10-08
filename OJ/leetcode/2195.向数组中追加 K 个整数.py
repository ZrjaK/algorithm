# 题目：2195.向数组中追加 K 个整数
# 难度：MEDIUM
# 最后提交：2022-09-01 17:30:56 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        c = 0
        ans = 0
        for i in nums:
            t = max(0, min(k, i-1-c))
            ans += (c+1 + c+t) * t // 2
            k -= t
            c = i
        if k:
            ans += (nums[-1] + 1 + nums[-1] + k) * k // 2
        return ans