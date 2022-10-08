# 题目：523.连续的子数组和
# 难度：MEDIUM
# 最后提交：2022-04-14 05:53:17 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        h = [nums[0]] * n
        for i in range(1, n):
            h[i] = h[i-1] + nums[i]
        d = {}
        for i in range(n):
            if h[i]%k in d:
                d[h[i]%k].append(i)
            else:
                d[h[i]%k] = [i]
        # print(d)
        if 0 in d and max(d[0]) >= 1:
            return True
        for i in d.values():
            if i and max(i) - min(i) >= 2:
                return True
        return False