# 题目：1589.所有排列中的最大和
# 难度：MEDIUM
# 最后提交：2022-08-31 15:11:36 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MODULO = 10**9 + 7
        length = len(nums)
        
        counts = [0] * length
        for start, end in requests:
            counts[start] += 1
            if end + 1 < length:
                counts[end + 1] -= 1
        
        for i in range(1, length):
            counts[i] += counts[i - 1]

        counts.sort()
        nums.sort()
        
        total = sum(num * count for num, count in zip(nums, counts))
        return total % MODULO