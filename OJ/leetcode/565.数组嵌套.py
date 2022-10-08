# 题目：565.数组嵌套
# 难度：MEDIUM
# 最后提交：2022-08-19 01:26:08 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        v = set()
        ans = 0
        for i in range(n):
            t = i
            c = 0
            while t < n and t not in v:
                v.add(t)
                t = nums[t]
                c += 1
            ans = max(ans, c)
        return ans