# 题目：2344.使数组可以被整除的最少删除次数
# 难度：HARD
# 最后提交：2022-07-17 11:07:25 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        t = numsDivide[0]
        for i in numsDivide[1:]:
            t = gcd(t, i)
        nums.sort()
        ans = 0
        for i in nums:
            if t % i == 0:
                return ans
            else:
                ans += 1
        return -1