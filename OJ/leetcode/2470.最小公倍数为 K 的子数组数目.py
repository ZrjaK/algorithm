# 题目：2470.最小公倍数为 K 的子数组数目
# 难度：MEDIUM
# 最后提交：2022-11-13 10:34:02 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            a = nums[i]
            for j in range(i, n):
                a = lcm(a, nums[j])
                if a == k:
                    ans += 1
        return ans