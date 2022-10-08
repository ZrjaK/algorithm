# 题目：1524.和为奇数的子数组数目
# 难度：MEDIUM
# 最后提交：2022-07-16 19:24:07 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MODULO = 10**9 + 7
        odd, even = 0, 1
        subarrays = 0
        total = 0
        
        for x in arr:
            total += x
            subarrays += (odd if total % 2 == 0 else even)
            if total % 2 == 0:
                even += 1
            else:
                odd += 1
        
        return subarrays % MODULO