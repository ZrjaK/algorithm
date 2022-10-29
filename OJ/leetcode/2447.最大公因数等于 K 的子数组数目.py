# 题目：2447.最大公因数等于 K 的子数组数目
# 难度：MEDIUM
# 最后提交：2022-10-23 10:46:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            t = nums[i]
            for j in range(i, -1, -1):
                t = gcd(t, nums[j])
                if t == k:
                    ans += 1
        return ans