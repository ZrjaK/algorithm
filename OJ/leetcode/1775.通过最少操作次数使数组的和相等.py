# 题目：1775.通过最少操作次数使数组的和相等
# 难度：MEDIUM
# 最后提交：2022-09-07 14:42:09 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        if sum1 == sum2:
            return 0
        if sum1 > sum2:
            return self.minOperations(nums2, nums1)
        
        diff = sum2 - sum1
        freq = Counter(6 - num for num in nums1) + Counter(num - 1 for num in nums2)
        ans = 0
        print(freq)
        for i in range(5, 0, -1):
            if diff <= 0:
                break
            for _ in range(freq[i]):
                if diff <= 0:
                    break
                ans += 1
                diff -= i
        
        return -1 if diff > 0 else ans