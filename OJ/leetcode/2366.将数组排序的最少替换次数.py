# 题目：2366.将数组排序的最少替换次数
# 难度：HARD
# 最后提交：2022-08-06 23:57:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        nxt = nums[-1]
        ans = 0
        for i in range(n-2, -1, -1):
            t = nums[i] // nxt
            if not nums[i] % nxt:
                t -= 1
            ans += t
            if t:
                nxt = max(1, nums[i] // (t+1))
            nxt = min(nxt, nums[i])
        return ans
            