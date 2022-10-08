# 题目：2401.最长优雅子数组
# 难度：MEDIUM
# 最后提交：2022-09-04 10:51:13 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        ans = 0
        d = [0] * 32
        for i in range(n):
            # print(i, d)
            if all(((nums[i]>>j)&1) & d[j] == 0 for j in range(32)):
                ans = max(ans, i-l+1)
            else:
                while l < i and not all(((nums[i]>>j)&1) & d[j] == 0 for j in range(32)):
                    for j in range(32):
                        if 1<<j&nums[l]:
                            d[j] -= 1
                    l += 1
            
            for j in range(32):
                    d[j] += nums[i]>>j&1
            
            
        return ans