# 题目：992.K 个不同整数的子数组
# 难度：HARD
# 最后提交：2022-09-25 16:29:27 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        num1, num2 = collections.Counter(), collections.Counter()
        tot1 = tot2 = 0
        left1 = left2 = right = 0
        ret = 0

        for right, num in enumerate(nums):
            if num1[num] == 0:
                tot1 += 1
            num1[num] += 1
            if num2[num] == 0:
                tot2 += 1
            num2[num] += 1
            
            while tot1 > k:
                num1[nums[left1]] -= 1
                if num1[nums[left1]] == 0:
                    tot1 -= 1
                left1 += 1
            while tot2 > k - 1:
                num2[nums[left2]] -= 1
                if num2[nums[left2]] == 0:
                    tot2 -= 1
                left2 += 1
            
            ret += left2 - left1
        
        return ret