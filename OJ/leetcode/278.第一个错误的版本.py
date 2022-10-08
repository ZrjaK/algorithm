# 题目：278.第一个错误的版本
# 难度：EASY
# 最后提交：2021-10-21 16:57:49 +0800 CST
# 语言：python3
# 作者：ZrjaK

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid) == True:
                right = mid
            else:
                left = mid + 1
        return right