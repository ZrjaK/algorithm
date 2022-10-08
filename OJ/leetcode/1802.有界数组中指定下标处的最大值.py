# 题目：1802.有界数组中指定下标处的最大值
# 难度：MEDIUM
# 最后提交：2022-05-10 14:22:47 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution(object):
    def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """
        def helper(val):
            if val > index:
                l = (val-1 + val-index) * index // 2
            else:
                l = (val-1 + 1) * (val -1) // 2 + (index - val + 1)
            if val > n - 1 - index:
                r = (val-1+val - n + 1 + index) * (n -1 - index) // 2
            else:
                r = (val-1+1) *(val-1) //2 + (n-1-index - val +1)
            return l + r > maxSum - val
            
        left, right = 1, maxSum - n + 1
        while left < right:
            mid = (left+right)//2
            if helper(mid):
                right = mid
            else:
                left = mid + 1
        return left if not helper(left) else left - 1