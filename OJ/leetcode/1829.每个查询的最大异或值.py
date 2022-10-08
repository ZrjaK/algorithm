# 题目：1829.每个查询的最大异或值
# 难度：MEDIUM
# 最后提交：2022-08-27 01:21:16 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        ans = []
        t = reduce(xor, nums)
        for _ in range(n):
            c = 0
            for i in range(maximumBit):
                if not t & 1<<i:
                    c |= 1<<i
            ans.append(c)
            t ^= nums.pop()
        return ans