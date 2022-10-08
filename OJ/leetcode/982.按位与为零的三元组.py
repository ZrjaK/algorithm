# 题目：982.按位与为零的三元组
# 难度：HARD
# 最后提交：2022-09-19 09:25:33 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        d = defaultdict(int)
        for i in nums:
            for j in nums:
                d[i&j] += 1
        ans = 0
        for i in nums:
            for j in d:
                if not i & j:
                    ans += d[j]
        return ans