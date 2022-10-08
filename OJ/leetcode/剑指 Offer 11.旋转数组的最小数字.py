# 题目：剑指 Offer 11.旋转数组的最小数字
# 难度：EASY
# 最后提交：2022-09-30 11:15:53 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        n = len(numbers)
        l, r = 0, n-1
        while l < r:
            mid = l+r>>1
            if numbers[mid] < numbers[r]:
                r = mid
            elif numbers[mid] > numbers[r]:
                l = mid + 1
            else:
                r -= 1
        return numbers[l]