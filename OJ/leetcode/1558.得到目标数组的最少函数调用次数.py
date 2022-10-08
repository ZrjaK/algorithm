# 题目：1558.得到目标数组的最少函数调用次数
# 难度：MEDIUM
# 最后提交：2022-05-07 17:10:29 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = 0
        t = 0
        for i in nums:
            k = 0
            while i > 0:
                if i % 2 == 1:
                    i -= 1
                    c += 1
                else:
                    i >>= 1
                    k += 1
            t = max(t, k)
        return c + t