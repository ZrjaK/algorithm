# 题目：2317.操作后的最大异或和
# 难度：MEDIUM
# 最后提交：2022-06-25 22:53:55 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        d = [0] * 32
        for i in nums:
            for j in range(32):
                if i & (1<<j):
                    d[j] += 1
        for j in range(32):
            if d[j] and not a & (1<<j):
                a ^= 1<<j
        return a